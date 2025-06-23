"""
Trad-Chem LLM - LLM Service
Service for handling interactions with large language models.
"""

import logging
import asyncio
from typing import Dict, Any, Optional, List
import json
import os
from datetime import datetime

# Try to import OpenAI, fallback to mock if not available
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    logging.warning("OpenAI not available. Using mock LLM service.")

logger = logging.getLogger(__name__)

class LLMService:
    """Service for handling LLM interactions."""
    
    def __init__(self):
        self.client = None
        self.model_name = "gpt-3.5-turbo"
        self.temperature = 0.7
        self.max_tokens = 1000
        self.api_key = os.getenv("OPENAI_API_KEY")
        
    async def initialize(self):
        """Initialize the LLM service."""
        if OPENAI_AVAILABLE and self.api_key:
            try:
                openai.api_key = self.api_key
                self.client = openai
                logger.info("LLM service initialized with OpenAI")
            except Exception as e:
                logger.error(f"Failed to initialize OpenAI: {e}")
                self.client = None
        else:
            logger.info("Using mock LLM service")
            self.client = None
    
    async def generate_response(
        self, 
        prompt: str, 
        context: Optional[str] = None,
        system_message: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate a response using the LLM.
        
        Args:
            prompt: User's question or prompt
            context: Additional context about traditional medicines
            system_message: System message to guide the LLM
            
        Returns:
            Dictionary containing response and metadata
        """
        try:
            if self.client and OPENAI_AVAILABLE:
                return await self._generate_openai_response(prompt, context, system_message)
            else:
                return await self._generate_mock_response(prompt, context, system_message)
        except Exception as e:
            logger.error(f"Error generating LLM response: {e}")
            return {
                "response": "I apologize, but I'm having trouble processing your request right now. Please try again later.",
                "confidence": 0.0,
                "timestamp": datetime.now().isoformat(),
                "error": str(e)
            }
    
    async def _generate_openai_response(
        self, 
        prompt: str, 
        context: Optional[str] = None,
        system_message: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate response using OpenAI API."""
        try:
            # Prepare messages
            messages = []
            
            # Add system message
            if system_message:
                messages.append({"role": "system", "content": system_message})
            else:
                messages.append({
                    "role": "system", 
                    "content": """You are Trad-Chem LLM, an expert assistant specializing in traditional medicine and chemical compounds. 
                    You have access to a comprehensive database of traditional medicines, their benefits, chemical compositions, and SMILES notations.
                    Always provide accurate, evidence-based information and cite sources when possible.
                    If you're not sure about something, say so rather than making up information."""
                })
            
            # Add context if provided
            if context:
                messages.append({
                    "role": "user", 
                    "content": f"Context about traditional medicines: {context}"
                })
            
            # Add user's question
            messages.append({"role": "user", "content": prompt})
            
            # Generate response
            response = await asyncio.to_thread(
                openai.ChatCompletion.create,
                model=self.model_name,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            return {
                "response": response.choices[0].message.content,
                "confidence": 0.9,  # OpenAI doesn't provide confidence scores
                "timestamp": datetime.now().isoformat(),
                "model": self.model_name,
                "tokens_used": response.usage.total_tokens
            }
            
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise
    
    async def _generate_mock_response(
        self, 
        prompt: str, 
        context: Optional[str] = None,
        system_message: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate mock response when OpenAI is not available."""
        
        # Simple keyword-based responses for demonstration
        prompt_lower = prompt.lower()
        
        if "turmeric" in prompt_lower or "curcumin" in prompt_lower:
            response = """Turmeric (Curcuma longa) is a traditional medicine with the active compound curcumin. 
            It has anti-inflammatory and antioxidant properties. The SMILES notation for curcumin is CC1=CC(=C(C=C1)O)C(=O)O.
            It's commonly used for inflammation, arthritis, and digestive issues."""
            
        elif "immunity" in prompt_lower or "immune" in prompt_lower:
            response = """Traditional medicines that boost immunity include:
            - Ashwagandha (Withania somnifera): Adaptogenic herb that supports immune function
            - Tulsi (Holy Basil): Rich in antioxidants and immune-modulating compounds
            - Amla (Indian Gooseberry): High in Vitamin C and antioxidants
            - Ginger: Contains gingerol with anti-inflammatory properties"""
            
        elif "cannabis" in prompt_lower or "marijuana" in prompt_lower:
            response = """Cannabis contains various active compounds including:
            - Cannabigerolic acid: CCCCCC1=CC(=C(C(=C1C(=O)O)O)C/C=C(\\C)/CCC=C(C)C)O
            - Cannabigerol: CCCCCC1=CC(=C(C(=C1)O)C/C=C(\\C)/CCC=C(C)C)O
            These compounds have various therapeutic properties including anti-inflammatory and analgesic effects."""
            
        elif "search" in prompt_lower or "find" in prompt_lower:
            response = """I can help you search for traditional medicines. You can search by:
            - Medicine name
            - Benefits (e.g., anti-inflammatory, immunity)
            - Diseases treated
            - Ingredients or chemical compounds
            Please specify what you're looking for and I'll search the database."""
            
        elif "smiles" in prompt_lower or "chemical" in prompt_lower:
            response = """SMILES (Simplified Molecular Input Line Entry System) is a notation for representing chemical structures.
            In our database, each traditional medicine ingredient has associated SMILES notations for its active compounds.
            This allows for chemical analysis, molecular property calculations, and drug discovery applications."""
            
        else:
            response = """I'm Trad-Chem LLM, your assistant for traditional medicine information. 
            I can help you with:
            - Information about specific traditional medicines
            - Chemical compositions and SMILES notations
            - Benefits and therapeutic uses
            - Searching the traditional medicine database
            - Understanding molecular properties
            
            Please ask me about any traditional medicine or chemical compound you're interested in!"""
        
        return {
            "response": response,
            "confidence": 0.8,
            "timestamp": datetime.now().isoformat(),
            "model": "mock-llm",
            "note": "Mock response - OpenAI not configured"
        }
    
    async def analyze_medicine_data(self, medicine_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze medicine data using LLM.
        
        Args:
            medicine_data: Medicine data to analyze
            
        Returns:
            Analysis results
        """
        prompt = f"""
        Analyze this traditional medicine data and provide insights:
        
        Medicine: {medicine_data.get('product_name', 'Unknown')}
        Benefits: {', '.join(medicine_data.get('benefits', []))}
        Diseases: {', '.join(medicine_data.get('diseases', []))}
        Ingredients: {list(medicine_data.get('chemical_composition', {}).get('ingredients', {}).keys())}
        
        Please provide:
        1. A summary of the medicine's properties
        2. Potential therapeutic mechanisms
        3. Safety considerations
        4. Modern research relevance
        """
        
        return await self.generate_response(prompt)
    
    async def suggest_medicines(self, symptoms: List[str], preferences: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Suggest traditional medicines based on symptoms.
        
        Args:
            symptoms: List of symptoms
            preferences: User preferences (e.g., traditional system preference)
            
        Returns:
            Medicine suggestions
        """
        prompt = f"""
        Based on these symptoms: {', '.join(symptoms)}
        
        Please suggest traditional medicines that might help. Consider:
        - Traditional medicine systems (Ayurvedic, TCM, etc.)
        - Safety and contraindications
        - Evidence-based recommendations
        - Chemical mechanisms of action
        
        User preferences: {preferences or 'None specified'}
        """
        
        return await self.generate_response(prompt)
    
    def is_available(self) -> bool:
        """Check if LLM service is available."""
        return self.client is not None or not OPENAI_AVAILABLE 