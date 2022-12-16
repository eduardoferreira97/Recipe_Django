from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Recipe

def index(request):

    recipes = Recipe.objects.filter(is_published=True).order_by('title')
    return render(request,"cook/home.html",{'recipes': recipes, 'title':f'Home | Recipes'})
    
def category(request,pk):

    # recipes = Recipe.objects.filter(category__id=pk,is_published=True).order_by('-id')
    recipes = get_list_or_404(Recipe.objects.filter(category__id=pk,is_published=True).order_by('-id'))

    return render(request,"cook/home.html",context = {'recipes':recipes, 'title':f'{recipes[0].category.name} | Category'})

def details(request,pk):

    recipes = get_object_or_404(Recipe,pk=pk)

    return render(request,"cook/recipe_details.html",context = {'recipe':recipes, 'title':f'{recipes.title}','is_detail_page': True})
