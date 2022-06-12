import discord
from discord.ext import commands
import random

lista = ['rock', 'paper', 'scissor']

class Rps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def compare(self, user_choice):

        bot_choice = random.choice(lista)
        if user_choice == 'rock':
            if bot_choice == 'rock':
                return('tied')
            if bot_choice == 'paper':
                return('lost')
            if bot_choice == 'scissor':
                return('won')

        if user_choice == 'paper':
            if bot_choice == 'rock':
                return('won')
            if bot_choice == 'paper':
                return('tied')
            if bot_choice == 'scissor':
                return('lost')

        if user_choice == 'scissor':
            if bot_choice == 'rock':
                return('lost')
            if bot_choice == 'paper':
                return('won')
            if bot_choice == 'scissor':
                return('tied')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        user_option = str(error).split()[1].strip('"')
        if user_option in lista:
            result = self.compare(user_option)
            if result == 'lost':
                await ctx.send('you lost')
            elif result == 'won':
                await ctx.send('you won')
            elif result == 'tied':
                await ctx.send('you tied')
        else:
            await ctx.send('Give a correct input')

    @commands.command()
    async def Compete(self, ctx, *args):
        try:
            option = args[0]
            if option in lista:
                result = self.compare(option)
                if result == 'lost':
                    await ctx.send('you lost')
                elif result == 'won':
                    await ctx.send('you won')
                elif result == 'tied':
                    await ctx.send('you tied')
            else:
                await ctx.send('Give a correct input')
        except:
            await ctx.send('give some input')


def setup(client):
    client.add_cog(Rps(client))
