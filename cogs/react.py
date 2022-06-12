import discord
from discord.ext import commands


class React(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 604361814569910324:
            await message.reply('abc')
            await message.reaction('🤣')


def setup(client):
    client.add_cog(React(client))
