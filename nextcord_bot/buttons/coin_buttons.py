import nextcord
from nextcord.ext import commands

class coin_buttons(nextcord.ui.View):

    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label = 'Head', style = nextcord.ButtonStyle.grey)
    async def head(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = 0
        self.stop()

    @nextcord.ui.button(label = 'Tail', style = nextcord.ButtonStyle.grey)
    async def tail(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = 1
        self.stop()


    

        