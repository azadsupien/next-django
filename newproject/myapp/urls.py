from django.urls import path
from myapp.endpoints import authentication


urlpatterns = [
    path('authenticate/signup', authentication.create_account),
    path('authenticate/login', authentication.login),

]