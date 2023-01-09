import discordBot, os
from getpass import getpass
from colorama import Fore, Style

print(f"""{Style.DIM}{Fore.MAGENTA}
███╗░░██╗░█████╗░██████╗░░█████╗░██████╗░██╗░░░██╗{Style.DIM}{Fore.LIGHTMAGENTA_EX}
████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝{Style.RESET_ALL}{Fore.MAGENTA}
██╔██╗██║██║░░██║██████╦╝██║░░██║██║░░██║░╚████╔╝░
██║╚████║██║░░██║██╔══██╗██║░░██║██║░░██║░░╚██╔╝░░{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}
██║░╚███║╚█████╔╝██████╦╝╚█████╔╝██████╔╝░░░██║░░░
╚═╝░░╚══╝░╚════╝░╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░{Style.BRIGHT}{Fore.LIGHTWHITE_EX}""")
print("===================================================================")

token = input(f"{Style.RESET_ALL}{Fore.YELLOW}[?] Bot token (User token not supported): ")
prefix = input(f"{Style.RESET_ALL}{Fore.YELLOW}[?] Prefix: ")

print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}===================================================================")
discordBot.nukbot(prefix, token)
