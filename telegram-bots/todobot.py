import time
import requests
import json
from dbhelper import DBHelper

TOKEN = '734516183:AAEs81N8bZdFK4YqwpBsYm7CODXNoe-1nqY'

URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)

db = DBHelper()

def get_updates(offset=None):
    url = URL + 'getUpdates'
    params = {
        'timeout': 100,
        'offset': offset
    }
    res = requests.get(url, params=params)
    updates = res.json()
    return updates

def get_last_update_id(updates):
    return updates['result'][-1]['update_id']

def send_message(chat_id, message, reply_markup=None):
    url = URL + 'sendMessage'
    params = {
    'chat_id': chat_id,
    'text': message 
    }
    if reply_markup:
        params['reply_markup'] = reply_markup
    requests.get(url, params)

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)

def handle_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            items = db.get_items(chat_id)
            if text == '/done':
                keyboard = build_keyboard(items)
                send_message(chat_id, 'Select an item to delete', keyboard)
            elif text == "/start":
                send_message(chat_id, '''Welcome to your personal To Do list. Send any text to me and 
                                I'll store it as an item. Send /done to remove items''')
            elif text.startswith("/"):
                continue
            elif text in items:
                db.delete_item(chat_id, text)
                items = db.get_items(chat_id)
                keyboard = build_keyboard(items)
                send_message(chat_id, 'Select an item to delete', keyboard)
            else:
                db.add_item(chat_id, text)
                items = db.get_items(chat_id)
            message = "\n".join(items)
            send_message(chat_id, message)
        except KeyError:
            pass

def main():
    db.create()
    last_update_id = None
    while True:
        print('updating')
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()