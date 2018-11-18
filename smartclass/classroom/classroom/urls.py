
from django.contrib import admin
from django.urls import path,include
from forum import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('post/forum/',include('forum.urls')),
    path('',views.home,name='home'),
    path('teacher/',views.teacher_page,name='teacher_page'),
    path('post/',views.post_list,name='post_list'),
    path('file/',include('fileindb.urls')),
    path('todo/',include('todo.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
