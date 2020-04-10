from django.db import models


class Evaluation(models.Model):
    """
    DESCRIPTION
    """
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)



