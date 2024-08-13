from django.urls import path
from .views import NutritionAnalyzerView, AnalyzeInterface

urlpatterns = [
    path('analyze/', NutritionAnalyzerView.as_view(), name='analyze'),
    path('analyze-interface', AnalyzeInterface.as_view(), name='analyze_interface'),
]
