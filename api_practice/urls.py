from django.urls import path
from . import views
urlpatterns = [
    path('products-api/', views.Product_api_view.as_view())
]
