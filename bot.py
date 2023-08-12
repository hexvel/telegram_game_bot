import config

from main import Main
from aiogram import Bot, types
from aiogram.types import Message
from aiogram.utils import executor
from User.user import UserProfile
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin=None):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.is_chat_admin()


bot = Bot(config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())
dp.filters_factory.bind(AdminFilter)


@dp.message_handler(commands=['start'])
async def start_bot(m: Message):
    await m.answer("Приветствую в новой версии бота!")


# Команды для профиля
@dp.message_handler(commands=['profile', 'me'])
async def profile(m: Message):
    await user.get_user_info(m)


@dp.message_handler(commands=['описание', 'description'])
async def profile(m: Message):
    description = m.text.split(maxsplit=1)
    if len(description) < 2:
        return await m.answer(f"{config.Icons.FALSE} Введите описание")

    await user.edit_user_settings(m, {
        "user_id": m.from_user.id},
        {"$set": {"description": description[1]}
         }
    )


@dp.message_handler(commands=['ник', 'nick'])
async def profile(m: Message):
    nickname = m.text.split(maxsplit=1)
    if len(nickname) < 2:
        return await m.answer(f"{config.Icons.FALSE} Введите ник")

    await user.edit_user_settings(m, {
        "user_id": m.from_user.id},
        {"$set": {"nickname": nickname[1]}
         }
    )


# Для чатов
@dp.message_handler(chat_type=types.ChatType.SUPERGROUP, commands=['del', 'уд'], commands_prefix=".!/", is_admin=True)
async def delete_message(m: Message):
    await chat.delete_message(bot, m)


@dp.message_handler(chat_type=types.ChatType.SUPERGROUP, commands=['mute', 'мут'], commands_prefix=".!/", is_admin=True)
async def mute_user(m: Message):
    await chat.mute_user(bot, m)


# Развлекательные команды
@dp.message_handler(chat_type=types.ChatType.SUPERGROUP, commands=['marry', 'брак'], commands_prefix=".!/")
async def marry_user(m: Message):
    await marry.create_marry(m)


@dp.message_handler(chat_type=types.ChatType.SUPERGROUP, commands=['divorce', 'развод'], commands_prefix=".!/")
async def marry_user(m: Message):
    await marry.delete_marry(m)


@dp.message_handler(chat_type=types.ChatType.SUPERGROUP, commands=['mymarry', 'мойбрак'], commands_prefix=".!/")
async def marry_user(m: Message):
    await marry.get_marry(m)


# Для лички
@dp.message_handler(chat_type=types.ChatType.PRIVATE, commands=['create'])
async def craete_profile(m: Message):
    await user.create_user(m)


@dp.message_handler(chat_type=types.ChatType.PRIVATE, commands=['sex'])
async def craete_profile(m: Message):
    await user.set_user_sex(m)


@dp.message_handler(chat_type=types.ChatType.PRIVATE, commands=['photo'])
async def craete_profile(m: Message):
    await user.set_profile_photo(m)


@dp.message_handler(state=UserProfile.profile_photo, content_types=['photo'])
async def update_state_profile(m: Message, state: FSMContext):
    await user.edit_profile_photo(m, m.photo[-1].file_id)
    await state.finish()


# Обработка callback клавиатуры для смены пола
@dp.callback_query_handler(Text(startswith='set_sex_'))
async def process_callback_keyboards_for_sex(callback: types.CallbackQuery):
    if callback.data == "set_sex_girl":
        await user.edit_user_settings(callback.message, {"user_id": callback.from_user.id}, {"$set": {"sex": "girl"}})
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)
        await callback.answer()

    if callback.data == "set_sex_boy":
        await user.edit_user_settings(callback.message, {"user_id": callback.from_user.id}, {"$set": {"sex": "boy"}})
        await bot.delete_message(callback.message.chat.id, callback.message.message_id)
        await callback.answer()


# Обработка callback клавиатуры для вступления в брак
@dp.callback_query_handler(Text(startswith='marry_set_'))
async def process_callback_keyboards_for_sex(callback: types.CallbackQuery):
    if callback.data.split("_")[-3] == "cancel":
        await marry.cancel_marry(bot, callback.message, callback)
        await callback.answer()

    elif callback.data.split("_")[-3] == "allow":
        await marry.allow_marry(bot, callback.message, callback)
        await callback.answer()


if __name__ == '__main__':
    main = Main()
    user = main.user
    chat = main.chat
    marry = main.marry
    executor.start_polling(dp, skip_updates=True)
