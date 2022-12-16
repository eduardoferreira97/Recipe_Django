from django.urls import include, path


from cook import views

app_name = 'cook'

urlpatterns = [
    path('',views.index, name="index"),
    path('recipes/category/<int:pk>/',views.category, name="category"),
    path('recipes/<int:pk>',views.details, name="details"),
    # path('', include(recipe_api_v2_router.urls)),
]