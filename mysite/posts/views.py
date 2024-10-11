from django.shortcuts import render
from .models import Post

# Create your views here.


def posts_list(request):
    # the minus(-) sign makes sure the order is in descending order
    posts = Post.objects.all().order_by("-date")
    return render(request, 'posts/posts_list.html', {"posts": posts})
