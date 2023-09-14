from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    # Pineapple
    path("pineapple-list/", views.pineapple_list_view, name="pineapple-list"),
    path("pineapple-detail/<int:pk>/",views.pineapple_detail_view, name="pineapple-detail"),
    path("pineapple-create/", views.pineapple_create_view, name="pineapple-create"),
    path("pineapple-update/<int:pk>/", views.pineapple_update_view,name="pineapple-update"),
    path("seller-pineapple-list/<int:seller_id>/", views.seller_pineapple_list_view,name="seller-pineapple-list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
