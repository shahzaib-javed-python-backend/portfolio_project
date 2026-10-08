from .models import Visitor

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Visitor ka IP address fetch karna
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Static files ya admin ki requests ko chhor kar baaki sab track karna
        if not request.path.startswith('/static/') and not request.path.startswith('/admin/'):
            Visitor.objects.create(ip_address=ip, path=request.path)

        response = self.get_response(request)
        return response