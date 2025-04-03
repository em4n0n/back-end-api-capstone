from django.urls import path
from .views import MenuItemView, SingleMenuItemView

urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu_items'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single_menu_item'),
]