from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone

class ForcePasswordChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            
            if request.user.check_password('123456'):
                
                if request.path != reverse('change_password') and request.path != reverse('logout'):
                    return redirect('change_password')
        response = self.get_response(request)
        return response
    

class LastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            print("✅ Middleware called for:", request.user.username)  # DEBUG
            profile = getattr(request.user, 'profile', None)
            if profile:
                profile.last_activity = timezone.now()
                profile.save(update_fields=['last_activity'])

        response = self.get_response(request)
        return response
