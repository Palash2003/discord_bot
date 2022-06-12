import discord
import os
from discord.ext import commands

token = os.environ.get('TOKEN')
prefix = os.environ.get('PREFIX')
print(token)
print(prefix)
client = commands.Bot(command_prefix=prefix)

cogs = ['cogs.helloworld', 'cogs.rps', 'cogs.react', 'cogs.level']

for cog in cogs:
    client.load_extension(cog)


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))


@client.event
async def on_message(message):
    if message.author.id == '604361814569910324' or message.author.id == '422738565215158273':
        await message.delete()

client.run(token)
