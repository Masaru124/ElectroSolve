from django.contrib import admin
from .models import Problem

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'option_a', 'option_b', 'option_c', 'option_d')  # Add required fields here


admin.site.register(Problem, ProblemAdmin)
