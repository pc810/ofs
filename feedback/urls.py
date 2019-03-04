from django.conf.urls import url, include
from . import views

app_name = "feedback"
urlpatterns = [
    url(r'^$', views.index, name="feedback-index"),
    # url(r'form/add$', views.CreateFormClass.as_view(), name="form-add"),
    url(r'form/add$', views.createForm, name="form-add")
]
