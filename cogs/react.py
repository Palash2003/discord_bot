import discord
from discord.ext import commands


class React(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 371218182356205568:
            await message.add_reaction('🤡')
            await message.reply('Stfu silver')


def setup(client):
    client.add_cog(React(client))
