import discord
from discord.ext import commands
import sqlite3
from lib import db

class select(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def insert(self,ctx):
        db.execute('''
            INSERT INTO wallet (UserID,Tokens)
            VALUES(?,?)
        ''',ctx.author.id , 21)
        db.commit()
        await ctx.send("Added to the database")

    @commands.command()
    async def select(self,ctx):
        token = db.record("SELECT Tokens FROM wallet WHERE UserID = ?",ctx.author.id)
        pure_token = str(token).rstrip(",)").lstrip("(") 

        await ctx.send(f"{pure_token} tokens")

    @commands.command()
    async def add(self,ctx,amount):
        db.execute("UPDATE wallet SET Tokens = Tokens + ? WHERE UserID = ?", amount , ctx.author.id)

        await ctx.send(f"Added {amount} tokens to your wallet")

def setup(client):
    client.add_cog(select(client))