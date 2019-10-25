import time
import requests

TOKEN = '734516183:AAEs81N8bZdFK4YqwpBsYm7CODXNoe-1nqY'

URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)

def get_updates(offset=None):
    url = URL + 'getUpdates'
    params = {
        'timeout': 100,
        'offset': offset
    }
    res = requests.get(url, params=params)
    data = res.json()
    return data

def get_last_update_id(data):
    return data['result'][-1]['update_id']

def send_message(chat_id, text):
    url = URL + 'sendMessage'
    params = {
    'chat_id': chat_id,
    'text': text 
    }
    requests.get(url, params)

def echo_all(data):
    for d in data["result"]:
        text = d["message"]["text"]
        chat_id = d["message"]["chat"]["id"]
        send_message(chat_id, text)

def main():
    last_update_id = None
    while True:
        print('updating')
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()