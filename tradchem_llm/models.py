"""
Trad-Chem LLM - Data Models
Pydantic models for API request and response schemas.
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class ChatRequest(BaseModel):
    """Request model for chat with LLM."""
    message: str = Field(..., description="User's message/question")
    context: Optional[str] = Field(None, description="Additional context for the conversation")
    user_id: Optional[str] = Field(None, description="User identifier for session tracking")

class ChatResponse(BaseModel):
    """Response model for chat with LLM."""
    response: str = Field(..., description="LLM's response")
    timestamp: str = Field(..., description="Response timestamp")
    sources: List[str] = Field(default=[], description="Sources/references used")
    confidence: Optional[float] = Field(None, description="Confidence score of the response")
    medicine_references: Optional[List[str]] = Field(None, description="Referenced medicines")

class SearchRequest(BaseModel):
    """Request model for medicine search."""
    query: str = Field(..., description="Search query")
    search_type: str = Field(default="name", description="Type of search (name, benefit, disease, ingredient)")
    limit: Optional[int] = Field(None, description="Maximum number of results")

class MedicineQuery(BaseModel):
    """Request model for adding a new medicine."""
    product_name: str = Field(..., description="Name of the medicine")
    benefits: List[str] = Field(..., description="List of benefits")
    diseases: List[str] = Field(..., description="List of diseases treated")
    chemical_composition: Dict[str, Any] = Field(..., description="Chemical composition data")
    description: Optional[str] = Field(None, description="Additional description")
    source: Optional[str] = Field(None, description="Source of information")
    traditional_system: Optional[str] = Field(None, description="Traditional medicine system (e.g., Ayurvedic, TCM)")

class MedicineResponse(BaseModel):
    """Response model for medicine data."""
    product_name: str = Field(..., description="Name of the medicine")
    benefits: List[str] = Field(..., description="List of benefits")
    diseases: List[str] = Field(..., description="List of diseases treated")
    chemical_composition: Dict[str, Any] = Field(..., description="Chemical composition data")
    entry_id: Optional[str] = Field(None, description="Unique entry identifier")
    date_added: Optional[str] = Field(None, description="Date when medicine was added")
    description: Optional[str] = Field(None, description="Additional description")
    source: Optional[str] = Field(None, description="Source of information")
    traditional_system: Optional[str] = Field(None, description="Traditional medicine system")

class DatabaseStats(BaseModel):
    """Response model for database statistics."""
    total_medicines: int = Field(..., description="Total number of medicines")
    total_benefits: int = Field(..., description="Total number of unique benefits")
    total_diseases: int = Field(..., description="Total number of unique diseases")
    total_ingredients: int = Field(..., description="Total number of unique ingredients")
    last_updated: str = Field(..., description="Last update timestamp")
    traditional_systems: Optional[List[str]] = Field(None, description="List of traditional medicine systems")
    avg_ingredients_per_medicine: Optional[float] = Field(None, description="Average ingredients per medicine")

class LLMConfig(BaseModel):
    """Configuration model for LLM service."""
    model_name: str = Field(default="gpt-3.5-turbo", description="LLM model to use")
    temperature: float = Field(default=0.7, description="Temperature for response generation")
    max_tokens: int = Field(default=1000, description="Maximum tokens in response")
    api_key: Optional[str] = Field(None, description="API key for LLM service")

class SystemHealth(BaseModel):
    """Response model for system health check."""
    status: str = Field(..., description="System status")
    service: str = Field(..., description="Service name")
    version: str = Field(..., description="Service version")
    timestamp: str = Field(..., description="Health check timestamp")
    database_connected: bool = Field(..., description="Database connection status")
    llm_available: bool = Field(..., description="LLM service availability")

class ErrorResponse(BaseModel):
    """Response model for errors."""
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")
    timestamp: str = Field(..., description="Error timestamp")
    request_id: Optional[str] = Field(None, description="Request identifier for tracking") 