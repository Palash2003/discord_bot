import discord
from discord.ext import commands

TOKEN = 'OTM3MzgwNzI5OTIxMzQ3NjA0.Yfa51Q.VAE1JbUB-hXS1JqnyLMdhlmLNGg'

prefix = '%'

client = commands.Bot(command_prefix=prefix)

cogs = ['cogs.helloworld', 'cogs.rps', 'cogs.react', 'cogs.level']

for cog in cogs:
    client.load_extension(cog)


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


client.run(TOKEN)
