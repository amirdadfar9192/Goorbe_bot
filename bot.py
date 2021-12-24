#imports
import os
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import json
#from flask_file import keep_alive
import youtube_dl
#vars
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '%', intents = intents)
dash = '!------------------------!'

#funcions
@client.event
async def on_ready():
    print("bot is now ready to use")
    print(dash)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Prefix = % , Have Fun =)'))
    
#useless commands
#!     
#!
#▼
@client.command()
async def what(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/821739231096602689/917020202871435275/unknown.png")


@client.command()
async def on(ctx):
    await ctx.send("im On bb")

@client.command()
async def bye(ctx):
    await ctx.send(' https://cdn.discordapp.com/attachments/662046048524435482/916652574294294578/unknown.png')

@client.command()
async def mood(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/821739231096602689/916663736893329459/unknown.png')


@client.command()
async def lie(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/821739231096602689/916966639994568764/unknown.png')  
#▲
#!
#!


#@client.event
#async def on_member_join(member):
#    channel = client.get_channel(821739231096602689)
#    await channel.send("Hi")    

#MUSIC

@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('piano.wav')
        player = voice.play(source)
    else:
        await ctx.send("You Are not In a VC!!!")   




@client.command(pass_context = True)
async def dc(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the VC")
    else:
        await ctx.send("I'm not in a VC")






























@client.command()
async def info(ctx):
    await ctx.send("`Commands = play to play a song(p,P,Play,play), join to join voice,remove to remove a song from your queue, skip to skip a song,np to see what song is playing right now, join to join your voice channel , resume to resume a paused song, pause to pause a song , disconnect to leave a vc,stop to stop the whole queue.Use % as its the bot's prefix . *This Bot Is just For Fun But I'll keep Updating This Project* , Enjoy <3 `")




#keep_alive fucntion uses uptimerobot to keep the application alive
#keep_alive()
#running the code with a secret called 'TOKEN' that is my bot's discord token
token = os.getenv("DISCORD_TOKEN")

client.run(token)
