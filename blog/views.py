from re import search

from django.shortcuts import render
from django.template.defaultfilters import title

from blog.algoritms.search import binary_search_by_id
from blog.algoritms.sorting import bubble_sort_by_title
from blog.models import Post


def list_posts(request):
    print(request.POST)
    if request.method == 'POST':
        if request.POST.get('search'):
            posts = Post.objects.filter(title__icontains=request.POST['search'])
        else:
            posts = Post.objects.all()
        if request.POST.get('sort'):
            posts = bubble_sort_by_title(posts) if request.POST.get('sort') == 'Заголовку' else posts
    else:
        posts = Post.objects.all()
    return render(request, 'blog/list_of_posts.html', {'posts':posts, 'search': request.POST.get('search') if request.POST.get('search') else ''})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/posts_details.html', {'post':post})
