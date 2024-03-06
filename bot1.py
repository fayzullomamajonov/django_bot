# token="7131350574:AAEF0SEHa0Bx1mTuMaxXfc_x9Mdvhq9VeHE"
# chat_id = '1807180991' 

import telegram
import datetime
import asyncio
import sqlite3
import os

bot = telegram.Bot(token="7131350574:AAEF0SEHa0Bx1mTuMaxXfc_x9Mdvhq9VeHE")
conn = sqlite3.connect("db.db")
cursor = conn.cursor()
async def send_good_morning():
    chat_id = "1807180991"  # chat ID to bot

    query = "SELECT * FROM bot_app_employeemodel"
    cursor.execute(query)
    data = cursor.fetchall()
    now = datetime.datetime.now().date()
    birthdays_today = []

    for row in data:
        full_name = f"{row[1]} {row[2]}"
        birth_date = datetime.datetime.strptime(row[3], "%Y-%m-%d").date() 
        if birth_date.month == now.month and birth_date.day == now.day:
            birthdays_today.append((full_name, birth_date, row[5]))

    if birthdays_today:
        for name, b_date, image_id in birthdays_today:
            image_path = os.path.join("media", "images", f"{image_id}")
            try:
                with open(image_path, "rb") as image:
                    caption = f"Full Name: {name}\nBirth Date: {b_date}"
                    await bot.send_photo(chat_id=chat_id, photo=image, caption=caption)
            except FileNotFoundError:
                print(f"Image file {image_path} not found.")
    else:
        message = "There are no birthdays today!"
        await bot.send_message(chat_id=chat_id, text=message)

async def send_message():
    chat_id = "1807180991"  # chat ID to bot
    now = datetime.datetime.now()
    message = f"List of today`s Birtdays({now.year}-{now.month}-{now.day})"
    await bot.send_message(chat_id=chat_id, text=message)
  
async def main():
    while True:
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute == 0:
            await send_message()
            await send_good_morning()

            await asyncio.sleep(24*3600)  # Sleep for 24 hours


if __name__ == "__main__":
    asyncio.run(main())
