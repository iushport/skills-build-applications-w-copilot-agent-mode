from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Removed model registrations as they are no longer compatible with Django admin due to pymongo usage.
