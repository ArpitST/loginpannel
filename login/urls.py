from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns=[
	path('dashboard/',views.dashboardView, name="dashboard"),
	path('login/',LoginView.as_view(),name="login_url"),
	path('register/',views.registerView, name="register_url"), 
	path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
	path('edit/',views.edit_profile, name="edit_profile"),
	path('upload/',views.image_upload_view, name="upload"),

	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	
	path('',views.indexView, name="home"),

]

# https://simpleisbetterthancomplex.com/tutorial/2016/09/19/how-to-create-password-reset-view.html
# http://127.0.0.1:8000/login/password_reset/done/
# https://stackoverflow.com/questions/6367014/how-to-send-email-via-django