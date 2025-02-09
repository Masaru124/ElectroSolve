from django.shortcuts import render, redirect
from .models import Problem

def homepage(request):
    return render(request, 'homepage.html')  # Render the homepage template

def problem_list(request):
    problems = Problem.objects.all()  # Fetch all problems
    return render(request, 'problem_list.html', {'problems': problems})

def problem_detail(request, problem_id):
    problem = Problem.objects.get(id=problem_id)  # Fetch a specific problem
    return render(request, 'problem_detail.html', {
        'problem': problem,
        'solutions': problem.solutions,
        'options': problem.options,
    })

def check_answer(request, problem_id):
    if request.method == "POST":
        selected_answer = request.POST.get('answer')
        problem = Problem.objects.get(id=problem_id)

        # Check if the selected answer is correct
        is_correct = (selected_answer == problem.correct_answer)

        # Render the problem detail page with the solution display
        return render(request, 'problem_detail.html', {
            'problem': problem,
            'solutions': problem.solutions,
            'options': problem.options,
            'solution_display': is_correct,
        })
