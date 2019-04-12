from datetime import datetime

from django.test import TestCase
from django.utils.timezone import make_aware
from django.urls import reverse_lazy

from . import views
from .models import DashboardData


class DashboardDataTest(TestCase):

    def create_dashboard_model(self, server_name='Test Server', memory_load=80, cpu_load=70, num_processes=250, num_apps=30, memory_intake=5.6):
        return DashboardData.objects.create(servername=server_name, timestamp=make_aware(datetime.now()), 
        memory_load=memory_load, cpu_load=cpu_load, num_processes=num_processes, num_apps=num_apps, memory_intake=memory_intake)

    def test_dashboard_data_creation(self):
        dashboard_test = self.create_dashboard_model()
        
        self.assertTrue(isinstance(dashboard_test, DashboardData))

    def test_doc_view(self):
        url = reverse_lazy("docs")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        url = reverse_lazy("index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

