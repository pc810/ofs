from django.conf.urls import url
from . import views
app_name = 'users'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register', views.signup, name="signup"),
    url(r'about', views.about, name="about")
]
