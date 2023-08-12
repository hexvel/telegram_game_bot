from aiogram import Bot
from aiogram import types
from config import Icons, Words
from Database.chat import ChatDB
from aiogram.types import Message
from datetime import datetime, timedelta


class Chat(ChatDB):
    def __init__(self) -> None:
        super().__init__()

    async def create_chat_in_db(self, message):
        chat_id = message.chat.id
        chat_name = message.chat.title

        if self.chat_find_one({"chat_id": chat_id})['result'] is not None:
            return await message.reply(Words.CHAT_EXISTS.format(FALSE=Icons.FALSE))

        create_chat = self.chat_insert_one(chat_id=chat_id, chat_moderators=[])
        if create_chat['is_done']:
            await message.reply(Words.CHAT_CREATED.format(TRUE=Icons.TRUE, name=chat_name, SETTINGS=Icons.SETTINGS))

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
        name = message.reply_to_message.from_user.get_mention(as_html=True)

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
            return await message.reply(f'{Icons.SETTINGS} <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{name}</a>\n{Icons.TIME} <b>Наказан(-а) до:</b> {to_date}\n{Icons.COMMENT} <b>Причина:</b> {comment}')

        if mute_type in ["m", "минут", "минута", "м"]:
            dt = datetime.now() + timedelta(minutes=mute_period)
            timestamp = dt.timestamp()
            to_date = dt.strftime("%H:%M:%S")
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
            return await message.reply(f'{Icons.SETTINGS} <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{name}</a>\n{Icons.TIME} <b>Наказан(-а) до:</b> {to_date}\n{Icons.COMMENT} <b>Причина:</b> {comment}')

        if mute_type in ["d", "день", "дня", "д"]:
            dt = datetime.now() + timedelta(days=mute_period)
            timestamp = dt.timestamp()
            to_date = dt.strftime("%H:%M:%S")
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
            return await message.reply(f'{Icons.SETTINGS} <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{name}</a>\n{Icons.TIME} <b>Наказан(-а) до:</b> {to_date}\n{Icons.COMMENT} <b>Причина:</b> {comment}')
        else:
            return await message.reply(f"{Icons.FALSE} Укажите тип периода (m - минут, h - час, d - день).")

    async def unmute_user(self, bot: Bot, message: Message):
        name = message.reply_to_message.from_user.get_mention(as_html=True)
        is_reply = False

        if message.reply_to_message:
            is_reply = True

            if not is_reply:
                return await message.reply(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

            user_id = message.reply_to_message.from_user.id
            if user_id != message.from_user.id:
                await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True))
                return await message.reply(f"{Icons.TRUE} <b>Участник <a href='tg://user?id={message.reply_to_message.from_user.id}'>{name}</a></b> успешно размучен.")

    async def get_staff(self, bot: Bot, message: Message):
        chat_id = message.chat.id

        staff = self.chat_find_one({"chat_id": message.chat.id})
        if staff is None:
            return await message.reply(Words.CHAT_NOT_EXISTS.format(FALSE=Icons.FALSE, SETTINGS=Icons.SETTINGS))

        chat_admins = await bot.get_chat_administrators(chat_id)
        admin_ids = [admin.user.id for admin in chat_admins]

        staff_text = f"{Icons.KING} <b>Администраторы данного чата:</b>\n"

        for admin in admin_ids:
            admin_data = await bot.get_chat_member(chat_id, admin)
            if admin_data.status == "creator":
                staff_text += f"{Icons.HUMAN_KING} <b><a href='tg://user?id={admin}'>{admin_data.user.first_name}</a></b> (Создатель)\n"
            elif admin_data.user.is_bot:
                staff_text += f"{Icons.BOT} <b><a href='tg://user?id={admin}'>{admin_data.user.first_name}</a></b> (бот)\n"
            else:
                staff_text += f"{Icons.USER} <b><a href='tg://user?id={admin}'>{admin_data.user.first_name}</a></b>\n"

        moderators = f"\n\n{Icons.BREAD} <b>Модераторы данного чата:</b>\n"

        if not staff['result']['chat_moderators']:
            moderators += f"{Icons.FALSE} Модераторы не найдены."
        else:
            for moderator in staff['result']['chat_moderators']:
                moderator_data = await bot.get_chat_member(chat_id, moderator)
                moderators += f"{Icons.BABY} <b><a href='tg://user?id={moderator}'>{moderator_data.user.first_name}</a></b>\n"

        staff_text += moderators
        return await message.reply(staff_text)

    async def set_moderator_role(self, bot, message):
        chat_id = message.chat.id
        admins_ids = [admin.user.id for admin in await bot.get_chat_administrators(chat_id)]
        moderator_id = message.reply_to_message.from_user.id

        moderators = self.chat_find_one({"chat_id": message.chat.id})
        if moderator_id in moderators['result']['chat_moderators']:
            return await message.reply(Words.MODERATOR_ALREADY_EXISTS.format(FALSE=Icons.FALSE, user_id=moderator_id))

        if moderator_id in admins_ids:
            return await message.reply(Words.USER_ALREAY_ADMIN.format(FALSE=Icons.FALSE, user_id=moderator_id))

        update = self.chat_update_one({"chat_id": message.chat.id}, {
            "$push": {"chat_moderators": moderator_id}})

        if update['is_done']:
            await message.reply(Words.MODERATOR_ADDED.format(TRUE=Icons.TRUE, user_id=moderator_id))
