from django.contrib import admin
from .models import Post, Category, Comment, Tag

# Register your models here.



class PostAdmin(admin.ModelAdmin):
	filter_horizontal=('tags',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)