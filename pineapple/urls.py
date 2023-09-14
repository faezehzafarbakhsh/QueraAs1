from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [

    # orders
    path('orders/', views.order_list_view, name='order-list'),
    path('orders/<int:pk>/', views.order_detail_view, name='order-detail'),
    path('order-create/', views.order_create_view, name='order-create'),
    path('orders/<int:pk>/update/', views.order_update_view, name='order-update'),

    # seller
    path('seller-list/', views.seller_list_view, name='seller-list'),
    path('seller-detail/<str:certificate_code>/', views.seller_detail_view, name='seller-detail'),
    path('seller-create/', views.seller_create_view, name='seller-create'),
    path('seller-update/<str:certificate_code>/', views.seller_update_view, name='seller-update'),

    # subscription
    path('subscription-create/', views.subscription_create_view, name='subscription-create'),
    path('subscription-list/', views.subscription_list_view, name='subscription-list'),

    # comment
    path('comment-create/', views.comment_create_view, name='comment-create'),
    path('seller-comment-list/<str:certificate_code>/', views.seller_comment_list_view, name='seller-comment-list'),

    # Pineapple
    path("pineapple-list/", views.pineapple_list_view, name="pineapple-list"),
    path("pineapple-detail/<int:pk>/", views.pineapple_detail_view, name="pineapple-detail"),
    path("pineapple-create/", views.pineapple_create_view, name="pineapple-create"),
    path("pineapple-update/<int:pk>/", views.pineapple_update_view, name="pineapple-update"),
    path("seller-pineapple-list/<int:seller_id>/", views.seller_pineapple_list_view, name="seller-pineapple-list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
