from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                    UpdateView, DeleteView)
from blog.models import Post, Comments
from blog.forms import CommentForm, PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte =  timezone.now()).order_by('-published_date') #__lte means less than or equal to
        # - means we can order_by in descending order
        # see what is ORM
class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    # These attributes are taken by mixins
    login_url = '/login/' # incase a person is not logged in, he should go here
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post
class PostUpdateView(LoginRequiredMixin,UpdateView):

    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('create_date')

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk = pk)
    if request.method == 'POST':
        form = CommentForm(data = request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk = pk)
        else:
            print(form.errors)
            return HttpResponse("The form you filled is not valid!")
    else:
        form = CommentForm()
        return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comments,pk = pk)
    comment.approve()
    return redirect('post_detail',pk = comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comments,pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk = post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk = pk)
    post.publish()
    return redirect('post_detail.html',pk = pk)