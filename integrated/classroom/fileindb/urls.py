from django.urls import path,include
from .views import *

urlpatterns = [
    path('upload/<str:course_id>/', simple_upload ,name='hello'),
    path('table/', create_table, name='table'),
    path('add_course/',course_add,name='add_course'),
    path('add_exams/<int:id>/',add_exams,name='add_exams'),
    path('', prof_dashboard,name='teacher_page'),
    path('attendence_data/', Attendence_data.as_view(), name='attendence_data'),
]
