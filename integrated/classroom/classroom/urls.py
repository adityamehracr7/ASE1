
from django.contrib import admin
from django.urls import path,include
from forum import views
from django.conf import settings
from django.conf.urls.static import static
from studentforum import views as student
from fileindb import views as file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('post/forum/',include('forum.urls')),
    path('post/',views.post_list,name='post_list'),
    path('teacher/',include('fileindb.urls')),
    path('todo/',include('todo.urls')),
    path('like/', views.like_post, name='like_post'),
    path('dislike/', views.dislike_post, name='dislike_post'),
    path('post/list/', views.user_post_list,name='user_post_list'),
    path('user_notifs/',views.user_notifs,name='see_notif'),
    path('student_post',student.blog_list,name='blog_list'),
    path('student/',include('studentforum.urls')),
    path('spost/list/', student.user_post_list,name='userblg_post_list'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
