# 🏥 TradChem LLM - Supabase Backend

A comprehensive traditional medicine AI assistant powered by Supabase backend, featuring real-time chat, traditional medicine database, and advanced search capabilities.

## 🚀 **Features**

### **Core Functionality**
- 🤖 **AI Chat Assistant** - Powered by OpenAI with traditional medicine knowledge
- 📚 **Traditional Medicine Database** - Comprehensive database of medicines, benefits, and chemical compounds
- 🔍 **Advanced Search** - Search by name, benefits, diseases, or ingredients
- 👤 **User Authentication** - Secure user accounts with Supabase Auth
- 💬 **Real-time Chat** - Live chat sessions with message history
- ❤️ **Favorites System** - Save and manage favorite medicines
- 📊 **Analytics Dashboard** - Statistics and insights
- 🔬 **SMILES Notation Support** - Chemical structure representation

### **Technical Features**
- 🗄️ **PostgreSQL Database** - Robust data storage with Supabase
- ⚡ **Edge Functions** - Serverless AI chat processing
- 🔄 **Real-time Subscriptions** - Live updates for chat and favorites
- 🔒 **Row Level Security** - Secure data access with RLS policies
- 📱 **Responsive Design** - Apple Design-inspired UI
- 🌐 **CORS Support** - Cross-origin resource sharing
- 📈 **Performance Optimized** - Indexed queries and caching

## 🏗️ **Architecture**

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Supabase      │    │   OpenAI API    │
│   (Netlify)     │◄──►│   Backend       │◄──►│   (AI Chat)     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   PostgreSQL    │
                       │   Database      │
                       └─────────────────┘
```

## 📊 **Database Schema**

### **Core Tables**
- `users` - User profiles and authentication
- `medicines` - Traditional medicine information
- `benefits` - Health benefits and effects
- `diseases` - Medical conditions and diseases
- `ingredients` - Chemical compounds and SMILES notations
- `medicine_systems` - Traditional medicine systems (Ayurveda, TCM, etc.)
- `categories` - Medicine categories and classifications

### **User Data Tables**
- `chat_sessions` - User chat sessions
- `chat_messages` - Individual chat messages
- `user_favorites` - User's favorite medicines
- `search_history` - User search queries

### **Relationship Tables**
- `medicine_benefits` - Medicine-benefit relationships
- `medicine_diseases` - Medicine-disease relationships
- `medicine_ingredients` - Medicine-ingredient relationships

## 🚀 **Quick Start**

### **1. Prerequisites**
```bash
# Install Supabase CLI
npm install -g supabase

# Install project dependencies
npm install
```

### **2. Setup Supabase Project**
```bash
# Login to Supabase
supabase login

# Initialize project
supabase init

# Start local development
supabase start
```

### **3. Deploy Database Schema**
```bash
# Deploy schema to local development
supabase db push

# Or deploy to production
supabase db push --linked
```

### **4. Deploy Edge Functions**
```bash
# Deploy chat function
supabase functions deploy chat

# Set environment variables
supabase secrets set OPENAI_API_KEY=your_openai_key
```

### **5. Configure Frontend**
```bash
# Update environment variables
cp .env.example .env.local

# Edit .env.local with your Supabase credentials
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

## 🔧 **Configuration**

### **Environment Variables**
```bash
# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# OpenAI Configuration
OPENAI_API_KEY=your-openai-api-key

# Application Configuration
NEXT_PUBLIC_APP_URL=https://your-app-domain.com
NODE_ENV=production
```

### **Supabase Settings**
1. **Authentication**:
   - Enable Email provider
   - Configure site URL and redirect URLs
   - Set up email templates

2. **Database**:
   - Enable Row Level Security (RLS)
   - Configure backup schedules
   - Set up monitoring

3. **Edge Functions**:
   - Deploy chat function
   - Set environment variables
   - Configure CORS

## 📱 **Frontend Integration**

### **Supabase Client Setup**
```javascript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
)
```

### **Authentication**
```javascript
// Sign up
const { data, error } = await supabase.auth.signUp({
  email: 'user@example.com',
  password: 'password'
})

// Sign in
const { data, error } = await supabase.auth.signInWithPassword({
  email: 'user@example.com',
  password: 'password'
})
```

### **Database Operations**
```javascript
// Get medicines
const { data, error } = await supabase
  .from('tradchem.medicines')
  .select('*')
  .limit(10)

// Search medicines
const { data, error } = await supabase
  .from('tradchem.medicines')
  .select('*')
  .or(`product_name.ilike.%${query}%`)
```

### **Real-time Subscriptions**
```javascript
// Subscribe to chat messages
const subscription = supabase
  .channel('chat_messages')
  .on('postgres_changes', {
    event: 'INSERT',
    schema: 'tradchem',
    table: 'chat_messages'
  }, (payload) => {
    console.log('New message:', payload.new)
  })
  .subscribe()
```

## 🤖 **AI Chat Function**

### **Edge Function Structure**
```typescript
// supabase/functions/chat/index.ts
export async function handler(req: Request) {
  // 1. Authenticate user
  // 2. Search database for relevant medicines
  // 3. Call OpenAI API with context
  // 4. Save chat message to database
  // 5. Return AI response
}
```

### **Chat Features**
- **Context-Aware Responses** - Uses database knowledge
- **Medicine References** - Links to relevant medicines
- **Source Citations** - Provides source information
- **Confidence Scoring** - Indicates response reliability
- **Multi-language Support** - Handles various languages

## 🔍 **Search Functionality**

### **Search Types**
1. **Name Search** - Search by medicine or ingredient names
2. **Benefit Search** - Find medicines by health benefits
3. **Disease Search** - Find medicines for specific conditions
4. **Ingredient Search** - Search by chemical compounds
5. **Full-text Search** - Comprehensive search across all fields

### **Search Implementation**
```sql
-- Full-text search with ranking
SELECT *, ts_rank(to_tsvector('english', product_name || ' ' || description), query) as rank
FROM tradchem.medicines
WHERE to_tsvector('english', product_name || ' ' || description) @@ query
ORDER BY rank DESC;
```

## 🔒 **Security**

### **Row Level Security (RLS)**
```sql
-- Public read access for medicines
CREATE POLICY "Public read access for medicines" 
ON tradchem.medicines FOR SELECT USING (true);

-- User-specific access for favorites
CREATE POLICY "Users can manage their own favorites" 
ON tradchem.user_favorites FOR ALL USING (auth.uid() = user_id);
```

### **Authentication**
- JWT-based authentication
- Secure session management
- Email verification
- Password policies

### **Data Protection**
- Encrypted data transmission
- Secure API endpoints
- Input validation
- SQL injection prevention

## 📊 **Performance**

### **Database Optimization**
- **Indexes** - Full-text search and foreign key indexes
- **Query Optimization** - Efficient joins and filtering
- **Connection Pooling** - Optimized database connections
- **Caching** - Supabase caching for frequently accessed data

### **Frontend Optimization**
- **Lazy Loading** - Load data on demand
- **Pagination** - Limit result sets
- **Debounced Search** - Optimize search queries
- **Real-time Updates** - Efficient subscription management

## 🧪 **Testing**

### **Database Testing**
```bash
# Run database tests
supabase db test

# Check schema consistency
supabase db diff
```

### **Function Testing**
```bash
# Test edge functions locally
supabase functions serve

# Test specific function
curl -X POST http://localhost:54321/functions/v1/chat \
  -H "Authorization: Bearer YOUR_ANON_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me about turmeric"}'
```

### **Frontend Testing**
```bash
# Run frontend tests
npm test

# Test authentication flow
npm run test:auth
```

## 📈 **Monitoring**

### **Supabase Dashboard**
- **Database Performance** - Query performance and slow queries
- **Function Logs** - Edge function execution logs
- **Authentication** - User sign-ups and sign-ins
- **Storage Usage** - Database and storage metrics

### **Custom Monitoring**
```javascript
// Track user interactions
await supabase
  .from('tradchem.user_analytics')
  .insert({
    user_id: user.id,
    action: 'search',
    query: searchTerm,
    timestamp: new Date()
  })
```

## 🚀 **Deployment**

### **Production Deployment**
```bash
# Deploy to production
./deploy-supabase.sh

# Or manual deployment
supabase db push --linked
supabase functions deploy
```

### **Environment Setup**
1. **Supabase Project** - Create production project
2. **Domain Configuration** - Set up custom domains
3. **SSL Certificates** - Enable HTTPS
4. **CDN Configuration** - Optimize content delivery

### **CI/CD Pipeline**
```yaml
# .github/workflows/deploy.yml
name: Deploy to Supabase
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: supabase/setup-cli@v1
      - run: supabase db push --linked
      - run: supabase functions deploy
```

## 🤝 **Contributing**

### **Development Workflow**
1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

### **Code Standards**
- **TypeScript** - Use TypeScript for type safety
- **ESLint** - Follow linting rules
- **Prettier** - Consistent code formatting
- **Comments** - Document complex logic

## 📚 **API Documentation**

### **Authentication Endpoints**
- `POST /auth/v1/signup` - User registration
- `POST /auth/v1/signin` - User login
- `POST /auth/v1/signout` - User logout

### **Database Endpoints**
- `GET /rest/v1/medicines` - Get medicines
- `POST /rest/v1/medicines` - Create medicine
- `GET /rest/v1/chat_messages` - Get chat messages
- `POST /rest/v1/chat_messages` - Create chat message

### **Edge Function Endpoints**
- `POST /functions/v1/chat` - AI chat endpoint

## 🆘 **Support**

### **Common Issues**
1. **CORS Errors** - Check domain configuration
2. **Authentication Issues** - Verify JWT tokens
3. **Function Errors** - Check Edge Function logs
4. **Database Errors** - Verify RLS policies

### **Getting Help**
- **Documentation** - Check this README
- **Issues** - Create GitHub issue
- **Discussions** - Use GitHub Discussions
- **Email** - Contact support team

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- **Supabase** - For the amazing backend platform
- **OpenAI** - For AI chat capabilities
- **Traditional Medicine Community** - For knowledge and data
- **Contributors** - For code contributions and feedback

---

**Built with ❤️ by SaltyHeart**

*Empowering traditional medicine with modern technology* 