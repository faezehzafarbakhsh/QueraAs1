from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    # seller
    path('seller-list/' , views.seller_list_view , name='seller-list'),
    path('seller-detail/<str:certificate_code>/' , views.seller_detail_view, name='seller-detail'),
    path('seller-create/', views.seller_create_view, name='seller-create'),
    path('seller-update/<str:certificate_code>/', views.seller_update_view, name='seller-update'),    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)