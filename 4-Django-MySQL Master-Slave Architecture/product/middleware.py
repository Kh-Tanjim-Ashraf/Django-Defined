# middleware.py
from asgiref.local import Local

# Thread-safe storage that persists only for the duration of the current HTTP request
_thread_locals = Local()

def get_current_request_is_admin():
    return getattr(_thread_locals, 'is_admin_request', False)

class AdminRouterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request URL starts with /admin/
        if request.path.startswith('/admin/'):
            _thread_locals.is_admin_request = True
        else:
            _thread_locals.is_admin_request = False

        response = self.get_response(request)
        
        # Clean up after the request finishes
        _thread_locals.is_admin_request = False
        return response