import discord
import os
from discord.ext import commands

intents = discord.Intents.all()
discord.members = True

client = commands.Bot(command_prefix = '!',intents = intents)

@client.event 
async def on_member_join(member):
  await member.add_roles(member.guild.get_role(905506001132851220))


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

f = open("token.txt", "r")
TOKEN = f.readline()

client.run(TOKEN)