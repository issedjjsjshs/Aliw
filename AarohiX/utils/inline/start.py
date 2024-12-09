from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["rcvcn"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["rcvcn"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["rcvcn "],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["rcvcn"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["rcvcn"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["rcvcn"], user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton("「 سرعة البوت 」", callback_data="bot_info_data"),
        ],
    ]
    return buttons
