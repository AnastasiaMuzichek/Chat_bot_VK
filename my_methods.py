from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk.Chat_bot_VK.elements import get_snack_event, get_carousel_main_menu
from vk.Chat_bot_VK.elements import get_carousel_meat_menu, get_carousel_vegetable_menu, get_carousel_sweet_menu
from traceback import print_exc


def send_carousel(api, peer, message, carousel):
    try:
        api.messages.send(peer_id=peer, message=message, random_id=get_random_id(), template=carousel)
    except Exception:
        print(f'При отправке карусели возникло исключение: {Exception}')
        print_exc()


def send_keyboard(vk, peer, message):
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_callback_button(label='Some button', color=VkKeyboardColor.POSITIVE, payload={})
    vk.messages.send(peer_id=peer, message=message, random_id=get_random_id(), keyboard=keyboard.get_keyboard())


def send_answer(api, peer, message):
    try:
        api.messages.send(peer_id=peer, message=message, random_id=get_random_id())
    except Exception:
        print(f'При отправке сообщения возникло исключение: {Exception}')
        print_exc()


def send_answer_on_event(api, message):
    try:
        api.messages.sendMessageEventAnswer(
            event_id=message.event_id,
            user_id=message.user_id,
            peer_id=message.peer_id,
            event_data=get_snack_event("Ваш продукт добавлен в заказ:)")
        )
    except Exception:
        print(f'При попытке отправки сообщения на события возникло исключение: {Exception}')
        print_exc()


def replacement_menu(api, peer, message_id, carousel):
    try:
        print(carousel)
        api.messages.edit(peer_id=peer, conversation_message_id=message_id, template=carousel, message='Вот твоё меню')
    except Exception:
        print('При попытке отредактировать сообщение возникло исключение: ', Exception)
        print_exc()


def process_message(api, message):
    text = message['text'].lower()
    peer_id = message['peer_id']

    if text == 'привет':
        send_answer(api, peer_id, 'Привет, я Бот!')
    elif text == 'как дела?':
        send_answer(api, peer_id, 'Хорошо, а твои как?')
    elif text == 'меню':
        send_carousel(api, peer_id, 'Вот наше меню!', get_carousel_main_menu())
    else:
        send_answer(api, peer_id, 'Я вас не понимаю! :(')


def process_button(api, message):
    my_type = message.payload['type']
    peer_id = message['peer_id']
    message_id = message.conversation_message_id

    if my_type == 'menu_button_1':
        replacement_menu(api, peer_id, message_id, get_carousel_meat_menu())
    elif my_type == 'menu_button_2':
        replacement_menu(api, peer_id, message_id, get_carousel_vegetable_menu())
    elif my_type == 'menu_button_3':
        replacement_menu(api, peer_id, message_id, get_carousel_sweet_menu())
    elif my_type == 'back':
        replacement_menu(api, peer_id, message_id, get_carousel_main_menu())
    elif my_type == 'show':
        send_answer_on_event(api, message)
