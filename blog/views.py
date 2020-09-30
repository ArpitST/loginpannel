from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect



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

def home(request):
	return render(request, 'home.html')