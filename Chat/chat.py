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

    async def kick_user(self, bot: Bot, message: Message):
        name = message.reply_to_message.from_user.get_mention(as_html=True)
        if not message.reply_to_message:
            return
        user_id = message.reply_to_message.from_user.id
        if user_id == 1982062215:
            return await message.reply("<b>А ты случаем хуеца от него соснуть не хочешь?</b> 🤡")
        try:
            await bot.kick_chat_member(message.chat.id, user_id)
            await message.reply(Words.KICKED.format(TRUE=Icons.TRUE, user_id=user_id, name=name))
        except:
            await message.reply(Words.CANT_KICK.format(FALSE=Icons.FALSE, COMMENT=Icons.COMMENT))

    async def delete_message(self, bot: Bot, message: Message):
        is_reply: bool = False
        message_id: int = message.message_id
        message_split = message.text.split(' ')

        if message.reply_to_message:
            is_reply = True
            reply_message_id: int = message.reply_to_message.message_id

        if len(message_split) > 1:
            if message_split[1] == '-':
                try:
                    await bot.delete_message(message.chat.id, reply_message_id)
                    return await bot.delete_message(message.chat.id, message_id)
                except:
                    return await message.reply(f"{Icons.FALSE} Не удалось удалить сообщение.")

        if is_reply:
            try:
                await bot.delete_message(message.chat.id, reply_message_id)
                await bot.delete_message(message.chat.id, message_id)
                await message.answer(f"{Icons.TRUE} Сообщение удалено.")
            except:
                await message.reply(f"{Icons.FALSE} Не удалось удалить сообщение.")
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
            to_date = dt.strftime("%d-%m %H:%M:%S (%Y-года)")
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
            return await message.reply(f'{Icons.SETTINGS} <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{name}</a>\n{Icons.TIME} <b>Наказан(-а) до:</b> {to_date}\n{Icons.COMMENT} <b>Причина:</b> {comment}')

        if mute_type in ["m", "минут", "минута", "м"]:
            dt = datetime.now() + timedelta(minutes=mute_period)
            timestamp = dt.timestamp()
            to_date = dt.strftime("%d-%m %H:%M:%S (%Y-года)")
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
            return await message.reply(f'{Icons.SETTINGS} <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{name}</a>\n{Icons.TIME} <b>Наказан(-а) до:</b> {to_date}\n{Icons.COMMENT} <b>Причина:</b> {comment}')

        if mute_type in ["d", "день", "дня", "дней", "д"]:
            dt = datetime.now() + timedelta(days=mute_period)
            timestamp = dt.timestamp()
            to_date = dt.strftime("%d-%m %H:%M:%S (%Y-года)")
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
                await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(
                    can_send_messages=True,
                    can_send_audios=True,
                    can_send_documents=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_send_videos=True
                ))
                return await message.reply(f"{Icons.TRUE} <b>Участник <a href='tg://user?id={message.reply_to_message.from_user.id}'>{name}</a></b> успешно размучен.")

    async def get_staff(self, bot: Bot, message: Message):
        chat_id = message.chat.id

        staff = self.chat_find_one({"chat_id": chat_id})
        if staff['result'] is None:
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

        moderators = self.chat_find_one({"chat_id": chat_id})
        if moderator_id in moderators['result']['chat_moderators']:
            return await message.reply(Words.MODERATOR_ALREADY_EXISTS.format(FALSE=Icons.FALSE, user_id=moderator_id))

        if moderator_id in admins_ids:
            return await message.reply(Words.USER_ALREAY_ADMIN.format(FALSE=Icons.FALSE, user_id=moderator_id))

        update = self.chat_update_one({"chat_id": chat_id}, {
            "$push": {"chat_moderators": moderator_id}})

        if update['is_done']:
            await message.reply(Words.MODERATOR_ADDED.format(TRUE=Icons.TRUE, user_id=moderator_id))

    async def remove_moderator_role(self, bot, message):
        chat_id = message.chat.id
        moderator_id = message.reply_to_message.from_user.id

        moderators = self.chat_find_one({"chat_id": chat_id})
        if moderator_id not in moderators['result']['chat_moderators']:
            return await message.reply(Words.IS_NOT_MODERATOR.format(FALSE=Icons.FALSE, user_id=moderator_id))

        update = self.chat_update_one({"chat_id": chat_id}, {
            "$pull": {"chat_moderators": moderator_id}})

        if update['is_done']:
            await message.reply(Words.MODERATOR_REMOVED.format(TRUE=Icons.TRUE, user_id=moderator_id))

    async def get_reward(self, message: Message):
        chat_id = message.chat.id
        reward_text = message.text.split('\n')[1].strip() if len(
            message.text.split('\n')) > 1 else None
        if not message.reply_to_message:
            return await message.reply(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        user_id = message.reply_to_message.from_user.id
        if user_id == message.from_user.id:
            return await message.reply(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        rewards = self.db.reward.find_one(
            {"chat_id": chat_id, "user_id": user_id, "reward_text": reward_text})

        if rewards is None:
            if self.db.reward.insert_one({"chat_id": chat_id,
                                          "user_id": user_id,
                                          "reward_text": reward_text}):
                await message.reply(Words.REWARD_CREATED.format(YES=Icons.TRUE, user_id=user_id))
        else:
            await message.reply(Words.REWARD_EXISTS.format(FALSE=Icons.FALSE, user_id=user_id))

    async def remove_reward(self, message: Message):
        chat_id = message.chat.id
        reward_text = message.text.split('\n')[0].split(maxsplit=1)[1] if len(
            message.text.split('\n')[0].split(maxsplit=1)[1]
        ) > 1 else None

        if not message.reply_to_message:
            user_id = message.from_user.id
        else:
            user_id = message.reply_to_message.from_user.id

        rewards = self.db.reward.find_one(
            {"chat_id": chat_id, "user_id": user_id, "reward_text": reward_text})

        if rewards is None:
            if self.db.reward.insert_one({"chat_id": chat_id,
                                          "user_id": user_id,
                                          "reward_text": reward_text}):
                await message.reply(Words.REWARD_NOT_EXISTS.format(FALSE=Icons.FALSE, user_id=user_id))
        else:
            self.db.reward.find_one_and_delete(
                {"chat_id": chat_id, "user_id": user_id, "reward_text": reward_text})

            await message.reply(Words.REWARD_DELETED.format(YES=Icons.TRUE, user_id=user_id))

    async def get_rewards_user(self, message: Message):
        chat_id = message.chat.id
        if not message.reply_to_message:
            user_id = message.from_user.id
        else:
            user_id = message.reply_to_message.from_user.id

        _list = self.db.reward.find(
            {"chat_id": chat_id, "user_id": user_id})

        if _list is None:
            return await message.reply(Words.REWARDS_NOT_FOUND.format(FALSE=Icons.FALSE, user_id=user_id))

        _list = [rewards for rewards in self.db.reward.find(
            {"chat_id": chat_id, "user_id": user_id})]

        reward_list = f"{Icons.SETTINGS} Награды <b>пользователя:</b>\n"
        if not _list:
            reward_list += "Отсутствуют."

        for index, reward in enumerate(_list, 1):
            if reward['reward_text'] is None:
                reward_list += "Отсутствуют."
                break
            reward_list += f"{index}. {reward['reward_text']}\n"

        await message.reply(reward_list)
