
import discord
from discord.ext import commands
from discord import Member
import os
import CusVars

intents = discord.Intents.default()
intents.members = True
dash = '!------------------------!'
client = commands.Bot(command_prefix = '%', intents = intents)


@client.event
async def on_ready():
    print("bot is now ready to use")
    print(dash)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Prefix == "%" Enjoy:)'))



initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])
    


if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)          

token = os.getenv("DISCORD_TOKEN")
client.run(token)    