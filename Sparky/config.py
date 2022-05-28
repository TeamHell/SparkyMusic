# Changing some lines of code won't make you a programmer.
# use with credits else gay.
# you will die.
# your mom will be fucked.
# © by @AKH1LS.


# Modules and Environments
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# Internal Variable (
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# Required Values 
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/a4c16c60dd1c46bbe7385.jpg")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1323020756").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Yaaro_Ki_Yaarii")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/HeroOfficialBots")

# Don't change if you don't know what you are doing...
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/AboutShailendra")
