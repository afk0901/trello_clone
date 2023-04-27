from django.contrib.auth import authenticate
from rest_framework.views import APIView


class Login(APIView):
    """
    Authenticates the user
    """

    def post(self, request):
        authenticate()


class SignUp:
    ...


class FargotPassword:
    ...
