from django.urls import path
from .import views

urlpatterns=[
	path('post_detail/<int:pk>/',views.post_detail, name="post_detail"),
	path('post_edit/<int:pk>/',views.post_edit, name="post_edit"),
	path('',views.post_list,name="post_list"),
]