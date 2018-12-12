from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoItem(models.Model):
    content=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True, null =False)
    uname =models.ForeignKey(User,on_delete=models.CASCADE,default=1)