from django.db import models
from django.urls import reverse



class Image(models.Model):
	title=models.CharField(max_length=200)
	image=models.ImageField(upload_to='images')
	# image.thumbnail(100)

	def __str__(self):
		return self.title
	