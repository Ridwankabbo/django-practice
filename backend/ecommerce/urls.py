from django.urls import path
from . import views
urlpatterns = [
    path('custommers/', views.CustommerApiView, name='customers'),
    path('catagory/', views.CatagroyApiView, name='catagory'),
    path('products/', views.ProductApiView, name='products'),
    path('order/', views.OrderApiView, name='order'),
    path('order-items/', views.OrderItemsApiView, name='order-items')
]
