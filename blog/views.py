from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category,Comment
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm, CommentForm


def  post_new(request):
	if request.method=="POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form=PostForm()		
	return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
	post=get_object_or_404(Post,pk=pk)
	if request.method=="POST":
		form=PostForm(request.POST, instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)	
	else:
		form=PostForm(instance=post)
	return render(request,'blog/post_edit.html',{'form':form})

def post_list(request):
	posts=Post.objects.all().order_by('created_date')
	return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
	post=Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html',{'post':post})


class AddCategoryView():
	model=Category
	template_name='blog/add_category.html'
	fields='__all__'

def CategoryView(request, cats):
	category_posts=Post.objects.filter(category=cats)
	return render(request,'blog/categories.html',{'cats':cats.title(), 'category_posts':category_posts})		

#functions for comment start here
def add_comment_to_post(request,pk):
	post=get_object_or_404(Post, pk=pk)
	if request.method=="POST":
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.post=post
			comment.save()
			return redirect('post_detail',pk=post.pk)
	else:
		form=CommentForm()
	return render(request,'blog/add_comment_to_post.html',{'form':form})


def comment_approve(request,pk):
	comment=get_object_or_404(Comment,pk=pk)
	comment.approve()
	return redirect('blog/post_detail.html',pk=comment.post.pk)


def comment_remove(request,pk):
	comment=get_object_or_404(Comment,pk=pk)
	comment.delete()
	return redirect('blog/post_detail.html',pk=comment.post.pk)

def home(request):
	return render(request, 'home.html')