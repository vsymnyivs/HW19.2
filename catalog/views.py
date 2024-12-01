from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from catalog.models import Product, Version


# Create your views here.
class HomeListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f'Имя: {name} \nТелефон: {phone} \nСообщение: {message}')
        return HttpResponseRedirect(reverse("catalog:contacts"))


class ProductDetailView(DetailView):
    model = Product


# def product(request, pk):
#     context = {'catalog': get_object_or_404(Product, pk=pk)}
#     return render(request, 'catalog/product_detail.html', context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(self.request.POST)
        else:
            context_data["formset"] = VersionFormset()
        return context_data

    def form_valid(self, form):
        if form.is_valid:
            new_object = form.save(commit=False)
            new_object.user = self.request.user
            new_object.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


    def get_form_class(self):
        user = self.request.user
        if user == self.object.user or user.is_superuser:
            return ProductForm
        if (
            user.has_perm("catalog.set_published_status")
            and user.has_perm("catalog.change_description")
            and user.has_perm("catalog.change_category")
        ):
            return ModeratorProductForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")
