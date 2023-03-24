from django.db import models
from django.contrib.auth.models import User

class Courses(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} - {self.code}'

class Module(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course} - {self.name}'

class Post(models.Model):
    
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.CharField(max_length=2000, blank=True, null=True)
    questionFile = models.CharField(max_length=200, blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    marks = models.CharField(max_length=2, blank=True, null=True)
    BT_level = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.question}'

class Upvotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.post}'
    

class Flag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.post}'

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.post}'