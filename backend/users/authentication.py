from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

class Bearer(Token):
    pass

class BearerAuthentication(TokenAuthentication):
    model = Bearer
    keyword = 'Bearer'