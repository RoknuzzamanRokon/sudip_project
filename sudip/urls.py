from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('base_app.urls')),
    path('admin/', admin.site.urls),
    # path('app/', include('ursamApp01.urls')),
]

