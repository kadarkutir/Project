import discord
from discord.ext import commands

class clear(commands.Cog):
    
    def __init__(self,client):
        self.client = client

    
    @commands.command(aliases = ['purge','delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount = 5):
        if int(amount):
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send("Not a number!!")


def setup(client):
    client.add_cog(clear(client))