from django.contrib.admin import register, ModelAdmin

from .models import Product


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        'name',
        'image',
        'description',
        'color',
        'price',
        'link_to_shop'
    )
    list_editable = (
        'description',
        'color',
        'price',
        'link_to_shop',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'
