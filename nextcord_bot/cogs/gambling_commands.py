import nextcord
from nextcord.ext import commands

class gambling_commands(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def gambling_commands(self,ctx):
        gc_embed = nextcord.Embed(title='Gambling Commands',description='These are the gambling commands',color= 0xba4141)
        gc_embed.add_field(name='!coin amount',value='Coin flip game',inline=False)
        gc_embed.add_field(name='!rps amount',value='Rock paper scissor game',inline=False)
        gc_embed.add_field(name='!dice amount',value='Dice game',inline=False)
        gc_embed.set_image(url='https://c.tenor.com/5vo_w_jDfwgAAAAC/calculation-math.gif')

        await ctx.channel.purge(limit= 1)
        await ctx.send(embed = gc_embed)




def setup(client):
    client.add_cog(gambling_commands(client))