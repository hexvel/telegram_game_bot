TOKEN = "6514252242:AAHTDOK5cbB_6mE38kzq_ZL52oYUAnS25mM"


class Icons:
    TRUE = "✅"
    FALSE = "❎"
    SETTINGS = "⚙️"
    KING = "👑"
    USER = "👤"
    USERS = "👥"
    COMMENT = "💬"
    TIME = "⏰"
    MONEY = "€"
    WIFE = "👰‍♀️"
    FACE = "👽"


class Words:
    NOTGETDB = "{FALSE} Произошла ошибка при получении <a href=tg://user?id={user_id}>пользователя</a> из базы данных."
    NOTFOUND = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> не найден в базе данных."
    REPLYNOTFOUND = "{FALSE} Укажите пользователя."
    CREATE = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> не найден в базе данных\n{SETTINGS} Чтобы зарегистрироваться в базе, напишите мне в личку /create"
    USERFOUND = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> уже зарегистрирован в базе данных."
    PROFILECREATED = "{TRUE} <a href='tg://user?id={user_id}'>Пользователь</a> успешно создал новый аккаунт\n{SETTINGS} По умолчанию ваш пол выбран как женский, можете поменять используя команду /sex"
    PROFILEWITHOUTDES = "{USER} Профиль <a href='tg://user?id={user_id}'>пользователя</a>\n{KING} Никнейм: {nickname}\n{COMMENT} Описание: Отстствует\n{FACE} Пол: {sex}"
    PROFILEWITHDES = "{USER} Профиль <a href='tg://user?id={user_id}'>пользователя</a>\n{KING} Никнейм: {nickname}\n{COMMENT} Описание: {description}\n{FACE} Пол: {sex}"

    ALREADY_MARRIED = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> уже в браке."
    NOTMARRIED = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> не в браке."
    MARRIED = "{TRUE} <a href='tg://user?id={user_id}'>Пользователь</a> теперь в браке с <a href='tg://user?id={partner_id}'>{partner_nickname}</a>."
    MARRIEDWITH = "{WIFE} <a href='tg://user?id={user_id}'>Пользователь</a> в браке с <a href='tg://user?id={partner_id}'>{partner_nickname}</a>"
    DIVORCE = "{TRUE} <a href='tg://user?id={user_id}'>Пользователь</a> решил уйти за хлебом. Пожелаем удачки ;)"
