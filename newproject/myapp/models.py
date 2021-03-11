from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100,default=None)
    email = models.EmailField(max_length=100,default=None)
    password = models.CharField(max_length=100,default=None)

    def __str___(self):
        return self.title