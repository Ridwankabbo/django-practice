from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsersApi.as_view())
]
