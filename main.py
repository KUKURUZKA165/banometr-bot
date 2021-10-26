import time
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

print("Загруз0чка")


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

    send_mess = "<b>Список команд:</b>\n\n<b>/plus</b> - Додати 0,25 бану\n\n<b>/minus</b> - Відняти 0,25 бану"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    send_mess = "<b>Наш канал: @Igrovshina\nНаш чат: @Igrovshinski_terevenki</b>"
    await bot.send_message(message.chat.id, send_mess, parse_mode="html")

    await log("Старт відправлено!")


@dp.message_handler(content_types=["text"])
async def mess(message):

    await log(f"--------------------\n{time.ctime()}\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} id={message.from_user.id}\n{message.chat.title} {message.chat.invite_link} id = {message.chat.id}\n-\nВідправив(ла): {message.text}")


print(f"Я живий!")

if __name__ == '__main__':
    executor.start_polling(dp)
