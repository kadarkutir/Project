import nextcord
from nextcord.ext import commands

class rps_buttons(nextcord.ui.View):

    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label = '🪨', style = nextcord.ButtonStyle.blurple)
    async def rock(self,button : nextcord.ui.Button, interaction : nextcord.Interaction):
        self.value = 1
        self.stop()

    @nextcord.ui.button(label = '🧻', style = nextcord.ButtonStyle.blurple)
    async def paper(self,button : nextcord.ui.Button, interaction : nextcord.Interaction):
        self.value = 2
        self.stop()

    @nextcord.ui.button(label = '✂️', style = nextcord.ButtonStyle.blurple)
    async def scissors(self,button : nextcord.ui.Button, interaction : nextcord.Interaction):
        self.value = 3
        self.stop()
    