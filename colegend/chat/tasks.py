from enum import Enum

import requests
from celery import shared_task
from django.conf import settings


class Channel(Enum):
    ANNOUNCEMENTS = settings.CHAT_ANNOUNCEMENTS_WEBHOOK
    COMMUNITY = settings.CHAT_COMMUNITY_WEBHOOK
    HEADQUATERS = settings.CHAT_HEADQUATERS_WEBHOOK


@shared_task
def send_chat_message(message, username="coDroid", avatar_url=None, embeds=[], channel=Channel.COMMUNITY.value):
    """
    Sends a message to a coLegend discord chat channel.
    :param message: The message content to be sent.
    :param color: A color in decimal representation (https://www.spycolor.com/).
    :param embeds: List of discord Embed objects (https://discordapp.com/developers/docs/resources/channel#embed-object) or discord.py Embed instances.
    :param channel: The destination channel (webhook).
    :return:
    """

    data = {
        'content': message,
        'embeds': embeds,
        'username': username,
        'avatar_url': avatar_url or ''
    }

    response = requests.post(channel, json=data)
    return response.ok
