# [django-fit](http://rockchalkwushock.pythonanywhere.com/)

PDX Code Guild Capstone Project - Fitbit Dashboard

## Project Overview

`django-fit` will allow an end user to sign in to the application and view their fitbit data. The application will make use of `django`, `vuejs`, and `chartjs`.

## Functionality

A user should be able to authenticate with their fitbit account.
A user should be able to give permission to fitbit for the app to access their data.
A user should be able to view their data.
A user should be able to filter their data for the current day, week, and month.
A user should be able to filter the category of data they are viewing.

## Data Model

I will need to store the tokens from the fitbit api of authentication and continued access to the user's data.

```python
class User(models.Model):
  access_token = models.CharField(maxlength=250, unique=True)
  refresh_token = models.CharField(maxlength=250, unique=True)
  # ... other values
```

## Schedule

I think spinning up the app for authentication between the application and the fitbit api will take the longest since I'm going to write this code from scratch instead of using a module. I am giving myself 2 weeks to write this (wish list: write tests for code). I feel the final 3 weeks of the program will be sufficient time to write the frontend views using VueJS and ChartJS.
