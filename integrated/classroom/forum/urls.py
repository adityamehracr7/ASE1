from django.urls import path
from .import views

app_name='forum'

urlpatterns = [

    path('post/create/', views.post_create, name='post_create'),
    path('post/update/<int:id>/', views.post_edit, name='post_update'),
    path('post/delete/<int:id>/', views.post_delete, name='post_delete'),
    path('post/<int:id>',views.post_detail,name='post_detail'),
    path('comment/<int:id>/delete/', views.comment_delete, name='comment_delete'),

    path('student_register/',views.student_register,name='student_register'),
path('teacher_register/',views.teacher_register,name='teacher_register'),
path('otp_verify/',views.verify,name='otp'),
path('otp_verify2/',views.verify2,name='otp2'),
path('forget_password/',views.forget_password,name='forget'),
path('forget_otp/',views.forget_otp_verification,name='forget_otp'),
path('reset_password/',views.reset_password,name='reset_password'),
]
