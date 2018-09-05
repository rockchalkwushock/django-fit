from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from requests import get
from json import dumps
from social_django.utils import load_strategy
from django.http import HttpResponse
from datetime import datetime, timedelta

from .serializers import UserSerializer


class UserList(viewsets.ModelViewSet):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


def get_today(request):
    today = datetime.now()
    social = request.user.social_auth.get(provider='fitbit')
    token = social.extra_data['access_token']
    r = get(f'https://api.fitbit.com/1/user/-/activities/date/{today.year}-{today.month}-{today.day}.json', headers={
        'authorization': f'Bearer {token}'
    })
    response = r.json()
    if response.get('errors', None):
        if response['errors'][0]['message'] == 'Too Many Requests':
            return HttpResponse(content='Too Many Requests')
    if response['summary'].get('heartRateZones', None):
        data = {
            'calories_out': response['summary']['caloriesOut'],
            'calories_bmr': response['summary']['caloriesBMR'],
            'distance': response['summary']['distances'][0]['distance'],
            'floors': response['summary']['floors'],
            'heart_rate': [
                {
                    'calories_out': round(response['summary']['heartRateZones'][0]['caloriesOut'], 0),
                    'max': response['summary']['heartRateZones'][0]['max'],
                    'min': response['summary']['heartRateZones'][0]['min'],
                    'minutes': response['summary']['heartRateZones'][0]['minutes'],
                    'name': 'Out of Range',
                },
                {
                    'calories_out': round(response['summary']['heartRateZones'][1]['caloriesOut'], 0),
                    'max': response['summary']['heartRateZones'][1]['max'],
                    'min': response['summary']['heartRateZones'][1]['min'],
                    'minutes': response['summary']['heartRateZones'][1]['minutes'],
                    'name': 'Fat burn',
                },
                {
                    'calories_out': round(response['summary']['heartRateZones'][2]['caloriesOut'], 0),
                    'max': response['summary']['heartRateZones'][2]['max'],
                    'min': response['summary']['heartRateZones'][2]['min'],
                    'minutes': response['summary']['heartRateZones'][2]['minutes'],
                    'name': 'Cardio',
                },
                {
                    'calories_out': round(response['summary']['heartRateZones'][3]['caloriesOut'], 0),
                    'max': response['summary']['heartRateZones'][3]['max'],
                    'min': response['summary']['heartRateZones'][3]['min'],
                    'minutes': response['summary']['heartRateZones'][3]['minutes'],
                    'name': 'Peak',
                }
            ],
            'steps': response['summary']['steps']
        }
    else:
        data = {
            'calories_out': response['summary']['caloriesOut'],
            'calories_bmr': response['summary']['caloriesBMR'],
            'distance': response['summary']['distances'][0]['distance'],
            'floors': response['summary']['floors'],
            'steps': response['summary']['steps']
        }

    return HttpResponse(content=dumps(data))


def get_last_week(request):
    today = datetime.now()
    social = request.user.social_auth.get(provider='fitbit')
    token = social.extra_data['access_token']
    calories = []
    distance = []
    floors = []
    labels = []
    steps = []
    for i in range(7):
        delta = timedelta(days=i)
        time = today - delta
        r = get(f'https://api.fitbit.com/1/user/-/activities/date/{time.year}-{time.month}-{time.day}.json', headers={
            'authorization': f'Bearer {token}'
        })
        response = r.json()
        if response.get('errors', None):
            if response['errors'][0]['message'] == 'Too Many Requests':
                return HttpResponse(content='Too Many Requests')
        calories.append(response['summary']['caloriesOut'])
        distance.append(response['summary']['distances'][0]['distance'])
        floors.append(response['summary']['floors'])
        labels.append(f'{time.year}-{time.month}-{time.day}')
        steps.append(response['summary']['steps'])
    calories.reverse()
    distance.reverse()
    floors.reverse()
    labels.reverse()
    steps.reverse()
    data = {
        'calories': calories,
        'distance': distance,
        'floors': floors,
        'labels': labels,
        'steps': steps
    }
    return HttpResponse(content=dumps(data))


def get_profile(request):
    social = request.user.social_auth.get(provider='fitbit')
    token = social.extra_data['access_token']
    r = get('https://api.fitbit.com/1/user/-/profile.json', headers={
        'authorization': f'Bearer {token}'
    })
    response = r.json()
    if response.get('errors', None):
        if response['errors'][0]['message'] == 'Too Many Requests':
            return HttpResponse(content='Too Many Requests')
        elif response['errors'][0]['errorType'] == 'expired_token':
            strategy = load_strategy()
            social.refresh_token(strategy)
    data = {
        'age': response['user']['age'],
        'avatar': response['user']['avatar150'],
        'distance_unit': response['user']['distanceUnit'],
        'full_name': response['user']['fullName'],
        'height': response['user']['height'],
        'height_unit': response['user']['heightUnit'],
        'username': response['user']['username'],
        'weight': response['user']['weight'],
        'weight_unit': response['user']['weightUnit'],
    }
    return HttpResponse(content=dumps(data))
