# 🎯 Frontend-Only Netlify Deployment

If you're still having issues with Netlify trying to install Python dependencies, here's an alternative approach:

## **Option 1: Create a Frontend-Only Branch**

### **Step 1: Create a new branch for frontend only**
```bash
# Create and switch to a new branch
git checkout -b frontend-only

# Remove all Python files
git rm -r tradchem_llm/main.py tradchem_llm/models.py tradchem_llm/config.py tradchem_llm/database.py tradchem_llm/services/ tradchem/ demo.py demo_contribution.py run_server.py requirements.txt

# Keep only static files
git add tradchem_llm/static/
git add netlify.toml
git add .netlifyignore

# Commit changes
git commit -m "Frontend-only deployment"

# Push the branch
git push origin frontend-only
```

### **Step 2: Deploy from the frontend-only branch**
1. Go to Netlify dashboard
2. Create new site from Git
3. Select your repository
4. Choose the `frontend-only` branch
5. Set publish directory: `tradchem_llm/static`
6. Deploy

## **Option 2: Create a Separate Frontend Repository**

### **Step 1: Create a new repository for frontend**
```bash
# Create a new directory
mkdir tradchem-frontend
cd tradchem-frontend

# Copy only frontend files
cp -r ../Trad-Chem/tradchem_llm/static/* .
cp ../Trad-Chem/netlify.toml .
cp ../Trad-Chem/.netlifyignore .

# Initialize git
git init
git add .
git commit -m "Initial frontend commit"

# Create repository on GitHub and push
git remote add origin https://github.com/your-username/tradchem-frontend.git
git push -u origin main
```

### **Step 2: Deploy the frontend repository**
1. Connect the frontend repository to Netlify
2. Set publish directory: `/` (root)
3. Deploy

## **Option 3: Manual Upload (Simplest)**

### **Step 1: Prepare static files**
```bash
# Create a clean deployment directory
mkdir netlify-deploy
cd netlify-deploy

# Copy only static files
cp -r ../tradchem_llm/static/* .

# Create a simple netlify.toml
cat > netlify.toml << EOF
[build]
  publish = "."
  command = ""

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
EOF
```

### **Step 2: Upload to Netlify**
1. Go to [netlify.com](https://netlify.com)
2. Drag and drop the `netlify-deploy` folder
3. Your site will be deployed instantly

## **Option 4: Use Netlify CLI with Specific Directory**

### **Step 1: Install Netlify CLI**
```bash
npm install -g netlify-cli
```

### **Step 2: Deploy specific directory**
```bash
# Navigate to your project
cd Trad-Chem

# Deploy only the static directory
netlify deploy --dir=tradchem_llm/static --prod
```

## **🔧 Troubleshooting**

### **If Netlify still tries to install Python dependencies:**

1. **Check your netlify.toml**:
   ```toml
   [build]
     publish = "tradchem_llm/static"
     command = ""  # Empty command
   ```

2. **Verify .netlifyignore**:
   Make sure `requirements.txt` is in the ignore list

3. **Clear Netlify cache**:
   - Go to your site settings in Netlify
   - Clear the build cache
   - Redeploy

4. **Use manual upload**:
   - Prepare only the static files
   - Drag and drop to Netlify

## **🎯 Recommended Approach**

For the simplest deployment, use **Option 3 (Manual Upload)**:

1. Create the `netlify-deploy` directory with only static files
2. Drag and drop to Netlify
3. Get your live URL instantly

This avoids all build process issues and gives you immediate deployment.

## **📞 Next Steps After Deployment**

1. **Deploy your backend** to Render/Railway/Heroku
2. **Update the API URL** in your frontend JavaScript
3. **Test the connection** between frontend and backend
4. **Configure CORS** on your backend

---

**Need help?** Try the manual upload method first - it's the most reliable for static sites! 