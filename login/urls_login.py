from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_staff),
    path('validateCreds/', views.login),
    path('logout/', views.logout_staff),
]