from django.urls import path
from . import views

app_name = 'name_posts'

urlpatterns = [
    path('', views.index, name='name_posts_index'),
    path('group/<slug>/', views.group_posts, name='name_posts_group_posts')
]
