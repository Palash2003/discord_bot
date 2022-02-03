import discord
import json
from discord.ext import commands


async def server_id(server):
    try:
        open(f'{server}.json', 'x')
        with open(f'{server}.json', 'w') as f:
            json.dump({}, f)
    except:
        pass


async def update_data(user, member):
    if not f'{member.id}' in user:
        user[f'{member.id}'] = {}
        user[f'{member.id}']['experience'] = 0
        user[f'{member.id}']['level'] = 1


async def add_experience(user, member, experience):
    user[f'{member.id}']['experience'] += experience


async def level_up(user, member, message):

    experience = user[f'{member.id}']['experience']
    lvl_start = user[f'{member.id}']['level']
    lvl_end = int(1 + experience * (1/100))
    if lvl_end > lvl_start:
        await message.channel.send(f'{member.mention} has levelled up to {lvl_end}')
        user[f'{member.id}']['level'] = lvl_end


class level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await server_id(member.guild.id)
        with open(f'{member.guild.id}.json', 'r') as x:
            user = json.load(x)

        await update_data(self, user, member)

        with open(f'{member.guild.id}.json', 'w') as y:
            json.dump(user, y)

    @commands.Cog.listener()
    async def on_message(self, message):
        await server_id(message.guild.id)
        if message.author.bot == False:
            with open(f'{message.guild.id}.json', 'r') as x:
                user = json.load(x)

            await update_data(user, message.author)
            await add_experience(user, message.author, (len(message.content)/2))
            await level_up(user, message.author, message)

            with open(f'{message.guild.id}.json', 'w') as y:
                json.dump(user, y)

    @commands.command()
    async def level(self, ctx):
        await server_id(ctx.guild.id)
        with open(f'{ctx.guild.id}.json', 'r') as x:
            user = json.load(x)
        level = user[f'{ctx.author.id}']['level']
        experience = user[f'{ctx.author.id}']['experience']
        await ctx.send(f'{ctx.author.mention} is at level {level} and has {experience} experience')


def setup(client):
    client.add_cog(level(client))
