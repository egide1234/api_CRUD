from django.db import models

class User(models.Model):
    age = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
