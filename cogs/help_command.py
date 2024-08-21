from typing import Any
import discord
from discord.ext import commands
from discord import Embed

class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping): 
        embed = Embed(
            title="Samson's Commands",
            description="Here are all the available commands:",
            color=0x7cb58b
        )

        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = cog.qualified_name if cog else "No Category"
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = Embed(
            title=self.get_command_signature(command),
            description=command.help or "No description provided.",
            color=0x7cb58b
        )
        channel = self.get_destination()
        await channel.send(embed=embed)

    def get_command_signature(self, command):
        return f'!{command.qualified_name} {command.signature}'
        

async def setup(bot):
    bot.help_command = CustomHelpCommand()