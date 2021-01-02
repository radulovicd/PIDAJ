from django.urls import path
from .views import SequentialAPI, ListComprehensionAPI, GeneratorAPI, MultiprocessingAPI

urlpatterns = [
    path('sequential', SequentialAPI.as_view()),
    path('comprehension', ListComprehensionAPI.as_view()),
    path('generator', GeneratorAPI.as_view()),
    path('multiprocessing', MultiprocessingAPI.as_view()),
]