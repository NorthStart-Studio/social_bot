from dotenv import load_dotenv, find_dotenv
from telebot import TeleBot, types
from typing import Final
from database import Database
from os import getenv


load_dotenv(find_dotenv())
TOKEN: Final = getenv("TOKEN")
YOUTUBE, TIKTOK, TG, DISCORD = getenv("YOUTUBE_LINK"), getenv("TIKTOK_LINK"), getenv("TG_LINK"), getenv("DISCORD_LINK")
bot = TeleBot(TOKEN, parse_mode="markdown")
db = Database()


GLOBAL_MENU = types.ReplyKeyboardMarkup(resize_keyboard=True)
GLOBAL_MENU.keyboard = [['📈 Курсы', '🌐 СоцСети'], ['📃 О боте']]

SOCIAL_MENU = types.InlineKeyboardMarkup()
SOCIAL_MENU.add(types.InlineKeyboardButton(text="YouTube", url=YOUTUBE), types.InlineKeyboardButton(text="TikTok", url=TIKTOK))
SOCIAL_MENU.add(types.InlineKeyboardButton(text="Telegram", url=TG), types.InlineKeyboardButton(text="Discord", url=DISCORD))

VERSIONS = types.ReplyKeyboardMarkup(resize_keyboard=True)
VERSIONS.keyboard = [['🪙 Подписка', '✏️ Курс'], ['◀️ Вернуться']]

LANGUAGES_MENU = types.ReplyKeyboardMarkup(resize_keyboard=True)
LANGUAGES_MENU.keyboard = [["💻 C#", "💻 Javascript", "💻 Python"], ["◀️ Вернуться"]]


PRICE = getenv("FULL_PRICE")
PAYLOAD_TOKEN = getenv("PAYLOAD_TOKEN")

NEED_SUBSCRIPTION = types.InlineKeyboardButton(text="❌ Нужна подписка", callback_data="need_subscription")

CSHARP_RESOURCES = types.InlineKeyboardMarkup()
JAVASCRIPT_RESOURCES = types.InlineKeyboardMarkup()
PYTHON_RESOURCES = types.InlineKeyboardMarkup()
CSHARP_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url="https://example.com"), types.InlineKeyboardButton(text=".NET", url="https://example.com"))
JAVASCRIPT_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url="https://example.com"), types.InlineKeyboardButton(text="TypeScript", url="https://example.com"), types.InlineKeyboardButton(text="React", url="https://example.com"))
PYTHON_RESOURCES.add(types.InlineKeyboardButton(text="Основы языка", url="https://example.com"), types.InlineKeyboardButton(text="FastAPI", url="https://example.com"), types.InlineKeyboardButton(text="Django", url="https://example.com"))


ABOUT_BOT = """*Learning Program* - проект по обучению пользователей, в котором вы узнаете основы языков:
*С#*, *Python* и *JavaScript*, а также самые популярные библиотеки. В будущем наш проект будет пополняться новыми знаниями.
Если вы нашли недочет или есть предложение, напишите нам в соцсетях. Будем рады любому фидбеку :)
©️ *NorthStartStudio*"""