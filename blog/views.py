from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from . import models

# Create your views here.
class BlogListView(ListView):
    model = models.Post
    template_name = 'blog_home.html'
    

class BlogDetailsView(DetailView):
    model = models.Post
    template_name = 'blog_details.html'
    

class BlogCreateView(CreateView):
    model = models.Post
    template_name = 'post_new.html'
    fields = '__all__'
    

class BlogUpdateView(UpdateView):
    model = models.Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

