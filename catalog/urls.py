from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactsTemplateView, HomeListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
]
