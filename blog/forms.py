from django import forms
from .models import Post, Category, Comment, Tag

# choices=[('coding','coding'),('sports','sports'),('entertainment','entertainment')]
choices=Category.objects.all().values_list('name','name')

choice_list=[]

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):

	class Meta:
		model=Post
		fields=('title','text','category',)

		widgets={
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'category':forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
		}


class CommentForm(forms.ModelForm):

	class Meta:
		model=Comment
		fields=('author','text',)

						

# class TagForm(forms.ModelForm):

# 	class Meta:
# 		model=Tag
# 		fields=('name', 'text',)



		# https://stackoverflow.com/questions/44837733/how-to-make-add-replies-to-comments-in-django/46992797   
		# check this link for comment reply	
