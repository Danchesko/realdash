from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, Http404
from pytz import UTC

from .models import DashboardData


def dashboard_current_time(request):
    now = datetime.now()
    timestamp = datetime(2019, 1, 1, 
                         now.hour, now.minute, now.second, 0, UTC)
    return _dashboard_render(request, timestamp)


def dashboard_request_time(request, hour, minute, second):
    try:
        timestamp = datetime(2019, 1, 1,
                             int(hour), int(minute),
                             int(second), 0, UTC)
    except ValueError:
        raise Http404('Invalid time requested')
    return _dashboard_render(request, timestamp)


def documentation(request):
    return render(request, 'docs.html')


def _dashboard_render(request, timestamp):
    try:
        data = DashboardData.objects.get(timestamp=timestamp)
    except DashboardData.DoesNotExist:
        raise Http404('Could not find {}'.format(timestamp))
    return render(request, 'index.html', {'data': data})


