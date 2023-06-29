import logging

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from .models import Group, Product

logger = logging.getLogger(__name__)


class ProductView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class GroupView(TemplateView):
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        groups = Group.objects.all()
        group = get_object_or_404(Group, slug=self.kwargs['slug'])
        page_obj = group.products.select_related('group')
        context['groups'] = groups
        context['group'] = group
        context['page_obj'] = page_obj
        return context


class DetailView(TemplateView):
    template_name = 'product-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(
            Product.objects.select_related('group'),
            pk=self.kwargs['id']
        )
        context['product'] = product
        return context
