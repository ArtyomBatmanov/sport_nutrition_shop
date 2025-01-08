from django.urls import path
from .views import category_detail, category_list

urlpatterns = [
    path('', category_list, name='category_list'),
    path('<slug:slug>/', category_detail, name='category_detail'),
]
