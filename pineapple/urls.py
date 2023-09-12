from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    path('order-list', views.order_list_view),
    path('order-detail', views.order_detail_view),
    path('order-create', views.order_create_view),
    path('order-update', views.order_update_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)