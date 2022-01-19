#imports
import asyncio
import os
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import json
#from flask_file import keep_alive
import DiscordUtilsMod

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

#MUSIC'
music = DiscordUtilsMod.Music()

@client.command()
async def join(ctx):
    await ctx.author.voice.channel.connect() #Joins author's voice channel
    
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
@client.command()
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        await ctx.author.voice.channel.connect()
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f"Playing {song.name}")
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"Queued {song.name}")
        


@client.command()
async def p(ctx, *, url):
    
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        
        await ctx.author.voice.channel.connect()
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f"Playing {song.name}")
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"Queued {song.name}")


@client.command()
async def Play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        await ctx.author.voice.channel.connect()
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f"Playing {song.name}")
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"Queued {song.name}")


@client.command()
async def P(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        await ctx.author.voice.channel.connect()
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f"Playing {song.name}")
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"Queued {song.name}")
@client.command()
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.send(f"Paused {song.name}")
    
@client.command()
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"Resumed {song.name}")
    
@client.command()
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Stopped")
    
@client.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")
    
@client.command()
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")
    
@client.command()
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(song.name)
    
@client.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")

@client.command()
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.send(f"Changed volume for {song.name} to {volume*100}%")
    
@client.command()
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")




@client.command()
async def info(ctx):
    await ctx.send("`Commands = play to play a song(p,P,Play,play), join to join voice,remove to remove a song from your queue, skip to skip a song,np to see what song is playing right now, join to join your voice channel , resume to resume a paused song, pause to pause a song , leaev to leave a vc,stop to stop the whole queue.Use % as its the bot's prefix . *This Bot Is just For Fun But I'll keep Updating This Project* , Enjoy <3 `")




#keep_alive fucntion uses uptimerobot to keep the application alive
#keep_alive()
#running the code with a secret called 'TOKEN' that is my bot's discord token
token = os.getenv("DISCORD_TOKEN")

client.run(token)
