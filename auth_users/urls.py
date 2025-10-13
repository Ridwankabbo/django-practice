from django.urls import path
from . import views

urlpatterns = [
    path('all-users/', views.UsersApi.as_view(), name="all-users"),
    path('register-user/', views.UserRegistrationView.as_view(), name='register')
]
