#=====by kyoja=====
import os
import discord
from discord.ext import commands
import asyncio
import time
from colorama import Fore, Style, init

init(autoreset=True)
os.system("clear")
TOKEN = input(Fore.RED + "Enter your Bot Token 🔑 :  " + Style.RESET_ALL)
os.system("clear")
GUILD_ID = int(input(Fore.RED + "Enter your Server ID 🆔 : " + Style.RESET_ALL))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
os.system("clear")
def show_banner():
    
    print(Fore.RED + Style.BRIGHT + """




██╗  ██╗██╗██╗     ██╗     ███████╗██████╗  ██████╗     ██╗ ██╗   ██╗██╗░█████╗   ███╗
██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗██╔════╝  ██████████╗░██╔╝██║██╔══██╗ ████║
█████═╝ ██║██║     ██║     █████╗  ██████╔╝╚█████╗   ╚═██╔═██╔═╝██╔╝ ██║╚█████╔╝██╔██║
██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗ ╚═══██╗  ██████████╗███████║██╔══██╗╚═╝██║
██║ ╚██╗██║███████╗███████╗███████╗██║  ██║██████╔╝  ╚██╔═██╔══╝╚════██║╚█████╔╝███████╗
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝ ╚═╝        ╚═╝ ╚════╝ ╚══════╝

""" + Style.RESET_ALL)
    print(Fore.RED + "Da404rk" + Style.RESET_ALL)
    print(Fore.RED + "https://discord.gg/jsmcJYyUXya" + Style.RESET_ALL)
    print()

def show_menu():
    print(Fore.WHITE + "─" * 50)
    print(Fore.LIGHTRED_EX + " " + Fore.LIGHTWHITE_EX + "fuck skids | made by kyoja" + Fore.LIGHTRED_EX + " ")
    print(Fore.WHITE + "─" * 50)
    print(Fore.RED + "[1]" + Fore.LIGHTWHITE_EX + " Delete All Channels")
    print(Fore.RED + "[2]" + Fore.LIGHTWHITE_EX + " Create Channels")
    print(Fore.RED + "[3]" + Fore.LIGHTWHITE_EX + " Nuker#Da404rk (Full Nuke)")
    print(Fore.RED + "[4]" + Fore.LIGHTWHITE_EX + " Rename All Channels")
    print(Fore.RED + "[5]" + Fore.LIGHTWHITE_EX + " Create Roles")
    print(Fore.RED + "[6]" + Fore.LIGHTWHITE_EX + " Delete All Roles")
    print(Fore.RED + "[7]" + Fore.LIGHTWHITE_EX + " Admin to everyone")
    print(Fore.RED + "[8]" + Fore.LIGHTWHITE_EX + " Delete All Emojis")
    print(Fore.RED + "[9]" + Fore.LIGHTWHITE_EX + " Ban All Members")
    print(Fore.RED + "[10]" + Fore.LIGHTWHITE_EX + "Kick All Members")
    print(Fore.RED + "[11]" + Fore.LIGHTWHITE_EX + "Change Server Name")
    print(Fore.RED + "[12]" + Fore.LIGHTWHITE_EX + "Spam Message (All Channels)")
    print(Fore.RED + "[a]" + Fore.LIGHTWHITE_EX + " About Us")
    print(Fore.RED + "[x]" + Fore.LIGHTWHITE_EX + " Exit")
    print(Fore.WHITE + "─" * 50)

async def progress_bar(current, total, start_time, action="Processing"):
    elapsed = int(time.time() - start_time)
    mins, secs = divmod(elapsed, 60)
    time_str = f"{mins:02d}:{secs:02d}"
    progress = (current / total) * 100 if total > 0 else 100
    print(f"\r{Fore.LIGHTBLUE_EX}{time_str} {Fore.RED}──▶ "
          f"{Fore.LIGHTGREEN_EX}{progress:.2f}% | {action} {current}/{total}",
          end="", flush=True)

async def delete_channels(guild):
    start_time = time.time()
