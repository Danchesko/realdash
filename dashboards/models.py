from django.db import models

class DashboardData(models.Model):
    timestamp = models.DateTimeField()
    memory_load = models.FloatField()
    cpu_load = models.FloatField()
    num_processes = models.IntegerField()
    num_apps = models.IntegerField()
    memory_intake = models.FloatField()