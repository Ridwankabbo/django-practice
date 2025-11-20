from django.urls import path
from . import views
urlpatterns = [
    path('products-api/', views.Product_api_view.as_view()),
    path('catagories-api/', views.CatagoryListView.as_view({'get':'list'}), name="catagory-api"),
    path('products-details/', views.ListProductDetails.as_view({'post':'creat', 'get':'list'}), name='product-details')

]
