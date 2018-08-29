from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('fitbit', views.UserList)

app_name = 'fitbit'
urlpatterns = [
    path('', TemplateView.as_view(template_name='fitbit/index.html')),
    path('api/', include(router.urls), name='api'),
    path('api/get_current_activity', views.get_current_activity, name='activity')
]
