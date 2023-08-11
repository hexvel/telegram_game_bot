from config import Icons, Words
from aiogram.types import Message
from Database.base import Database


class Marry(Database):
    def __init__(self):
        super().__init__()

    async def create_marry(self, message: Message):
        user_id = message.from_user.id
        if message.reply_to_message:
            partner_id = message.reply_to_message.from_user.id
        else:
            return await message.reply(Words.REPLYNOTFOUND.format(FALSE=Icons.FALSE))

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

        self.update_one({"user_id": user_id}, {
                        "$set": {"married_to": partner_id}})
        self.update_one({"user_id": partner_id}, {
                        "$set": {"married_to": user_id}})

        return await message.reply(Words.MARRIED.format(TRUE=Icons.TRUE, user_id=user_id, partner_id=partner_id,
                                                        partner_nickname=message.from_user.get_mention(as_html=True)))

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
