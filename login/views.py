from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ImageForm


def indexView(request):
	return render(request,'index.html')
	
@login_required
def dashboardView(request):
	return render(request,'dashboard.html')
	return redirect('login.html') 

def registerView(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login.html')
	else:
		form=UserCreationForm
	return render(request,'registration/register.html',{'form':form})


def edit_profile(request):
	if request.method=="POST":
		form=UserChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			form=UserChangeForm(instance=request.user)
	return render(request,'registration/edit_profile.html',{'form':form})
	return redirect('login.html')


def image_upload_view(request):
	if request.method=='POST':
		form=ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			img_obj=form.instance
			return render(request,'registration/upload.html',{'form':form, 'img_obj':img_obj})
	else:
		form=ImageForm()
	return render(request,'registration/upload.html',{'form':form})