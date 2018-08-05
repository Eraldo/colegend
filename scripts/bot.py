import logging
import random

from discord import Game, Member
from discord.ext import commands
from django.conf import settings

from colegend.journey.models import Quote


def run():
    """
    Run coDroind: coLegend's discord chat bot.
    Howto: `./manage.py runscript bot`
    :return:
    """
    logger = logging.getLogger(__name__)

    description = '''coDroid: I am coLegends chat service robot. :D'''
    bot = commands.Bot(command_prefix='?', description=description)

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
