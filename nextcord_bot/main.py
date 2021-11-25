import nextcord
from nextcord.ext import commands
import os
from token_func import token_reader

intents = nextcord.Intents.all()
nextcord.members = True

client = commands.Bot(command_prefix= '!', intents = intents)

@client.event
async def on_ready():
    print('I am online')

    await client.get_channel(910210085979050004).send('<@&905506455606669333> I am online')

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

client.run(token_reader.token_reader_file("token_func/bot_token.txt"))