from django.views.generic import ListView, DetailView
from .models import News


class PostsList(ListView):
    model = News
    ordering = '-dateCreation'
    template_name = 'flatpages/posts.html'
    context_object_name = 'posts'

class PostsDetail(DetailView):
    model = News
    template_name = 'flatpages/post.html'
    context_object_name = 'post'