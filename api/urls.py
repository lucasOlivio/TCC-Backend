from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from invest_back_end import views
from django.contrib import admin
from django.conf.urls import include, url

# URLs redirecting to views functions or apps
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('profile-data/', views.MainDataView.as_view(), name='profile_data'),
    path('graphcomp-data/', views.CompGraphView.as_view(), name='graphcomp_data'),
    path('stockdetail-data/', views.StockDetailView.as_view(), name='stockdetail_data'),
    path('main-graph/', views.MainGraphView.as_view(), name='main_graph'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]