# 🚀 Netlify Deployment Guide for TradChem LLM

This guide will help you deploy your TradChem LLM project to Netlify. Since this is a Python FastAPI application with a frontend, you'll need to deploy the frontend to Netlify and the backend to a different service.

## 📋 **Prerequisites**

- A GitHub account
- A Netlify account (free tier available)
- A backend hosting service (Render, Railway, Heroku, etc.)
- Python 3.8+ installed locally

## 🏗️ **Project Structure Overview**

```
TradChem/
├── tradchem_llm/
│   ├── static/              # Frontend files (deploy to Netlify)
│   │   ├── index.html
│   │   └── js/
│   │       └── app.js
│   ├── main.py              # FastAPI backend (deploy elsewhere)
│   └── services/            # Backend services
├── netlify.toml             # Netlify configuration
└── requirements.txt         # Python dependencies
```

## 🌐 **Step 1: Deploy Backend (FastAPI)**

Since Netlify doesn't support persistent Python servers, you need to deploy your FastAPI backend to a different service.

### **Option A: Render (Recommended)**

1. **Sign up for Render**: Go to [render.com](https://render.com) and create an account

2. **Create a new Web Service**:
   - Connect your GitHub repository
   - Choose the repository
   - Set the following:
     - **Name**: `tradchem-llm-backend`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn tradchem_llm.main:app --host 0.0.0.0 --port $PORT`

3. **Add Environment Variables**:
   ```
   OPENAI_API_KEY=your_openai_api_key
   TRADCHEM_DATABASE_PATH=/opt/render/project/src/tradchem/data/tradchem_database.json
   ```

4. **Deploy**: Click "Create Web Service"

### **Option B: Railway**

1. **Sign up for Railway**: Go to [railway.app](https://railway.app)

2. **Deploy from GitHub**:
   - Connect your repository
   - Railway will auto-detect Python
   - Add environment variables as needed

### **Option C: Heroku**

1. **Create a `Procfile`**:
   ```
   web: uvicorn tradchem_llm.main:app --host 0.0.0.0 --port $PORT
   ```

2. **Deploy using Heroku CLI**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## 🎨 **Step 2: Deploy Frontend to Netlify**

### **Method 1: Deploy from GitHub (Recommended)**

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for Netlify deployment"
   git push origin main
   ```

2. **Connect to Netlify**:
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Choose GitHub and select your repository

3. **Configure build settings**:
   - **Build command**: Leave empty (no build step needed)
   - **Publish directory**: `tradchem_llm/static`
   - Click "Deploy site"

### **Method 2: Drag and Drop**

1. **Prepare your static files**:
   ```bash
   # Create a deployment folder
   mkdir netlify-deploy
   cp -r tradchem_llm/static/* netlify-deploy/
   ```

2. **Deploy**:
   - Go to Netlify dashboard
   - Drag the `netlify-deploy` folder to the deploy area

## ⚙️ **Step 3: Configure Frontend-Backend Connection**

### **Update API Base URL**

1. **Edit `tradchem_llm/static/js/app.js`**:
   ```javascript
   getApiBaseUrl() {
       // Replace with your actual backend URL
       return 'https://your-backend-url.onrender.com/api';
       // or
       return 'https://your-app.railway.app/api';
   }
   ```

2. **Or use environment variables**:
   ```javascript
   getApiBaseUrl() {
       return process.env.REACT_APP_API_URL || 'https://your-backend-url.com/api';
   }
   ```

### **Add Environment Variables in Netlify**

1. Go to your Netlify site dashboard
2. Navigate to **Site settings** → **Environment variables**
3. Add:
   ```
   REACT_APP_API_URL=https://your-backend-url.com/api
   ```

## 🔧 **Step 4: Configure CORS**

Update your FastAPI backend to allow requests from your Netlify domain:

```python
# In tradchem_llm/main.py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-netlify-site.netlify.app",
        "http://localhost:3000",  # For local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🚀 **Step 5: Test Your Deployment**

1. **Test the frontend**: Visit your Netlify URL
2. **Test the backend**: Visit `https://your-backend-url.com/api/health`
3. **Test the connection**: Try using the chat feature

## 📊 **Step 6: Monitor and Debug**

### **Netlify Functions (Optional)**

If you want to add serverless functions to Netlify:

1. **Create functions directory**:
   ```bash
   mkdir -p netlify/functions
   ```

2. **Create a simple function**:
   ```python
   # netlify/functions/hello.py
   def handler(event, context):
       return {
           "statusCode": 200,
           "body": "Hello from Netlify Functions!"
       }
   ```

3. **Update `netlify.toml`**:
   ```toml
   [functions]
     directory = "netlify/functions"
   ```

### **Custom Domain (Optional)**

1. Go to **Domain settings** in Netlify
2. Add your custom domain
3. Configure DNS settings

## 🔍 **Troubleshooting**

### **Common Issues**

1. **CORS Errors**:
   - Check that your backend CORS settings include your Netlify domain
   - Verify the API URL is correct

2. **404 Errors**:
   - Ensure `netlify.toml` has the correct publish directory
   - Check that all files are in the right location

3. **API Connection Issues**:
   - Verify your backend is running
   - Check environment variables
   - Test the API endpoint directly

### **Debug Commands**

```bash
# Test backend locally
python -m uvicorn tradchem_llm.main:app --reload

# Test frontend locally
cd tradchem_llm/static
python -m http.server 8000

# Check Netlify build logs
# Go to your Netlify dashboard → Deploys → Click on a deploy
```

## 📈 **Performance Optimization**

### **Frontend Optimization**

1. **Minify assets**:
   ```bash
   # Install minification tools
   npm install -g uglify-js clean-css-cli
   
   # Minify JavaScript
   uglifyjs tradchem_llm/static/js/app.js -o tradchem_llm/static/js/app.min.js
   ```

2. **Enable compression** in `netlify.toml`:
   ```toml
   [[headers]]
     for = "*.js"
     [headers.values]
       Cache-Control = "public, max-age=31536000, immutable"
   ```

### **Backend Optimization**

1. **Add caching headers**
2. **Implement rate limiting**
3. **Use connection pooling**

## 🔒 **Security Considerations**

1. **Environment Variables**: Never commit API keys to Git
2. **HTTPS**: Netlify provides HTTPS by default
3. **CORS**: Restrict origins to your domains only
4. **Input Validation**: Validate all user inputs

## 📚 **Additional Resources**

- [Netlify Documentation](https://docs.netlify.com/)
- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/)
- [Render Documentation](https://render.com/docs)
- [Railway Documentation](https://docs.railway.app/)

## 🎉 **Success!**

Your TradChem LLM application is now deployed and accessible online! 

- **Frontend**: `https://your-site.netlify.app`
- **Backend API**: `https://your-backend-url.com/api`
- **API Documentation**: `https://your-backend-url.com/api/docs`

---

**Need help?** Check the troubleshooting section or create an issue in the GitHub repository. 