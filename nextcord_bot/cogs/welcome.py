import nextcord
from nextcord.ext import commands
from lib import db
from embeds.other_embeds import other_embeds

check ='✅'

class welcome(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self,member):
        
        welcome_embed = other_embeds.welcome_embed(member)
        
        await self.client.get_channel(905200327597379605).send(embed = welcome_embed)


        db.execute("INSERT INTO wallet (UserID,Tokens) VALUES(?,?)",member.id, 21)
        db.commit()



    @commands.Cog.listener()
    async def on_member_leave(self,member):

        db.execute("DELETE FROM wallet WHERE UserID = ?",member.id)
        db.commit()
        


def setup(client):
    client.add_cog(welcome(client))