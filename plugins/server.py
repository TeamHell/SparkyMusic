import os
import sys
from pyrogram.types import Message
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from os import system, execle, environ
from Sparky.helpers.decorators import sudo_users_only
from Sparky.config import BOT_USERNAME


@Client.on_message(commandpro(["R", "/restart", "/restart@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def restart_bot(_, message: Message):
    msg = await message.reply("`Restarting...`")
    args = [sys.executable, "main.py"]
    await msg.edit("ā Bot restarted\nā Now gib party Karo š")
    execle(sys.executable, *args, environ)
    return

