from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nutrition_analyzer.urls')),  # Remove the 'api/' prefix
]
