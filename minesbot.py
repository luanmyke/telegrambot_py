import asyncio
import telegram
from telegram.constants import ParseMode
import random
from datetime import datetime, timedelta
import pytz

TOKEN = "6205800356:AAG8HfBwoqp8NfLyNeNLqJNFHDDaXjPIUsg"
chat_id = "-1001874069535"
emoji_sets = ["\U0001F4A3", "\u2B50"]

random.seed()

stars = []

def randArr(arr):
    global stars
    r = random.randrange(0, 24)
    if r not in stars:
        arr[r] = emoji_sets[1]
    else:
        randArr(arr)
    stars.append(r)
    return arr

async def send_message():
    bot = telegram.Bot(TOKEN)
    arr = []
    for _ in range(0,25):
        arr.append(emoji_sets[0])

    stars.clear()
    for _ in range(0,3):
        arr = randArr(arr)
    fmtstr = ''.join(arr)
    fmtstr = "\n".join(fmtstr[i:i+5] for i in range(0, len(fmtstr), 5))

    now = datetime.now(pytz.timezone('America/Sao_Paulo'))
    later = (now + timedelta(minutes=2)).strftime("%H:%M")

    message = f"""

ALGORITMO CONFIRMADO ✅
Tentativas: 3

{fmtstr}


Validade até: {later} horas
<a href='https://shre.ink/sssMines'>CADASTRE-SE</a>
"""

    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)

async def main():
    while True:
        await asyncio.ensure_future(send_message())
        await asyncio.sleep(59)

if __name__ == "__main__":
    asyncio.run(main())

