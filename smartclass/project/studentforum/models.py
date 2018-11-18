from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Question(models.Model):
    QuestionId=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=200,null=False,default='No title')
    question=models.TextField(null=False)
    Date=models.DateTimeField(default=timezone.now)
    Author = models.ForeignKey(User, on_delete=models.CASCADE,default='1')
    
    #def __str__(self):
    #    return self.QuestionId

    def get_absolute_url(self):
        return reverse('PostDetail',kwargs={'pk': self.pk})

class Solution(models.Model):
    SolutionsId=models.AutoField(primary_key=True)
    solutions=models.CharField(max_length=1500,null=False)
    QuestionId=models.ForeignKey(Question,on_delete=models.PROTECT)

    #def __str__(self):
    #    return self.SolutionsId

class Comment(models.Model):
    CommentsId=models.AutoField(primary_key=True)
    Comments=models.CharField(max_length=1500,null=False)
    SolutionsId=models.ForeignKey(Solution,on_delete=models.PROTECT)

    #def __str__(self):
    #    return self.CommentsId

class Reply(models.Model):
    RepliesId=models.AutoField(primary_key=True)
    Replies=models.CharField(max_length=1500,null=False)
    CommentsId=models.ForeignKey(Comment,on_delete=models.PROTECT)

#    def __str__(self):
    #    return self.RepliesId
