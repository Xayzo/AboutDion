from telethon import events, TelegramClient
import logging
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import os


logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TOKEN", None)

bot = TelegramClient(
        "AboutDion",
        api_id=6,
        api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        ).start(
                bot_token=TOKEN
                )
db = {}

@bot.on(events.NewMessage(pattern="^[!?/]start$"))
async def stsrt(event):
    await event.reply(
            "**Heya, You can view Dion's profile by click the button below!**",
            buttons=[
                   [
                       InlineKeyboardButton(text="Click Here", callback_data="dion_"
                       ),
                   ],
               ]



def dion_about_callback(update, context):
    query = update.callback_query
    if query.data == "dion_":
        query.message.edit_text(
            text="๐ฐ Hi friends, I'm Dion"
            "\nClick on button bellow to see my profile",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Dion Profile", callback_data="dion_profile"),
                 ],
                 [
                    InlineKeyboardButton(text="Support", callback_data="dionsup_"),
                 ]
                ]
            ),
        )
    elif query.data == "dion_profile":
        query.message.edit_text(
            text=f"*เน This is my profile เน*"
            "\n\n๐๐ป Hi, introduce my real name is Gideon, known on telegram as Dion."
            "\nI'm from Indonesia, my age is a secret but I'm still a student."
            "\n\n๐ My favorite hobbies are playing games and coding(with @puffypawsy & @SkyiArul)."
            "\n\n๐ก I started to slide into the programming world about 2 years ago during the early days of the pandemic, Quarantine at home makes me bored and interested in learning new things besides graphic design."
            "\nThe programming languages I'm currently learning are Python and JavaScript"
            "\n\n๐ฃ๏ธ The languages โโI speak are: ๐ฎ๐ฉ Indonesia and ๐ด๓?ง๓?ข๓?ฅ๓?ฎ๓?ง๓?ฟ English.",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="My Social Media", callback_data="dion_sosmed"),
                 ],
                 [
                    InlineKeyboardButton(text="๐ Back", callback_data="dion_"),
                 ]
                ]
            ),
        )

    elif query.data == "dion_sosmed":
        query.message.edit_text(
            text=f"*เน My Social Media เน*"
            "\n\nnClick on button bellow to see my sosial media.",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Twitter", url="https://twitter.com/seorangdion"),
                    InlineKeyboardButton(text="Instagram", url="https://instagram.com/seorangdion"),
                 ],
                 [
                    InlineKeyboardButton(text="Github", url="https://github.com/SeorangDion"),
                    InlineKeyboardButton(text="Telegram", url="https://t.me/Royzu"),
                 ],
                 [
                    InlineKeyboardButton(text="๐ Back", callback_data="dion_profile"),
                 ]
                ]
            ),
        )

def dion_support_callback(update, context):
    query = update.callback_query
    if query.data == "dionsup_":
        query.message.edit_text(
            text="*เน My support channel & group*"
            "\nJoin My Support Channel/Group for see my Projects๐ฅ.",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Updates", url="t.me/DionProjects"),
                    InlineKeyboardButton(text="Support", url="https://t.me/DionSupport"),
                 ],
                 [
                    InlineKeyboardButton(text="๐ Go Back", callback_data="dion_"),
                 
                 ]
                ]
            ),
        )



    about_callback_handler = CallbackQueryHandler(
        dion_about_callback, pattern=r"dion_", run_async=True
    )

    source_callback_handler = CallbackQueryHandler(
        dion_support_callback, pattern=r"dionsup_", run_async=True
    )

    dispatcher.add_handler(about_callback_handler)
    dispatcher.add_handler(source_callback_handler)


print("Succesfully Started Bot!")
bot.run_until_disconnected()
