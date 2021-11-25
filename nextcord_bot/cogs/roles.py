import nextcord
from nextcord.ext import commands
from buttons.roles_buttons import roles_buttons
from embeds import other_embeds

class role(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def roles(self,ctx):
        view = roles_buttons()

        roles_embed = other_embeds.roles_embed()

        await ctx.channel.purge(limit = 1)

        await ctx.send(embed = roles_embed,view = view)

        await view.wait()



def setup(client):
    client.add_cog(role(client))