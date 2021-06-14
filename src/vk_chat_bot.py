from vk_api import VkApi
from vk.Chat_bot_VK.src.my_methods import process_message, process_button
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import json


if __name__ == '__main__':
    try:
        with open('../../config.json', 'r') as file:
            settings = json.load(file)['api']
    except Exception:
        print('НЕ УДАЛОСЬ ПОЛУЧИТЬ НАСТРОЙКИ ДЛЯ ПОДКЛЮЧЕНИЯ')
        exit(1)

    print(settings)
    # Подключаем токен и long_poll
    try:
        session = VkApi(token=settings['token'], api_version=settings['version'])
        print("Старт сессии")

        api = session.get_api()
        long_poll = VkBotLongPoll(session, group_id=settings['group_id'])
        print("Старт long poll подключения")

        # Слушаем long poll(Сообщения)
        for event in long_poll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:

                if event.message['text'] != '':
                    process_message(api, event.message)

            elif event.type == VkBotEventType.MESSAGE_EVENT:
                process_button(api, event.object)
    except Exception:
        print(f'Возникла ошибка при работе бота. Исключение: {Exception}')

    exit(0)
