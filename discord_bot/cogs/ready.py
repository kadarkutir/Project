import discord
from discord.ext import commands

class ready(commands.Cog):
    
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is online!")

        await self.client.get_channel(910210085979050004).send('<@&905506455606669333> I am online')
        


def setup(client):
    client.add_cog(ready(client))