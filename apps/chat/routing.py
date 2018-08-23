from django.conf.urls import url
from . import consumers


websocket_urlpatterns = [
    url(r'^ws/chatSync/(?P<room_name>[^/]+)/$', consumers.ChatSyncConsumer),
    url(r'^ws/chatAsync/(?P<room_name>[^/]+)/$', consumers.ChatAsyncConsumer),
]
