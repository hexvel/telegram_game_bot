# Можете даже не стараться спиздить токен, я его сразу же поменял :D 
TOKEN = "6514252242:AAEwNLelWO03RKYKeQJjFDbrvn1ib4dOZhM"


class Icons:
    TRUE = "✅"
    FALSE = "❎"
    SETTINGS = "⚙️"
    KING = "👑"
    HUMAN_KING = "🤴"
    USER = "👤"
    USERS = "👥"
    COMMENT = "💬"
    TIME = "⏰"
    MONEY = "€"
    WIFE = "👰‍♀️"
    BOT = "🤖"
    FACE = "👽"
    BABY = "👶"
    HEART = "❤️"
    BREAD = "🍞"


class Words:
    NOTSELF = "{FALSE} Эта команда может быть использована только с ответом на сообщение пользователя."
    NOTGETDB = "{FALSE} Произошла ошибка при получении <a href=tg://user?id={user_id}>пользователя</a> из базы данных."
    NOTFOUND = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> не найден в базе данных."
    REPLYNOTFOUND = "{FALSE} Укажите пользователя."
    CREATE = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> не найден в базе данных\n{SETTINGS} Чтобы зарегистрироваться в базе, напишите мне в личку /create"
    USERFOUND = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> уже зарегистрирован в базе данных."
    PROFILECREATED = "{TRUE} <a href='tg://user?id={user_id}'>Пользователь</a> успешно создал новый аккаунт\n{SETTINGS} По умолчанию ваш пол выбран как женский, можете поменять используя команду /sex"
    PROFILEWITHOUTDES = "{USER} Профиль <a href='tg://user?id={user_id}'>пользователя</a>\n{KING} Никнейм: {nickname}\n{COMMENT} Описание: Отстствует\n{FACE} Пол: {sex}"
    PROFILEWITHDES = "{USER} Профиль <a href='tg://user?id={user_id}'>пользователя</a>\n{KING} Никнейм: {nickname}\n{COMMENT} Описание: {description}\n{FACE} Пол: {sex}"

    REQUEST_MARRY = "{WIFE} <b><a href='tg://user?id={partner_id}'>{partner_nickname}</a></b>, Вам сделали предложение руки и сердца. Вы согласны?."
    ALREADY_MARRIED = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> уже в браке."
    NOTMARRIED = "{FALSE} <a href='tg://user?id={user_id}'>Пользователь</a> не в браке."
    MARRIED = "{TRUE} <a href='tg://user?id={user_id}'>Пользователь</a> теперь в браке с <a href='tg://user?id={partner_id}'>{partner_nickname}</a>."
    MARRIEDWITH = "{WIFE} <a href='tg://user?id={user_id}'>Пользователь</a> в браке с <a href='tg://user?id={partner_id}'>{partner_nickname}</a>"
    DIVORCE = "{TRUE} <a href='tg://user?id={user_id}'>Пользователь</a> решил уйти за хлебом. Пожелаем удачки ;)"
    CANCELREQUEST = "{FALSE} К сожалению <b><a href='tg://user?id={user_id}'>пользователь</a></b> не принял запрос."
    NOTPERMISSION = "{FALSE} Бля, чел, не вмешивайся а\nУ нас тут молодожёны намечаются :D"
    ALLOWREQUEST = "{TRUE} <a href='tg://user?id={user_id}'>Пользователь</a> принял запрос\n{WIFE} Поприветствуем молодожён!"

    CHAT_EXISTS = "{FALSE} Данный чат уже зарегистрирован в базе данных."
    CHAT_CREATED = "{TRUE} Чат {name} успешно зарегистрирован в базе даннх\n{SETTINGS} Теперь можете выдавать роль модератора участникам."
    CHAT_NOT_EXISTS = "{FALSE} Данноа чат не зарезистрирован в базе данных\n{SETTINGS} Чтобы зарезистрировать чат, напедите мне в личку /reg"

    MODERATOR_ALREADY_EXISTS = "{FALSE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> уже является модератором."
    USER_ALREAY_ADMIN = "{FALSE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> уже является администратором."
    MODERATOR_ADDED = "{TRUE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> теперь является модератором."
