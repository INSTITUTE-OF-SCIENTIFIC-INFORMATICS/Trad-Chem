# 🚀 Supabase Backend Setup Guide for TradChem LLM

This guide will help you set up a complete Supabase backend for your TradChem LLM application, replacing the previous Python FastAPI backend.

## 📋 **Prerequisites**

- A Supabase account (free tier available)
- Node.js installed (for Supabase CLI)
- Git repository with your project

## 🏗️ **Step 1: Create Supabase Project**

### **1.1 Create Project on Supabase Dashboard**
1. Go to [supabase.com](https://supabase.com)
2. Sign up/Login to your account
3. Click "New Project"
4. Fill in project details:
   - **Name**: `tradchem-llm`
   - **Database Password**: Choose a strong password
   - **Region**: Select closest to your users
5. Click "Create new project"

### **1.2 Get Project Credentials**
After project creation, go to **Settings** → **API** and note:
- **Project URL**: `https://your-project-id.supabase.co`
- **Anon Key**: `your-anon-key`
- **Service Role Key**: `your-service-role-key` (keep secret)

## 🔧 **Step 2: Install Supabase CLI**

```bash
# Install Supabase CLI globally
npm install -g supabase

# Login to Supabase
supabase login

# Initialize Supabase in your project
supabase init
```

## 📊 **Step 3: Set Up Database Schema**

### **3.1 Run Migration**
```bash
# Apply the database schema
supabase db push
```

### **3.2 Verify Tables**
Go to **Table Editor** in Supabase Dashboard and verify these tables exist:
- `public.users`
- `tradchem.medicines`
- `tradchem.benefits`
- `tradchem.diseases`
- `tradchem.ingredients`
- `tradchem.medicine_systems`
- `tradchem.categories`
- `tradchem.chat_sessions`
- `tradchem.chat_messages`
- `tradchem.user_favorites`
- `tradchem.search_history`

## 🤖 **Step 4: Deploy Edge Functions**

### **4.1 Deploy Chat Function**
```bash
# Deploy the chat edge function
supabase functions deploy chat
```

### **4.2 Set Environment Variables**
In Supabase Dashboard → **Settings** → **Edge Functions**:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 🔐 **Step 5: Configure Authentication**

### **5.1 Enable Email Auth**
1. Go to **Authentication** → **Providers**
2. Enable **Email** provider
3. Configure settings:
   - **Enable sign up**: ✅
   - **Enable email confirmations**: ❌ (for development)
   - **Secure email change**: ✅

### **5.2 Set Site URL**
1. Go to **Authentication** → **URL Configuration**
2. Set **Site URL**: `https://your-netlify-site.netlify.app`
3. Add **Redirect URLs**:
   - `https://your-netlify-site.netlify.app`
   - `http://localhost:3000` (for development)

## 📝 **Step 6: Insert Sample Data**

### **6.1 Medicine Systems**
```sql
INSERT INTO tradchem.medicine_systems (name, description, origin_country) VALUES
('Ayurvedic Medicine', 'Traditional Indian medicine system based on dosha theory', 'India'),
('Traditional Chinese Medicine', 'Ancient Chinese medical system based on qi and yin-yang', 'China'),
('Unani Medicine', 'Islamic traditional medicine based on four humors', 'Middle East'),
('African Traditional Medicine', 'Traditional healing practices from African continent', 'Africa'),
('Indigenous Medicine', 'Traditional medicine from various indigenous cultures', 'Global');
```

### **6.2 Categories**
```sql
INSERT INTO tradchem.categories (name, description) VALUES
('Adaptogens', 'Herbs that help the body adapt to stress'),
('Anti-inflammatory', 'Substances that reduce inflammation'),
('Antioxidants', 'Compounds that protect against oxidative damage'),
('Digestive Health', 'Herbs that support digestive function'),
('Immune Support', 'Substances that enhance immune function'),
('Energy Boosters', 'Herbs that increase energy and vitality');
```

### **6.3 Sample Medicines**
```sql
INSERT INTO tradchem.medicines (product_name, scientific_name, description, traditional_system_id, category_id, source) VALUES
('Turmeric', 'Curcuma longa', 'Golden spice with powerful anti-inflammatory properties', 
 (SELECT id FROM tradchem.medicine_systems WHERE name = 'Ayurvedic Medicine'),
 (SELECT id FROM tradchem.categories WHERE name = 'Anti-inflammatory'),
 'Traditional Ayurvedic texts'),
('Ashwagandha', 'Withania somnifera', 'Adaptogenic herb that helps the body adapt to stress',
 (SELECT id FROM tradchem.medicine_systems WHERE name = 'Ayurvedic Medicine'),
 (SELECT id FROM tradchem.categories WHERE name = 'Adaptogens'),
 'Charaka Samhita'),
('Ginseng', 'Panax ginseng', 'Traditional Chinese herb for energy and vitality',
 (SELECT id FROM tradchem.medicine_systems WHERE name = 'Traditional Chinese Medicine'),
 (SELECT id FROM tradchem.categories WHERE name = 'Energy Boosters'),
 'Shennong Ben Cao Jing');
```

## 🔗 **Step 7: Update Frontend Configuration**

### **7.1 Update Environment Variables**
In your Netlify deployment, add these environment variables:
```
NEXT_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

### **7.2 Update JavaScript Configuration**
In `netlify-deploy/js/app.js`, update:
```javascript
this.supabaseUrl = 'https://your-project-id.supabase.co'
this.supabaseAnonKey = 'your-anon-key'
```

## 🧪 **Step 8: Test the Backend**

### **8.1 Test Authentication**
1. Go to your deployed site
2. Try signing up with an email
3. Verify user appears in **Authentication** → **Users**

### **8.2 Test Chat Function**
1. Sign in to your account
2. Send a message in the chat
3. Check **Edge Functions** → **Logs** for function execution

### **8.3 Test Database Operations**
1. Search for medicines
2. Check **Table Editor** for search history entries
3. Add medicines to favorites
4. Verify data appears in respective tables

## 🔒 **Step 9: Security Configuration**

### **9.1 Row Level Security (RLS)**
All tables have RLS enabled with appropriate policies:
- Public read access for medicines, benefits, diseases
- User-specific access for chat sessions, favorites, search history
- Admin access for data management

### **9.2 API Security**
- CORS configured for your domain
- Rate limiting enabled
- JWT token validation

## 📈 **Step 10: Performance Optimization**

### **10.1 Database Indexes**
Full-text search indexes are created for:
- Medicine names and descriptions
- Benefit and disease names
- Ingredient names

### **10.2 Caching**
- Enable Supabase caching for frequently accessed data
- Use Edge Functions for compute-intensive operations

## 🔄 **Step 11: Real-time Features**

### **11.1 Enable Realtime**
1. Go to **Database** → **Replication**
2. Enable realtime for:
   - `tradchem.chat_messages`
   - `tradchem.user_favorites`

### **11.2 Subscribe to Changes**
The frontend automatically subscribes to real-time updates for:
- New chat messages
- Favorite changes

## 🚀 **Step 12: Production Deployment**

### **12.1 Environment Variables**
Set production environment variables:
```
NEXT_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
OPENAI_API_KEY=your-openai-api-key
```

### **12.2 Domain Configuration**
1. Add your production domain to Supabase
2. Update CORS settings
3. Configure email templates

### **12.3 Monitoring**
1. Set up Supabase monitoring
2. Configure alerts for:
   - Function errors
   - Database performance
   - Authentication issues

## 🛠️ **Troubleshooting**

### **Common Issues**

1. **CORS Errors**:
   - Check domain configuration in Supabase
   - Verify environment variables

2. **Authentication Issues**:
   - Check site URL configuration
   - Verify email provider settings

3. **Function Errors**:
   - Check Edge Function logs
   - Verify environment variables

4. **Database Connection**:
   - Check RLS policies
   - Verify table permissions

### **Debug Commands**
```bash
# Check Supabase status
supabase status

# View function logs
supabase functions logs chat

# Reset database (development only)
supabase db reset

# Generate types
supabase gen types typescript --local > types.ts
```

## 📚 **Next Steps**

1. **Add More Data**: Import traditional medicine data
2. **Enhance AI**: Improve chat function with better prompts
3. **Add Features**: User profiles, medicine reviews, etc.
4. **Scale**: Monitor usage and upgrade plan if needed

## 🎉 **Success!**

Your TradChem LLM application now has a fully functional Supabase backend with:
- ✅ User authentication
- ✅ Real-time chat with AI
- ✅ Traditional medicine database
- ✅ Search functionality
- ✅ User favorites
- ✅ Search history
- ✅ Secure data access

The application is now ready for production use! 🚀 