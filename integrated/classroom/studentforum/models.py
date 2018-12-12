from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from fileindb.models import  student,faculty


class StudentPost(models.Model):
    title = models.CharField(max_length=100)
    student = models.ForeignKey(User, related_name='%(class)s_request_create',on_delete=models.CASCADE)
    tags = models.CharField(max_length=50,blank=True)
    body = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def get_tags(self):
        arr = []
        arr = self.tags.split('  ')
        return arr

    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse('post_list', args=[self.id])



class Comment(models.Model):
    post = models.ForeignKey(StudentPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  related_name='comments_student',on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')

    def __str__(self):
        return '{}'.format(self.post.title)+"Comment"
