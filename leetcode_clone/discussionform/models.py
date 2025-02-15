from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
    topic = models.CharField(max_length=255)
    topic_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rooms')
    created_at = models.DateTimeField(auto_now_add=True)
    first_comment = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.topic
