from django.db import models

class DashboardData(models.Model):
    servername = models.CharField(max_length=50, default = 'Server 1')
    timestamp = models.DateTimeField()
    memory_load = models.FloatField()
    cpu_load = models.FloatField()
    num_processes = models.IntegerField()
    num_apps = models.IntegerField()
    memory_intake = models.FloatField()