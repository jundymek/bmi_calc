from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^charts$', views.charts, name='charts'),
    url(r'^localization$', views.localization, name='localization'),

]
