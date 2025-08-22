from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    description = models.TextField()
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description