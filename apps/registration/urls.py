from django.conf.urls import url
from . import views as v

urlpatterns = [
    url(r'^$', v.index, name="main"),
    url(r'^register$', v.register, name="register"),
    url(r'^login$', v.login, name="login"),
    url(r'^success$', v.success, name="success"),
    url(r'^logout$', v.logout, name="logout")
]
