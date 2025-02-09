from django.db import models

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
