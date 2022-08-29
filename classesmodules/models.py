from django.db import models

# Create your models here.

class Module(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return f"{self.module.name} - {self.name}"
