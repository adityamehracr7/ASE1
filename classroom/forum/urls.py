from django.urls import path
from .import views

app_name='forum'

urlpatterns = [

    path('post/create/', views.post_create, name='post_create'),
    path('post/update/<int:id>/', views.post_edit, name='post_update'),
    path('post/delete/<int:id>/', views.post_delete, name='post_delete'),
    path('post/<int:id>',views.post_detail,name='post_detail'),
    path('comment/<int:id>/delete/', views.comment_delete, name='comment_delete'),
]
