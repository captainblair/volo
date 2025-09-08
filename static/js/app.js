// Main application JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Initialize notifications
    loadNotifications();
    
    // Setup CSRF token for all AJAX requests
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
    if (csrfToken) {
        // Set default headers for fetch requests
        const originalFetch = window.fetch;
        window.fetch = function(url, options = {}) {
            if (options.method && options.method.toUpperCase() !== 'GET') {
                options.headers = {
                    ...options.headers,
                    'X-CSRFToken': csrfToken
                };
            }
            return originalFetch(url, options);
        };
    }
});

// Load notifications
async function loadNotifications() {
    try {
        const response = await fetch('/api/communications/notifications/');
        if (response.ok) {
            const notifications = await response.json();
            updateNotificationBadge(notifications);
        }
    } catch (error) {
        console.error('Error loading notifications:', error);
    }
}

// Update notification badge
function updateNotificationBadge(notifications) {
    const unreadCount = notifications.filter(n => !n.is_read).length;
    const badge = document.querySelector('.notification-badge');
    if (badge) {
        badge.textContent = unreadCount;
        badge.style.display = unreadCount > 0 ? 'flex' : 'none';
    }
}

// WebSocket for real-time notifications
function initializeNotificationSocket() {
    const notificationSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/notifications/'
    );
    
    notificationSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        if (data.type === 'notification') {
            showNotificationToast(data.notification);
            loadNotifications(); // Refresh notifications
        }
    };
    
    notificationSocket.onclose = function(e) {
        console.error('Notification socket closed unexpectedly');
        // Attempt to reconnect after 5 seconds
        setTimeout(initializeNotificationSocket, 5000);
    };
}

// Show notification toast
function showNotificationToast(notification) {
    const toast = document.createElement('div');
    toast.className = 'fixed top-4 right-4 bg-white shadow-lg rounded-lg p-4 border-l-4 border-blue-500 z-50 max-w-sm';
    toast.innerHTML = `
        <div class="flex">
            <div class="flex-shrink-0">
                <i class="fas fa-bell text-blue-500"></i>
            </div>
            <div class="ml-3">
                <p class="text-sm font-medium text-gray-900">${notification.title}</p>
                <p class="text-sm text-gray-500">${notification.message}</p>
            </div>
            <div class="ml-auto pl-3">
                <button onclick="this.parentElement.parentElement.parentElement.remove()" class="text-gray-400 hover:text-gray-600">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        </div>
    `;
    
    document.body.appendChild(toast);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (toast.parentElement) {
            toast.remove();
        }
    }, 5000);
}

// Initialize notification socket if user is authenticated
if (document.querySelector('nav')) {
    initializeNotificationSocket();
}

// Utility functions
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
}

function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `fixed top-4 right-4 p-4 rounded-md shadow-lg z-50 ${
        type === 'success' ? 'bg-green-50 text-green-800 border border-green-200' :
        type === 'error' ? 'bg-red-50 text-red-800 border border-red-200' :
        type === 'warning' ? 'bg-yellow-50 text-yellow-800 border border-yellow-200' :
        'bg-blue-50 text-blue-800 border border-blue-200'
    }`;
    
    alertDiv.innerHTML = `
        <div class="flex">
            <div class="flex-shrink-0">
                <i class="fas ${
                    type === 'success' ? 'fa-check-circle' :
                    type === 'error' ? 'fa-exclamation-circle' :
                    type === 'warning' ? 'fa-exclamation-triangle' :
                    'fa-info-circle'
                }"></i>
            </div>
            <div class="ml-3">
                <p class="text-sm font-medium">${message}</p>
            </div>
            <div class="ml-auto pl-3">
                <button onclick="this.parentElement.parentElement.parentElement.remove()" class="text-gray-400 hover:text-gray-600">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        </div>
    `;
    
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
        if (alertDiv.parentElement) {
            alertDiv.remove();
        }
    }, 5000);
}
