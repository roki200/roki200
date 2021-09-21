#Телеграм бот с RP командами и с командами модерирование (код не совсем мой)
#оригинал @Krasbot
from time import sleep

import mybot as mybot
from pyrogram.errors import FloodWait

import config
import random

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from filters import IsAdminFilter

bot = Bot(token=config.TOKEN, parse_mode="html")
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.reply(
        f"""Привет <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>, я Котёнок😸 . Чтобы узнать что я умею введите команду /help""")


###########команды

@dp.message_handler(commands=['help'])
async def help_message(message: types.Message):
    await message.reply(
        "Мои RP команды(все команды пишутся в ответ на сообщение):\n gay - на сколько процентов гей (все рандомно и не стоит воспринимать всерьез.) ;\n  Снять штаны\n  Поцеловать\n  Выебать\n  Обнять\n  Пнуть\n  Ущипнуть\n  Ущипнуть попку\n  Пожать руку\n  Потрогать член\n  Трахнуть\n  Женится-Жениться на кого-то\n  Подрочить-подрочить на кого-то\n  Подрочить на-почти тоже самое как подрочить\n  Ударить\n  Ударить сковородкой\n  Когда я умру")




@dp.message_handler(Text("!лох", ignore_case=True))
async def gay_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a> лох 🤓 на {random.randint(00,100)}%""")


@dp.message_handler(commands=["filters"])
async def filters_message(message: types.Message):
    await message.reply()



@dp.message_handler(Text("роки", ignore_case=True))
async def kras_message(message: types.Message):
    await message.reply(
        "Извините, что вмешиваюсь, я его бот, если он не отвечает, то напишите своё сообщение мне в личку, я передам.")


@dp.message_handler(Text("бот", ignore_case=True))
async def bot_message(message: types.Message):
    await message.reply("Я тут. Нахуй звал ?")


@dp.message_handler(Text("привет", ignore_case=True))
async def bot_message(message: types.Message):
    await message.reply("Приветик🥺")


@dp.message_handler(Text("всем привет", ignore_case=True))
async def bot_message(message: types.Message):
    await message.reply("Приветик🥺")


@dp.message_handler(Text("браки", ignore_case=True))
async def bot_message(message: types.Message):
    await message.reply("Вам по 10 лет. Какие нахуй браки?!")


@dp.message_handler(Text("мой брак", ignore_case=True))
async def bot_message(message: types.Message):
    await message.reply("Лол чел. Тебе 10 лет, и ты в браке...?")


@dp.message_handler(Text("пинг", ignore_case=True))
async def bot_message(message: types.Message):
    await message.reply("ПОНГ")


@dp.message_handler(Text(".ping", ignore_case=True))
async def bot_message(message: types.Message):
    await message.reply("PONG")


@dp.message_handler(content_types=["new_chat_members"])
async def new_member_message(message: types.Message):
    await message.answer(
        f"""Приветсвую тебя <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>, в нашем уютном чате, но прошу тебя прочитать правила и не нарушать их! """)


@dp.message_handler(content_types=["left_chat_member"])
async def left_member_message(message: types.Message):
    await message.reply("Бля, минус один пидор. Ну и пошёл он в пизду.)")

@dp.message_handler(Text("приветствуй", ignore_case=True))
async def bot_message(message: types.Message):
    await message.reply("Приветствую всех, в нашем уютном чате, но прошу вас скинуть сиськи мне в лс🥺🥺 ")


@dp.message_handler(Text("снять штаны", ignore_case=True))
async def take_off_pants_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> снял штаны 🩳🔞  у <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("gay", ignore_case=True))
async def gay_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a> гей 🏳️‍🌈 👬  на {random.randint(0, 100)}%""")


@dp.message_handler(Text("поцеловать", ignore_case=True))
async def kiss_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    y = ["😚", "😙", "😗", "😘"]
    o = random.choice(y)
    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> поцеловал {o}  <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("выебать", ignore_case=True))
async def fuck_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> выебал(а) 💪👉👌  <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("обнять", ignore_case=True))
async def hug_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> обнял(а) 🤗  <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("послать нахуй", ignore_case=True))
async def hug_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> послал(а) 🤗  <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a> нахуй 🖕😬""")


@dp.message_handler(Text("пнуть", ignore_case=True))
async def kick_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> пнул(а) 👞 <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("ущипнуть", ignore_case=True))
async def pinch_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> ущипнул(а) 🤏  <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("пожать руку", ignore_case=True))
async def shake_hands_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> пожал(а) руку 🤝 <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("ущипнуть попку", ignore_case=True))
async def pinch_ass_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> ущипнул(а) попку 🍑🤏 <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("потрогать член", ignore_case=True))
async def touch_penis(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> потрогал(а) член 🍌🤏 <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("трахнуть", ignore_case=True))
async def fuck2_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> трахнул(а) 👉👌  <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("отсосать", ignore_case=True))
async def suck_off_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> отсосал(а) 👄🍌 у <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("подрочить", ignore_case=True))
async def jerk_off_message(message: types.Message):
    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> успешно подрочил 🍆 и получил удовольствие 💦.""")


@dp.message_handler(Text("подрочить на", ignore_case=True))
async def jerk2_off_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> подрочил(а) 🍆  на <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("ударить", ignore_case=True))
async def hit_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> ударил(а) 👊 <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")

@dp.message_handler(Text("ударить сковородкой", ignore_case=True))
async def hit2_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> ударил(а) сковородкой 💥👊 <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("жениться", ignore_case=True))
async def get_married_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    h = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября",
         "Декабря"]

    g = random.choice(h)
    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> женился(ась) 🤴👰 {random.randint(1, 30)} {g} {random.randint(2021, 2031)} году на <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>""")


@dp.message_handler(Text("когда умрешь ?", ignore_case=True))
async def when_die_message(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Эта сообщение должна быть ответом на сообщение !")
        return

    h = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября",
         "Декабря"]
    j = ["😱", "⚰️", "☠️"]
    u = random.choice(j)
    g = random.choice(h)

    await message.answer(
        f"""<a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a> умрет {u}  {random.randint(1, 30)} {g} {random.randint(2021, 2031)} года.""")


@dp.message_handler(Text("когда я умру", ignore_case=True))
async def when2_die_message(message: types.Message):
    h = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября",
         "Декабря"]
    j = ["😱", "⚰️", "☠️"]
    u = random.choice(j)
    g = random.choice(h)

    await message.answer(
        f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> ты умрешь {u}  {random.randint(1, 30)} {g} {random.randint(2021, 2031)} года.""")


#########################################################################################

@dp.message_handler(is_admin=True, commands=["mute", "мут", "молчипидр"], commands_prefix="!")
async def mute_member(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    user = await message.bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_chat_admin():
        await message.reply("🙅‍♂️  я не буду мутить админа.")
        return

    await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                           types.ChatPermissions())

    await message.answer(
        f"""<a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a> помолчика ты 🤐""")


@dp.message_handler(is_admin=True, commands=["unmute", "размут"], commands_prefix="!")
async def unmute_member(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                           types.ChatPermissions(True))

    await message.answer(
        f"""ОК. <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a> может дальше балаболить 🤡 """)

@dp.message_handler(is_admin=True, commands=["ban", "бан", "банан"], commands_prefix="!")
async def ban_member(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    user = await message.bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_chat_admin():
        await message.reply("🙅‍♂️  я не буду банить админа.")
        return

    await message.bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)

    await message.answer(
        f"""<a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a> улетел в бан 😉""")


@dp.message_handler(is_admin=True, commands=["unban", "разбан"], commands_prefix="!")
async def unban_member(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    await message.bot.unban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)

    await message.answer(
        f"""<a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a> вышел из бана 😧""")


@dp.message_handler(is_admin=True, commands=['deleate', "удалить"], commands_prefix="!")
async def delete_message(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение !")
        return

    user = await message.bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    if user.is_chat_admin():
        await message.reply("🙅‍♂️  я не буду удалять сообщение админа.")
        return

    await message.reply_to_message.delete()
    await message.reply("Сообщение удалено !")


if name == 'main':
    executor.start_polling(dp, skip_updates=True)
