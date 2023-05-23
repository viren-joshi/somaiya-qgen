from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    userType = models.CharField(
        max_length = 20,
        choices = (
        ("Teacher", "Teacher"),
        ("Expert", "Expert"),
        ),
        default = 'Teacher'
        )
    subjectInCharge =  models.ForeignKey(to='main.Courses', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subjectInCharge} - {self.userType} - {self.name}'


    