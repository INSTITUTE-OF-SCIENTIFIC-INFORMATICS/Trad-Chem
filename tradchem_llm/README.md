# Trad-Chem LLM Web Server

A modern web server that provides an intelligent interface to the TradChem traditional medicine database using Large Language Models (LLMs).

## 🌟 Features

- **Intelligent Chat Interface**: Ask questions about traditional medicines in natural language
- **Real-time Database Search**: Search medicines by name, benefits, diseases, and ingredients
- **SMILES Analysis**: Chemical structure analysis and molecular property calculations
- **Modern Web UI**: Responsive, user-friendly interface
- **RESTful API**: Complete API for integration with other applications
- **LLM Integration**: OpenAI GPT and Anthropic Claude support
- **Real-time Statistics**: Live database statistics and insights

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- TradChem database (from the main project)
- OpenAI API key (optional, for full LLM functionality)

### Installation

1. **Install dependencies**:
   ```bash
   pip install -r tradchem_llm/requirements.txt
   ```

2. **Set environment variables** (create a `.env` file):
   ```bash
   # LLM Configuration
   OPENAI_API_KEY=your_openai_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   
   # Database Configuration
   TRADCHEM_DATABASE_PATH=path/to/your/tradchem_database.json
   
   # Server Configuration
   HOST=0.0.0.0
   PORT=8000
   DEBUG=false
   ```

3. **Start the server**:
   ```bash
   python run_server.py
   ```

4. **Access the application**:
   - Web Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/api/docs
   - Health Check: http://localhost:8000/api/health

## 📖 Usage

### Web Interface

1. **Chat with AI**: Ask questions about traditional medicines in the chat interface
2. **Search Medicines**: Use the search panel to find specific medicines
3. **View Statistics**: Check database statistics in real-time
4. **Quick Actions**: Use predefined questions for common queries

### API Endpoints

#### Chat with LLM
```bash
POST /api/chat
{
    "message": "Tell me about turmeric and its benefits",
    "context": "Additional context (optional)"
}
```

#### Search Medicines
```bash
POST /api/search
{
    "query": "immunity",
    "search_type": "benefit"
}
```

#### Get Medicine Details
```bash
GET /api/medicine/{medicine_name}
```

#### Get Database Statistics
```bash
GET /api/stats
```

#### List All Medicines
```bash
GET /api/medicines?limit=10
```

#### Add New Medicine
```bash
POST /api/medicine
{
    "product_name": "New Medicine",
    "benefits": ["Benefit 1", "Benefit 2"],
    "diseases": ["Disease 1", "Disease 2"],
    "chemical_composition": {
        "ingredients": {
            "Ingredient": {
                "primary_smiles": "SMILES_NOTATION"
            }
        }
    }
}
```

## 🏗️ Architecture

```
tradchem_llm/
├── main.py                 # FastAPI application
├── models.py              # Pydantic data models
├── config.py              # Configuration settings
├── database.py            # Database dependency injection
├── services/              # Business logic services
│   ├── llm_service.py     # LLM integration
│   ├── tradchem_service.py # TradChem wrapper
│   └── chat_service.py    # Chat coordination
├── static/                # Web interface files
│   └── index.html         # Main web interface
└── requirements.txt       # Python dependencies
```

### Service Layer

- **LLMService**: Handles interactions with OpenAI, Anthropic, and other LLM providers
- **TradChemService**: Wraps the TradChem library for web server use
- **ChatService**: Coordinates between LLM and TradChem services

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | None |
| `ANTHROPIC_API_KEY` | Anthropic API key | None |
| `TRADCHEM_DATABASE_PATH` | Path to TradChem database | Default |
| `HOST` | Server host | 0.0.0.0 |
| `PORT` | Server port | 8000 |
| `DEBUG` | Debug mode | false |

### LLM Configuration

The system supports multiple LLM providers:

- **OpenAI GPT**: Primary LLM provider
- **Anthropic Claude**: Alternative LLM provider
- **Mock Service**: Fallback when no API keys are provided

## 🧪 Testing

### Run Tests
```bash
pytest tradchem_llm/tests/
```

### Test API Endpoints
```bash
# Test health check
curl http://localhost:8000/api/health

# Test chat endpoint
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me about turmeric"}'
```

## 📊 Monitoring

### Health Check
```bash
GET /api/health
```

### Metrics
- Request count
- Response times
- Error rates
- Database statistics

## 🔒 Security

- CORS configuration
- Rate limiting
- Input validation
- Error handling

## 🚀 Deployment

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "tradchem_llm.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Considerations

1. **Environment Variables**: Set all required environment variables
2. **SSL/TLS**: Use HTTPS in production
3. **Rate Limiting**: Configure appropriate rate limits
4. **Monitoring**: Set up logging and monitoring
5. **Backup**: Regular database backups

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 API Documentation

Full API documentation is available at:
- Swagger UI: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc

## 🐛 Troubleshooting

### Common Issues

1. **LLM not responding**: Check API keys and internet connection
2. **Database errors**: Verify TradChem database path
3. **Import errors**: Ensure all dependencies are installed
4. **Port conflicts**: Change the port in configuration

### Logs

Check server logs for detailed error information:
```bash
tail -f logs/tradchem_llm.log
```

## 📄 License

This project is licensed under the Mozilla Public License Version 2.0.

## 🙏 Acknowledgments

- TradChem project for the traditional medicine database
- OpenAI for LLM capabilities
- FastAPI for the web framework
- Bootstrap for the UI components

---

**Trad-Chem LLM** - Bridging traditional wisdom with modern AI technology. 