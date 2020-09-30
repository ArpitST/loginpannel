from django.urls import path
from .import views

urlpatterns=[
	path('<slug:slug>/',views.post_detail, name="post_detail"),
	path('',views.home,name="home"),
	# path('add_category/', AddCategoryView.as_view(), name='add_category'),
	# path('category/<str:cats>/', CategoryView, name='category'),

]