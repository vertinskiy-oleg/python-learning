import time
import requests

token = '734516183:AAEs81N8bZdFK4YqwpBsYm7CODXNoe-1nqY'

url = 'https://api.telegram.org/bot{}/'.format(token)

def get_updates(url, offset=None):
    url = url + 'getUpdates'
    params = {
        'timeout': 100,
        'offset': offset
    }
    res = requests.get(url, params=params)
    data = res.json()
    return data
    
def get_last_chat_id_and_text(data):
    chat_id = data['result'][-1]["message"]["chat"]["id"]
    text = data['result'][-1]["message"]["text"]
    return (chat_id, text)

def get_last_update_id(data):
    return data['result'][-1]['update_id']

print(get_last_update_id(get_updates(url)))

# def send_message(url, chat_id, text):
#     url = url + 'sendMessage'
#     params = {
#     'chat_id': chat_id,
#     'text': text 
#     }
#     requests.get(url, params)

    
# def main():
#     last_textchat = ()
#     while True:
#         print('getting updates')
#         chat_id, text = get_last_chat_id_and_text(get_updates(url))
#         if (chat_id, text) != last_textchat:
#             send_message(url, chat_id, text)
#             last_textchat = (chat_id, text)
#         time.sleep(0.5)

# if __name__ == '__main__':
#     main()



