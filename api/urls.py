from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from invest_back_end import views

# URLs redirecting to views functions or apps
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]