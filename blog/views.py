from django.shortcuts import render

from blog.models import Post


def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/list_of_posts.html', {'posts':posts})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/posts_details.html', {'post':post})
