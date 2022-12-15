from django.urls import include, path


from cook import views

app_name = 'cook'

urlpatterns = [
    path('',views.index, name="index")
]