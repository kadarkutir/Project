import nextcord
from nextcord.ext import commands
from embeds.other_embeds import other_embeds
from buttons.rules_buttons import rules_buttons

check ='✅'

class rules(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def rules(self,ctx):
        view = rules_buttons()

        rules_embed = other_embeds.rules_embed(check)

        await ctx.channel.purge(limit = 1)

        await ctx.send(embed = rules_embed,view = view)

        await view.wait()

def setup(client):
    client.add_cog(rules(client))