from django.urls import path,include
from . import views
urlpatterns = [
    path('upload/', views.simple_upload,name='hello'),
    path('table/', views.create_table, name='table'),
    path('', views.profile, name="Profile.profile"),
]
