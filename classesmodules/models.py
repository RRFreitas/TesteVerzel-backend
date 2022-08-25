from django.db import models

# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()

    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.name