from django.conf.urls import url
from . import views as v

urlpatterns = [
    url(r'^$', v.index, name="main"),
    url(r'^courses/add$', v.add, name="add_course"),
    url(r'^courses/delete/(?P<course_id>\d*)$', v.remove, name="delete_course")
]
