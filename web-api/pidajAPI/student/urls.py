from django.urls import path
from .views import StudentAPI, GradeAPI

app_name = 'student'

urlpatterns = [
    path('', StudentAPI.as_view()),
    path('<int:id>', StudentAPI.as_view()),
    path('grades/', GradeAPI.as_view()),
    path('grades/<int:id>', GradeAPI.as_view())
]