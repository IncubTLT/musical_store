from django.views.generic import TemplateView

from .models import Product


class ProductView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_objects"] = Product.objects.all()
        return context
