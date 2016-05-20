"""
Utility functions to handle slack invites and information.
"""
from django.conf import settings
from .api import invite, get_users


def invite_user(user):
    team_id = settings.SLACK_TEAM_ID
    api_token = settings.SLACK_TOKEN
    email = user.email
    return invite(team_id, api_token, email)


def check_user(user):
    team_id = settings.SLACK_TEAM_ID
    api_token = settings.SLACK_TOKEN
    email = user.email
    username = user.username
    users, online_users = get_users(team_id, api_token)
    user = [user for user in users if user.get('name') == username and user.get('profile', {}).get('email') == email]
    return bool(user)
