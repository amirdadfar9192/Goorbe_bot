import discord
from discord.ext import commands
from discord import member


class Minecraft(commands.cog):
    def __init__(self,client):
        self.client = client

        @commands.command(name="end_cord",aliases=["endportal","portal_cord"])
        def end_cord(self,ctx):
            embed = discord.Embed(title="Cords:", description="X:86 Y:58 Z:-3", color=0xe9dc43)
            embed.set_thumbnail(
                url='https://my.mcpedl.com/storage/texturepacks/775/images/nice-cats-texture-pack_3.png')
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        @commands.command(name="home",aliases=["minecraft_home"])
        def home(self,ctx):
            embed = discord.Embed(title="Cords:", description="X:-359 Y:121 Z:-61", color=0xe9dc43)
            embed.set_thumbnail(
                url='https://my.mcpedl.com/storage/texturepacks/775/images/nice-cats-texture-pack_3.png')
            embed.set_footer(text=f"requested by {ctx.author.name}"
                                  ,icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


        @commands.command(name="stronghold", aliases=["Stronghold","str_cord","Str_cord"])
        def stronghold(self,ctx):
            embed = discord.Embed(title="Cords:", description="X:-696 Y:~ Z:1432", color=0xe9dc43)
            embed.set_thumbnail(
                url='https://my.mcpedl.com/storage/texturepacks/775/images/nice-cats-texture-pack_3.png')
            embed.set_footer(text=f'Requsted by {ctx.author.name}',icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Minecraft(client))