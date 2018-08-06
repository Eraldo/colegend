import logging
import random

from discord import Game, Member
from discord.ext import commands
from django.conf import settings
from django.core.management.base import BaseCommand

from colegend.journey.models import Quote


class Command(BaseCommand):
    help = 'Run coDroid chatbot.'

    def handle(self, *args, **options):
        """
        Run coDroind: coLegend's discord chat bot.
        Howto: `./manage.py runscript bot`
        :return:
        """
        logger = logging.getLogger(__name__)

        self.stdout.write('Starting coDroid')

        description = '''coDroid: I am coLegends chat service robot. :D'''
        bot = commands.Bot(command_prefix='?', description=description)


        @bot.event
        async def on_message(message):
            # we do not want the bot to reply to itself
            if message.author == bot.user:
                return

            # TODO: Only introductions channel counts.
            if 'I was here'.lower() in message.content.lower():
                portal = 'http://app.colegend.org/#/portal/unlock-chat'
                msg = f'I welcome you to our coChat and confirm that you were here.\nTo continue your quest, walk through this portal: {portal}'
                await bot.send_message(message.author, msg)

        @bot.command()
        async def quote():
            """Today's daily quote."""
            quote = Quote.objects.daily_quote()
            if quote:
                await bot.say(f'{quote.content} — {quote.author}')

        @bot.event
        async def on_ready():
            game = Game(name='coLegend.org', url='www.coLegend.org')
            await bot.change_presence(game=game, activity=game)
            logger.info(f'Logged in as {bot.user.name}, id: {bot.user.id}')

        @bot.command()
        async def joined(member: Member):
            """Says when a member joined."""
            await bot.say(f'{member.name} joined in {member.joined_at}')

        @bot.command()
        async def roll(dice: str):
            """Rolls a dice in NdN format."""
            try:
                rolls, limit = map(int, dice.split('d'))
            except Exception:
                await bot.say('Format has to be in NdN!')
                return

            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            await bot.say(result)

        @bot.event
        async def on_ready():
            logger.info(f'Logged in as {bot.user.name}, id: {bot.user.id}')

        # login & start
        bot.run(settings.BOT_TOKEN)
