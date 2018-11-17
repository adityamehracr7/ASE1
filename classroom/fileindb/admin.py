from django.contrib import admin



from .models import faculty
from .models import course
from .models import table
from .models import file
from .models import examtype

admin.site.register(faculty)
admin.site.register(course)
admin.site.register(table)
admin.site.register(file)
admin.site.register(examtype)

