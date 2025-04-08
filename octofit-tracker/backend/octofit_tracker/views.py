from pymongo import MongoClient
from rest_framework.response import Response
from rest_framework.decorators import api_view

# MongoDB connection setup
client = MongoClient('localhost', 27017)
db = client['octofit_db']

@api_view(['GET'])
def get_users(request):
    users = list(db.users.find({}, {'_id': 0}))
    return Response(users)

@api_view(['GET'])
def get_teams(request):
    teams = list(db.teams.find({}, {'_id': 0}))
    return Response(teams)

@api_view(['GET'])
def get_activities(request):
    activities = list(db.activity.find({}, {'_id': 0}))
    return Response(activities)

@api_view(['GET'])
def get_leaderboard(request):
    leaderboard = list(db.leaderboard.find({}, {'_id': 0}))
    return Response(leaderboard)

@api_view(['GET'])
def get_workouts(request):
    workouts = list(db.workouts.find({}, {'_id': 0}))
    return Response(workouts)
