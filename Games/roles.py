from aiogram.utils.markdown import hide_link
from Database.base import Database
from aiogram.types import Message


class RolePlay(Database):
    def __init__(self):
        super().__init__()

    async def marry_user(self, user_id: int, partner_id: int):
        ...
