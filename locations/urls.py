from . import views as vs
from django.conf.urls import url

urlpatterns = [
    url(r'^$', vs.update_loc, name='home_loc'),
]
