from django.contrib import admin
from .models import Question
from .models import Solution
from .models import Comment
from .models import Reply
# Register your models here.

admin.site.register(Question)
admin.site.register(Solution)
admin.site.register(Comment)
admin.site.register(Reply)
