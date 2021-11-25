import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.core import has_permissions
from buttons.kick_button import Kick_button
from lib import db

class kick(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    @has_permissions(kick_members = True)
    async def kick(self,ctx,user: nextcord.Member,*,reason = "No reason"):
        view = Kick_button()

        await ctx.send(f"Are you sure you want to kick {user}",view = view)

        await view.wait()

        if view.value is None:
            return
        elif view.value == True:
            await user.send(f"You have been kicked for {reason}")
            await user.kick(reason = reason)
            await ctx.send(f"{user} has been kicked")
            db.execute("DELETE FROM wallet WHERE UserID = ?",user.id)
            db.commit()
        else:
            await ctx.send(f"You didnt banned {user}")

def setup(client):
    client.add_cog(kick(client))