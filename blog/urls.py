from django.urls import path

from . import views

urlpatterns = [
    path('blogHome/', views.BlogListView.as_view(), name='block_views'),
]
