from django.urls import re_path
from .views import index, room


urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room')
]
