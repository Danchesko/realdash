from django.contrib import admin
from django.urls import re_path
from django.urls import path

from dashboards import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('docs/', views.documentation, name='docs'),
    re_path(r'^$', views.dashboard_current_time, name='index'),
    re_path(r'^t=(\d{2}):(\d{2}):(\d{2})$', views.dashboard_request_time, name='index_with_arg'),
]
