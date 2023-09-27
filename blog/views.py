from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy
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
    

class BlogDeleteView(DeleteView):
    model = models.Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blog_home') 