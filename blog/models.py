from django.conf import settings
from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField

class Category(models.Model):
	name=models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Tag(models.Model):
	title=models.CharField(max_length=150)
	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog/tag_detail_url', kwargs={'slug':self.slug})

class Post(models.Model):
	author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True, null=True)
	slug=AutoSlugField(populate_from='title', editable=True)
	
	category=models.CharField(max_length=200, default='coding')

	tags=models.ManyToManyField(Tag, blank=True, related_name='posts')

	def publish(self):
		self.published_date=timezone.now()
		self.save()
	
	def __str__(self):
		return self.title

	def slugify_function(self,content):
		return content.replace('_', '-').lower()


class Comment(models.Model):
	post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	approved_comment=models.BooleanField(default=False)


	def approve(self):
		self.approved_comment=True
		self.save()

	def __str__(self):
		return self.text

	def approved_comments(self):
		return self.comments.filter(approved_comments=True)
