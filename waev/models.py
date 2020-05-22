from django.db import models
from django.contrib.auth.models import User

class AudioFile(models.Model):
    filename = models.CharField(max_length=100)
    audio = models.FileField()
    transcript = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_modified=models.DateTimeField(auto_now=True)
    date_created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.filename