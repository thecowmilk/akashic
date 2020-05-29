import discord
from discord.ext import commands
import random

class Rate(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rate(self, ctx):
        await ctx.send(f'{random.randint(0, 100)}')




def setup(client):
        client.add_cog(Rate(client))
