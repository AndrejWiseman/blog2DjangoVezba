from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),

    #da se napravi nova stranica
    path('<slug:post>/', views.post_single, name='post_single'),

]