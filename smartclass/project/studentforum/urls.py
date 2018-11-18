from django.urls import path
from .views import PostView,PostDetail,NewQuestion,UpdateQuestion,DeleteQuestion
from . import views

urlpatterns = [
    path('forumhome/', PostView.as_view(), name='forumhome'),
    path('forumhome/<int:pk>/',PostDetail.as_view(),name="PostDetail"),
    path('forumhome/ask/',NewQuestion.as_view(),name="AskQuestion"),
    path('forumhome/<int:pk>/update/',UpdateQuestion.as_view(),name="UpdateQuestion"),
    path('forumhome/<int:pk>/delete/',DeleteQuestion.as_view(),name="Delete"),
]
