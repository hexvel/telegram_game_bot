import random

from aiogram.types import Message
from Database.base import Database
from aiogram.utils.markdown import hide_link
from config import Icons, Words, RolePlay_Words, RolePlay_Links


class RolePlay(Database):
    def __init__(self):
        super().__init__()

    def get_user_info(self, message):
        user_id = message.from_user.id
        user_name = message.from_user.full_name
        actioned_user_id = message.reply_to_message.from_user.id
        actioned_user_name = message.reply_to_message.from_user.full_name
        return user_id, user_name, actioned_user_id, actioned_user_name

    async def fuck_user(self, message: Message):
        if message.reply_to_message is None:
            return await message.answer(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        user_id, user_name, fucked_user_id, fucked_user_name = self.get_user_info(
            message)

        fuck_user = RolePlay_Words.FUCK_USER.format(
            FUCK=Icons.HARD, user_id=user_id, user_name=user_name, fucked_user_id=fucked_user_id, fucked_user_name=fucked_user_name)

        comment = message.text.split('\n')[1].strip() if len(
            message.text.split('\n')) > 1 else None

        if comment is None:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.FUCK))}"
                f"{fuck_user}")
        else:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.FUCK))}"
                f"{fuck_user}\n{Icons.COMMENT} <b>С репликой</b>: {comment}"
            )

    async def kiss_user(self, message: Message):
        if message.reply_to_message is None:
            return await message.answer(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        user_id, user_name, kissed_user_id, kissed_user_name = self.get_user_info(
            message)

        kiss_user = RolePlay_Words.KISS_USER.format(
            KISS=Icons.KISS, user_id=user_id, user_name=user_name, kissed_user_id=kissed_user_id, kissed_user_name=kissed_user_name)

        comment = message.text.split('\n')[1].strip() if len(
            message.text.split('\n')) > 1 else None

        if comment is None:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.KISS))}"
                f"{kiss_user}")
        else:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.KISS))}"
                f"{kiss_user}\n{Icons.COMMENT} <b>С репликой</b>: {comment}")

    async def suck_user(self, message: Message):
        if message.reply_to_message is None:
            return await message.answer(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        user_id, user_name, sucked_user_id, sucked_user_name = self.get_user_info(
            message)

        suck_user = RolePlay_Words.SUCK_USER.format(
            SUCK=Icons.YUM, user_id=user_id, user_name=user_name, sucked_user_id=sucked_user_id, sucked_user_name=sucked_user_name)

        comment = message.text.split('\n')[1].strip() if len(
            message.text.split('\n')) > 1 else None

        if comment is None:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.SUCK))}"
                f"{suck_user}")
        else:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.SUCK))}"
                f"{suck_user}\n{Icons.COMMENT} <b>С репликой</b>: {comment}")

    async def hug_user(self, message: Message):
        if message.reply_to_message is None:
            return await message.answer(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        user_id, user_name, huged_user_id, huged_user_name = self.get_user_info(
            message)

        hug_user = RolePlay_Words.HUG_USER.format(
            HUG=Icons.HUG, user_id=user_id, user_name=user_name, huged_user_id=huged_user_id, huged_user_name=huged_user_name)

        comment = message.text.split('\n')[1].strip() if len(
            message.text.split('\n')) > 1 else None

        if comment is None:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.HUG))}"
                f"{hug_user}")
        else:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.HUG))}"
                f"{hug_user}\n<b>{Icons.COMMENT} С репликой</b>: {comment}")

    async def kick_user(self, message: Message):
        if message.reply_to_message is None:
            return await message.answer(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        user_id, user_name, kicked_user_id, kicked_user_name = self.get_user_info(
            message)

        kick_user = RolePlay_Words.KICK_USER.format(
            KICK=Icons.KICKRP, user_id=user_id, user_name=user_name, kicked_user_id=kicked_user_id, kicked_user_name=kicked_user_name)

        comment = message.text.split('\n')[1].strip() if len(
            message.text.split('\n')) > 1 else None

        if comment is None:
            return await message.answer(f"{kick_user}")
        else:
            return await message.answer(f"{kick_user}\n<b>{Icons.COMMENT} С репликой</b>: {comment}")

    async def uebat_user(self, message: Message):
        if message.reply_to_message is None:
            return await message.answer(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        user_id, user_name, uebated_user_id, uebated_user_name = self.get_user_info(
            message)

        uebat_user = RolePlay_Words.UEBAT_USER.format(
            UEBAT=Icons.HARD, user_id=user_id, user_name=user_name, uebated_user_id=uebated_user_id, uebated_user_name=uebated_user_name)

        comment = message.text.split('\n')[1].strip() if len(
            message.text.split('\n')) > 1 else None

        if comment is None:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.UEBAT))}"
                f"{uebat_user}")
        else:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.UEBAT))}"
                f"{uebat_user}\n<b>{Icons.COMMENT} С репликой</b>: {comment}")

    async def otliz_user(self, message: Message):
        if message.reply_to_message is None:
            return await message.answer(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        user_id, user_name, otlized_user_id, otlized_user_name = self.get_user_info(
            message)

        uebat_user = RolePlay_Words.OTLIZ_USER.format(
            OTLIZ=Icons.OTLIZ, user_id=user_id, user_name=user_name, otlized_user_id=otlized_user_id, otlized_user_name=otlized_user_name)

        comment = message.text.split('\n')[1].strip() if len(
            message.text.split('\n')) > 1 else None

        if comment is None:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.OTLIZ))}"
                f"{uebat_user}")
        else:
            return await message.answer(
                f"{hide_link(random.choice(RolePlay_Links.OTLIZ))}"
                f"{uebat_user}\n<b>{Icons.COMMENT} С репликой</b>: {comment}")
