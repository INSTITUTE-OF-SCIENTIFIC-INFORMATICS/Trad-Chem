#!/bin/bash

# TradChem LLM Netlify Deployment Script
# This script prepares and deploys the frontend to Netlify

echo "🌿 TradChem LLM - Netlify Deployment Script"
echo "=========================================="

# Check if Netlify CLI is installed
if ! command -v netlify &> /dev/null; then
    echo "❌ Netlify CLI not found. Installing..."
    npm install -g netlify-cli
fi

# Create deployment directory
echo "📁 Creating deployment directory..."
rm -rf netlify-deploy
mkdir netlify-deploy

# Copy static files
echo "📋 Copying static files..."
cp -r tradchem_llm/static/* netlify-deploy/

# Copy Netlify configuration
echo "⚙️ Copying Netlify configuration..."
cp netlify.toml netlify-deploy/

# Check if we're in a Git repository
if [ -d ".git" ]; then
    echo "🔗 Git repository detected"
    
    # Deploy using Netlify CLI
    echo "🚀 Deploying to Netlify..."
    cd netlify-deploy
    
    # Check if user is logged in to Netlify
    if ! netlify status &> /dev/null; then
        echo "🔐 Please log in to Netlify..."
        netlify login
    fi
    
    # Deploy
    netlify deploy --prod --dir=.
    
    echo "✅ Deployment completed!"
    echo "🌐 Your site is now live at the URL shown above"
    
else
    echo "📦 No Git repository detected"
    echo "📁 Static files prepared in 'netlify-deploy' directory"
    echo "📤 You can manually upload this folder to Netlify"
    echo ""
    echo "To deploy manually:"
    echo "1. Go to https://app.netlify.com"
    echo "2. Drag and drop the 'netlify-deploy' folder"
    echo "3. Your site will be deployed automatically"
fi

echo ""
echo "🎯 Next steps:"
echo "1. Deploy your backend to Render/Railway/Heroku"
echo "2. Update the API URL in js/app.js"
echo "3. Test the connection between frontend and backend"
echo ""
echo "📚 For detailed instructions, see: netlify-deploy-guide.md" 