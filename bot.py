import os
import requests
import time

BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_ACTUAL_BOT_TOKEN_HERE')

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    params = {'offset': offset, 'timeout': 30}
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text):
    keyboard = {
        "inline_keyboard": [[
            {"text": "🟡️ Join Channel 🟡️", "url": "https://t.me/senseiRedirect"}
        ]]
    }
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": keyboard,
        "disable_web_page_preview": True
    }
    requests.post(url, json=payload)

def main():
    last_update_id = None
    welcome_message = """
Welcome to our Travel Deals Bot, Sensei Reloaded 🟡!

✗ Get ready for amazing travel deals and exclusive offers!

📌 Join our channel for the latest updates:  
https://t.me/senseiRedirect

Start your journey with us! 🟡️
    """
    
    print("Bot is running...")
    
    while True:
        try:
            updates = get_updates(last_update_id)
            
            if 'result' in updates:
                for update in updates['result']:
                    last_update_id = update['update_id'] + 1
                    
                    if 'message' in update and 'text' in update['message']:
                        message = update['message']
                        chat_id = message['chat']['id']
                        text = message['text']
                        
                        if text == '/start':
                            send_message(chat_id, welcome_message)
            
            time.sleep(1)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == '__main__':
    main()
