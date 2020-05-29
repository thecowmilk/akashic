import discord
from discord.ext import commands
import random


class fun(commands.Cog):

    def __init__(self, client):

        self.client = client


    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
	    responses = ['It is certain.',
	                 'No',
	                 'Yes.',
	                 'I can say so...',
	                 'Most Likely...',
	                 'It is decided - YES!'
	                 'My sources says no.'
	                 'It is decided - NO.']

	    if "how big" in question.lower() or "on a scale" in question.lower():
	        await ctx.send(f'Question: {question}\nAnswer: {random.randint(0, 100)}')

	    else:
	        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    


def setup(client):
    client.add_cog(fun(client))





