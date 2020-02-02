from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import json
import requests
import random

# Connect
vk = vk_api.VkApi(token="ed46e4b42cdd59ed93db354818f5b7851bbe8d6a1977a760ef5f10e640558af429597dc891bbefb3a81f5")
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, 182910634)


def photos():
    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open('popa.jpg', 'rb')}).json()
    c = vk.method("photos.saveMessagesPhoto", {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    d = 'photo{}_{}'.format(c['owner_id'], c['id'])
    vk.method('messages.send',
              {'peer_id': event.object.peer_id, "attachment": 'photo-182910634_457239028', 'random_id': 0})

def phota():
    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open('popa2.jpg', 'rb')}).json()
    c = vk.method("photos.saveMessagesPhoto", {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    d = 'photo{}_{}'.format(c['owner_id'], c['id'])
    vk.method('messages.send',
              {'peer_id': event.object.peer_id, "attachment": 'photo-182910634_457239029', 'random_id': 0})

def photak():
    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open('popa3.jpg', 'rb')}).json()
    c = vk.method("photos.saveMessagesPhoto", {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    d = 'photo{}_{}'.format(c['owner_id'], c['id'])
    vk.method('messages.send',
              {'peer_id': event.object.peer_id, "attachment": 'photo-182910634_457239053', 'random_id': 0})
    
    
photo_list = [photos, phota, photak]

keyboard = {

    "one_time": True,
    "inline": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Покажи попу"
            }
        }],

        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "ЧикиБамбони"
            },
            "color": "positive"
        }]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

print('Запускаемся')

for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:
        response = event.object.text.lower()
        if event.from_user and not event.from_group:
            if response == "/help":
                vk.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': 'Я могу: \n 1) кнопочки \n 2) Тест',
                    'random_id': 0
                })

            elif response == "кнопочки":
                vk.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': 'Приколюха',
                    'keyboard': keyboard,
                    'random_id': 0
                })

            elif response == "покажи попу":
                papapapa = random.choice(photo_list)
                papapapa()

            elif response == "чикибамбони":
                vk.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': 'Lol',
                    'random_id': 0
                })

            else:
                vk.method('messages.send', {
                    'peer_id': event.object.peer_id,
                    'message': 'Я вас не понял!',
                    'random_id': 0
                })
            print(event.object)
            print(event.object.geo)



