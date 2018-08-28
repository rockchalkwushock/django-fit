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
        'caloriesOut': response['summary']['caloriesOut'],
        'distance': response['summary']['distances'][0]['distance'],
        'floors': response['summary']['floors'],
        'steps': response['summary']['steps']
    }


# {
#     'activities': [],
#     'goals': {
#         'activeMinutes': 30,
#         'caloriesOut': 2978,
#         'distance': 8.05,
#         'floors': 10,
#         'steps': 10000
#     },
#     'summary': {
#         'activeScore': -1,
#         'activityCalories': 365,
#         'caloriesBMR': 1037,
#         'caloriesOut': 1363,
#         'distances': [
#             {'activity': 'total', 'distance': 2.21},
#             {'activity': 'tracker', 'distance': 2.21},
#             {'activity': 'loggedActivities', 'distance': 0},
#             {'activity': 'veryActive', 'distance': 0},
#             {'activity': 'moderatelyActive', 'distance': 0},
#             {'activity': 'lightlyActive', 'distance': 2.21},
#             {'activity': 'sedentaryActive', 'distance': 0}],
#         'elevation': 27.43,
#         'fairlyActiveMinutes': 0,
#         'floors': 9,
#         'heartRateZones': [
#             {'caloriesOut': 537.42096, 'max': 95, 'min': 30,
#                 'minutes': 299, 'name': 'Out of Range'},
#             {'caloriesOut': 105.70242, 'max': 133, 'min': 95,
#                 'minutes': 19, 'name': 'Fat Burn'},
#             {'caloriesOut': 72.47478, 'max': 161,
#                 'min': 133, 'minutes': 6, 'name': 'Cardio'},
#             {'caloriesOut': 0, 'max': 220, 'min': 161, 'minutes': 0, 'name': 'Peak'}
#         ],
#         'lightlyActiveMinutes': 67,
#         'marginalCalories': 232,
#         'restingHeartRate': 62,
#         'sedentaryMinutes': 795,
#         'steps': 2996,
#         'veryActiveMinutes': 0
#     }
# }
