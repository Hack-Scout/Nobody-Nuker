import discord, os, asyncio
from discord.ext import commands
from colorama import Fore


def nukbot(prefix,token):
	class Nukr(commands.Bot):
		def __init__(self,pre):
			intents = discord.Intents.all()
			intents.message_content = True
			super().__init__(command_prefix=pre, 
				intents=intents, help_command=None)
	
	
	client = Nukr(prefix)
	
	async def load():		
		for folder in os.listdir("./cogs"):
			if folder.endswith(".py"):
				await client.load_extension(f"cogs.commands.{folder[:-3]}")
				print(f"{Fore.LIGHTGREEN_EX}[+] Loaded {folder[:-3]}")
			else:
				for file in os.listdir(f"./cogs/{folder}"):
					if file.endswith(".py"):
						await client.load_extension(f"cogs.{folder}.{file[:-3]}")
						print(f"{Fore.LIGHTGREEN_EX}[+] Loaded {folder} > {file}")
				
				
	
	
	print(f"{Fore.LIGHTMAGENTA_EX}[=] Loading Commands")
	asyncio.run(load())
	print(f"{Fore.LIGHTMAGENTA_EX}[=] Cogs Added")
	
	client.run(token)
