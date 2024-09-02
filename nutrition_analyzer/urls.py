from django.urls import path
from .views import NutritionAnalyzerView, AnalyzeInterface

urlpatterns = [
    path('analyze/', NutritionAnalyzerView.as_view(), name='analyze'),
    path('', AnalyzeInterface.as_view(), name='analyze_interface'),
]
