from django.conf.urls import url
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
app_name = 'users'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register', views.signup, name="signup"),
    url(r'about', views.about, name="about"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password-reset.html'),
         name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html'),
         name="password_reset_confirm"),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'),
         name="password_reset_complete"),
]
