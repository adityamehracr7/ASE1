from django.shortcuts import render
from .models import Question
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# from django.urls import reverse_lazy
# Create your views here.

def forum(request):
    #post = post.objects.all()
    dic = {'post': Question.objects.all() }
    return render(request,"forum/forum.html",dic)

class PostView(LoginRequiredMixin,ListView):
    model=Question
    template_name="forum/forum.html"
    context_object_name="post"
    ordering=['-Date']


class PostDetail(LoginRequiredMixin,DetailView):
    model=Question
    template_name="forum/individual.html"
    context_object_name="post"


class NewQuestion(LoginRequiredMixin,CreateView):
    model=Question
    fields=['Title','question']
    template_name="forum/ask.html"

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

class UpdateQuestion(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Question
    fields=['Title','question']
    template_name="forum/ask.html"

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Question=self.get_object()
        if self.request.user == Question.Author:
            return True
        else:
            return False

class DeleteQuestion(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Question
    template_name="forum/delete.html"
    success_url='/forumhome'

    def test_func(self):
        Question=self.get_object()
        if self.request.user == Question.Author:
            return True
        else:
            return False
    # def get_absolute_url(self):
    #     return reverse('PostDetail',kwargs={'pk': self.pk})
