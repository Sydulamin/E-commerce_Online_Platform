from django.urls import path
from .views import register, login, product_list, product_detail, category_list, stock_list
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('categories/', category_list, name='category_list'),
    path('stocks/', stock_list, name='stock_list'),
]
