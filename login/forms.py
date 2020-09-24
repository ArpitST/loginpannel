from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
	"""docstring for I"""
	class Meta:
		model=Image
		fields=('title','image')		
