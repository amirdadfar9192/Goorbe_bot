import discord
from discord.ext import commands
import time 
import ffmpeg
from discord import FFmpegPCMAudio

class Socials(commands.Cog):

    def __init__(self, client):
        self.client = client
    #commands
    @commands.command()
    async def what(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/821739231096602689/917020202871435275/unknown.png")

    @commands.command()
    async def info(ctx):
        await ctx.send("`Commands = play to play a song(p,P,Play,play), join to join voice,remove to remove a song from your queue, skip to skip a song,np to see what song is playing right now, join to join your voice channel , resume to resume a paused song, pause to pause a song , leave to leave a vc,stop to stop the whole queue.Kick/Ban @user to kick/ban a user.Use % as its the bot's prefix . *This Bot Is just For Fun But I'll keep Updating This Project* , Enjoy <3 `")
    @commands.command()
    async def on(self, ctx):
        await ctx.send("im On bb")

    @commands.command()
    async def bye(self , ctx):
        await ctx.send(' https://cdn.discordapp.com/attachments/662046048524435482/916652574294294578/unknown.png')

    @commands.command()
    async def mood(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/821739231096602689/916663736893329459/unknown.png')


    @commands.command()
    async def lie(self , ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/821739231096602689/916966639994568764/unknown.png')  


    @commands.command()
    async def jumpscare(self ,ctx):
        # Gets voice channel of message author
        voice_channel = ctx.author.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="C:<path_to_file>"))
            # Sleep while audio is playing.
            while vc.is_playing():
                time.sleep(3)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete()    
    
#events
    @commands.Cog.listener()
    async def on_member_join(member : discord.Member,*, message=None):
        chmessage = "Welcome To Our Server :) "
        embed = discord.Embed(title = chmessage)
        await member.send(embed=embed)



def setup(client):
    client.add_cog(Socials(client))
