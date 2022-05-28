from Sparky.config import (
    START_PIC, 
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from Sparky.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**Hello, I am **Sparky Music Player**, a lag free with smooth functioning
music player with awesome features, provide your query, only a minisecond after your command, based on private server.
If you wanted a unique and better music bot, give my try...**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Add me to your group",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("Creator", url=f"https://t.me/Tera_Baap_Sparky"),
                    InlineKeyboardButton("Contributer", url=f"https://t.me/AKH1LS"),
                ],
                [
                    InlineKeyboardButton(
                        "SUPPORT", url=f"{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "CHANNEL", url=f"{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
    )


