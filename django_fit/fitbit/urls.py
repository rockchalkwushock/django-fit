from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'fitbit'
urlpatterns = [
    path('', TemplateView.as_view(template_name='fitbit/index.html')),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail')
]
