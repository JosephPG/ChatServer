import json
from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name, type_chat):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'type_chat': mark_safe(json.dumps(type_chat))
    })
