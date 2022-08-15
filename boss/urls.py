from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:shop>', views.order_list, name="order_list"),
    path('timeinput/', views.time_input, name="timeinput"),
    # path('menus/<int:shop>', views.menu, name="menu"),
    # path('orders/',views.orders, name="orders")
]
