import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions

class kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(kick_members = True)
    async def kick(self,ctx,user : discord.Member,*,reason = "No reason"):
        await user.send(f"You have been kicked for {reason}")
        await user.kick(reason = reason)
        await ctx.send(f"{user} has been kicked")

def setup(client):
    client.add_cog(kick(client))