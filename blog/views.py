from re import search

from django.shortcuts import render
from django.template.defaultfilters import title

from blog.algoritms.search import binary_search_by_id
from blog.algoritms.sorting import bubble_sort_by_title
from blog.models import Post


def list_posts(request):
    search_by = request.POST.get('search', '')
    sort = request.POST.get('sort', None)
    if search_by:
        if search_by.split('::')[0] == 'id':
            posts = binary_search_by_id((list(Post.objects.all())), int(search_by.split('::')[1]))
        else:
            posts = Post.objects.filter(title__icontains=search_by)
    else:
        posts = Post.objects.all()
    posts = bubble_sort_by_title(posts) if sort == 'Заголовку' else posts
    return render(request, 'blog/list_of_posts.html', {'posts':posts, 'search': search_by})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/posts_details.html', {'post':post})
