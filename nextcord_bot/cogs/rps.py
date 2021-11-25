import nextcord
from nextcord.ext import commands
import random
from nextcord.ui import view
from buttons.rps_buttons import rps_buttons
from embeds import gambling_embeds
from database_functions import db_funcs

class rps(commands.Cog):

    def __init__(self,client):
        self.client = client

    
    @commands.command()
    async def rps(self,ctx,amount:int):

        random_num = random.randint(1,3)

        win = gambling_embeds.win_embed(amount)
        lose = gambling_embeds.lose_embed(amount)
        tie = gambling_embeds.tie_embed()
        view = rps_buttons()


        await ctx.send(embed = gambling_embeds.rps_embed(amount),view= view)

        await view.wait()

        if view.value == 1:

            if random_num == 1:

                tie.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                await ctx.send(embed = tie)

            elif random_num == 2:
                db_funcs.update_minus(amount,ctx.author.id)

                lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                await ctx.send(embed = lose)

            elif random_num == 3:
                db_funcs.update_plus(amount,ctx.author.id)

                win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                await ctx.send(embed = win)

        elif view.value == 2:

            if random_num == 2:
                tie.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                await ctx.send(embed = tie)

            elif random_num == 3:
                db_funcs.update_minus(amount,ctx.author.id)

                lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                await ctx.send(embed = lose)

            elif random_num == 1:
                db_funcs.update_plus(amount,ctx.author.id)

                win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                await ctx.send(embed = win)

        elif view.value == 3:

            if random_num == 3:
                tie.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                await ctx.send(embed = tie)

            elif random_num == 1:
                db_funcs.update_minus(amount,ctx.author.id)

                lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                await ctx.send(embed = lose)
                
            elif random_num == 2:
                db_funcs.update_plus(amount,ctx.author.id)

                win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                await ctx.send(embed = win)

        else:
            await ctx.send('?')



def setup(client):
    client.add_cog(rps(client))