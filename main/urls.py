from django.urls import path
from main.views import home,sign_up,CreatePost

urlpatterns = [
    path('',home,  name='home'),
    path('home',home,  name='home'),
    path('sign_up',sign_up,name='sign_up'),
    path('create_post',CreatePost,name='create_post'),
]
