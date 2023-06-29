from django.contrib.admin import register, ModelAdmin

from .models import Product, Group


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        'name',
        'image',
        'description',
        'color',
        'price',
        'link_to_shop',
        'group',
    )
    list_editable = (
        'description',
        'color',
        'price',
        'link_to_shop',
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@register(Group)
class GroupAdmin(ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
    )
    list_editable = (
        'title',
        'slug',
    )
    search_fields = ('title',)
    empty_value_display = '-пусто-'
