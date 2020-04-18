from django.contrib.postgres.fields import JSONField
from django.db import models
from services.users.models import User



class Evaluation(models.Model):
    """
    DESCRIPTION
    """
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='.')
    results = JSONField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    objects = models.Manager()

