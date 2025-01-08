from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import category_detail, category_list

urlpatterns = [
    path('', category_list, name='category_list'),
    path('<slug:slug>/', category_detail, name='category_detail'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)