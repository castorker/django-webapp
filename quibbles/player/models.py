from django.db import models

from django.contrib.auth.models import User


class Invite(models.Model):
    from_user = models.ForeignKey(User,
                                  related_name="invites_sent",
                                  on_delete=models.CASCADE)

    to_user = models.ForeignKey(User,
                                related_name="invites_received",
                                verbose_name="User to invite",
                                help_text="Please select the user you want to invite.",
                                on_delete=models.CASCADE)

    message = models.CharField(max_length=300,
                               blank=True,
                               verbose_name="Optional Message",
                               help_text="Add a quibble message!")

    timestamp = models.DateTimeField(auto_now_add=True)
