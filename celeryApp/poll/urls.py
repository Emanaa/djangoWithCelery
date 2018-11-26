from django.urls import  path
from . import views




urlpatterns = [
    path(r'', views.index,name='index'),
    path(r'poll_state', views.poll_state,name='poll_state'),
]