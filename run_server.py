#!/usr/bin/env python3
"""
Trad-Chem LLM - Server Startup Script
Script to start the Trad-Chem LLM web server.
"""

import uvicorn
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def main():
    """Start the Trad-Chem LLM server."""
    print("🌿 Starting Trad-Chem LLM Web Server...")
    print("=" * 50)
    
    # Check if required environment variables are set
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("⚠️  Warning: OPENAI_API_KEY not set. Using mock LLM service.")
        print("   Set OPENAI_API_KEY environment variable for full LLM functionality.")
    
    # Check if TradChem database exists
    tradchem_db_path = os.getenv("TRADCHEM_DATABASE_PATH")
    if not tradchem_db_path:
        print("ℹ️  Using default TradChem database path.")
    
    print("\n🚀 Starting server...")
    print("   Web Interface: http://localhost:8000")
    print("   API Documentation: http://localhost:8000/api/docs")
    print("   Health Check: http://localhost:8000/api/health")
    print("\n" + "=" * 50)
    
    # Start the server
    uvicorn.run(
        "tradchem_llm.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
        access_log=True
    )

if __name__ == "__main__":
    main() 