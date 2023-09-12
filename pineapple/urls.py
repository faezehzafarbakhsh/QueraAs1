from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    path('order-list', views.order_list_view, name='order-list'),
    path('order-detail', views.order_detail_view, name='order-detail'),
    path('order-create', views.order_create_view, name='order-create'),
    path('order-update', views.order_update_view, name='order-update'),
    path('comment-create', views.comment_create_view, name='comment-create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)