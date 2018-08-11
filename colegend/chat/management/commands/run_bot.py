import logging
import random

from discord import Game, Member, TextChannel
from discord.ext import commands
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from colegend.journey.models import Quote

User = get_user_model()


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
        async def on_ready():
            self.stdout.write('...ready')
            logger.info(f'Logged in as {bot.user.name}, id: {bot.user.id}')
            game = Game(name='coLegend.org', url='www.coLegend.org')
            await bot.change_presence(activity=game)

        @bot.listen(name='on_message')
        async def confirm_introduction(message):
            if message.author == bot.user:
                return

            channel = message.channel
            if isinstance(channel, TextChannel) and channel.name == 'introductions':
                # In introducations channel.
                if 'I was here'.lower() in message.content.lower():
                    portal = f'http://app.colegend.org/#/portal/unlock-chat/{message.author.id}'
                    msg = f'I welcome you to our coChat and confirm that you were here.\nTo continue your quest, walk through this portal: {portal}'
                    await message.author.send(msg)

        @bot.command()
        async def quote(ctx):
            """Today's daily quote."""
            quote = Quote.objects.daily_quote()
            if quote:
                await ctx.send(f'{quote.content} — {quote.author}')

        @bot.command()
        async def joined(ctx, member: Member):
            """Says when a member joined."""
            await ctx.send(f'{member.name} joined in {member.joined_at}')

        @bot.command()
        async def roll(ctx, dice: str):
            """Rolls a dice in NdN format."""
            try:
                rolls, limit = map(int, dice.split('d'))
            except Exception:
                await ctx.send('Format has to be in NdN!')
                return

            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            await ctx.send(result)

        @bot.command(name='OUTCOME:')
        async def create_outcome(ctx, *args):
            """Create an outcome. Example: `OUTCOME: my outcome`"""
            try:
                user = User.objects.get(chat_id=ctx.author.id)
            except User.DoesNotExist:
                await ctx.send('No registered coLegend user found.')
                return
            name = ' '.join(args).strip()
            outcome = user.outcomes.create(name=name)
            if quote:
                await ctx.send(f'Created outcome: {outcome}')

        # login & start
        bot.run(settings.BOT_TOKEN)
