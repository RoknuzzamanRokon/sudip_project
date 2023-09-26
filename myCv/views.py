from django.views.generic import ListView
from .models import Rost


class Something(ListView):
    model = Rost
    template_name = 'index.html'
    context_object_name = 'objects'
    
