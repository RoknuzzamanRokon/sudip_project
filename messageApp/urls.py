from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('message/', HomePageView.as_view(), name='home')
]

