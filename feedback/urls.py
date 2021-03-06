from django.conf.urls import url, include
from . import views
#from .views import IndexListView

app_name = "feedback"

urlpatterns = [
    #url(r'^$', views.index, name="feedback-index"),
    # url(r'form/add$', views.CreateFormClass.as_view(), name="form-add"),
   # url(r'^$', IndexListView.as_view(), name="feedback-index"),
    url(r'^$', views.index, name="feedback-index"),
    url(r'form/add$', views.createForm, name="form-add"),
    url(r'form/display$', views.displayForm, name="form-display"),
    url(r'manage', views.manage, name="manage"),
    url(r'^form/about/(?P<formid>[0-9]+)$', views.aboutForm, name="form-about"),
    url(r'^form/update/(?P<pk>[0-9]+)$', views.UpdateForm.as_view(), name="form-update"),
    url(r'^formresp/(?P<formid>[0-9]+)$', views.formResponse, name="form-response"),
    url(r'subans', views.subans, name="submitanswer"),
    url(r'^formrespindividual/(?P<formid>[0-9]+)$', views.IndividualFormAns, name="individual-resp"),
    url(r'^formrespindividual/userresp/', views.UserResp, name="user-resp"),
    url(r'^question/update$', views.updatequestion, name="question-update"),
    url(r'^question/delete', views.delete_question, name="question-delete"),
    url(r'^form/add/course', views.form_course, name="form-course"),
]
