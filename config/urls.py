from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('nutrition_analyzer.urls')),  # Include the nutrition_analyzer app's URLs
]

