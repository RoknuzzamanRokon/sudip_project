from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.BlogListView.as_view(), name='blog_home'),
    path('post/<int:pk>/', views.BlogDetailsView.as_view(), name='blog_details'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'), 
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    
    path('signup/', views.BlogUserSignUp.as_view(), name='signup'),
]
