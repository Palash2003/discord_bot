from cmath import exp
import sys
import json
import discord
from discord.ext import commands

path = sys.path[0]+'/database'


async def load_user(guild):
    with open(f'{path}/{guild}.json', 'r') as f:
        user = json.load(f)
    return user


async def save_user(user, guild):
    with open(f'{path}/{guild}.json', 'w') as f:
        json.dump(user, f, indent=2)
    return user


async def server_id(server):
    try:
        open(f'{path}/{server}.json', 'x')
        with open(f'{path}/{server}.json', 'w') as f:
            json.dump({}, f, indent=2)
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
        user = await load_user(member.guild.id)
        await update_data(self, user, member)
        await save_user(user, member.guild.id)

    @commands.Cog.listener()
    async def on_message(self, message):
        await server_id(message.guild.id)
        if message.author.bot == False:
            user = await load_user(message.guild.id)
            await update_data(user, message.author)
            await add_experience(user, message.author, (len(message.content)/2))
            await level_up(user, message.author, message)
            await save_user(user, message.guild.id)

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        await server_id(ctx.guild.id)
        user = await load_user(ctx.guild.id)
        if not member:
            await update_data(user, ctx.author)
            member = ctx.author
            level = user[f'{ctx.author.id}']['level']
            experience = user[f'{ctx.author.id}']['experience']
        else:
            print(member.id)
            await update_data(user, member)
            level = user[f'{member.id}']['level']
            experience = user[f'{member.id}']['experience']
            print(level, experience)
        await ctx.send(embed=discord.Embed(title=f'{member.name}', description=f'Level: {level}\nExperience: {experience}', color=discord.Color.blue()))


def setup(client):
    client.add_cog(level(client))
