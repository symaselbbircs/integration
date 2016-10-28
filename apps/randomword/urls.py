from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.default),
    url(r'^random_word$', views.show, name="word_page"),
    url(r'^random_word/generate$', views.create, name="generate_word")
]
