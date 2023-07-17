<<<<<<< HEAD
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    is_completed = models.BooleanField(default=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
=======
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    is_completed = models.BooleanField(default=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
>>>>>>> d508546 (first commit)
    