import time
from config import TOKEN
from aiogram import Bot, Dispatcher, executor
from db import BotDB

BotDB = BotDB("ban.db3")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def log(text):
    print(text)
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write(f"\n{text}")


@dp.message_handler(commands=["start"])
async def start(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запрошено старт")

    send_mess = f"<b>Привіт, {message.from_user.first_name}!\nЦе - банометр</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Список команд:</b>\n\n<b>/plus</b> - Додати 0,25 бану\n\n<b>/minus</b> - Відняти 0,25 бану\n\n<b>/info</b> - Інформація про людину\n\n<b>/ping</b> - Понг!\n\n<b>/help</b> - Допомога"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Наш канал: @Igrovshina\nНаш чат: @Igrovshinski_terevenki</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    await log("Старт відправлено!")


@dp.message_handler(commands=["ping"])
async def ping(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Пінг?")
    send_mess = f"<b>Понг! Я живий!</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    await log("Понг!")


@dp.message_handler(commands=["help"])
async def help_command(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запросили help")
    send_mess = "<b>Список команд:</b>\n\n<b>/plus</b> - Додати 0,25 бану\n\n<b>/minus</b> - Відняти 0,25 бану\n\n<b>/ping</b> - Понг!\n\n<b>/help</b> - Допомога"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    await log("Зроблено")


@dp.message_handler(commands=["plus"])
async def plus(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    if message.reply_to_message is None:
        send_mess = "<b>Треба відправляти цю команду у відповідь до потрібного користувача</b>"
        await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    else:
        kor_id = message.reply_to_message.from_user.id
        kor_username = message.reply_to_message.from_user.username
        kor_name = message.reply_to_message.from_user.first_name
        await log(f"+0,25 Бану користувачу {kor_name}")
        send_mess = f"<b>+0,25 Бану користувачу {kor_name}</b>"
        await bot.send_message(message.chat.id, send_mess, parse_mode="html")

        if not BotDB.user_exists(kor_id):
            BotDB.add_user(kor_id, kor_username)
            await log("Цього користувача додано до бази даних")
            send_mess = f"<b>Цього користувача додано до бази даних</b>"
            await bot.send_message(message.chat.id, send_mess, parse_mode="html")
        change_ban = BotDB.check_ban(kor_id) + 0.25
        BotDB.change_ban(kor_id, change_ban)
        stalo = BotDB.check_ban(kor_id)
        send_mess = f"<b>В цього користувача зараз {stalo} бану</b>"
        await bot.send_message(message.chat.id, send_mess, parse_mode="html")
        await log(f"Стало {stalo} бану")

    await log("Зроблено")


@dp.message_handler(commands=["minus"])
async def minus(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    if message.reply_to_message is None:
        send_mess = "<b>Треба відправляти цю команду у відповідь до потрібного користувача</b>"
        await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    else:
        kor_id = message.reply_to_message.from_user.id
        kor_username = message.reply_to_message.from_user.username
        kor_name = message.reply_to_message.from_user.first_name
        await log(f"-0,25 Бану користувачу {kor_name}")
        send_mess = f"<b>-0,25 Бану користувачу {kor_name}</b>"
        await bot.send_message(message.chat.id, send_mess, parse_mode="html")

        if not BotDB.user_exists(kor_id):
            BotDB.add_user(kor_id, kor_username)
            await log("Цього користувача додано до бази даних")
            send_mess = f"<b>Цього користувача додано до бази даних</b>"
            await bot.send_message(message.chat.id, send_mess, parse_mode="html")
        change_ban = BotDB.check_ban(kor_id) - 0.25
        BotDB.change_ban(kor_id, change_ban)
        stalo = BotDB.check_ban(kor_id)
        send_mess = f"<b>В цього користувача зараз {stalo} бану</b>"
        await bot.send_message(message.chat.id, send_mess, parse_mode="html")
        await log(f"Стало {stalo} бану")

    await log("Зроблено")


@dp.message_handler(commands=["info"])
async def info(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-")
    await log("Запросили кількість бану")
    if message.reply_to_message is None:
        send_mess = "<b>Треба відправляти цю команду у відповідь до потрібного користувача</b>"
        await bot.send_message(message.chat.id, send_mess, parse_mode="html")
    else:
        kor_id = message.reply_to_message.from_user.id
        kor_username = message.reply_to_message.from_user.username
        kor_name = message.reply_to_message.from_user.first_name

        if not BotDB.user_exists(kor_id):
            BotDB.add_user(kor_id, kor_username)
            await log("Цього користувача додано до бази даних")
            send_mess = f"<b>Цього користувача додано до бази даних</b>"
            await bot.send_message(message.chat.id, send_mess, parse_mode="html")
        banu = BotDB.check_ban(kor_id)
        send_mess = f"<b>У користувача {kor_name} {banu} бану</b>"
        await bot.send_message(message.chat.id, send_mess, parse_mode="html")
        await log(f"У користувача {kor_name} {banu} бану")
    await log("Зроблено")


@dp.message_handler(content_types=["text"])
async def mess(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-\nВідправив(ла): {message.text}")


@dp.message_handler(content_types=["sticker"])
async def mess(message):
    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-\nВідправив(ла) стікер")
    if message.sticker == "3":
        await log("lol")
    else:
        if message.sticker.file_unique_id == "AgADNxIAAoL0kEs":
            await log("Я бачу стікер -0.25 бану")
            await minus(message)
        else:
            if message.sticker.file_unique_id == "AgADHxEAAq8dmEs":
                await log("Я бачу стікер +0.25 бану")
                await plus(message)
            else:
                await log("Цей стікер мені не знайомий")

print(f"Я живий!")

if __name__ == '__main__':
    executor.start_polling(dp)
