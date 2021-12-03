import nextcord
from nextcord.ext import commands

class dice_buttons(nextcord.ui.View):

    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label = '1',style = nextcord.ButtonStyle.grey)
    async def one(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = 1
        self.stop()

    @nextcord.ui.button(label = '2',style = nextcord.ButtonStyle.grey)
    async def two(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = 2
        self.stop()

    @nextcord.ui.button(label = '3',style = nextcord.ButtonStyle.grey)
    async def three(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = 3
        self.stop()

    @nextcord.ui.button(label = '4',style = nextcord.ButtonStyle.grey)
    async def four(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = 4
        self.stop()

    @nextcord.ui.button(label = '5',style = nextcord.ButtonStyle.grey)
    async def five(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = 5
        self.stop()

    @nextcord.ui.button(label = '6',style = nextcord.ButtonStyle.grey)
    async def six(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = 6
        self.stop()