
from django.http import HttpResponse
from django.http import HttpResponseForbidden

class CustomMiddleware:
    # b_ipss = ['127.0.0.1']
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code executed fo_r each request **before** the view (and later middleware) are called.
        print("Before view")
        # ip = request.META.get('REMOTE_ADDR')

        # if ip in self.b_ipss:
        #     return HttpResponseForbidden('Your IP is blocked')

        response = self.get_response(request)

        # Code executed for each response **after** the view is called.
        print("After view")

        return response
