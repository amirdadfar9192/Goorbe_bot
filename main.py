from utils.keep_alive import keep_alive
import discord
from discord.ext import commands
from discord import Member
import os
#import CusVars
import asyncio

print
intents = discord.Intents.all()
intents.members = True
dash = '!------------------------!'
client = commands.Bot(command_prefix='%', intents=intents)


@client.event
async def on_ready():
  print("bot is now ready to use")
  print(dash)
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.listening, name='Prefix == "%" Enjoy:)'))
  keep_alive()


initial_extensions = []


async def load_extt():

  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      initial_extensions.append("cogs." + filename[:-3])
      print(filename)

  if __name__ == '__main__':
    for extension in initial_extensions:
      client.load_extension(extension)


asyncio.run(load_extt())
#token = os.environ.get("Dis-tok")
client.run('OTE2MzIxODQ3NjYwOTI5MDY3.GWI7cw.Fe1EOiJt_KgZFOCqBTEFMqs8eIdc0TtJbD81Bo')
