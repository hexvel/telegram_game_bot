from config import Icons, Words
from Database.base import Database
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class UserProfile(StatesGroup):
    profile_photo = State()


class User(Database):
    def __init__(self):
        super().__init__()

    async def get_user_info(self, message):
        user_id = message.from_user.id
        user_in_base = self.find_one({"user_id": user_id})
        if not user_in_base['is_done']:
            return await message.answer(Words.NOTGETDB.format(FALSE=Icons.FALSE, user_id=user_id))

        if user_in_base['result'] is None:
            await message.answer(Words.CREATE.format(FALSE=Icons.FALSE, user_id=user_id, SETTINGS=Icons.SETTINGS))

        user_info = user_in_base['result']
        text = Words.PROFILEWITHDES.format(
            USER=Icons.USER, user_id=user_id, KING=Icons.KING,
            nickname=user_info['nickname'], COMMENT=Icons.COMMENT,
            description=user_info['description'], FACE=Icons.FACE,
            sex=user_info['sex']
        ) if user_info['description'] != "Empty" else Words.PROFILEWITHOUTDES.format(
            USER=Icons.USER, user_id=user_id, KING=Icons.KING,
            nickname=user_info['nickname'], COMMENT=Icons.COMMENT,
            FACE=Icons.FACE, sex=user_info['sex']
        )

        if user_info['married_to'] == "null":
            text += f"\n{Icons.WIFE} Семья: не создана"
        else:
            name = self.find_one({"user_id": user_info['married_to']})[
                'result']['nickname']
            text += f"\n{Icons.WIFE} В паре с: <a href='tg://user?id={user_info['married_to']}'>{name}</a>"

        text = text.replace("boy", "Парень").replace("girl", "Девушка")
        if user_info['profile_photo'] == "null":
            await message.answer(text)
        else:
            await message.answer_photo(user_info['profile_photo'], text)

    async def create_user(self, message):
        user_id = message.from_user.id
        user_in_base = self.find_one({"user_id": user_id})
        if not user_in_base['is_done']:
            return await message.answer(Words.NOTGETDB.format(FALSE=Icons.FALSE, user_id=user_id))

        if user_in_base['result'] is not None:
            return await message.answer(Words.USERFOUND.format(FALSE=Icons.FALSE, user_id=user_id))

        create = self.insert_one(sex="boy", user_id=user_id, married_to="null",
                                 nickname="Default", description="Empty", profile_photo="null")

        if create['is_done']:
            await message.answer(Words.PROFILECREATED.format(TRUE=Icons.TRUE, user_id=user_id, SETTINGS=Icons.SETTINGS))

    async def set_user_sex(self, message):
        user_id = message.from_user.id
        user_in_base = self.find_one({"user_id": user_id})
        if not user_in_base['is_done']:
            return await message.answer(Words.NOTGETDB.format(FALSE=Icons.FALSE, user_id=user_id))

        if user_in_base['result'] is None:
            return await message.answer(Words.NOTFOUND.format(FALSE=Icons.FALSE, user_id=user_id))

        keyboards = InlineKeyboardMarkup().add(
            InlineKeyboardButton("Парень", callback_data="set_sex_boy"),
            InlineKeyboardButton("девушка", callback_data="set_sex_girl")
        )

        await message.answer("Пожалуйста, выберите пол", reply_markup=keyboards)

    async def edit_user_settings(self, message, item, replace):
        replace = self.update_one(item, replace)
        if not replace['is_done']:

            return await message.answer(f"{Icons.FALSE} Произошла ошибка.")
        await message.answer(f"{Icons.TRUE} Данные успешно изменены.")

    async def set_profile_photo(self, message):
        await message.answer(f"{Icons.USER} Пришлите фотографию для профиля.")
        await UserProfile.profile_photo.set()

    async def edit_profile_photo(self, message, photo_id):
        update = self.update_one({"user_id": message.from_user.id}, {
            "$set": {"profile_photo": photo_id}})

        if not update['is_done']:
            return await message.answer(f"{Icons.FALSE} Произошла ошибка.")
        await message.answer(f"{Icons.TRUE} Изображение профиля успешно обновлён.")
