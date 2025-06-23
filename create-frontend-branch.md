# Create Frontend-Only Branch for Netlify

## Step 1: Create a new branch
```bash
git checkout -b frontend-only
```

## Step 2: Remove Python files from this branch
```bash
# Remove Python files and dependencies
git rm requirements.txt
git rm -r tradchem_llm/main.py tradchem_llm/models.py tradchem_llm/config.py tradchem_llm/database.py tradchem_llm/services/
git rm -r tradchem/
git rm demo.py demo_contribution.py run_server.py

# Keep only static files and config
git add tradchem_llm/static/
git add netlify.toml
git add .netlifyignore

# Commit changes
git commit -m "Frontend-only branch for Netlify deployment"

# Push the branch
git push origin frontend-only
```

## Step 3: Deploy from frontend-only branch
1. Go to Netlify dashboard
2. Create new site from Git
3. Select your repository
4. Choose the `frontend-only` branch
5. Set publish directory: `tradchem_llm/static`
6. Deploy

This branch will only contain the static files needed for Netlify deployment. 