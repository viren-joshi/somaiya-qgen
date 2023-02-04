from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.IntegerField() # 0-Teacher,1-Expert

    def __str__(self):
        if self.user_type == 0:
            t = 'Teacher'
        else:
            t = 'Expert'

        return f'{self.user} - {t}'

# Password = Puppy@123
    