from django.contrib import admin
from .models import file
from .models import examtype
from .models import course
from .models import faculty
from .models import table
from .models import studentattendence
# Register your models here.

admin.site.register(file)
admin.site.register(faculty)
admin.site.register(course)
admin.site.register(examtype)
admin.site.register(table)
admin.site.register(studentattendence)
