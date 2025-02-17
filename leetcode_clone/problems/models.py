from django.db import models
from django.conf import settings

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = models.CharField(
        max_length=6,
        choices=DIFFICULTY_CHOICES,
        default='easy',
    )

    solutions = models.TextField(default='No solution provided')  # Keep one field for the solution

    option_a = models.CharField(max_length=255, default='Option A')
    option_b = models.CharField(max_length=255, default='Option B')
    option_c = models.CharField(max_length=255, default='Option C')
    option_d = models.CharField(max_length=255, default='Option D')

    correct_answer = models.CharField(
        max_length=1, 
        choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')], 
        default='A'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Problem'
        verbose_name_plural = 'Problems'

class QuestionAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    
    # Tracking the answer that was selected by the user
    selected_answer = models.CharField(
        max_length=1,
        choices=[('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')]
    )
    
    # Whether the answer was correct or incorrect
    is_correct = models.BooleanField(default=False)

    # Timestamp of when the question was attempted
    attempted_at = models.DateTimeField(auto_now_add=True)

    # Ensuring a question can only be attempted once
    class Meta:
        unique_together = ('user', 'problem')  # A user can attempt each question only once

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {'Correct' if self.is_correct else 'Incorrect'}"

    def check_answer(self):
        # This method checks if the selected answer is part of the solution
        # If the selected answer is mentioned in the solutions, it's correct
        if self.selected_answer in self.problem.solutions:
            self.is_correct = True
        else:
            self.is_correct = False
        self.save()
