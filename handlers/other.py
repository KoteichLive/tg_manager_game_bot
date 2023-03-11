from aiogram import types, Dispatcher
from bor_ import dp, bot
from aiogram.types import ContentType, Message



async def send_message_to_channel(text):
    # создаем объект сообщения
    message = types.Message(text=text)
    # отправляем сообщение в канал с указанием его ID
    await bot.send_message(chat_id='@название_канала', text=message.text)

#@dp.message_handler(content_types=[ContentType.NEW_CHAT_MEMBERS])# приветствие
async def new_members_handler(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name

    new_member = message.new_chat_members[0]
    await bot.send_message(message.chat.id, f"""Привет, {user_first_name} {user_last_name}
Добро пожаловать в чат...
если ты тут с вк, с вопросом какова хрена и почему?
то знай.. кот просто решил переехать с вк оно его сильно бесит...

И та.. тубя ждут пару плюшек..

и если у вас есть правки по орфографии то предлагайте..
естественно за вознаграждение""")

#@dp.message_handler()# счёчик
async def plus_balda(message: Message):
    pass
#{"message_id": 392, "from": {"id": 5502308935, "is_bot": false, "first_name": "koteich live", "username": "Koteich_l", "language_code": "ru"}, "chat": {"id": -1001636025024, "title": "Koteich piterLive", "type": "supergroup"}, "date": 1678563447, "text": "/"}


def register_other(dp : Dispatcher):
    dp.register_message_handler(new_members_handler, content_types=[ContentType.NEW_CHAT_MEMBERS])
    dp.register_message_handler(plus_balda)
