import asyncio
import telegram
from telegram.constants import ParseMode
import random

TOKEN = "6046660801:AAH4SrcmWMc698s9UPuTBjIYkBkB8rH35mA"
chat_id = "-1001803295485"


GREEN_WEIGHT = 9  # Weight of the "GREEN" message (out of 10)
RED_WEIGHT = 1  # Weight of the "RED" message (out of 10)


async def send_message():
    bot = telegram.Bot(TOKEN)
    entry_point = round(random.uniform(1.00, 5.00), 2)
    message = """
🚨 <b>Analisando Possivel Entrada</b> 🚨

✋ <b>Aguarde Confirmação...</b> ✋

🚀 <b>Saindo maior que 1.5x fazer a entrada que será confirmada.</b>

<a href='https://shre.ink/VIPJack'>Cadastre e Entre Agora !!!</a>
    """
    msg = await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
    await asyncio.sleep(35)

    await bot.delete_message(chat_id=chat_id, message_id=msg.message_id)

    # Weighted random selection of "GREEN" or "RED" message
    message_type = random.choices(["GREEN", "RED"], [GREEN_WEIGHT, RED_WEIGHT])[0]

    if message_type == "GREEN":
        message = f"""
🚨  OPORTUNIDADE CONFIRMADA 🚨

🔄 <b>Saida:</b> até {entry_point}x

<a href='https://shre.ink/VIPJack'>Cadastre e Entre Agora !!!</a>
        """
        await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
        await asyncio.sleep(20)
        message = f"✅✅✅ GREEN {entry_point} ✅✅✅"
    else:
        message = f"""
🚨  OPORTUNIDADE PERDIDA 🚨

🔄 <b>Saida:</b> até {entry_point}x

<a href='https://shre.ink/VIPJack'>Cadastre e Entre Agora !!!</a>
        """
        await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
        await asyncio.sleep(20)
        message = f"❌❌❌ RED {entry_point} ❌❌❌"
    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)


async def main():
    while True:
        await asyncio.ensure_future(send_message())
        await asyncio.sleep(40)


if __name__ == "__main__":
    asyncio.run(main())