import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from Sparky.clientbot.clientbot import client as rudra
from Sparky.config import SUDO_USERS

@Client.on_message(filters.command(["gcast", "broadcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**`🚶 Broadcasting...`**")
        if not message.reply_to_message:
            await wtf.edit("**🙄 Reply to a message to broadcast vro ...**")
            return
        lmao = message.reply_to_message.text
        async for dialog in rudra.iter_dialogs():
            try:
                await rudra.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**🚶 Broadcasting ...** \n\n**✔️ Sent :** `{sent}` **Chats** \n**❌ Failed:** `{failed}` **chats**")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await wtf.delete()
        await message.reply_text(f"**🚶 Gcast successful ...**\n\n**✔️ Sent in:** `{sent}` **chats**\n**❌ Failed in:** `{failed}` **chats**")
