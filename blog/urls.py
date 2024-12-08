from django.shortcuts import render
from django.urls import path

from blog.views import list_posts, post_detail

urlpatterns = [
    path('', list_posts, name='list_posts'),
    path('<int:post_id>/', post_detail, name='post'),
    path('sort_by_<str:sort_by>', list_posts, name='sorted_posts'),
]