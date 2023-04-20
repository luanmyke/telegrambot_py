import asyncio
import telegram
from telegram.constants import ParseMode
from datetime import datetime, timedelta
import pytz
import time

TOKEN = "6211820662:AAEf_8JcyZb3yY2imUzvTvoQg_ZoS0IwqyA"
chat_id = "-1001908349156"

async def send_message():
    bot = telegram.Bot(TOKEN)
    now = datetime.now(pytz.timezone('America/Sao_Paulo'))
    later = (now + timedelta(minutes=5)).strftime("%H:%M")

    message = f"""

ALGORITMO CONFIRMADO ✅

🐯 Fortune Tiger 
🕹 N° de Jogadas



⏳ validade até : {later} horas

<a href='https://shre.ink/VIPJack'>Entre Agora !!!</a>
    """
    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
    time.sleep(240)
    message = "✅✅✅ GREEN ✅✅✅"
    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)

async def main():
    while True:
        await asyncio.ensure_future(send_message())
        await asyncio.sleep(300)

if __name__ == "__main__":
    asyncio.run(main())


