from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from . import models

# Create your views here.
class BlogListView(ListView):
    model = models.Post
    template_name = 'blog_home.html'
    context_object_name = 'all_posts_list'

class BlogDetailsView(DetailView):
    model = models.Post
    template_name = 'blog_details.html'
    context_object_name = 'post'
    


class BlogCreateView(CreateView):
    model = models.Post
    template_name = 'post_new.html'
    fields = '__all__'
    
    
class BlogUpdateView(UpdateView):
    model = models.Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    

