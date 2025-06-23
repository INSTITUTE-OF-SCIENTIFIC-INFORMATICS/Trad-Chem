// TradChem LLM Frontend Application
// This file handles all frontend functionality and API communication

class TradChemApp {
    constructor() {
        this.apiBaseUrl = this.getApiBaseUrl();
        this.chatMessages = [];
        this.isLoading = false;
        this.init();
    }

    getApiBaseUrl() {
        // In production, this should point to your deployed backend
        // For local development, use localhost
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            return 'http://localhost:8000/api';
        } else {
            // Replace with your actual backend URL when deployed
            return 'https://your-backend-url.com/api';
        }
    }

    init() {
        this.bindEvents();
        this.loadStatistics();
        this.loadRecentMedicines();
    }

    bindEvents() {
        // Chat functionality
        const sendButton = document.getElementById('sendButton');
        const messageInput = document.getElementById('messageInput');
        
        if (sendButton) {
            sendButton.addEventListener('click', () => this.sendMessage());
        }
        
        if (messageInput) {
            messageInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    this.sendMessage();
                }
            });
        }

        // Search functionality
        const searchInput = document.getElementById('searchInput');
        const searchButton = document.getElementById('searchButton');
        
        if (searchButton) {
            searchButton.addEventListener('click', () => this.searchMedicines());
        }
        
        if (searchInput) {
            searchInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    this.searchMedicines();
                }
            });
        }

        // Add medicine form
        const addMedicineForm = document.getElementById('addMedicineForm');
        if (addMedicineForm) {
            addMedicineForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.addMedicine();
            });
        }
    }

    async sendMessage() {
        const messageInput = document.getElementById('messageInput');
        const message = messageInput.value.trim();
        
        if (!message || this.isLoading) return;

        // Add user message to chat
        this.addChatMessage('user', message);
        messageInput.value = '';
        
        this.setLoading(true);

        try {
            const response = await fetch(`${this.apiBaseUrl}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    user_id: this.getUserId()
                })
            });

            const data = await response.json();
            
            if (response.ok) {
                this.addChatMessage('assistant', data.response);
                
                // Add sources if available
                if (data.sources && data.sources.length > 0) {
                    this.addSources(data.sources);
                }
            } else {
                this.addChatMessage('assistant', 'Sorry, I encountered an error. Please try again.');
            }
        } catch (error) {
            console.error('Error sending message:', error);
            this.addChatMessage('assistant', 'Sorry, I\'m having trouble connecting. Please check your internet connection.');
        } finally {
            this.setLoading(false);
        }
    }

    addChatMessage(sender, content) {
        const chatMessages = document.getElementById('chatMessages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        
        const avatar = document.createElement('div');
        avatar.className = `message-avatar ${sender}-avatar`;
        avatar.innerHTML = sender === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = content;
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(messageContent);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        this.chatMessages.push({ sender, content, timestamp: new Date() });
    }

    addSources(sources) {
        const chatMessages = document.getElementById('chatMessages');
        const sourcesDiv = document.createElement('div');
        sourcesDiv.className = 'message assistant';
        sourcesDiv.style.fontSize = '0.9em';
        sourcesDiv.style.opacity = '0.8';
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar assistant-avatar';
        avatar.innerHTML = '<i class="fas fa-book"></i>';
        
        const sourcesContent = document.createElement('div');
        sourcesContent.className = 'message-content';
        sourcesContent.innerHTML = `<strong>Sources:</strong><br>${sources.join('<br>')}`;
        
        sourcesDiv.appendChild(avatar);
        sourcesDiv.appendChild(sourcesContent);
        chatMessages.appendChild(sourcesDiv);
        
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    setLoading(loading) {
        this.isLoading = loading;
        const sendButton = document.getElementById('sendButton');
        if (sendButton) {
            sendButton.disabled = loading;
            sendButton.innerHTML = loading ? '<i class="fas fa-spinner fa-spin"></i>' : '<i class="fas fa-paper-plane"></i>';
        }
    }

    async searchMedicines() {
        const searchInput = document.getElementById('searchInput');
        const query = searchInput.value.trim();
        
        if (!query) return;

        try {
            const response = await fetch(`${this.apiBaseUrl}/search`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: query,
                    search_type: 'name'
                })
            });

            const medicines = await response.json();
            this.displaySearchResults(medicines);
        } catch (error) {
            console.error('Error searching medicines:', error);
            this.showError('Error searching medicines. Please try again.');
        }
    }

    displaySearchResults(medicines) {
        const resultsContainer = document.getElementById('searchResults');
        if (!resultsContainer) return;

        resultsContainer.innerHTML = '';
        
        if (medicines.length === 0) {
            resultsContainer.innerHTML = '<p class="text-muted">No medicines found.</p>';
            return;
        }

        medicines.forEach(medicine => {
            const medicineCard = document.createElement('div');
            medicineCard.className = 'medicine-card';
            medicineCard.innerHTML = `
                <div class="medicine-name">${medicine.product_name}</div>
                <div class="medicine-benefits">
                    <strong>Benefits:</strong> ${medicine.benefits.join(', ')}
                </div>
                <div class="medicine-system">
                    <small class="text-muted">${medicine.traditional_system || 'Unknown system'}</small>
                </div>
            `;
            resultsContainer.appendChild(medicineCard);
        });
    }

    async loadStatistics() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/stats`);
            const stats = await response.json();
            this.updateStatistics(stats);
        } catch (error) {
            console.error('Error loading statistics:', error);
        }
    }

    updateStatistics(stats) {
        const statsContainer = document.getElementById('statsContainer');
        if (!statsContainer) return;

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
        `;
    }

    async loadRecentMedicines() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/medicines?limit=5`);
            const medicines = await response.json();
            this.displayRecentMedicines(medicines);
        } catch (error) {
            console.error('Error loading recent medicines:', error);
        }
    }

    displayRecentMedicines(medicines) {
        const recentContainer = document.getElementById('recentMedicines');
        if (!recentContainer) return;

        recentContainer.innerHTML = '';
        
        medicines.forEach(medicine => {
            const medicineItem = document.createElement('div');
            medicineItem.className = 'list-group-item';
            medicineItem.textContent = medicine;
            recentContainer.appendChild(medicineItem);
        });
    }

    async addMedicine() {
        const form = document.getElementById('addMedicineForm');
        const formData = new FormData(form);
        
        const medicineData = {
            product_name: formData.get('product_name'),
            benefits: formData.get('benefits').split(';').map(b => b.trim()).filter(b => b),
            diseases: formData.get('diseases').split(';').map(d => d.trim()).filter(d => d),
            chemical_composition: {
                ingredients: {
                    [formData.get('ingredient_name')]: {
                        primary_smiles: formData.get('smiles')
                    }
                }
            },
            description: formData.get('description'),
            source: formData.get('source'),
            traditional_system: formData.get('traditional_system')
        };

        try {
            const response = await fetch(`${this.apiBaseUrl}/medicine`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(medicineData)
            });

            const result = await response.json();
            
            if (response.ok) {
                this.showSuccess('Medicine added successfully!');
                form.reset();
                this.loadStatistics();
                this.loadRecentMedicines();
            } else {
                this.showError(result.detail || 'Error adding medicine');
            }
        } catch (error) {
            console.error('Error adding medicine:', error);
            this.showError('Error adding medicine. Please try again.');
        }
    }

    showSuccess(message) {
        this.showAlert(message, 'success');
    }

    showError(message) {
        this.showAlert(message, 'danger');
    }

    showAlert(message, type) {
        const alertContainer = document.getElementById('alertContainer');
        if (!alertContainer) return;

        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        alertContainer.appendChild(alertDiv);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (alertDiv.parentNode) {
                alertDiv.remove();
            }
        }, 5000);
    }

    getUserId() {
        // Generate a simple user ID for session tracking
        let userId = localStorage.getItem('tradchem_user_id');
        if (!userId) {
            userId = 'user_' + Math.random().toString(36).substr(2, 9);
            localStorage.setItem('tradchem_user_id', userId);
        }
        return userId;
    }
}

// Initialize the app when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new TradChemApp();
}); 