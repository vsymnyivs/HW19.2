from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from catalog.models import Product


# Create your views here.
class HomeListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Контакты"
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name} \nТелефон: {phone} \nСообщение: {message}')
        return HttpResponseRedirect(reverse('catalog:contacts'))


class ProductDetailView(DetailView):
    model = Product
# def product(request, pk):
#     context = {'catalog': get_object_or_404(Product, pk=pk)}
#     return render(request, 'catalog/product_detail.html', context)