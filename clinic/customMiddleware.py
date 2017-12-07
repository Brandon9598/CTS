from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)
        if (request.user.is_authenticated() == False and request.path !="/accounts/login/"):
            return HttpResponseRedirect(reverse('login')) # or http response

        response = self.get_response(request)
        return response
