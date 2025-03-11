from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.conf import settings 

class CustomUser(AbstractUser):
    # Add any custom fields here if needed
    pass

def user_profile_picture_path(instance, filename):
    return f'profile_pictures/{instance.user.username}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(
        upload_to=user_profile_picture_path,
        default='profile_pictures/default.jpeg'  # Explicit .jpeg extension
    )
    problems_solved = models.PositiveIntegerField(default=0)
    streak = models.PositiveIntegerField(default=0)  # Daily coding streak
    max_streak = models.PositiveIntegerField(default=0)  # Highest streak achieved
    rating = models.PositiveIntegerField(default=1500)  # ELO-like rating
    easy_solved = models.PositiveIntegerField(default=0)
    medium_solved = models.PositiveIntegerField(default=0)
    hard_solved = models.PositiveIntegerField(default=0)

    def update_streak(self):
        """ Updates the streak count based on last submission time """
        from datetime import datetime, timedelta
        last_attempt = self.user.questionattempt_set.order_by('-attempted_at').first()
        if last_attempt:
            last_attempt_date = last_attempt.attempted_at.date()
            today = datetime.today().date()
            yesterday = today - timedelta(days=1)

            if last_attempt_date == today:
                return  # Streak already counted today
            elif last_attempt_date == yesterday:
                self.streak += 1  # Continue streak
            else:
                self.streak = 1  # Reset streak

            self.max_streak = max(self.max_streak, self.streak)
            self.save()


    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Achievement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    unlocked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

def check_achievements(user):
    """ Checks if the user has unlocked any new achievements """
    profile = user.profile
    new_achievements = []

    if profile.problems_solved >= 100:
        new_achievements.append(("Problem Solver", "Solved 100+ problems"))

    if profile.streak >= 30:
        new_achievements.append(("Consistent Coder", "Maintained a 30-day streak"))

    if profile.rating >= 1800:
        new_achievements.append(("Expert Coder", "Reached 1800 rating"))

    for name, desc in new_achievements:
        Achievement.objects.get_or_create(user=user, name=name, description=desc)
