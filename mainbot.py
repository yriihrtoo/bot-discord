
     await ctx.send(coins(second))
import discord
from discord.ext import commands
from bot_logic import coins, gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def kooin(ctx, second=1):
@bot.command()
async def createpass(ctx):
     await ctx.send(gen_pass(8))

bot.run("MTE1MTUwMDQ4OTc4NDA0NTY2MQ.GIfVsr.SEjp0Fv8HvE3w_a1ANQx_8YCQGtdz8jL-ZLwqQ")
