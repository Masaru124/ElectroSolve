from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Problem
from django.shortcuts import render, get_object_or_404


def homepage(request):
    return render(request, 'homepage.html')

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problem_list.html', {'problems': problems})

def problem_detail(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    return render(request, 'problem_detail.html', {
        'problem': problem,
        'option_a': problem.option_a,
        'option_b': problem.option_b,
        'option_c': problem.option_c,
        'option_d': problem.option_d,
    })

def check_answer(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)  

    if request.method == "POST":
        selected_answer = request.POST.get('answer')  
        is_correct = (selected_answer == problem.correct_answer)  

     
        if is_correct:
            feedback_message = "Your answer was correct."
        else:
            feedback_message = f"Your answer was incorrect. The correct answer is {problem.correct_answer}."

        
        return render(request, 'problem_detail.html', {
            'problem': problem,
            'option_a': problem.option_a,
            'option_b': problem.option_b,
            'option_c': problem.option_c,
            'option_d': problem.option_d,
            'user_answer': selected_answer,  # Send user's selected answer
            'solution_display': is_correct,  # Whether the answer is correct or not
            'feedback_message': feedback_message  # Display feedback message
        })
