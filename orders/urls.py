from . import views as vs
from django.shortcuts import redirect
from django.urls import path


urlpatterns = [
    path('', lambda request: redirect('new_order', permanent=True)),
    path('upd/<str:order_id>', vs.post_back, name='post_back'),
    path('get/<int:order_id>', vs.get_data_order, name='data_order'),
    path('new', vs.new_order, name='new_order'),
    path('my', vs.my_order, name='my_order'),
    path('<int:order_id>', vs.order, name='order'),
]
