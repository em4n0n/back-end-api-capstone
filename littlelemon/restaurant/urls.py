from django.urls import path
from .views import MenuItemView, SingleMenuItemView
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth', obtain_auth_token),
    path('menu/', MenuItemView.as_view(), name='menu_items'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single_menu_item'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]