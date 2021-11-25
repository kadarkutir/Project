import  nextcord
from nextcord.ext import commands
from nextcord.ext.commands.flags import F

def welcome_embed(member):
    welcome_embed = nextcord.Embed(title = f"Welcome to the **{member.guild.name}**" , description = f"Go to the <#912759943927562290> to get further information about the sever!", color = 0xc8fc0d)
    welcome_embed.set_image(url = "https://acegif.com/wp-content/uploads/2021/4fh5wi/welcome-15.gif")

    return welcome_embed

def rules_embed(check):
    rules_embed = nextcord.Embed(title = 'Rules:' ,description = 'These are the rules',color = 0x9966ff)
        
    rules_embed.add_field(name = "1." , value = "Be respectful, civil, and welcoming." , inline= False)
    rules_embed.add_field(name = "2." , value = "No inappropriate or unsafe content.", inline= False)
    rules_embed.add_field(name = "3." , value = "Any content that is NSFW is not allowed under any circumstances.", inline= False)
    rules_embed.add_field(name = "4." , value = "Spamming in any form is not allowed.", inline= False)
    rules_embed.add_field(name = "5." , value = "Don’t ping without legitimate reasoning behind them.", inline= False)
    rules_embed.add_field(name = "6." , value = "This is a gambling server only 18+")
    rules_embed.add_field(name = "To enter the server:" , value = f"Click on the {check} emote" , inline= False)
    rules_embed.set_image(url= "https://c.tenor.com/vmtAb5F7auoAAAAd/rules.gif")

    return rules_embed

def roles_embed():
    roles_embed = nextcord.Embed(title = 'Roles:',description = 'These are the roles',color = 0x9966ff)

    roles_embed.add_field(name = '🎵' , value = 'Music role' ,inline = False)
    roles_embed.add_field(name = '💜' , value = 'Purple role' , inline = False)
    roles_embed.add_field(name = '💛' , value = 'Yellow role' ,inline = False)
    roles_embed.add_field(name = '💚' , value = 'Green role' , inline = False)

    roles_embed.set_image(url = 'https://c.tenor.com/j7h26rYOqnAAAAAC/roles.gif')
    roles_embed.set_footer(text = 'Choose your roles')

    return roles_embed