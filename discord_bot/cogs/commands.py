import discord
from discord.ext import commands

class commands(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def commands(self,ctx):


        embedVar = discord.Embed(title = "Commands",description = "These are the commands", color = 0x9966ff)

        embedVar.add_field(name = "Ping", value = "Simple ping command, sends pong", inline = False)

        embedVar.add_field(name = "Clear", value = "Clears the amount of message you give", inline = False)

        embedVar.add_field(name = "Kick", value = "After command name you give the name and the tag and you can give the reason of the kick", inline = False)

        embedVar.set_image(url='https://c.tenor.com/0X9ZWWPhRXMAAAAd/thats-my-command-serpentor.gif')

        embedVar.set_author(name='Deader', icon_url='https://www.italy24news.com/sports/content/uploads/2021/08/29/707e67cd02.jpg')

        await ctx.channel.purge(limit=1)
        
        await ctx.channel.send(embed=embedVar)



def setup(client):
    client.add_cog(commands(client))