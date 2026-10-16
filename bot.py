import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("Missing Telegram bot token")
else:
    url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    response = requests.get(url, timeout=15)
    print(response.json())
