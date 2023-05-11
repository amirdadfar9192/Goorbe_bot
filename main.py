from utils.keep_alive import keep_alive
import discord
import discord.ext
from discord.ext import commands
from discord import Member
import os
#import CusVars
import asyncio

intents = discord.Intents.all()
intents.members = True
dash = '!------------------------!'
client = commands.Bot(command_prefix='%', intents=intents)

initial_extensions = []


async def load_extensions():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      # cut off the .py from the file name
      await client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_ready():
  print("bot is now ready to use")
  print(dash)
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.listening, name='Prefix == "%" Enjoy:)'))
  await client.tree.sync()
  keep_alive()


asyncio.run(load_extensions())


@client.tree.command(
  name="hello", description="Hello"
)  #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
  await interaction.response.send_message("Hello!")


token = os.environ.get("token")
client.run(token)
