from django.db import models

class ARRCModels(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    data = models.CharField(max_length=50, blank=True, default='')
    user = models.CharField(max_length=20, blank=True, default='')

    class Meta:
        ordering = ('user',)