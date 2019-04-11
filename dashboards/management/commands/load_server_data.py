from datetime import datetime
import random 

import pandas as pd
from django.core.management import BaseCommand
from django.utils.timezone import make_aware

from dashboards.models import DashboardData

secs = pd.date_range(start = '2019-01-01', end = '2019-01-02', freq='S', closed='left')

class Command(BaseCommand):
    help = "Populates database with artificial data"

    def handle(self, *args, **kwargs):
        if DashboardData.objects.exists():
            print("Dashboard data is already in database")
            return 
        print('Populating the database with artificial data')
        for second in secs:
            data = DashboardData()
            data.servername = 'Test Server'
            data.timestamp = make_aware(second.to_pydatetime())
            data.memory_load = round(random.uniform(1,100), 1)
            data.cpu_load = round(random.uniform(1,100), 1)
            data.num_processes = random.randint(1,1000)
            data.num_apps = random.randint(1,50)
            data.memory_intake = round(random.uniform(1,32), 2)
            data.save()
        print('Data finished loading')


