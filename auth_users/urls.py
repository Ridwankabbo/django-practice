from django.urls import path
from . import views

urlpatterns = [
    path('all-users/', views.UsersApi.as_view(), name="all-users"),
    path('register-user/', views.UserRegistration, name='register-user')
]
