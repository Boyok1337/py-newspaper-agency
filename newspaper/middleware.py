from django.http import Http404
from newspaper.views import custom_404


class BaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        pass


class PageNotFoundMiddleware(BaseMiddleware):
    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return custom_404(request, exception)
