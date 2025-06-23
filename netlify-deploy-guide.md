# 🚀 Netlify CI/CD Setup Guide for Trad-Chem LLM

This guide will help you set up continuous integration and deployment (CI/CD) for your Trad-Chem LLM project using Netlify.

## 📋 Prerequisites

1. **GitHub Account**: Your code should be in a GitHub repository
2. **Netlify Account**: Sign up at [netlify.com](https://netlify.com)
3. **OpenAI API Key**: For LLM functionality (optional)

## 🔧 Setup Steps

### Step 1: Prepare Your Repository

Your repository should have the following structure:
```
tradchem-llm/
├── tradchem_llm/           # Main application
├── netlify/               # Netlify configuration
│   └── functions/         # Serverless functions
├── netlify.toml          # Netlify configuration
├── package.json          # Frontend build config
├── .github/workflows/    # GitHub Actions
└── README.md
```

### Step 2: Set Up Netlify Site

1. **Connect to GitHub**:
   - Go to [Netlify Dashboard](https://app.netlify.com)
   - Click "New site from Git"
   - Choose GitHub and select your repository

2. **Configure Build Settings**:
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`
   - **Functions directory**: `netlify/functions`

3. **Set Environment Variables**:
   - Go to Site settings → Environment variables
   - Add the following variables:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ANTHROPIC_API_KEY=your_anthropic_api_key
     TRADCHEM_DATABASE_PATH=path/to/database
     ```

### Step 3: Configure GitHub Secrets

1. **Get Netlify Tokens**:
   - Go to Netlify User settings → Applications → Personal access tokens
   - Create a new token

2. **Get Site ID**:
   - Go to your site settings in Netlify
   - Copy the Site ID

3. **Add GitHub Secrets**:
   - Go to your GitHub repository → Settings → Secrets and variables → Actions
   - Add the following secrets:
     ```
     NETLIFY_AUTH_TOKEN=your_netlify_token
     NETLIFY_SITE_ID=your_site_id
     ```

### Step 4: Deploy

1. **Push to Main Branch**:
   ```bash
   git add .
   git commit -m "Setup Netlify CI/CD"
   git push origin main
   ```

2. **Monitor Deployment**:
   - Check GitHub Actions tab for build status
   - Check Netlify dashboard for deployment status

## 🔄 CI/CD Workflow

### What Happens on Each Push:

1. **GitHub Actions Trigger**:
   - Runs tests
   - Checks code quality
   - Builds frontend

2. **Netlify Deployment**:
   - Deploys static frontend
   - Deploys serverless functions
   - Updates live site

3. **Automatic Updates**:
   - Every push to main branch triggers deployment
   - Pull requests create preview deployments

## 🌐 Access Your Application

After deployment, your application will be available at:
- **Production**: `https://your-site-name.netlify.app`
- **Preview**: `https://deploy-preview-{PR_NUMBER}--your-site-name.netlify.app`

## 📊 Monitoring and Analytics

### Netlify Analytics:
- Page views and traffic
- Function invocations
- Performance metrics
- Error tracking

### GitHub Actions:
- Build status
- Test results
- Deployment logs

## 🔧 Customization Options

### Custom Domain:
1. Go to Netlify Site settings → Domain management
2. Add your custom domain
3. Configure DNS settings

### Environment-Specific Configs:
```toml
# netlify.toml
[context.production.environment]
  OPENAI_API_KEY = "production_key"

[context.deploy-preview.environment]
  OPENAI_API_KEY = "preview_key"
```

### Function Configuration:
```toml
# netlify.toml
[functions]
  directory = "netlify/functions"
  node_bundler = "esbuild"
```

## 🐛 Troubleshooting

### Common Issues:

1. **Build Failures**:
   - Check GitHub Actions logs
   - Verify all dependencies are installed
   - Ensure Python version compatibility

2. **Function Errors**:
   - Check Netlify function logs
   - Verify environment variables
   - Test functions locally

3. **CORS Issues**:
   - Check `netlify.toml` headers configuration
   - Verify API endpoint URLs

### Debug Commands:

```bash
# Test locally
netlify dev

# Check function logs
netlify functions:list
netlify functions:invoke api

# Deploy manually
netlify deploy --prod
```

## 📈 Performance Optimization

### Frontend:
- Minify CSS/JS
- Optimize images
- Use CDN for static assets

### Functions:
- Keep functions lightweight
- Use caching where possible
- Optimize cold starts

### Database:
- Use connection pooling
- Implement caching
- Optimize queries

## 🔒 Security Considerations

1. **Environment Variables**:
   - Never commit API keys to repository
   - Use Netlify environment variables
   - Rotate keys regularly

2. **CORS Configuration**:
   - Restrict origins in production
   - Validate request headers
   - Implement rate limiting

3. **Function Security**:
   - Validate input data
   - Implement authentication
   - Use HTTPS only

## 📝 Best Practices

1. **Code Quality**:
   - Run tests before deployment
   - Use linting and formatting
   - Review pull requests

2. **Deployment**:
   - Use feature branches
   - Test in preview environments
   - Monitor deployment health

3. **Monitoring**:
   - Set up error tracking
   - Monitor performance
   - Track user analytics

## 🎯 Next Steps

1. **Set up monitoring** with tools like Sentry
2. **Configure custom domain** for production
3. **Implement authentication** for protected endpoints
4. **Add analytics** to track usage
5. **Set up backup** for database

## 📞 Support

- **Netlify Docs**: [docs.netlify.com](https://docs.netlify.com)
- **GitHub Actions**: [docs.github.com/en/actions](https://docs.github.com/en/actions)
- **Community**: [community.netlify.com](https://community.netlify.com)

---

Your Trad-Chem LLM application is now ready for automated deployment with Netlify! 🚀 