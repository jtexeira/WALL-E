import discord
from discord.ext import commands

class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='castigo',
                    brief='Punish someone for their sins. [ADMIN ONLY]',
                    help='This command gives the role "castigo" to the specified user(s).',
                    usage='user1[, user2[, ...]] [reason]')
    @commands.check_any(commands.is_owner(), commands.has_permissions(administrator=True))
    async def castigo(self, ctx : commands.Context):
        castigo = [x for x in ctx.guild.roles if x.name.lower() == "castigo"][0]
        for member in ctx.message.mentions:
            await member.add_roles(castigo, reason=(' '.join([x for x in ctx.message.content.split()[2:] if '<@!' not in x])))

    @commands.command(name='perdoar',
                    brief='Forgive someone for their sins. [ADMIN ONLY]',
                    help='This command removes the role "castigo" from the specified user(s).',
                    usage='user1[, user2[, ...]] [reason]')
    @commands.check_any(commands.is_owner(), commands.has_permissions(administrator=True))
    async def perdoar(self, ctx : commands.Context):
        castigo = [x for x in ctx.guild.roles if x.name.lower() == "castigo"][0]
        for member in ctx.message.mentions:
            await member.remove_roles(castigo, reason=(' '.join([x for x in ctx.message.content.split()[2:] if '<@!' not in x])))

def setup(bot):
    bot.add_cog(Manage(bot))
