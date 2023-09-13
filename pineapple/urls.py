from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    path('comment-create/', views.comment_create_view, name='comment_create'),
    path('seller-comment-list/<slug:certificate_code>/', views.seller_comment_list_view, name='seller-comment-list')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)