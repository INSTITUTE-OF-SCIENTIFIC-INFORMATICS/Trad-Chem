-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Create custom schema for TradChem data
CREATE SCHEMA IF NOT EXISTS tradchem;

-- Users table (extends Supabase auth.users)
CREATE TABLE IF NOT EXISTS public.users (
    id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    avatar_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Traditional medicine systems
CREATE TABLE IF NOT EXISTS tradchem.medicine_systems (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    origin_country TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Medicine categories
CREATE TABLE IF NOT EXISTS tradchem.categories (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    parent_id UUID REFERENCES tradchem.categories(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Traditional medicines table
CREATE TABLE IF NOT EXISTS tradchem.medicines (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    product_name TEXT NOT NULL,
    scientific_name TEXT,
    common_names TEXT[],
    description TEXT,
    traditional_system_id UUID REFERENCES tradchem.medicine_systems(id),
    category_id UUID REFERENCES tradchem.categories(id),
    geographic_origin TEXT,
    harvesting_season TEXT,
    preparation_method TEXT,
    dosage_info TEXT,
    contraindications TEXT,
    interactions TEXT,
    source TEXT,
    source_url TEXT,
    created_by UUID REFERENCES public.users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Benefits table
CREATE TABLE IF NOT EXISTS tradchem.benefits (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    category TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Diseases/Conditions table
CREATE TABLE IF NOT EXISTS tradchem.diseases (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    category TEXT,
    icd_code TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Medicine-Benefits relationship
CREATE TABLE IF NOT EXISTS tradchem.medicine_benefits (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    medicine_id UUID REFERENCES tradchem.medicines(id) ON DELETE CASCADE,
    benefit_id UUID REFERENCES tradchem.benefits(id) ON DELETE CASCADE,
    evidence_level TEXT CHECK (evidence_level IN ('traditional', 'anecdotal', 'preliminary', 'clinical')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(medicine_id, benefit_id)
);

-- Medicine-Diseases relationship
CREATE TABLE IF NOT EXISTS tradchem.medicine_diseases (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    medicine_id UUID REFERENCES tradchem.medicines(id) ON DELETE CASCADE,
    disease_id UUID REFERENCES tradchem.diseases(id) ON DELETE CASCADE,
    effectiveness_rating INTEGER CHECK (effectiveness_rating >= 1 AND effectiveness_rating <= 5),
    evidence_level TEXT CHECK (evidence_level IN ('traditional', 'anecdotal', 'preliminary', 'clinical')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(medicine_id, disease_id)
);

-- Chemical ingredients table
CREATE TABLE IF NOT EXISTS tradchem.ingredients (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name TEXT NOT NULL,
    scientific_name TEXT,
    smiles_notation TEXT,
    molecular_formula TEXT,
    molecular_weight DECIMAL,
    cas_number TEXT,
    pubchem_id TEXT,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Medicine-Ingredients relationship
CREATE TABLE IF NOT EXISTS tradchem.medicine_ingredients (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    medicine_id UUID REFERENCES tradchem.medicines(id) ON DELETE CASCADE,
    ingredient_id UUID REFERENCES tradchem.ingredients(id) ON DELETE CASCADE,
    concentration TEXT,
    unit TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(medicine_id, ingredient_id)
);

-- Chat sessions table
CREATE TABLE IF NOT EXISTS tradchem.chat_sessions (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    session_name TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Chat messages table
CREATE TABLE IF NOT EXISTS tradchem.chat_messages (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    session_id UUID REFERENCES tradchem.chat_sessions(id) ON DELETE CASCADE,
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    message TEXT NOT NULL,
    response TEXT,
    message_type TEXT CHECK (message_type IN ('user', 'assistant', 'system')) DEFAULT 'user',
    confidence_score DECIMAL CHECK (confidence_score >= 0 AND confidence_score <= 1),
    sources TEXT[],
    medicine_references UUID[],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- User favorites table
CREATE TABLE IF NOT EXISTS tradchem.user_favorites (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    medicine_id UUID REFERENCES tradchem.medicines(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(user_id, medicine_id)
);

-- Search history table
CREATE TABLE IF NOT EXISTS tradchem.search_history (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
    query TEXT NOT NULL,
    search_type TEXT CHECK (search_type IN ('name', 'benefit', 'disease', 'ingredient', 'general')),
    results_count INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_medicines_name ON tradchem.medicines USING gin(to_tsvector('english', product_name));
CREATE INDEX IF NOT EXISTS idx_medicines_scientific_name ON tradchem.medicines USING gin(to_tsvector('english', scientific_name));
CREATE INDEX IF NOT EXISTS idx_medicines_traditional_system ON tradchem.medicines(traditional_system_id);
CREATE INDEX IF NOT EXISTS idx_medicines_category ON tradchem.medicines(category_id);
CREATE INDEX IF NOT EXISTS idx_benefits_name ON tradchem.benefits USING gin(to_tsvector('english', name));
CREATE INDEX IF NOT EXISTS idx_diseases_name ON tradchem.diseases USING gin(to_tsvector('english', name));
CREATE INDEX IF NOT EXISTS idx_ingredients_name ON tradchem.ingredients USING gin(to_tsvector('english', name));
CREATE INDEX IF NOT EXISTS idx_ingredients_smiles ON tradchem.ingredients(smiles_notation);
CREATE INDEX IF NOT EXISTS idx_chat_messages_session ON tradchem.chat_messages(session_id);
CREATE INDEX IF NOT EXISTS idx_chat_messages_user ON tradchem.chat_messages(user_id);
CREATE INDEX IF NOT EXISTS idx_search_history_user ON tradchem.search_history(user_id);
CREATE INDEX IF NOT EXISTS idx_search_history_query ON tradchem.search_history USING gin(to_tsvector('english', query));

-- Create full-text search indexes
CREATE INDEX IF NOT EXISTS idx_medicines_fulltext ON tradchem.medicines USING gin(
    to_tsvector('english', 
        COALESCE(product_name, '') || ' ' || 
        COALESCE(scientific_name, '') || ' ' || 
        COALESCE(description, '')
    )
);

-- Row Level Security (RLS) policies
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;
ALTER TABLE tradchem.medicines ENABLE ROW LEVEL SECURITY;
ALTER TABLE tradchem.chat_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE tradchem.chat_messages ENABLE ROW LEVEL SECURITY;
ALTER TABLE tradchem.user_favorites ENABLE ROW LEVEL SECURITY;
ALTER TABLE tradchem.search_history ENABLE ROW LEVEL SECURITY;

-- Public read access for medicines, benefits, diseases, ingredients
CREATE POLICY "Public read access for medicines" ON tradchem.medicines FOR SELECT USING (true);
CREATE POLICY "Public read access for benefits" ON tradchem.benefits FOR SELECT USING (true);
CREATE POLICY "Public read access for diseases" ON tradchem.diseases FOR SELECT USING (true);
CREATE POLICY "Public read access for ingredients" ON tradchem.ingredients FOR SELECT USING (true);
CREATE POLICY "Public read access for medicine systems" ON tradchem.medicine_systems FOR SELECT USING (true);
CREATE POLICY "Public read access for categories" ON tradchem.categories FOR SELECT USING (true);

-- User-specific policies
CREATE POLICY "Users can view their own profile" ON public.users FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users can update their own profile" ON public.users FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Users can manage their own chat sessions" ON tradchem.chat_sessions 
    FOR ALL USING (auth.uid() = user_id);

CREATE POLICY "Users can manage their own chat messages" ON tradchem.chat_messages 
    FOR ALL USING (auth.uid() = user_id);

CREATE POLICY "Users can manage their own favorites" ON tradchem.user_favorites 
    FOR ALL USING (auth.uid() = user_id);

CREATE POLICY "Users can view their own search history" ON tradchem.search_history 
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own search history" ON tradchem.search_history 
    FOR INSERT WITH CHECK (auth.uid() = user_id);

-- Admin policies (for authenticated users with admin role)
CREATE POLICY "Admins can manage all data" ON tradchem.medicines 
    FOR ALL USING (auth.jwt() ->> 'role' = 'admin');

-- Functions for automatic timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Triggers for updated_at
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON public.users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_medicines_updated_at BEFORE UPDATE ON tradchem.medicines
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_chat_sessions_updated_at BEFORE UPDATE ON tradchem.chat_sessions
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Function to handle user creation
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.users (id, email, full_name, avatar_url)
    VALUES (
        NEW.id,
        NEW.email,
        NEW.raw_user_meta_data->>'full_name',
        NEW.raw_user_meta_data->>'avatar_url'
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Trigger for new user creation
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user(); 