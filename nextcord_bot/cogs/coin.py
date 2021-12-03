import nextcord
from nextcord.ext import commands
from buttons.coin_buttons import coin_buttons
import random
from database_functions.db_funcs import db_funcs
from embeds.gambling_embeds import gambling_embeds

class coin(commands.Cog):

    def __init__(self,client):
        self.client = client

 
    @commands.command()
    async def coin(self,ctx,amount: int):

        view = coin_buttons()


        random_number = random.randint(0,1)

        win = gambling_embeds.win_embed(amount)
        lose = gambling_embeds.lose_embed(amount)
        coin_embed = gambling_embeds.coin_embed(amount)

        wallet = int(db_funcs.select(ctx.author.id))

        if amount > wallet:
            await ctx.send('You dont have enough token!')
        elif isinstance(amount,int) == False:
            await ctx.send('Enter a number!')
        elif amount <= 0:
            await ctx.send('Enter a valid number!')
        else:
            await ctx.send(embed = coin_embed, view = view)

            await view.wait()

            if view.value == 0:
                if random_number == 0:
                    db_funcs.update_plus(amount,ctx.author.id)

                    win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = win)
                else:
                    db_funcs.update_minus(amount,ctx.author.id)

                    lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = lose)
            elif view.value == 1:
                if random_number == 1:
                    db_funcs.update_plus(amount,ctx.author.id)

                    win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = win)
                else:
                    db_funcs.update_minus(amount,ctx.author.id)

                    lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = lose)
            else:
                await ctx.send("?")

def setup(client):
    client.add_cog(coin(client))