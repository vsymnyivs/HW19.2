from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, product, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', product, name='product')
]
