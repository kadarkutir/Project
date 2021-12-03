import nextcord
from nextcord.ext import commands
from buttons.dice_buttons import dice_buttons
from embeds.gambling_embeds import gambling_embeds
import random
from database_functions.db_funcs import db_funcs

class dice(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def dice(self,ctx,amount:int):
        
        view = dice_buttons()

        random_number = random.randint(1,6)

        dice_embed = gambling_embeds.dice_embed(amount)
        win = gambling_embeds.win_embed(amount)
        lose = gambling_embeds.lose_embed(amount)
        wallet = int(db_funcs.select(ctx.author.id))

        if amount > wallet:
            await ctx.send('You dont have enough token!')
        elif isinstance(amount,int) == False:
            await ctx.send('Enter a number!')
        elif amount <= 0:
            await ctx.send('Enter a valid number!')
        else:

            await ctx.send(embed = dice_embed,view= view)

            await view.wait()

            if view.value == 1:
                if random_number == 1:
                    db_funcs.update_plus_5(amount,ctx.author.id)

                    win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = win)
                else:
                    db_funcs.update_minus(amount,ctx.author.id)

                    lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = lose)

            elif view.value == 2:
                if random_number == 2:
                    db_funcs.update_plus_5(amount,ctx.author.id)

                    win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = win)
                else:
                    db_funcs.update_minus(amount,ctx.author.id)

                    lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = lose)
            
            elif view.value == 3:
                if random_number == 3:
                    db_funcs.update_plus_5(amount,ctx.author.id)

                    win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = win)
                else:
                    db_funcs.update_minus(amount,ctx.author.id)

                    lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = lose)

            elif view.value == 4:
                if random_number == 4:
                    db_funcs.update_plus_5(amount,ctx.author.id)

                    win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = win)
                else:
                    db_funcs.update_minus(amount,ctx.author.id)

                    lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = lose)

            elif view.value == 5:
                if random_number == 5:
                    db_funcs.update_plus_5(amount,ctx.author.id)

                    win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = win)
                else:
                    db_funcs.update_minus(amount,ctx.author.id)

                    lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = lose)

            elif view.value == 6:
                if random_number == 6:
                    db_funcs.update_plus_5(amount,ctx.author.id)

                    win.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = win)
                else:
                    db_funcs.update_minus(amount,ctx.author.id)

                    lose.add_field(name = 'Wallet:' , value = f'Your wallet has {db_funcs.select(ctx.author.id)} tokens',inline= False)

                    await ctx.send(embed = lose)
            else:
                await ctx.send('?')




def setup(client):
    client.add_cog(dice(client))