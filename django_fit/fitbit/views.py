from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from requests import get
from datetime import datetime

from .serializers import UserSerializer


class UserList(viewsets.ModelViewSet):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


def get_current_activity(request):
    today = datetime.now()
    social = self.request.user.social_auth.get(provider='fitbit')
    token = social.extra_data['access_token']
    r = get(f'https://api.fitbit.com/1/user/-/activities/date/{today.year}-{today.month}-{today.day}.json', headers={
        'authorization': f'Bearer {token}'
    })
    response = r.json()
    return {
        'calories_out': response['summary']['caloriesOut'],
        'calories_bmr': response['summary']['caloriesBMR'],
        'distance': response['summary']['distances'][0]['distance'],
        'floors': response['summary']['floors'],
        'heart_rate': [
            {
                'calories_out': response['summary']['heartRateZones'][0]['caloriesOut'],
                'max': response['summary']['heartRateZones'][0]['max'],
                'min': response['summary']['heartRateZones'][0]['min'],
                'minutes': response['summary']['heartRateZones'][0]['minutes'],
                'name': 'Out of Range',
            },
            {
                'calories_out': response['summary']['heartRateZones'][1]['caloriesOut'],
                'max': response['summary']['heartRateZones'][1]['max'],
                'min': response['summary']['heartRateZones'][1]['min'],
                'minutes': response['summary']['heartRateZones'][1]['minutes'],
                'name': 'Fat burn',
            },
            {
                'calories_out': response['summary']['heartRateZones'][2]['caloriesOut'],
                'max': response['summary']['heartRateZones'][2]['max'],
                'min': response['summary']['heartRateZones'][2]['min'],
                'minutes': response['summary']['heartRateZones'][2]['minutes'],
                'name': 'Cardio',
            },
            {
                'calories_out': response['summary']['heartRateZones'][3]['caloriesOut'],
                'max': response['summary']['heartRateZones'][3]['max'],
                'min': response['summary']['heartRateZones'][3]['min'],
                'minutes': response['summary']['heartRateZones'][3]['minutes'],
                'name': 'Peak',
            }
        ],
        'steps': response['summary']['steps']
    }
