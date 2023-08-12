from config import Icons, Words
from Database.base import Database

from aiogram import Bot
from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Marry(Database):
    def __init__(self):
        super().__init__()

    async def create_marry(self, message: Message):
        user_id = message.from_user.id
        if message.reply_to_message:
            partner_id = message.reply_to_message.from_user.id
        else:
            return await message.reply(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

        if partner_id == user_id:
            return await message.reply(Words.NOTSELF.format(FALSE=Icons.FALSE))

        get_self_info = self.find_one({"user_id": user_id})
        get_partner_info = self.find_one({"user_id": partner_id})

        if get_self_info['result'] is None:
            return await message.reply(Words.CREATE.format(FALSE=Icons.FALSE, user_id=user_id, SETTINGS=Icons.SETTINGS))

        if get_self_info['result']['married_to'] != "null":
            return await message.reply(Words.ALREADY_MARRIED.format(FALSE=Icons.FALSE, user_id=user_id))

        if not get_partner_info['is_done']:
            return await message.reply(Words.NOTFOUND.format(FALSE=Icons.FALSE, user_id=partner_id))

        partner_info = get_partner_info['result']

        if partner_info['married_to'] != "null":
            return await message.reply(Words.ALREADY_MARRIED.format(FALSE=Icons.FALSE, user_id=partner_id))

        keyboard = InlineKeyboardMarkup().add(
            InlineKeyboardButton(
                text=f"{Icons.BREAD} Отказаться", callback_data=f"marry_set_cancel_{user_id}_{partner_id}"
            ),
            InlineKeyboardButton(
                text=f"{Icons.HEART} Согласиться", callback_data=f"marry_set_allow_{user_id}_{partner_id}"
            )
        )

        await message.reply(Words.REQUEST_MARRY.format(WIFE=Icons.WIFE, partner_id=partner_id,
                                                       partner_nickname=partner_info['nickname']),
                            reply_markup=keyboard)

    async def delete_marry(self, message: Message):
        user_id = message.from_user.id
        get_self_info = self.find_one({"user_id": user_id})

        if get_self_info['result'] is None:
            return await message.reply(Words.CREATE.format(FALSE=Icons.FALSE, user_id=user_id, SETTINGS=Icons.SETTINGS))

        if get_self_info['result']['married_to'] == "null":
            return await message.reply(Words.NOTMARRIED.format(FALSE=Icons.FALSE, user_id=user_id))

        self.update_one({"user_id": user_id}, {"$set": {"married_to": "null"}})
        self.update_one({"user_id": get_self_info['result']['married_to']}, {
                        "$set": {"married_to": "null"}})
        return await message.reply(Words.DIVORCE.format(TRUE=Icons.TRUE, user_id=user_id))

    async def get_marry(self, message: Message):
        user_id = message.from_user.id
        get_self_info = self.find_one({"user_id": user_id})

        if get_self_info['result'] is None:
            return await message.reply(Words.CREATE.format(FALSE=Icons.FALSE, user_id=user_id, SETTINGS=Icons.SETTINGS))

        if get_self_info['result']['married_to'] == "null":
            return await message.reply(Words.NOTMARRIED.format(FALSE=Icons.FALSE, user_id=user_id))

        get_partner_info = self.find_one(
            {"user_id": get_self_info['result']['married_to']})

        await message.reply(Words.MARRIEDWITH.format(WIFE=Icons.WIFE, user_id=user_id,
                                                     partner_id=get_self_info['result']['married_to'],
                                                     partner_nickname=get_partner_info['result']['nickname']))

    async def cancel_marry(self, bot: Bot, message: Message, callback):
        pushed_id = callback.from_user.id
        partner_id = int(callback.data.split("_")[-1])
        requester_id = int(callback.data.split("_")[-2])

        if pushed_id not in [partner_id, requester_id]:
            return await callback.answer(Words.NOTPERMISSION.format(FALSE=Icons.FALSE))

        await bot.delete_message(message.chat.id, message.message_id)
        await message.answer(Words.CANCELREQUEST.format(FALSE=Icons.FALSE, user_id=partner_id))

    async def allow_marry(self, bot: Bot, message: Message, callback):
        pushed_id = callback.from_user.id
        partner_id = int(callback.data.split("_")[-1])
        requester_id = int(callback.data.split("_")[-2])

        if pushed_id not in [partner_id, requester_id]:
            return await callback.answer(Words.NOTPERMISSION.format(FALSE=Icons.FALSE))

        if pushed_id == partner_id:
            self.update_one({"user_id": requester_id}, {
                            "$set": {"married_to": partner_id}})
            self.update_one({"user_id": partner_id}, {
                            "$set": {"married_to": requester_id}})

            await bot.delete_message(message.chat.id, message.message_id)
            await message.answer(Words.ALLOWREQUEST.format(TRUE=Icons.TRUE, user_id=partner_id, WIFE=Icons.WIFE))
