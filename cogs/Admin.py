import asyncio
from discord.utils import get
import discord
import os
from discord import Member
from discord.ext import commands
from discord.ext.commands import MissingPermissions, has_permissions


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def embed(self, ctx):
        embed = discord.Embed(title="Amir", url="https://github.com/amirdadfar9192",
                              description="`Commands = play to play a song(p,P,Play,play), join to join voice,remove to remove a song from your queue, skip to skip a song,np to see what song is playing right now, join to join your voice channel , resume to resume a paused song, pause to pause a song , leave to leave a vc,stop to stop the whole queue.Kick/Ban @user to kick/ban a user.Use % as its the bot's prefix . *This Bot Is just For Fun But I'll keep Updating This Project* , Enjoy <3 `",
                              color=0x8000ff)
        embed.set_author(name=ctx.author.display_name,
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/avatars/365898254631567360/d325980732e089e58664f01c7174bac9.webp')
        embed.set_footer(text="Thanks For Using This Bot :)")
        await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"user {member} has been kicked")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You Dont Have The Required Permission")

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been Banned')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You Dont Have The Required Permission")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, user: discord.Member, role: discord.Role):
        if role in user.roles:
            await ctx.send(f"user already has {role} :)")
        else:
            await user.add_roles(role)
            await ctx.send(f"Added {role} to {user.mention}")

    @addrole.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You Dont Have The Permission :(")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, user: discord.Member, role: discord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"Removed {role} from {user.mention}:)")
        else:
            await ctx.send(f"{user.mention} Doesn't Have {role} :( ")

    @removerole.error
    async def removerole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You Dont Have The Permission :(")

    @commands.command(name='clear', aliases=['c'], help='Clears the current text channel')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = None):
        global confirmMsgID, confirmMsgUserID

        if amount is None:
            em = discord.Embed(
                title="React to this message with :no_entry_sign: to confirm clearing the whole text channel. (This message automatically deletes after 5 seconds)",
                colour=discord.Color.purple())
            em.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)

            confirmMsg = await ctx.send(embed=em)
            await confirmMsg.add_reaction('\N{NO ENTRY SIGN}')
            confirmMsgID = confirmMsg.id
            confirmMsgUserID = ctx.author.id
            return

        if isinstance(amount, int) and amount > 0:
            await ctx.channel.purge(limit=amount + 1)

            em = discord.Embed(
                title=f"**{amount}** messages were deleted", colour=discord.Color.purple())
            em.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)

            delMsg = await ctx.send(embed=em)
            await asyncio.sleep(3)
            await delMsg.delete()
        else:
            em = discord.Embed(title=f"Please specify a valid number of messages to delete",
                               colour=discord.Color.purple())
            em.set_footer(
                text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)

            return await ctx.send(embed=em)

    @commands.Cog.listener()
    async def on_command_error(self,error,ctx):
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            em = discord.Embed(title=f"Unknown command {str(error)}",colour=discord.Color.dark_magenta())
            em.set_footer(text="Use %help TO See Available Commands :)")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        try:
            confirmMsgID
        except NameError:
            return
        if reaction.message.id == confirmMsgID and reaction.emoji == '\N{NO ENTRY SIGN}' and user.id != self.client.user.id and user.id == confirmMsgUserID:
            await reaction.message.channel.purge(limit=None)

            em = discord.Embed(title=f"This channel was cleared",
                               colour=discord.Color.purple())
            em.set_footer(
                text=f"Requested by {user.name}", icon_url=user.avatar_url)

            delMsg = await reaction.message.channel.send(embed=em)
            await asyncio.sleep(3)
            return await delMsg.delete()


def setup(client):
    client.add_cog(Admin(client))
