# monitors/models.py

from django.db import models

class Monitor(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=255)
    interval = models.IntegerField(default=60)
    created_at = models.DateTimeField(auto_now_add=True)

class Check(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    status = models.BooleanField()
    response_time = models.FloatField()
    checked_at = models.DateTimeField(auto_now_add=True)