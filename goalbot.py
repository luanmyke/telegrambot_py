import asyncio
import telegram
from telegram.constants import ParseMode
import random
from datetime import datetime, timedelta
import pytz

TOKEN = "6197824892:AAHUI_6JYeeBgsNDwIEEUiyPi5FXnqjF4u4"
chat_id = "-1001929881148"
emoji_sets = ["🟩", "⚽"]

bot = telegram.Bot(token=TOKEN)

# Create an empty 7x4 array
array = [["" for _ in range(7)] for _ in range(4)]

# Add one ⚽️ to each column
for i in range(7):
    row = random.randint(0, 3)
    array[row][i] = "⚽️"

# Fill the remaining spaces with 🟩
for i in range(4):
    for j in range(7):
        if array[i][j] == "":
            array[i][j] = "🟩"

# Convert array to a string
array_str = ""
for i in range(4):
    for j in range(7):
        array_str += array[i][j]
    array_str += "\n"

# Construct the message with the array
now = datetime.now(pytz.timezone('America/Sao_Paulo'))
later = (now + timedelta(minutes=2)).strftime("%H:%M")

async def send_message():
    message = f'''✅ ENTRADA CONFIRMADA ✅
🕹Tentativas: 3

{array_str}

Validade até ➡️: {later} horas
<a href='https://shre.ink/VIPJack'>CADASTRE-SE</a>
'''
    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)

async def main():
    while True:
        await send_message()
        await asyncio.sleep(120)


if __name__ == "__main__":
    asyncio.run(main())
