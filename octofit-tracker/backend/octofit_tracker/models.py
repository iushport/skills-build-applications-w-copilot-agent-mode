from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('localhost', 27017)
db = client['octofit_db']

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        db.users.insert_one(self.__dict__)

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def save(self):
        db.teams.insert_one(self.__dict__)

class Activity:
    def __init__(self, user, activity_type, duration):
        self.user = user
        self.activity_type = activity_type
        self.duration = duration

    def save(self):
        db.activities.insert_one(self.__dict__)

class Leaderboard:
    def __init__(self, user, score):
        self.user = user
        self.score = score

    def save(self):
        db.leaderboards.insert_one(self.__dict__)

class Workout:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def save(self):
        db.workouts.insert_one(self.__dict__)
