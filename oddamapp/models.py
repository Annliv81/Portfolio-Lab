from django.db import models

# Create your models here.

class Gift(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name
