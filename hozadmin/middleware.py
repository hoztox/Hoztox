# middleware.py
from django.shortcuts import redirect
from django.conf import settings

class NoCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Add cache control headers to all responses
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        # If user is not authenticated, enforce redirect to login page
        if not request.user.is_authenticated:
            # Skip for login page and static files
            if not request.path.startswith(settings.STATIC_URL) and request.path != '/login/':
                return redirect('login')
        
        return response