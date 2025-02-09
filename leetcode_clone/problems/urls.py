from django.urls import path
from .views import problem_list, problem_detail, check_answer  # Ensure all views are imported

urlpatterns = [
    path('list/', problem_list, name='problem_list'),  # List all problems
    path('<int:problem_id>/', problem_detail, name='problem_detail'),  # Problem detail
    path('check_answer/<int:problem_id>/', check_answer, name='check_answer'),  # Check answer
]
