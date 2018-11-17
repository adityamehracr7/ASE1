from django.urls import path,include
from . import views
urlpatterns = [
    path('upload/<str:course_id>/', views.simple_upload ,name='hello'),
    path('table/', views.create_table, name='table'),
    path('add_course/',views.course_add,name='add_course'),
    path('add_exams/<int:id>/',views.add_exams,name='add_exams'),
]
