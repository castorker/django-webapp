from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from wordplay.models import Quibble
from .models import Invite
from .forms import InviteForm


@login_required
def home(request):
    user_quibbles = Quibble.objects.quibbles_for_user(request.user)
    current_quibbles = user_quibbles.current()

    invites = request.user.invites_received.all()
    return render(request, "player/home.html",
                  {'quibbles': current_quibbles, 'invites': invites})


@login_required
def new_invite(request):
    if request.method == "POST":
        invite = Invite(from_user=request.user)
        form = InviteForm(instance=invite, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InviteForm()
    return  render(request, "player/new_invite_form.html", {'form': form})


@login_required
def accept_invite(request, id):
    invite = get_object_or_404(Invite, pk=id)
    if not request.user == invite.to_user:
        raise PermissionDenied

    if request.method == 'POST':
        if "accept" in request.POST:
            quibble = Quibble.objects.create(
                user = invite.from_user,
            )
        invite.delete()
        return redirect('player_home')
    else:
        return render(request,
                      "player/accept_invite_form.html",
                      {'invite': invite})
