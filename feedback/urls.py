from django.conf.urls import url, include
from . import views
app_name = "feedback"
urlpatterns = [
    url(r'^$', views.index, name="feedback-index"),
]