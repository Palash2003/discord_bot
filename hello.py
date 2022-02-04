import discord
import os
from discord.ext import commands

token = os.environ.get('TOKEN')
prefix = os.environ.get('PREFIX')

client = commands.Bot(command_prefix=prefix)

cogs = ['cogs.helloworld', 'cogs.rps', 'cogs.react', 'cogs.level']

for cog in cogs:
    client.load_extension(cog)


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))


client.run(token)
