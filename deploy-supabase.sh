#!/bin/bash

# TradChem LLM Supabase Deployment Script
# This script sets up and deploys the complete Supabase backend

set -e  # Exit on any error

echo "🚀 Starting TradChem LLM Supabase Deployment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Supabase CLI is installed
check_supabase_cli() {
    print_status "Checking Supabase CLI installation..."
    if ! command -v supabase &> /dev/null; then
        print_error "Supabase CLI is not installed. Please install it first:"
        echo "npm install -g supabase"
        exit 1
    fi
    print_success "Supabase CLI is installed"
}

# Check if user is logged in
check_supabase_login() {
    print_status "Checking Supabase login status..."
    if ! supabase status &> /dev/null; then
        print_warning "You are not logged in to Supabase. Please login:"
        echo "supabase login"
        exit 1
    fi
    print_success "Logged in to Supabase"
}

# Initialize Supabase project
init_supabase() {
    print_status "Initializing Supabase project..."
    if [ ! -f "supabase/config.toml" ]; then
        supabase init
        print_success "Supabase project initialized"
    else
        print_status "Supabase project already initialized"
    fi
}

# Deploy database schema
deploy_database() {
    print_status "Deploying database schema..."
    supabase db push
    print_success "Database schema deployed"
}

# Deploy Edge Functions
deploy_functions() {
    print_status "Deploying Edge Functions..."
    
    # Deploy chat function
    if [ -d "supabase/functions/chat" ]; then
        supabase functions deploy chat
        print_success "Chat function deployed"
    else
        print_warning "Chat function directory not found"
    fi
    
    # Deploy other functions if they exist
    for func in $(ls supabase/functions/ 2>/dev/null | grep -v chat); do
        if [ -d "supabase/functions/$func" ]; then
            supabase functions deploy $func
            print_success "$func function deployed"
        fi
    done
}

# Insert sample data
insert_sample_data() {
    print_status "Inserting sample data..."
    
    # Check if sample data SQL file exists
    if [ -f "supabase/seed.sql" ]; then
        supabase db reset --linked
        print_success "Sample data inserted"
    else
        print_warning "No seed.sql file found. Creating basic sample data..."
        
        # Create basic sample data
        cat > supabase/seed.sql << 'EOF'
-- Insert basic medicine systems
INSERT INTO tradchem.medicine_systems (name, description, origin_country) VALUES
('Ayurvedic Medicine', 'Traditional Indian medicine system based on dosha theory', 'India'),
('Traditional Chinese Medicine', 'Ancient Chinese medical system based on qi and yin-yang', 'China'),
('Unani Medicine', 'Islamic traditional medicine based on four humors', 'Middle East')
ON CONFLICT (name) DO NOTHING;

-- Insert basic categories
INSERT INTO tradchem.categories (name, description) VALUES
('Adaptogens', 'Herbs that help the body adapt to stress'),
('Anti-inflammatory', 'Substances that reduce inflammation'),
('Antioxidants', 'Compounds that protect against oxidative damage'),
('Digestive Health', 'Herbs that support digestive function'),
('Immune Support', 'Substances that enhance immune function')
ON CONFLICT (name) DO NOTHING;

-- Insert sample medicines
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
 (SELECT id FROM tradchem.categories WHERE name = 'Adaptogens'),
 'Shennong Ben Cao Jing')
ON CONFLICT (product_name) DO NOTHING;
EOF
        
        supabase db reset --linked
        print_success "Basic sample data inserted"
    fi
}

# Generate TypeScript types
generate_types() {
    print_status "Generating TypeScript types..."
    supabase gen types typescript --local > types.ts
    print_success "TypeScript types generated"
}

# Setup environment variables
setup_env() {
    print_status "Setting up environment variables..."
    
    # Get project info
    PROJECT_URL=$(supabase status --output json | jq -r '.api.url' 2>/dev/null || echo "")
    ANON_KEY=$(supabase status --output json | jq -r '.api.anon_key' 2>/dev/null || echo "")
    
    if [ -n "$PROJECT_URL" ] && [ -n "$ANON_KEY" ]; then
        # Create .env.local file
        cat > .env.local << EOF
# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=$PROJECT_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY=$ANON_KEY

# Application Configuration
NEXT_PUBLIC_APP_URL=http://localhost:3000
NODE_ENV=development
EOF
        print_success "Environment variables configured"
        print_status "Project URL: $PROJECT_URL"
        print_status "Anon Key: $ANON_KEY"
    else
        print_warning "Could not automatically get project credentials"
        print_status "Please manually configure your .env.local file"
    fi
}

# Start local development
start_local() {
    print_status "Starting local Supabase development environment..."
    supabase start
    print_success "Local Supabase environment started"
    
    # Show status
    supabase status
}

# Main deployment function
main() {
    echo "🎯 TradChem LLM Supabase Deployment"
    echo "=================================="
    
    # Run all deployment steps
    check_supabase_cli
    check_supabase_login
    init_supabase
    deploy_database
    deploy_functions
    insert_sample_data
    generate_types
    setup_env
    
    print_success "🎉 Supabase backend deployment completed!"
    
    echo ""
    echo "📋 Next Steps:"
    echo "1. Update your frontend configuration with the provided credentials"
    echo "2. Test the authentication system"
    echo "3. Test the chat functionality"
    echo "4. Deploy your frontend to Netlify"
    echo ""
    echo "🔗 Useful Commands:"
    echo "- Start local development: ./deploy-supabase.sh --local"
    echo "- View logs: supabase functions logs"
    echo "- Check status: supabase status"
    echo "- Reset database: supabase db reset"
}

# Handle command line arguments
case "${1:-}" in
    --local)
        start_local
        ;;
    --help|-h)
        echo "Usage: $0 [OPTIONS]"
        echo ""
        echo "Options:"
        echo "  --local    Start local development environment"
        echo "  --help     Show this help message"
        echo ""
        echo "Examples:"
        echo "  $0          # Deploy to production"
        echo "  $0 --local  # Start local development"
        ;;
    *)
        main
        ;;
esac 