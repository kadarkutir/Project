import nextcord
from nextcord.ext import commands
from lib import db

class db_commands(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def tokens(self,ctx):
        token = db.record("SELECT Tokens FROM wallet WHERE UserID = ?",ctx.author.id)
        pure_token = str(token).rstrip(",)").lstrip("(")
        text = f"You have {pure_token} tokens in your wallet"

        tokens_embed = nextcord.Embed(title = "Tokens",description = text)
        tokens_embed.set_image(url='https://cdn.dribbble.com/users/370759/screenshots/2266474/untitled-1.gif')


        await ctx.channel.purge(limit = 1)
        await ctx.send(embed = tokens_embed)

    @commands.command()
    async def add(self,ctx,amount):
        db.execute("UPDATE wallet SET Tokens = Tokens + ? WHERE UserID = ?", amount , ctx.author.id)
        db.commit()

        text = f"You added {amount} tokens to your wallet"

        tokens_add_embed = nextcord.Embed(title = "Tokens added", description = text)

        await ctx.channel.purge(limit = 1)
        await ctx.send(embed = tokens_add_embed)

    @commands.command()
    async def token_remove(self,ctx,amount):
        db.execute("UPDATE wallet SET Tokens = Tokens - ? WHERE UserID = ?",amount, ctx.author.id)
        db.commit()

        text = f"You removed {amount} tokens from your wallet"

        tokens_remove_embed = nextcord.Embed(title = "Tokens removed", description = text)

        await ctx.channel.purge(limit = 1)
        await ctx.send(embed = tokens_remove_embed)



def setup(client):
    client.add_cog(db_commands(client))