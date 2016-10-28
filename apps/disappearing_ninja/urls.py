from django.conf.urls import url
from . import views as v
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^turtles/(?P<color>\w*)$', v.show_turtles, name='turtles'),
    url(r'^$', v.index, name='index')
]
