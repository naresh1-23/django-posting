from django.shortcuts import redirect, render 
from django.http import HttpResponse
from .models import Post
from django.views.generic import  UpdateView, DeleteView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts' : posts})

class ListPost(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-time_now']


class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['caption', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['caption', 'post_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model  = Post
    success_url= '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

def about(request):
    return render(request, 'blog/about.html',{ 'title' : 'About page'})