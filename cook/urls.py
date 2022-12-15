from django.urls import include, path


from cook import views

app_name = 'cook'

urlpatterns = [
    path('',views.index, name="index"),
    path('recipes/category/<int:category_id>/',views.category, name="category")
    # path('', include(recipe_api_v2_router.urls)),
]