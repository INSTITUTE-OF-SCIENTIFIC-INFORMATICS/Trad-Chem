// TradChem LLM Frontend Application with Supabase Backend
// This file handles all frontend functionality and Supabase communication

class TradChemApp {
    constructor() {
        this.supabaseUrl = 'https://your-project.supabase.co' // Replace with your Supabase URL
        this.supabaseAnonKey = 'your-anon-key' // Replace with your Supabase anon key
        this.supabase = null
        this.currentUser = null
        this.currentSession = null
        this.chatMessages = []
        this.isLoading = false
        this.init()
    }

    async init() {
        await this.initializeSupabase()
        this.bindEvents()
        await this.loadStatistics()
        await this.loadRecentMedicines()
        this.setupAuthListener()
    }

    async initializeSupabase() {
        // Load Supabase client
        if (typeof window !== 'undefined') {
            const { createClient } = await import('https://esm.sh/@supabase/supabase-js@2')
            this.supabase = createClient(this.supabaseUrl, this.supabaseAnonKey)
            
            // Get current session
            const { data: { session } } = await this.supabase.auth.getSession()
            this.currentSession = session
            this.currentUser = session?.user || null
        }
    }

    setupAuthListener() {
        if (this.supabase) {
            this.supabase.auth.onAuthStateChange((event, session) => {
                this.currentSession = session
                this.currentUser = session?.user || null
                this.updateAuthUI()
            })
        }
    }

    updateAuthUI() {
        const authSection = document.getElementById('authSection')
        const userSection = document.getElementById('userSection')
        
        if (this.currentUser) {
            if (authSection) authSection.style.display = 'none'
            if (userSection) {
                userSection.style.display = 'block'
                userSection.innerHTML = `
                    <div class="d-flex align-items-center">
                        <span class="me-2">Welcome, ${this.currentUser.email}</span>
                        <button class="btn btn-outline-danger btn-sm" onclick="app.signOut()">Sign Out</button>
                    </div>
                `
            }
        } else {
            if (authSection) authSection.style.display = 'block'
            if (userSection) userSection.style.display = 'none'
        }
    }

    bindEvents() {
        // Chat functionality
        const sendButton = document.getElementById('sendButton')
        const messageInput = document.getElementById('messageInput')
        
        if (sendButton) {
            sendButton.addEventListener('click', () => this.sendMessage())
        }
        
        if (messageInput) {
            messageInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault()
                    this.sendMessage()
                }
            })
        }

        // Search functionality
        const searchInput = document.getElementById('searchInput')
        const searchButton = document.getElementById('searchButton')
        
        if (searchButton) {
            searchButton.addEventListener('click', () => this.searchMedicines())
        }
        
        if (searchInput) {
            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault()
                    this.searchMedicines()
                }
            })
        }

        // Add medicine form
        const addMedicineForm = document.getElementById('addMedicineForm')
        if (addMedicineForm) {
            addMedicineForm.addEventListener('submit', (e) => {
                e.preventDefault()
                this.addMedicine()
            })
        }

        // Auth forms
        const signInForm = document.getElementById('signInForm')
        const signUpForm = document.getElementById('signUpForm')
        
        if (signInForm) {
            signInForm.addEventListener('submit', (e) => {
                e.preventDefault()
                this.signIn()
            })
        }
        
        if (signUpForm) {
            signUpForm.addEventListener('submit', (e) => {
                e.preventDefault()
                this.signUp()
            })
        }
    }

    async signIn() {
        const email = document.getElementById('signInEmail').value
        const password = document.getElementById('signInPassword').value
        
        if (!email || !password) {
            this.showError('Please enter both email and password')
            return
        }

        try {
            const { data, error } = await this.supabase.auth.signInWithPassword({
                email,
                password
            })

            if (error) throw error

            this.showSuccess('Signed in successfully!')
            document.getElementById('signInForm').reset()
        } catch (error) {
            this.showError(error.message)
        }
    }

    async signUp() {
        const email = document.getElementById('signUpEmail').value
        const password = document.getElementById('signUpPassword').value
        const fullName = document.getElementById('signUpName').value
        
        if (!email || !password) {
            this.showError('Please enter both email and password')
            return
        }

        try {
            const { data, error } = await this.supabase.auth.signUp({
                email,
                password,
                options: {
                    data: {
                        full_name: fullName
                    }
                }
            })

            if (error) throw error

            this.showSuccess('Account created! Please check your email to verify your account.')
            document.getElementById('signUpForm').reset()
        } catch (error) {
            this.showError(error.message)
        }
    }

    async signOut() {
        try {
            const { error } = await this.supabase.auth.signOut()
            if (error) throw error
            this.showSuccess('Signed out successfully!')
        } catch (error) {
            this.showError(error.message)
        }
    }

    async sendMessage() {
        const messageInput = document.getElementById('messageInput')
        const message = messageInput.value.trim()
        
        if (!message || this.isLoading) return

        // Add user message to chat
        this.addChatMessage('user', message)
        messageInput.value = ''
        
        this.setLoading(true)

        try {
            // Create or get chat session
            let sessionId = this.currentSession?.id
            if (!sessionId && this.currentUser) {
                const { data: session } = await this.supabase
                    .from('tradchem.chat_sessions')
                    .insert({
                        user_id: this.currentUser.id,
                        session_name: `Chat ${new Date().toLocaleString()}`
                    })
                    .select()
                    .single()
                sessionId = session?.id
            }

            // Call Supabase Edge Function for AI response
            const { data, error } = await this.supabase.functions.invoke('chat', {
                body: {
                    message,
                    sessionId,
                    context: 'traditional medicine'
                }
            })

            if (error) throw error

            // Add AI response to chat
            this.addChatMessage('assistant', data.response, data.sources)
            
        } catch (error) {
            console.error('Error sending message:', error)
            this.addChatMessage('assistant', 'Sorry, I\'m having trouble connecting. Please try again later.')
        } finally {
            this.setLoading(false)
        }
    }

    addChatMessage(sender, content, sources = []) {
        const chatMessages = document.getElementById('chatMessages')
        const messageDiv = document.createElement('div')
        messageDiv.className = `message ${sender}`
        
        const avatar = document.createElement('div')
        avatar.className = `message-avatar ${sender}-avatar`
        avatar.innerHTML = sender === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>'
        
        const messageContent = document.createElement('div')
        messageContent.className = 'message-content'
        messageContent.innerHTML = content
        
        if (sources && sources.length > 0) {
            messageContent.innerHTML += '<br><small class="text-muted">Sources: ' + sources.join(', ') + '</small>'
        }
        
        messageDiv.appendChild(avatar)
        messageDiv.appendChild(messageContent)
        chatMessages.appendChild(messageDiv)
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight
        
        this.chatMessages.push({ sender, content, timestamp: new Date() })
    }

    setLoading(loading) {
        this.isLoading = loading
        const sendButton = document.getElementById('sendButton')
        if (sendButton) {
            sendButton.disabled = loading
            sendButton.innerHTML = loading ? '<i class="fas fa-spinner fa-spin"></i>' : '<i class="fas fa-paper-plane"></i>'
        }
    }

    async searchMedicines() {
        const searchInput = document.getElementById('searchInput')
        const query = searchInput.value.trim()
        
        if (!query) return

        try {
            const { data, error } = await this.supabase
                .from('tradchem.medicines')
                .select(`
                    *,
                    traditional_system:medicine_systems(name),
                    category:categories(name),
                    benefits:medicine_benefits(benefit:benefits(name, description)),
                    diseases:medicine_diseases(disease:diseases(name, description)),
                    ingredients:medicine_ingredients(ingredient:ingredients(name, smiles_notation, molecular_weight))
                `)
                .or(`product_name.ilike.%${query}%,scientific_name.ilike.%${query}%,description.ilike.%${query}%`)
                .limit(20)

            if (error) throw error

            this.displaySearchResults(data || [])
            
            // Save search history if user is logged in
            if (this.currentUser) {
                await this.supabase
                    .from('tradchem.search_history')
                    .insert({
                        user_id: this.currentUser.id,
                        query,
                        search_type: 'general',
                        results_count: data?.length || 0
                    })
            }
        } catch (error) {
            console.error('Error searching medicines:', error)
            this.showError('Error searching medicines. Please try again.')
        }
    }

    displaySearchResults(medicines) {
        const resultsContainer = document.getElementById('searchResults')
        if (!resultsContainer) return

        resultsContainer.innerHTML = ''
        
        if (medicines.length === 0) {
            resultsContainer.innerHTML = '<p class="text-muted">No medicines found.</p>'
            return
        }

        medicines.forEach(medicine => {
            const medicineCard = document.createElement('div')
            medicineCard.className = 'medicine-card'
            medicineCard.innerHTML = `
                <div class="medicine-name">${medicine.product_name}</div>
                <div class="medicine-benefits">
                    <strong>Benefits:</strong> ${medicine.benefits?.map(b => b.benefit.name).join(', ') || 'N/A'}
                </div>
                <div class="medicine-system">
                    <small class="text-muted">${medicine.traditional_system?.name || 'Unknown system'}</small>
                </div>
                ${this.currentUser ? `
                    <button class="btn btn-sm btn-outline-primary mt-2" onclick="app.addToFavorites('${medicine.id}')">
                        <i class="fas fa-heart"></i> Add to Favorites
                    </button>
                ` : ''}
            `
            resultsContainer.appendChild(medicineCard)
        })
    }

    async loadStatistics() {
        try {
            const [medicines, benefits, diseases, ingredients, systems] = await Promise.all([
                this.supabase.from('tradchem.medicines').select('*', { count: 'exact', head: true }),
                this.supabase.from('tradchem.benefits').select('*', { count: 'exact', head: true }),
                this.supabase.from('tradchem.diseases').select('*', { count: 'exact', head: true }),
                this.supabase.from('tradchem.ingredients').select('*', { count: 'exact', head: true }),
                this.supabase.from('tradchem.medicine_systems').select('*', { count: 'exact', head: true })
            ])

            const stats = {
                total_medicines: medicines.count || 0,
                total_benefits: benefits.count || 0,
                total_diseases: diseases.count || 0,
                total_ingredients: ingredients.count || 0,
                total_systems: systems.count || 0
            }

            this.updateStatistics(stats)
        } catch (error) {
            console.error('Error loading statistics:', error)
        }
    }

    updateStatistics(stats) {
        const statsContainer = document.getElementById('statsContainer')
        if (!statsContainer) return

        statsContainer.innerHTML = `
            <div class="row">
                <div class="col-md-3">
                    <div class="stat-item">
                        <div class="stat-number">${stats.total_medicines}</div>
                        <div class="stat-label">Medicines</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="stat-item">
                        <div class="stat-number">${stats.total_benefits}</div>
                        <div class="stat-label">Benefits</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="stat-item">
                        <div class="stat-number">${stats.total_diseases}</div>
                        <div class="stat-label">Diseases</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="stat-item">
                        <div class="stat-number">${stats.total_ingredients}</div>
                        <div class="stat-label">Ingredients</div>
                    </div>
                </div>
            </div>
        `
    }

    async loadRecentMedicines() {
        try {
            const { data, error } = await this.supabase
                .from('tradchem.medicines')
                .select('product_name')
                .limit(5)
                .order('created_at', { ascending: false })

            if (error) throw error

            this.displayRecentMedicines(data || [])
        } catch (error) {
            console.error('Error loading recent medicines:', error)
        }
    }

    displayRecentMedicines(medicines) {
        const recentContainer = document.getElementById('recentMedicines')
        if (!recentContainer) return

        recentContainer.innerHTML = ''
        
        medicines.forEach(medicine => {
            const medicineItem = document.createElement('div')
            medicineItem.className = 'list-group-item'
            medicineItem.textContent = medicine.product_name
            recentContainer.appendChild(medicineItem)
        })
    }

    async addToFavorites(medicineId) {
        if (!this.currentUser) {
            this.showError('Please sign in to add favorites')
            return
        }

        try {
            const { error } = await this.supabase
                .from('tradchem.user_favorites')
                .insert({
                    user_id: this.currentUser.id,
                    medicine_id: medicineId
                })

            if (error) throw error

            this.showSuccess('Added to favorites!')
        } catch (error) {
            console.error('Error adding to favorites:', error)
            this.showError('Error adding to favorites')
        }
    }

    async addMedicine() {
        if (!this.currentUser) {
            this.showError('Please sign in to add medicines')
            return
        }

        const form = document.getElementById('addMedicineForm')
        const formData = new FormData(form)
        
        const medicineData = {
            product_name: formData.get('product_name'),
            scientific_name: formData.get('scientific_name'),
            description: formData.get('description'),
            source: formData.get('source'),
            traditional_system_id: formData.get('traditional_system_id'),
            category_id: formData.get('category_id'),
            created_by: this.currentUser.id
        }

        try {
            const { error } = await this.supabase
                .from('tradchem.medicines')
                .insert(medicineData)

            if (error) throw error

            this.showSuccess('Medicine added successfully!')
            form.reset()
            this.loadStatistics()
            this.loadRecentMedicines()
        } catch (error) {
            console.error('Error adding medicine:', error)
            this.showError('Error adding medicine. Please try again.')
        }
    }

    showSuccess(message) {
        this.showAlert(message, 'success')
    }

    showError(message) {
        this.showAlert(message, 'danger')
    }

    showAlert(message, type) {
        const alertContainer = document.getElementById('alertContainer')
        if (!alertContainer) return

        const alertDiv = document.createElement('div')
        alertDiv.className = `alert alert-${type} alert-dismissible fade show`
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `
        
        alertContainer.appendChild(alertDiv)
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove()
            }
        }, 5000)
    }
}

// Initialize the app when the DOM is loaded
let app
document.addEventListener('DOMContentLoaded', () => {
    app = new TradChemApp()
}) 