from django.urls import path
from .views import (
    product_list_view,
    product_detail_view,
    product_create_view,
    product_update_view,
    product_delete_view
)

urlpatterns = [
    path('',product_list_view,name='home'),
    path('<int:id>/',product_detail_view,name='product'),
    path('create/',product_create_view),
    path('<int:id>/update/',product_update_view,name='update'),
    path('<int:id>/delete/',product_delete_view,name='delete'),
]
