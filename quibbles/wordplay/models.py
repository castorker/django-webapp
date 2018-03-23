from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

QUIBBLE_STATUS_CHOICES = (
    ('C', 'Created'),
    ('M', 'Modified'),
)


@python_2_unicode_compatible
class Quibble(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=50)

    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, related_name="quibbles_user_id", on_delete=models.CASCADE)

    status = models.CharField(max_length=1, default='C', choices=QUIBBLE_STATUS_CHOICES)

    def __str__(self):
        return f'{self.text} - {self.category} - {self.user.username}'
