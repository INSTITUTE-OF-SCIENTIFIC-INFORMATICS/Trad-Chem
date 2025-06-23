"""
Trad-Chem LLM - Chat Service
Service for coordinating chat interactions between LLM and TradChem data.
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
import re

from .llm_service import LLMService
from .tradchem_service import TradChemService

logger = logging.getLogger(__name__)

class ChatService:
    """Service for coordinating chat interactions."""
    
    def __init__(self):
        self.conversation_history: List[Dict[str, Any]] = []
    
    async def process_chat(
        self,
        user_message: str,
        tradchem_service: TradChemService,
        llm_service: LLMService,
        context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Process a chat message and generate a response.
        
        Args:
            user_message: User's message
            tradchem_service: TradChem service instance
            llm_service: LLM service instance
            context: Additional context
            
        Returns:
            Response with answer and metadata
        """
        try:
            # Analyze the user's intent
            intent = self._analyze_intent(user_message)
            
            # Gather relevant data based on intent
            relevant_data = await self._gather_relevant_data(
                user_message, intent, tradchem_service
            )
            
            # Generate context for LLM
            llm_context = self._build_llm_context(relevant_data, context)
            
            # Generate response using LLM
            llm_response = await llm_service.generate_response(
                prompt=user_message,
                context=llm_context,
                system_message=self._get_system_message(intent)
            )
            
            # Extract sources and references
            sources = self._extract_sources(relevant_data)
            medicine_references = self._extract_medicine_references(relevant_data)
            
            # Build final response
            response = {
                "response": llm_response.get("response", "I'm sorry, I couldn't generate a response."),
                "timestamp": datetime.now().isoformat(),
                "sources": sources,
                "medicine_references": medicine_references,
                "confidence": llm_response.get("confidence", 0.0),
                "intent": intent,
                "data_used": len(relevant_data) > 0
            }
            
            # Store in conversation history
            self.conversation_history.append({
                "user_message": user_message,
                "response": response,
                "timestamp": response["timestamp"]
            })
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing chat: {e}")
            return {
                "response": "I apologize, but I encountered an error processing your request. Please try again.",
                "timestamp": datetime.now().isoformat(),
                "sources": [],
                "medicine_references": [],
                "confidence": 0.0,
                "error": str(e)
            }
    
    def _analyze_intent(self, message: str) -> str:
        """Analyze user intent from message."""
        message_lower = message.lower()
        
        # Search intent
        if any(word in message_lower for word in ["search", "find", "look for", "what medicines"]):
            return "search"
        
        # Information intent
        if any(word in message_lower for word in ["what is", "tell me about", "information about", "explain"]):
            return "information"
        
        # Comparison intent
        if any(word in message_lower for word in ["compare", "difference between", "vs", "versus"]):
            return "comparison"
        
        # Recommendation intent
        if any(word in message_lower for word in ["recommend", "suggest", "good for", "help with"]):
            return "recommendation"
        
        # Chemical analysis intent
        if any(word in message_lower for word in ["smiles", "chemical", "molecular", "compound"]):
            return "chemical_analysis"
        
        # General intent
        return "general"
    
    async def _gather_relevant_data(
        self,
        message: str,
        intent: str,
        tradchem_service: TradChemService
    ) -> List[Dict[str, Any]]:
        """Gather relevant data from TradChem database."""
        relevant_data = []
        
        try:
            # Extract potential medicine names and keywords
            keywords = self._extract_keywords(message)
            
            for keyword in keywords:
                # Search by different criteria
                search_results = []
                
                # Search by name
                search_results.extend(tradchem_service.search_medicines(keyword, "name"))
                
                # Search by benefits
                search_results.extend(tradchem_service.search_medicines(keyword, "benefit"))
                
                # Search by diseases
                search_results.extend(tradchem_service.search_medicines(keyword, "disease"))
                
                # Search by ingredients
                search_results.extend(tradchem_service.search_medicines(keyword, "ingredient"))
                
                # Add unique results
                for result in search_results:
                    if not any(d.get("product_name") == result.get("product_name") for d in relevant_data):
                        relevant_data.append(result)
            
            # Limit results to avoid overwhelming the LLM
            relevant_data = relevant_data[:10]
            
        except Exception as e:
            logger.error(f"Error gathering relevant data: {e}")
        
        return relevant_data
    
    def _extract_keywords(self, message: str) -> List[str]:
        """Extract potential keywords from message."""
        # Simple keyword extraction - can be enhanced with NLP
        words = re.findall(r'\b\w+\b', message.lower())
        
        # Filter out common words
        stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by",
            "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did",
            "will", "would", "could", "should", "may", "might", "can", "what", "how", "why", "when", "where",
            "tell", "me", "about", "information", "search", "find", "look", "for", "medicine", "medicines"
        }
        
        keywords = [word for word in words if word not in stop_words and len(word) > 2]
        
        # Add common traditional medicine terms
        medicine_terms = [
            "turmeric", "curcumin", "ginger", "ashwagandha", "neem", "tulsi", "amla", "shatavari", "brahmi",
            "cannabis", "honey", "ghee", "guggulu", "shilajit", "immunity", "inflammation", "antioxidant",
            "anti-inflammatory", "digestive", "stress", "energy", "vitality", "fatigue", "arthritis"
        ]
        
        # Add medicine terms that appear in the message
        for term in medicine_terms:
            if term in message.lower():
                keywords.append(term)
        
        return list(set(keywords))  # Remove duplicates
    
    def _build_llm_context(self, relevant_data: List[Dict[str, Any]], additional_context: Optional[str] = None) -> str:
        """Build context string for LLM."""
        context_parts = []
        
        if additional_context:
            context_parts.append(f"Additional context: {additional_context}")
        
        if relevant_data:
            context_parts.append("Relevant traditional medicine data from the database:")
            for i, medicine in enumerate(relevant_data, 1):
                context_parts.append(f"""
                {i}. {medicine.get('product_name', 'Unknown')}:
                - Benefits: {', '.join(medicine.get('benefits', []))}
                - Diseases: {', '.join(medicine.get('diseases', []))}
                - Ingredients: {list(medicine.get('chemical_composition', {}).get('ingredients', {}).keys())}
                """)
        
        return "\n".join(context_parts) if context_parts else "No specific data available."
    
    def _get_system_message(self, intent: str) -> str:
        """Get appropriate system message based on intent."""
        base_message = """You are Trad-Chem LLM, an expert assistant specializing in traditional medicine and chemical compounds. 
        You have access to a comprehensive database of traditional medicines, their benefits, chemical compositions, and SMILES notations.
        Always provide accurate, evidence-based information and cite sources when possible.
        If you're not sure about something, say so rather than making up information."""
        
        intent_messages = {
            "search": base_message + " Focus on helping users find specific medicines and provide detailed information about them.",
            "information": base_message + " Provide comprehensive information about traditional medicines, their properties, and uses.",
            "comparison": base_message + " Help users compare different traditional medicines and their properties.",
            "recommendation": base_message + " Provide evidence-based recommendations while noting that you're not a medical professional.",
            "chemical_analysis": base_message + " Focus on chemical properties, SMILES notations, and molecular analysis.",
            "general": base_message
        }
        
        return intent_messages.get(intent, base_message)
    
    def _extract_sources(self, relevant_data: List[Dict[str, Any]]) -> List[str]:
        """Extract sources from relevant data."""
        sources = []
        for medicine in relevant_data:
            source = medicine.get("source")
            if source and source not in sources:
                sources.append(source)
        return sources
    
    def _extract_medicine_references(self, relevant_data: List[Dict[str, Any]]) -> List[str]:
        """Extract medicine references from relevant data."""
        return [medicine.get("product_name", "") for medicine in relevant_data if medicine.get("product_name")]
    
    def get_conversation_history(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get conversation history."""
        if limit:
            return self.conversation_history[-limit:]
        return self.conversation_history
    
    def clear_conversation_history(self):
        """Clear conversation history."""
        self.conversation_history = []
    
    async def get_medicine_insights(
        self,
        medicine_name: str,
        tradchem_service: TradChemService,
        llm_service: LLMService
    ) -> Dict[str, Any]:
        """Get detailed insights about a specific medicine."""
        try:
            # Get medicine data
            medicine = tradchem_service.get_medicine_by_name(medicine_name)
            if not medicine:
                return {
                    "error": f"Medicine '{medicine_name}' not found in database",
                    "timestamp": datetime.now().isoformat()
                }
            
            # Generate insights using LLM
            prompt = f"""
            Provide detailed insights about this traditional medicine:
            
            Name: {medicine.get('product_name')}
            Benefits: {', '.join(medicine.get('benefits', []))}
            Diseases: {', '.join(medicine.get('diseases', []))}
            Ingredients: {list(medicine.get('chemical_composition', {}).get('ingredients', {}).keys())}
            
            Please provide:
            1. Traditional uses and history
            2. Modern scientific understanding
            3. Chemical mechanisms of action
            4. Safety considerations
            5. Potential interactions
            6. Dosage guidelines (general information only)
            """
            
            llm_response = await llm_service.generate_response(prompt)
            
            return {
                "medicine": medicine,
                "insights": llm_response.get("response", ""),
                "timestamp": datetime.now().isoformat(),
                "confidence": llm_response.get("confidence", 0.0)
            }
            
        except Exception as e:
            logger.error(f"Error getting medicine insights: {e}")
            return {
                "error": f"Error generating insights: {str(e)}",
                "timestamp": datetime.now().isoformat()
            } 