from django.urls import path
from .views import cart_detail, cart_remove, cart_add

app_name = 'cart'  # Добавляем app_name


urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
]
