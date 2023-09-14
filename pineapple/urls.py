from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    path('orders/', views.order_list, name='order-list'),
    path('orders/<int:pk>/', views.order_detail, name='order-detail'),
    path('orders-create/', views.order_create, name='order-create'),
    path('orders/<int:pk>/update/', views.order_update, name='order-update')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)