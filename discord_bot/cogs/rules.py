import discord
from discord import message
from discord.colour import Color
from discord.ext import commands

class rules(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def rules(self,ctx):
        check = ':white_check_mark:'

        rules_embed = discord.Embed(title = 'Rules:' ,description = 'These are the rules',color = 0x9966ff)
        

        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed = rules_embed)
        await message.add_reaction(emoji=check)



def setup(client):
    client.add_cog(rules(client))