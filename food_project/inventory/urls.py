from django.urls import path
from . import views

urlpatterns = [
    path('add_food/', views.add_food, name='add_food'),
    path('inventory/', views.get_inventory),
    path('', views.home, name='home'),
    path('edit/<int:food_id>/', views.edit_food, name='edit_food'),
    path('delete/<int:food_id>/', views.delete_food, name='delete_food'),
    path('stock-overview/', views.stock_overview, name='stock_overview'),
    path('expiring-soon/', views.expiring_soon, name='expiring_soon'),
    path('shopping-list/', views.shopping_list, name='shopping_list'),
    path('search/', views.search_food, name='search_food'),
    path('add-category/', views.add_category, name='add_category'),
]
