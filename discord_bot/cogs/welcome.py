import discord
from discord.ext import commands

class welcome(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self,member):
        
        await self.client.get_channel(905200327597379605).send(f"Welcome to the **{member.guild.name}** {member.mention}! Head over to <#891459240475107361> to say hi!")
        


def setup(client):
    client.add_cog(welcome(client))