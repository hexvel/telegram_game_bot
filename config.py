# Можете даже не стараться спиздить токен, я его сразу же поменял :D
TOKEN = "6514252242:AAGCxqDHfmQY8sgmUaOpmAyG9bUNkBTgikY"


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
    KISS = "😘"
    HARD = "😬"
    YUM = "😋"
    KICKRP = "👟"
    OTLIZ = "😋"
    HUG = "🤗"


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
    CHAT_NOT_EXISTS = "{FALSE} Данный чат не зарегистрирован в базе данных\n{SETTINGS} Чтобы зарегистрировать чат, напишите в чате /reg"

    MODERATOR_ALREADY_EXISTS = "{FALSE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> уже является модератором."
    IS_NOT_MODERATOR = "{FALSE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> не является модератором."
    USER_ALREAY_ADMIN = "{FALSE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> уже является администратором."
    MODERATOR_ADDED = "{TRUE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> теперь является модератором."
    MODERATOR_REMOVED = "{TRUE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> больше не является модератором."

    CANT_KICK = "{FALSE} Не удалось исключить участника\n{COMMENT} Возможно этот участник является администратором данного чата."
    KICKED = "{TRUE} <b>Участник: <a href='tg://user?id={user_id}'>{name}</a></b> был исключен из чата."

    REWARD_CREATED = "{YES} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> успешно награждён."
    REWARD_DELETED = "{YES} У <b><a href='tg://user?id={user_id}'>пользователя</a></b> успешно снята награда."
    REWARD_EXISTS = "{FALSE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> уже имеет такую награду."
    REWARD_NOT_EXISTS = "{FALSE} <b><a href='tg://user?id={user_id}'>Пользователь</a></b> не имеет такую награду."
    REWARDS_NOT_FOUND = "{FALSE} У <b><a href='tg://user?id={user_id}'>пользователя</a></b> нет наград."


class RolePlay_Words:
    HUG_USER = "{HUG} | <b><a href='tg://user?id={user_id}'>{user_name}</a></b> обнял(-а) <b><a href='tg://user?id={huged_user_id}'>{huged_user_name}</a></b>"
    KISS_USER = "{KISS} | <b><a href='tg://user?id={user_id}'>{user_name}</a></b> поцеловал(-а) <b><a href='tg://user?id={kissed_user_id}'>{kissed_user_name}</a></b>"
    FUCK_USER = "{FUCK} | <b><a href='tg://user?id={user_id}'>{user_name}</a></b> выебал(-а) <b><a href='tg://user?id={fucked_user_id}'>{fucked_user_name}</a></b>"
    SUCK_USER = "{SUCK} | <b><a href='tg://user?id={user_id}'>{user_name}</a></b> отсосал(-а) у <b><a href='tg://user?id={sucked_user_id}'>{sucked_user_name}</a></b>"
    KICK_USER = "{KICK} | <b><a href='tg://user?id={user_id}'>{user_name}</a></b> пнул(-а) <b><a href='tg://user?id={kicked_user_id}'>{kicked_user_name}</a></b>"
    UEBAT_USER = "{UEBAT} | <b><a href='tg://user?id={user_id}'>{user_name}</a></b> уебал(-а) <b><a href='tg://user?id={uebated_user_id}'>{uebated_user_name}</a></b>"
    OTLIZ_USER = "{OTLIZ} | <b><a href='tg://user?id={user_id}'>{user_name}</a></b> отлизал(-а) у <b><a href='tg://user?id={otlized_user_id}'>{otlized_user_name}</a></b>"


class RolePlay_Links:
    HUG = [
        'https://pm1.aminoapps.com/6659/30e30a871331073a2016f6024579633d3706c9da_00.jpg',
        'https://pibig.info/uploads/posts/2021-05/1620650978_1-pibig_info-p-anime-grustnie-obnimashki-anime-krasivo-1.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNib40b0IL9JvpJFqOJv_lN2MlBuBubky3Eg&usqp=CAU',
        'https://oir.mobi/uploads/posts/2021-03/1616368640_42-p-anime-obnimashki-paren-i-devushka-48.jpg'
    ]

    KISS = [
        'https://cm1.aminoapps.com/7084/5c95d4a2f742cb0dd5bd841798ab64a4fdf63389_00.jpg',
        'https://foni.club/uploads/posts/2023-01/1673188172_foni-club-p-oboi-anime-parnie-potselui-2.jpg',
        'https://aniyuki.com/wp-content/uploads/2022/05/aniyuki-anime-kiss-image-44-1024x576.jpg',
        'https://aniyuki.com/wp-content/uploads/2022/05/aniyuki-anime-kiss-image-17-1024x768.jpg'
    ]

    FUCK = [
        'https://pbs.twimg.com/media/CBb7fPWVEAEoPwr?format=jpg&name=medium',
        'https://img3.gelbooru.com/images/18/22/1822088d61510bba9b381886c8386a3b.jpg',
        'https://static3.hentai-img.com/upload/20160930/146/149416/16.jpg',
        'https://topdevka.com/uploads/posts/2023-01/thumbs/1674178154_40-topdevka-com-p-porno-ravtaliya-54.jpg',
        'https://3.bp.blogspot.com/-Z_GQINTZ9cY/Tdb0Qa64eSI/AAAAAAAAGJE/_DMhmLTATig/s1600/Aerith_Dry.jpg',
        'https://sun9-72.userapi.com/impg/B92zabJ6DdvovJdeLtUSf29FbBxkKUWYz7L7Cw/bMBCnJJMHbA.jpg?size=1200x750&quality=96&sign=047ce677c027aae3e2a40deb298f32ec&c_uniq_tag=5Fo2jt9noOAvuCHOypnbmDQl5-7TFMSZXBrQqmNDiUg&type=album',
        'https://static2.hentai-img.com/upload/20160903/118/120014/25.jpg',
        'https://static13.hentai-img.com/upload/20211113/797/816125/p=700/4.jpg',
        'https://хентайманга.рф/images/slides/4111/309847/0.jpg',
        'https://хентайманга.рф/images/slides/4111/309824/1.jpg',
        'https://хентайманга.рф/images/slides/4111/309884/0.jpg',
        'https://xxx.sexkomix1.com/uploads_images/porno-komiks-gweda--kokomi--kazeki-yuy--yoimiya--marin--mitsuri-seks-komiks-artov-i-kartinok-2022-07-23/porno-komiks-gweda--kokomi--kazeki-yuy--yoimiya--marin--mitsuri-seks-komiks-artov-i-kartinok-2022-07-23-153953989.jpg'
    ]

    SUCK = [
        'https://havepussy.com/0-0/8452_havepussy_.jpg',
        'https://www.mymypic.net/data/attachment/forum/201710/08/145221zx3hhi7f7k7d7ik1.jpg',
        'https://static3.hentai-img.com/upload/20160912/138/140938/18.jpg',
        'http://img02.rl0.ru/5bc92dd557df7ee4922047216d22faca/c1200x900/40.media.tumblr.com/d6460021d086c93db7a0a8ccda98bf72/tumblr_n61akhPz8w1r31yk3o1_1280.jpg',
        'https://pbs.twimg.com/media/FHnXj04acAAOwQ4.jpg:large',
        'https://static3.hentai-img.com/upload/20160917/143/145448/42.jpg',
        'https://avatars.mds.yandex.net/i?id=0d964f72365f9657bc8cf2fe0e5ca3b96e964d69-4268172-images-thumbs&ref=rim&n=33&w=141&h=200',
        'https://static4.hentai-img.com/upload/20170226/261/266808/14.jpg',
        'https://pbs.twimg.com/media/C3z7CMuVYAE23jr?format=jpg&name=medium',
        'https://avatars.mds.yandex.net/i?id=9bff765239eaaed751584b0113bb4930b20b5098-8179254-images-thumbs&ref=rim&n=33&w=141&h=200',
        'https://pbs.twimg.com/media/E_PXfrSVEAU0jhT.jpg'
    ]

    UEBAT = [
        'https://gas-kvas.com/uploads/posts/2023-01/1673345310_gas-kvas-com-p-anime-udar-risunki-29.jpg',
        'https://i.ytimg.com/vi/DOTGrI55zyw/maxresdefault.jpg',
        'https://i.ytimg.com/vi/Uwq76Blw_iQ/maxresdefault.jpg',
        'https://i.imgur.com/Ngc9RNv.png',
        'https://i.ytimg.com/vi/b06KyNFY9dA/maxresdefault.jpg',
        'https://img4.goodfon.ru/wallpaper/nbig/6/d0/one-punch-man-saitama-suiryu-punch-fight-strong-anime-manga.jpg'
    ]

    OTLIZ = [
        'https://static2.hentai-img.com/upload/20160803/78/79633/16.jpg',
        'https://github-production-user-asset-6210df.s3.amazonaws.com/27140154/72470175-5b953900-381b-11ea-936a-ead5ee92df00.jpg',
        'http://www.sankakucomplex.com/wp-content/uploads/2009/05/heterosexual-hentai-cunnilingus-61.jpg',
        'https://static3.hentai-img.com/upload/20170104/167/170502/8.jpg',
        'https://static2.hentai-img.com/upload/20160605/63/64308/7.jpg',
        'https://i.artfile.ru/2560x1440_885573_[www.ArtFile.ru].jpg',
        'https://static3.hentai-img.com/upload/20160904/113/114721/14.jpg',
        'https://static3.hentai-img.com/upload/20160904/113/114721/41.jpg'
    ]
