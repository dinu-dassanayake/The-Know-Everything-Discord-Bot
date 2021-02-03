import discord
from discord.ext import commands
import random

intents = discord.Intents().all()
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print('Bot is ready. ')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server. ')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server. ')


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidely so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I seeit, yes.',
                 'Most Likely.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
client.run('ODAxOTcwODE2MDc3OTIyMzI0.YAobhg.UsXNaK6NnIfZxj94pmhYzOqHlY8')
