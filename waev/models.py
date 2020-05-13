from django.db import models
from django.contrib.auth.models import User

class AudioFile(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField()
    transcript = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

