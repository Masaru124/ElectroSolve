from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Problem

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
    if request.method == "POST":
        selected_answer = request.POST.get('answer')
        problem = Problem.objects.get(id=problem_id)

        is_correct = (selected_answer == problem.correct_answer)

        return render(request, 'problem_detail.html', {
            'problem': problem,
            'option_a': problem.option_a,
            'option_b': problem.option_b,
            'option_c': problem.option_c,
            'option_d': problem.option_d,
            'solution_display': is_correct,
        })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')