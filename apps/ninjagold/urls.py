from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main_gold"),
    url(r'^process/(?P<building>\w*)$', views.process_money, name="process_gold")
]
