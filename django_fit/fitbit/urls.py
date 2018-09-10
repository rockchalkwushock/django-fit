from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

app_name = 'fitbit'
urlpatterns = [
    path('', TemplateView.as_view(template_name='fitbit/index.html')),
    path('api/get_today', views.get_today, name='today'),
    path('api/get_last_week', views.get_last_week, name='last_week'),
    path('api/get_profile', views.get_profile, name='profile')
]
