import nextcord
from nextcord.ext import commands

class rules_buttons(nextcord.ui.View):

    def __init__(self):
        super().__init__(timeout = None)

    @nextcord.ui.button(label = '✅', style = nextcord.ButtonStyle.green)
    async def Confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role = interaction.guild.get_role(910575316525801502)

        await interaction.user.add_roles(role)
