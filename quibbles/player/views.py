from django.shortcuts import render

from wordplay.models import Quibble


def home(request):
    user_quibbles = Quibble.objects.quibbles_for_user(request.user)
    current_quibbles = user_quibbles.current()

    return render(request, "player/home.html", {'quibbles': current_quibbles})
