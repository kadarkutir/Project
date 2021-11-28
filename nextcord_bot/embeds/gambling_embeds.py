import nextcord
from nextcord.ext import commands

def coin_embed(amount):
    coin_embed = nextcord.Embed(title = 'Coin Flip',color= 0x1adb51)
    coin_embed.add_field(name = 'Bet:' ,value = f'Your bet is {amount} tokens',inline = False)
    coin_embed.set_image(url='https://acegif.com/wp-content/uploads/coin-flip.gif')
    coin_embed.set_footer(text = 'Choose one!')

    return coin_embed

def rps_embed(amount):
    rps_embed = nextcord.Embed(title = 'Rock Paper Scissors',color = 0x1adb51)
    rps_embed.add_field(name = 'Bet:' , value = f'Your bet is {amount} tokens',inline = False)
    rps_embed.set_image(url = 'https://cdn.dribbble.com/users/14356/screenshots/2406950/hands.gif')
    rps_embed.set_footer(text = 'Choose one!')

    return rps_embed

def dice_embed(amount):
    dice_embed = nextcord.Embed(title = 'Dice',color = 0x1adb51)
    dice_embed.add_field(name = 'Bet:' ,value = f'Your bet is {amount} tokens',inline = False)
    dice_embed.set_image(url = 'https://c.tenor.com/IfbgWLbg_88AAAAC/dice.gif')
    dice_embed.set_footer(text = 'Choose one!')

    return dice_embed

def win_embed(amount):
    win = nextcord.Embed(title = 'You won',color = 0x1adb51)
    win.add_field(name = 'Bet:' , value = f'You won {amount}.',inline= False)
    win.set_image(url='https://c.tenor.com/9oyVodbFp0AAAAAM/win-confetti.gif')

    return win

def lose_embed(amount):
    lose = nextcord.Embed(title = 'You lost' , color = 0xdb201a)
    lose.add_field(name = 'Bet:' , value = f'You lost {amount}.',inline= False)
    lose.set_image(url= 'https://media.giphy.com/media/eJ4j2VnYOZU8qJU3Py/giphy.gif')

    return lose


def tie_embed():
    tie = nextcord.Embed(title = 'Its a tie!',color = 0xfc0390)
    tie.set_image(url = 'https://c.tenor.com/aZ567AEAfqcAAAAM/helen-magnus.gif')

    return tie