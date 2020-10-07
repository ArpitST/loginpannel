from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category,Comment, Tag
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

# def post_detail(request,pk):
#     post=Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html',{'post':post})

#this one is for comment reply
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    # comments = Comment.objects.filter(post=post, parent__isnull=True)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            text=request.POST.get('text')
            author = request.POST.get('author')
            if parent_id:
                print(parent_id)
                parent_obj = Comment.objects.get(id=parent_id)
            new_comment = comment_form.save(commit=False)
            new_comment.parent = parent_obj
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post_detail.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})
#which finish here

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

#functions for tags start from here
def tags_list(request):
    tags=Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})

def tag_detail(request, slug):
    tag=Tag.objects.get(slug__iexact=slug)
    return render(request,'blog/tag_detail.html', context={'tag':tag})
#and end here

def home(request):
    return render(request, 'home.html')
