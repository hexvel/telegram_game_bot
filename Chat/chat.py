from aiogram import Bot
from config import Icons
from aiogram import types
from aiogram.types import Message
from datetime import datetime, timedelta


class Chat:
    def __init__(self) -> None:
        super().__init__()

    async def delete_message(self, bot: Bot, message: Message):
        is_reply: bool = False
        message_id: int = message.message_id
        message_split = message.text.split(' ')

        if message.reply_to_message:
            is_reply = True
            reply_message_id: int = message.reply_to_message.message_id

        if len(message_split) > 1:
            if message_split[1].lower() == '-':
                await bot.delete_message(message.chat.id, reply_message_id)
                await bot.delete_message(message.chat.id, message_id)
                return

        if is_reply:
            await bot.delete_message(message.chat.id, reply_message_id)
            await bot.delete_message(message.chat.id, message_id)
            await message.answer(f"{Icons.TRUE} Сообщение удалено.")
        else:
            await message.answer(f"{Icons.FALSE} Ответьте на сообщение, которое нужно удалить.")

    async def mute_user(self, bot: Bot, message: Message):
        name = message.from_user.get_mention(as_html=True)

        if not message.reply_to_message:
            return await message.reply(f"{Icons.FALSE} Ответьте на сообщение пользователя, которого вы хотите замутить!")

        message_split = message.text.split('\n')[0].split(' ')
        if len(message_split) < 3:
            return await message.reply(f"{Icons.FALSE} Укажите срок оказания наказания.")

        mute_period = message_split[1]
        if not mute_period.isdigit():
            return await message.reply(f"{Icons.FALSE} Укажите срококазания в цифрах.")
        mute_period = int(mute_period)

        mute_type = message_split[2]
        comment = message.text.split('\n')
        comment = comment[1] if len(comment) > 1 else 'Не указан'

        if mute_type in ["h", "час", "часа", "ч"]:
            dt = datetime.now() + timedelta(hours=mute_period)
            timestamp = dt.timestamp()
            to_date = dt.strftime("%H:%M:%S")
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
            return await message.reply(f'{Icons.SETTINGS} <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{name}</a>\n{Icons.TIME} <b>Срок наказания:</b> {to_date}\n{Icons.COMMENT} <b>Причина:</b> {comment}')

        if mute_type in ["m", "минут", "минута", "м"]:
            dt = datetime.now() + timedelta(minutes=mute_period)
            timestamp = dt.timestamp()
            to_date = dt.strftime("%H:%M:%S")
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
            return await message.reply(f'{Icons.SETTINGS} <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{name}</a>\n{Icons.TIME} <b>Срок наказания:</b> {to_date}\n{Icons.COMMENT} <b>Причина:</b> {comment}')

        if mute_type in ["d", "день", "дня", "д"]:
            dt = datetime.now() + timedelta(days=mute_period)
            timestamp = dt.timestamp()
            to_date = dt.strftime("%H:%M:%S")
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
            return await message.reply(f'{Icons.SETTINGS} <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{name}</a>\n{Icons.TIME} <b>Срок наказания:</b> {to_date}\n{Icons.COMMENT} <b>Причина:</b> {comment}')
        else:
            return await message.reply(f"{Icons.FALSE} Укажите тип периода (m - минут, h - час, d - день).")
