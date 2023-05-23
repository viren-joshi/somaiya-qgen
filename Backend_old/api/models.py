from django.db import models
from django.contrib.postgres.fields import ArrayField


class upvote_check(models.Model):
    user_id = models.CharField(max_length=100)
    question_id = ArrayField(models.IntegerField(),blank=True,null=True)

class bookmarks(models.Model):
    user_id = models.CharField(max_length=100)
    question_id = ArrayField(models.IntegerField(),blank=True,null=True)

class flag_check(models.Model):
    user_id = models.CharField(max_length=100)
    question_id = ArrayField(models.IntegerField(),blank=True,null=True)

class Questions(models.Model):

    question = models.CharField(max_length=500, blank=True, null=True)
    q_image = models.CharField(max_length=200, blank=True, null=True)
    q_file = models.CharField(max_length=200, blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    BT_level = models.IntegerField(blank=True, null=True)
    max_marks = models.IntegerField(blank=True, null=True)
    upvotes = models.IntegerField(blank=True, null=True)
    flag_count = models.IntegerField(blank=True, null=True)

    type = models.IntegerField(blank=True, null=True,default=1)

    option_1 = models.CharField(max_length=500,blank=True,null=True,default="default")
    option_2 = models.CharField(max_length=500,blank=True,null=True,default="default")
    option_3 = models.CharField(max_length=500,blank=True,null=True,default="default")
    option_4 = models.CharField(max_length=500,blank=True,null=True,default="default")
    correct_option = models.IntegerField(blank=True,null=True)

    has_upvoted = models.BooleanField(default=False)
    has_bookmarked = models.BooleanField(default=False)
    has_flagged = models.BooleanField(default=False)

    def __str__(self):
        return f'Type = {self.type}, ques = {self.question}'



class Topics(models.Model):

    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Questions,blank=True,null=True)

    def __str__(self):
        return f'{self.name}'


class Module(models.Model):

    name = models.CharField(max_length=100)
    topics = models.ManyToManyField(Topics,blank=True,null=True)

    def __str__(self):
        return f'{self.name}'


class Courses(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    modules = models.ManyToManyField(Module,blank=True,null=True)

    def __str__(self):
        return f'{self.name}'


class MCQ(models.Model):

    question = models.CharField(max_length=500,blank=True,null=True)
    option_1 = models.CharField(max_length=500,blank=True,null=True)
    option_2 = models.CharField(max_length=500,blank=True,null=True)
    option_3 = models.CharField(max_length=500,blank=True,null=True)
    option_4 = models.CharField(max_length=500,blank=True,null=True)
    correct_option = models.IntegerField()

class temp_mcq(models.Model):
    question = models.CharField(max_length=500,blank=True,null=True)
    choices = ArrayField( models.CharField(max_length=500,blank=True,null=True),blank=True,null=True)
    correct_option = models.CharField(max_length=500,blank=True,null=True)
    more_options = ArrayField( models.CharField(max_length=500,blank=True,null=True),blank=True,null=True)
