from django.conf.urls import url, include
from . import views

app_name = "feedback"
urlpatterns = [
    url(r'^$', views.index, name="feedback-index"),
    # url(r'form/add$', views.CreateFormClass.as_view(), name="form-add"),
    url(r'form/add$', views.createForm, name="form-add"),
    url(r'form/display$', views.displayForm, name="form-display"),
    url(r'manage', views.manage, name="manage"),
    url(r'^form/about/(?P<formid>[0-9]+)$', views.aboutForm, name="form-about"),
    url(r'^form/update/(?P<pk>[0-9]+)$', views.UpdateForm.as_view(), name="form-update"),
]
