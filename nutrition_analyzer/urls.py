from django.urls import path
from .views import NutritionAnalyzerView, AnalyzeInterface, HomePageView, AboutPageView, APIPageView

urlpatterns = [
    path('api/analyze/', NutritionAnalyzerView.as_view(), name='analyze'),
    path('api/', APIPageView.as_view(), name='api'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('analyze', AnalyzeInterface.as_view(), name='analyze_interface'),
]
