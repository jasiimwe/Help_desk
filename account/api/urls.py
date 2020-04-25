from django.urls import path
from account.api.views import (
    registeration_view,
)
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'account'

urlpatterns = [
    path('register', registeration_view, name='register'),
    path('login', obtain_auth_token, name='login'),
]