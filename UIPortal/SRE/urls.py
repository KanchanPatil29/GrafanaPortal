from django.urls import path
from .views import switch_comapny, project_dashbaord

app_name = "admin"

urlpatterns = [
    path(r'http://grafana.monitoring.bfsgodirect.com:3000/login', project_dashbaord, name='project_dashboard'),
    path(r'switchcompany', switch_comapny, name='switchcompany'),

    ]