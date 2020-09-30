from django.urls import path
from .import views, AddCategoryView, CategoryView

urlpatterns=[
	path('<slug:slug>/',views.post_detail, name="post_detail"),
	path('add_category/', AddCategoryView.as_view(), name='add_category'),
	path('category/<str:cats>/', CategoryView, name='category'),
	
]