from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . import models

# Create your views here.
class BlogListView(ListView):
    model = models.Post
    template_name = 'blog_home.html'
    

class BlogDetailsView(DetailView):
    model = models.Post
    template_name = 'blog_details.html'
    
    