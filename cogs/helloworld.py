import discord
from discord.ext import commands


class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def helloworld(self, ctx, *args):

        await ctx.send(" ".join(args))


def setup(client):
    client.add_cog(Hello(client))
