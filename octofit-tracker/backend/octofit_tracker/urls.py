"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import get_users, get_teams, get_activities, get_leaderboard, get_workouts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', get_users, name='get_users'),
    path('api/teams/', get_teams, name='get_teams'),
    path('api/activities/', get_activities, name='get_activities'),
    path('api/leaderboard/', get_leaderboard, name='get_leaderboard'),
    path('api/workouts/', get_workouts, name='get_workouts'),
]
