from discord.ext import commands
from colorama import Fore


class nukeDestroyRole(commands.Cog):
	def __init__(self,client):
		self.client=client
		self.delOn=0
	
	@commands.Cog.listener()
	async def on_guild_role_delete(self,role):
		if self.delOn:None
		else:
			self.delOn=1
			for a in role.guild.members:
				try:
					await a.edit(nick="𝐍𝐔𝐊𝐄𝐃 𝐁𝐘 𝐍𝐎𝐁𝐎𝐃𝐘")
					print(f"{Fore.LIGHTGREEN_EX}[+] Member nicked")
				except:
					print(f"{Fore.RED}[-] Member cannot be nicked")

async def setup(client):
	await client.add_cog(nukeDestroyRole(client))