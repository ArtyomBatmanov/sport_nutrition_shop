from django.shortcuts import render, get_object_or_404
from .models import Category

def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.subcategories.all()
    return render(request, 'categories/category_detail.html', {'category': category, 'subcategories': subcategories})
