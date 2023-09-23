from django.urls import path

from . import views

urlpatterns = [
    path('blogHome/', views.BlogListView.as_view(), name='block_views'),
    path('blogHome/<int:pk>/', views.BlogDetailsView.as_view(), name='block_Details_Views'),
]
