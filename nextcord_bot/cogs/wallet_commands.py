import nextcord
from nextcord.ext import commands

class wallet_commands(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def wallet_commands(self,ctx):
        wc_embed = nextcord.Embed(title='Wallet Commands',description='These are the wallet commands',color = 0xfc0313)
        wc_embed.add_field(name='!tokens',value = 'You can check how many tokens you have',inline=False)
        wc_embed.add_field(name='!add amount',value='You can add tokens to your wallet',inline=False)
        wc_embed.set_image(url='https://cdn.dribbble.com/users/527753/screenshots/3743466/coin_gif_dribbble.gif')

        await ctx.channel.purge(limit = 1)
        await ctx.send(embed = wc_embed)


def setup(client):
    client.add_cog(wallet_commands(client))