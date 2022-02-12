
import discord
from discord.ext import commands
import time 
from discord import member
import requests
import json
from discord import FFmpegPCMAudio, channel
import CusVars

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

    #@commands.command()
    #async def mood(self, ctx):
   #     await ctx.send('https://cdn.discordapp.com/attachments/821739231096602689/916663736893329459/unknown.png')


#    @commands.command()
 #   async def lie(self , ctx):
  #      await ctx.send('https://cdn.discordapp.com/attachments/821739231096602689/916966639994568764/unknown.png')  

    @commands.command()
    async def random_joke(self, ctx):

        joke_url = "https://random-stuff-api.p.rapidapi.com/joke"
        querystring = {"type":"any"}
        headers = {
            'authorization': "A8LHhqDIb455",
            'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
            'x-rapidapi-key': "f93f5ef4e9mshc465320543c1b4ep1cd458jsnea1c0c7208d0"
        }
        response = requests.request("GET", joke_url, headers=headers, params=querystring)

        embed = discord.Embed(title="Joke",description="These jokes aren't even funny and i know it",color=0x02d475)
        embed.add_field(name="Setup", value=json.loads(response.text)['setup'], inline=True)
        embed.add_field(name="Delivery", value=json.loads(response.text)['delivery'], inline=True)
        await ctx.send(embed=embed)
        #print(joke_1)


    @commands.command()
    async def avatar(self, ctx):
        embed = discord.Embed()
        embed.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)   
 
    @commands.command()
    async def jumpscare(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('jumpscare.ogg')
            player = voice.play(source)
            time.sleep(5)
            await ctx.voice_client.disconnect()
            #kalam gir karde
    @commands.command()
    async def namosn(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('namosn.ogg')
            player = voice.play(source)
            time.sleep(5)
            await ctx.voice_client.disconnect()
            #kalam gir karde  
    @commands.command()
    async def iran(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('srdmeli.ogg')
            player = voice.play(source)
            time.sleep(120)
            await ctx.voice_client.disconnect()        
    @commands.command()
    async def ajili(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('ajili.ogg')
            player = voice.play(source)
            time.sleep(120)
            await ctx.voice_client.disconnect()
#events
    @commands.Cog.listener()
    async def on_member_join(member : discord.Member,message=None):
        
        chmessage = "Welcome To Our Server :) "
        embed = discord.Embed(title = chmessage)
        await channel.send(embed=embed)



def setup(client):
    client.add_cog(Socials(client))

