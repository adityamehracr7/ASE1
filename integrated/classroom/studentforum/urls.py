from django.urls import path
from .import views

app_name='studentforum'

urlpatterns = [

    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/update/<int:id>/', views.blog_edit, name='blog_update'),
    path('blog/delete/<int:id>/', views.blog_delete, name='blog_delete'),
    path('blog/<int:id>',views.blog_detail,name='blog_detail'),
    path('type_comment/<int:id>/delete/', views.comments_delete, name='blogcomment_delete'),
]
