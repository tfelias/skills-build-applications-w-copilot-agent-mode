from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        users = [
            User(_id=ObjectId(), username='user1', email='user1@example.com', password='password1'),
            User(_id=ObjectId(), username='user2', email='user2@example.com', password='password2'),
        ]
        User.objects.bulk_create(users)

        team = Team(_id=ObjectId(), name='Team A')
        team.save()
        for user in users:
            team.members.add(user)

        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Running', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Cycling', duration=timedelta(hours=2)),
        ]
        Activity.objects.bulk_create(activities)

        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        workouts = [
            Workout(_id=ObjectId(), name='Workout A', description='Description A'),
            Workout(_id=ObjectId(), name='Workout B', description='Description B'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))