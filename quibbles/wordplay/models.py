from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Quibble(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=50)

    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, related_name="quibbles_user_id", on_delete=models.CASCADE)

    status = models.CharField(max_length=1, default='C')
