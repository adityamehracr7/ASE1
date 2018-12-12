from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from fileindb.models import student,faculty



class otp_verify(models.Model):
    name=models.CharField(max_length=50)
    otp=models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)


class TeacherPost(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    }

    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, related_name='forum_post',on_delete=models.CASCADE)
    tags = models.CharField(max_length=50,blank=True)
    body = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='publish')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)

    def get_tags(self):
        arr = []
        arr = self.tags.split('  ')
        return arr

    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse('post_list', args=[self.id])

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()




class Images(models.Model):
    post = models.ForeignKey(TeacherPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.post.title + ' image'

class Comment(models.Model):
    post = models.ForeignKey(TeacherPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')

    def __str__(self):
        return '{}'.format(self.post.title)+"Comment"
class notifications(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    com_id=models.ForeignKey(Comment,on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

