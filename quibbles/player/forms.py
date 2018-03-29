from django.forms import ModelForm

from .models import Invite


class InviteForm(ModelForm):
    class Meta:
        model = Invite
        exclude = ('from_user', 'timestamp')
