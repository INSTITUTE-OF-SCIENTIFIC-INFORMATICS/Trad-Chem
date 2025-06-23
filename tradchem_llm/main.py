"""
Trad-Chem LLM - Main FastAPI Application
Web server for traditional medicine chemical database with LLM integration.
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
import logging
from typing import List, Dict, Any, Optional
import os

from .models import (
    ChatRequest, 
    ChatResponse, 
    MedicineQuery, 
    MedicineResponse,
    DatabaseStats,
    SearchRequest
)
from .services.llm_service import LLMService
from .services.tradchem_service import TradChemService
from .services.chat_service import ChatService
from .database import get_tradchem_service

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Trad-Chem LLM",
    description="Web server for traditional medicine chemical database with LLM integration",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
llm_service = LLMService()
chat_service = ChatService()

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    logger.info("Starting Trad-Chem LLM server...")
    await llm_service.initialize()
    logger.info("Trad-Chem LLM server started successfully!")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("Shutting down Trad-Chem LLM server...")

# Health check endpoint
@app.get("/api/health", response_model=Dict[str, str])
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "Trad-Chem LLM"}

# Chat with LLM about traditional medicine
@app.post("/api/chat", response_model=ChatResponse)
async def chat_with_llm(
    request: ChatRequest,
    tradchem_service: TradChemService = Depends(get_tradchem_service)
):
    """
    Chat with the LLM about traditional medicine.
    
    This endpoint allows users to ask questions about traditional medicines,
    their benefits, chemical compositions, and more.
    """
    try:
        response = await chat_service.process_chat(
            user_message=request.message,
            tradchem_service=tradchem_service,
            llm_service=llm_service
        )
        return ChatResponse(
            response=response,
            timestamp=response.get("timestamp", ""),
            sources=response.get("sources", [])
        )
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Search medicines in database
@app.post("/api/search", response_model=List[MedicineResponse])
async def search_medicines(
    request: SearchRequest,
    tradchem_service: TradChemService = Depends(get_tradchem_service)
):
    """
    Search for medicines in the database.
    
    Supports searching by name, benefits, diseases, and ingredients.
    """
    try:
        results = tradchem_service.search_medicines(
            query=request.query,
            search_type=request.search_type
        )
        return [MedicineResponse(**medicine) for medicine in results]
    except Exception as e:
        logger.error(f"Error in search endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Get medicine by name
@app.get("/api/medicine/{medicine_name}", response_model=MedicineResponse)
async def get_medicine(
    medicine_name: str,
    tradchem_service: TradChemService = Depends(get_tradchem_service)
):
    """
    Get detailed information about a specific medicine.
    """
    try:
        medicine = tradchem_service.get_medicine_by_name(medicine_name)
        if not medicine:
            raise HTTPException(status_code=404, detail="Medicine not found")
        return MedicineResponse(**medicine)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting medicine: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Get database statistics
@app.get("/api/stats", response_model=DatabaseStats)
async def get_database_stats(
    tradchem_service: TradChemService = Depends(get_tradchem_service)
):
    """
    Get comprehensive database statistics.
    """
    try:
        stats = tradchem_service.get_statistics()
        return DatabaseStats(**stats)
    except Exception as e:
        logger.error(f"Error getting stats: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# List all medicines
@app.get("/api/medicines", response_model=List[str])
async def list_medicines(
    limit: Optional[int] = None,
    tradchem_service: TradChemService = Depends(get_tradchem_service)
):
    """
    List all medicines in the database.
    """
    try:
        medicines = tradchem_service.list_medicines()
        if limit:
            medicines = medicines[:limit]
        return medicines
    except Exception as e:
        logger.error(f"Error listing medicines: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Add new medicine
@app.post("/api/medicine", response_model=Dict[str, str])
async def add_medicine(
    medicine: MedicineQuery,
    tradchem_service: TradChemService = Depends(get_tradchem_service)
):
    """
    Add a new medicine to the database.
    """
    try:
        success = tradchem_service.add_medicine(medicine.dict())
        if success:
            return {"message": "Medicine added successfully", "status": "success"}
        else:
            raise HTTPException(status_code=400, detail="Failed to add medicine")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error adding medicine: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Serve static files for web interface
app.mount("/static", StaticFiles(directory="tradchem_llm/static"), name="static")

# Serve the main web interface
@app.get("/", response_class=HTMLResponse)
async def serve_web_interface():
    """Serve the main web interface."""
    try:
        with open("tradchem_llm/static/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="""
        <html>
            <head><title>Trad-Chem LLM</title></head>
            <body>
                <h1>Trad-Chem LLM</h1>
                <p>Web interface not found. Please check the static files.</p>
                <p><a href="/api/docs">API Documentation</a></p>
            </body>
        </html>
        """)

if __name__ == "__main__":
    uvicorn.run(
        "tradchem_llm.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 