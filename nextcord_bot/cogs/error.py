import nextcord
from nextcord.ext import commands

class unknown(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        await ctx.send(f"An error occured: {str(error)}")
    
    @commands.Cog.listener()
    async def on_message_error(self,ctx, error):
        if isinstance(error, nextcord.ext.commands.errors.CommandNotFound):
            await ctx.send("Unknown command")

def setup(client):
    client.add_cog(unknown(client))