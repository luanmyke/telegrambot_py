import asyncio
import telegram
from telegram.constants import ParseMode
import random
from datetime import datetime, timedelta
import pytz
import time

TOKEN = "6080356044:AAHWA6HCTHmB-KBimtIn0ewOjhbP45KJj80"
chat_id = "-1001954149729"
emoji_sets = ["🧤", "⚽", "🔴"]

random.seed()

async def send_message():
    bot = telegram.Bot(TOKEN)

    # Generate 3x2 grid of "🔴" emojis
    grid = [["🔴" for i in range(3)] for j in range(2)]

    # Place "🧤" and "⚽" emojis on the grid
    random.shuffle(emoji_sets)
    for emoji in emoji_sets:
        while True:
            random_row = random.randrange(2)
            random_col = random.randrange(3)
            if grid[random_row][random_col] == "🔴":
                grid[random_row][random_col] = emoji
                break

    # Format the grid into a message
    fmtstr = ""
    for row in grid:
        fmtstr += " ".join(row) + "\n"

    now = datetime.now(pytz.timezone('America/Sao_Paulo'))
    later = (now + timedelta(minutes=2)).strftime("%H:%M")

    message = f"""

✅ ENTRADA CONFIRMADA ✅
🕹Tentativas: 3

{fmtstr}
Validade até ➡️: {later} horas
<a href='https://shre.ink/VIPJack'>CADASTRE-SE</a>
"""

    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)

async def main():
    while True:
        await asyncio.ensure_future(send_message())
        await asyncio.sleep(119)

if __name__ == "__main__":
    asyncio.run(main())
