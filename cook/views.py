from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Recipe

def index(request):
    recipes = Recipe.objects.order_by('title')
    return render(request,"cook/home.html",{'recipe': recipes})
    
def category(request,category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request,"cook/home.html",context = {'recipes':recipes})
