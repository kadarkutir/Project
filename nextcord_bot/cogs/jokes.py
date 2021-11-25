import nextcord
from nextcord.ext import commands



class jokes(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def geri(self,ctx):
        heor = nextcord.Embed(title = "Geri" , color = 0xFFC0CB)

        heor.set_image(url = 'https://phoneky.co.uk/thumbs/screensavers/down/seasonal/romania_gd84sYVa.gif')

        await ctx.channel.send(embed=heor)

    @commands.command()
    async def java(self,ctx):
        java = nextcord.Embed(title = "Uf Java" , color = 0xFFFFFF)

        java.set_image(url = 'https://c.tenor.com/fMUOPRVdSzUAAAAC/python.gif')

        await ctx.channel.send(embed = java)

    @commands.command()
    async def kiehes(self,ctx):
        await ctx.send("Heor heor heor",tts=True)

    @commands.command()
    async def something(self,ctx):
        await ctx.send("Vau vau vau",tts=True)

def setup(client):
    client.add_cog(jokes(client))