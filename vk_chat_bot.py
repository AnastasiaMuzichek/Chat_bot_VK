from vk_api import VkApi
from vk.Chat_bot_vk.my_methods import process_message, process_button
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk.Chat_bot_vk.data_base import get_settings_from_db

if __name__ == '__main__':
    # Подключаем токен и long_poll
    settings = get_settings_from_db()
    if not settings:
        print('НЕ УДАЛОСЬ ПОЛУЧИТЬ НАСТРОЙКИ ДЛЯ ПОДКЛЮЧЕНИЯ')
        exit(1)

    try:
        session = VkApi(token=settings[0][0], api_version=settings[0][1])
        print("Старт сессии")

        api = session.get_api()
        long_poll = VkBotLongPoll(session, group_id=settings[0][2])
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
