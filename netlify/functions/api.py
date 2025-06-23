"""
Netlify Function for Trad-Chem LLM API
This function serves as the backend API for the Trad-Chem LLM system.
"""

import json
import os
import sys
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import logging

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Import TradChem LLM services
try:
    from tradchem_llm.services.llm_service import LLMService
    from tradchem_llm.services.tradchem_service import TradChemService
    from tradchem_llm.services.chat_service import ChatService
    from tradchem_llm.models import ChatRequest, SearchRequest, MedicineQuery
    TRADCHEM_AVAILABLE = True
except ImportError:
    TRADCHEM_AVAILABLE = False
    logging.warning("TradChem LLM services not available")

# Initialize services
llm_service = None
tradchem_service = None
chat_service = None

def initialize_services():
    """Initialize the services."""
    global llm_service, tradchem_service, chat_service
    
    if TRADCHEM_AVAILABLE:
        try:
            llm_service = LLMService()
            tradchem_service = TradChemService()
            chat_service = ChatService()
            logging.info("Services initialized successfully")
        except Exception as e:
            logging.error(f"Error initializing services: {e}")

class APIHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the API."""
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
    
    def do_GET(self):
        """Handle GET requests."""
        try:
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            query_params = parse_qs(parsed_url.query)
            
            if path == '/api/health':
                self.handle_health_check()
            elif path == '/api/stats':
                self.handle_get_stats()
            elif path.startswith('/api/medicines'):
                self.handle_list_medicines(query_params)
            elif path.startswith('/api/medicine/'):
                medicine_name = path.split('/')[-1]
                self.handle_get_medicine(medicine_name)
            else:
                self.send_error(404, "Endpoint not found")
                
        except Exception as e:
            self.send_error(500, f"Internal server error: {str(e)}")
    
    def do_POST(self):
        """Handle POST requests."""
        try:
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(body) if body else {}
            
            if path == '/api/chat':
                self.handle_chat(data)
            elif path == '/api/search':
                self.handle_search(data)
            elif path == '/api/medicine':
                self.handle_add_medicine(data)
            else:
                self.send_error(404, "Endpoint not found")
                
        except Exception as e:
            self.send_error(500, f"Internal server error: {str(e)}")
    
    def handle_health_check(self):
        """Handle health check requests."""
        response = {
            "status": "healthy",
            "service": "Trad-Chem LLM",
            "version": "1.0.0",
            "timestamp": "2024-01-01T00:00:00Z"
        }
        self.send_json_response(response)
    
    def handle_get_stats(self):
        """Handle database statistics requests."""
        if not tradchem_service:
            self.send_error(503, "Service unavailable")
            return
        
        try:
            stats = tradchem_service.get_statistics()
            self.send_json_response(stats)
        except Exception as e:
            self.send_error(500, f"Error getting stats: {str(e)}")
    
    def handle_list_medicines(self, query_params):
        """Handle list medicines requests."""
        if not tradchem_service:
            self.send_error(503, "Service unavailable")
            return
        
        try:
            limit = int(query_params.get('limit', [10])[0])
            medicines = tradchem_service.list_medicines()
            if limit:
                medicines = medicines[:limit]
            self.send_json_response(medicines)
        except Exception as e:
            self.send_error(500, f"Error listing medicines: {str(e)}")
    
    def handle_get_medicine(self, medicine_name):
        """Handle get medicine requests."""
        if not tradchem_service:
            self.send_error(503, "Service unavailable")
            return
        
        try:
            medicine = tradchem_service.get_medicine_by_name(medicine_name)
            if medicine:
                self.send_json_response(medicine)
            else:
                self.send_error(404, "Medicine not found")
        except Exception as e:
            self.send_error(500, f"Error getting medicine: {str(e)}")
    
    def handle_chat(self, data):
        """Handle chat requests."""
        if not all([llm_service, tradchem_service, chat_service]):
            self.send_error(503, "Service unavailable")
            return
        
        try:
            # Create chat request
            chat_request = ChatRequest(
                message=data.get('message', ''),
                context=data.get('context'),
                user_id=data.get('user_id')
            )
            
            # Process chat
            import asyncio
            response = asyncio.run(chat_service.process_chat(
                user_message=chat_request.message,
                tradchem_service=tradchem_service,
                llm_service=llm_service,
                context=chat_request.context
            ))
            
            self.send_json_response(response)
        except Exception as e:
            self.send_error(500, f"Error processing chat: {str(e)}")
    
    def handle_search(self, data):
        """Handle search requests."""
        if not tradchem_service:
            self.send_error(503, "Service unavailable")
            return
        
        try:
            search_request = SearchRequest(
                query=data.get('query', ''),
                search_type=data.get('search_type', 'name'),
                limit=data.get('limit')
            )
            
            results = tradchem_service.search_medicines(
                query=search_request.query,
                search_type=search_request.search_type
            )
            
            if search_request.limit:
                results = results[:search_request.limit]
            
            self.send_json_response(results)
        except Exception as e:
            self.send_error(500, f"Error searching medicines: {str(e)}")
    
    def handle_add_medicine(self, data):
        """Handle add medicine requests."""
        if not tradchem_service:
            self.send_error(503, "Service unavailable")
            return
        
        try:
            medicine_query = MedicineQuery(**data)
            success = tradchem_service.add_medicine(medicine_query.dict())
            
            if success:
                response = {"message": "Medicine added successfully", "status": "success"}
            else:
                response = {"message": "Failed to add medicine", "status": "error"}
            
            self.send_json_response(response)
        except Exception as e:
            self.send_error(500, f"Error adding medicine: {str(e)}")
    
    def send_json_response(self, data):
        """Send JSON response."""
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

def handler(request, context):
    """Netlify function handler."""
    # Initialize services on first request
    if not llm_service:
        initialize_services()
    
    # Create handler instance
    handler = APIHandler(request, None, None)
    
    # Handle the request
    if request['httpMethod'] == 'GET':
        handler.do_GET()
    elif request['httpMethod'] == 'POST':
        handler.do_POST()
    elif request['httpMethod'] == 'OPTIONS':
        handler.do_OPTIONS()
    else:
        handler.send_error(405, "Method not allowed")
    
    return {
        'statusCode': handler.response_code,
        'headers': handler.response_headers,
        'body': handler.response_body
    } 