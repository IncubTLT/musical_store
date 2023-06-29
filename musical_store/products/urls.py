from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ProductView, GroupView, DetailView

app_name = 'products'

urlpatterns = [
    path('', ProductView.as_view(), name='index'),
    path('group/<slug:slug>/', GroupView.as_view(), name='group_list'),
    path(
        'product-detail/<int:id>/',
        DetailView.as_view(),
        name='product-detail'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
