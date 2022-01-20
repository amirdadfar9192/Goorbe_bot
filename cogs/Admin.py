import discord
import asyncio
import os
from discord import Member
from discord.ext import commands
from discord.ext.commands import MissingPermissions, has_permissions

class Admin(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def embed(self , ctx):
        embed = discord.Embed(title="Amir", url="https://github.com/amirdadfar9192", description="`Commands = play to play a song(p,P,Play,play), join to join voice,remove to remove a song from your queue, skip to skip a song,np to see what song is playing right now, join to join your voice channel , resume to resume a paused song, pause to pause a song , leave to leave a vc,stop to stop the whole queue.Kick/Ban @user to kick/ban a user.Use % as its the bot's prefix . *This Bot Is just For Fun But I'll keep Updating This Project* , Enjoy <3 `", color=0x8000ff)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/365898254631567360/d325980732e089e58664f01c7174bac9.webp')
        embed.set_footer(text="Thanks For Using This Bot :)")
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx):
        embed = discord.Embed()
        embed.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)    
 
 
    @commands.command()
    @has_permissions(kick_members = True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')
        
    @kick.error
    async def kick_error(self, ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You Dont Have The Required Permission")

    @commands.command()
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been Banned')

    @ban.error
    async def ban_error(self, ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You Dont Have The Required Permission") 



def setup(client):
    client.add_cog(Admin(client))                   

    