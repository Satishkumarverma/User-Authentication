from django.urls import path
from django.contrib.auth import views as auth_views
from app import views
from .forms import ResetpasswordForm, PasswordsetForm

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user_change_pass/', views.user_change_pass, name='change_password'),
    path("user_reset_pass/", auth_views.PasswordResetView.as_view(template_name='app/reset_password.html', form_class=ResetpasswordForm), name='user_reset_pass'),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name='app/reset_password_done.html'), name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='app/reset_password_confirm.html', form_class=PasswordsetForm), name='password_reset_confirm'),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='app/reset_password_complete.html'), name='password_reset_complete'),
]