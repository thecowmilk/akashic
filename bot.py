import discord
from discord.ext import commands
import random
import os
from discord.ext.commands import Bot
import datetime

client = commands.Bot(command_prefix = '%')


@client.event

async def on_ready():
    
    print("Bot is ready!")


@client.event
async def on_member_join(member):
    
    print(f'{member} has joined the server!')
@client.event
async def on_member_remove(member):
    
    print(f'{member} has left he server! :(')

@client.command()
async def ping(ctx):
    
    await ctx.send(f'Latency of the bot is {round(client.latency * 1000)}ms')
"""
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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
"""

@client.command()
# Clear command is to clear messages, it should be +1 the amount of the messages you want to clear because it counts even the recent command
async def clear(ctx, amount=6):

    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been sent to Gulag')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:

        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} is removed from Gulag')
            return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('/home/kali/Desktop/DiscordBot/PythonSourceCode/cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_message_delete(message):
	guild = message.guild
	log_channel = discord.utils.get(guild.channels, name="log-channel")
	if log_channel is None:
		await client.process_commands(message)
		return
	if not message.author.bot:
		embed=discord.Embed(
			color=0xffd700,
			timestamp=datetime.datetime.utcnow(),
			description="in {}:\n{}".format(message.channel.mention, message.content)
		)
		embed.set_author(name=message.author, icon_url=message.author.avatar_url)
		embed.set_footer(text=message.author.id)
		if len(message.attachments) > 0:
			embed.set_image(url = message.attachments[0].url)
		await log_channel.send(embed=embed)
		await client.process_commands(message)


client.run('NzE0Mzg4MTU0MDA1ODQ4MDc1.Xst9Qg.8tzUOIoCWfAbtxIHK57GvVMWU5I')
