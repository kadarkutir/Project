import nextcord
from nextcord.ext import commands

class roles_buttons(nextcord.ui.View):

    def __init__(self):
        super().__init__(timeout = None)


    @nextcord.ui.button(label = '🎵', style = nextcord.ButtonStyle.grey)
    async def music(self,button: nextcord.ui.Button,interaction: nextcord.Interaction):
        music_role = interaction.guild.get_role(913060931032981504)

        await interaction.user.add_roles(music_role)


    @nextcord.ui.button(label = '💜',style= nextcord.ButtonStyle.grey)
    async def purple(self,button: nextcord.ui.Button,interaction: nextcord.Interaction):
        purple_role = interaction.guild.get_role(913061116979068929)

        await interaction.user.add_roles(purple_role)

    @nextcord.ui.button(label = '💛',style= nextcord.ButtonStyle.grey)
    async def yellow(self,button: nextcord.ui.Button,interaction: nextcord.Interaction):
        yellow_role = interaction.guild.get_role(913070056768946256)

        await interaction.user.add_roles(yellow_role)

    @nextcord.ui.button(label = '💚',style= nextcord.ButtonStyle.grey)
    async def green(self,button: nextcord.ui.Button,interaction: nextcord.Interaction):
        green_role = interaction.guild.get_role(913070202416148490)

        await interaction.user.add_roles(green_role)

    