from typing import Union

from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter


class ChatTypeFilter(BoundFilter):
    def __init__(self, chat_type: Union[str, list]):
        self.chat_type = chat_type

    async def check(self, message: Message) -> bool:
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type
