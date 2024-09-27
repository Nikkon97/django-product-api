from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Маршрут для главной страницы
    path('products/', views.product_list, name='product-list'),  # API для продуктов
]
