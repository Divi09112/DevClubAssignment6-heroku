from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$',views.notes,name='notes',),
    url(r'^welcome$', views.welcome, name='welcome'),
    url(r'^create$',views.create_todo, name='create'),
    url(r'^show/(?P<pk>\d)$',views.show,name='show'),
    url(r'^signup/$',views.create_user,name='signup'),
]
