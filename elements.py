from vk.Chat_bot_vk.data_base import get_bakery_veg_from_db, get_categories_from_db, get_bakery_meat_from_db, get_bakery_sweet_from_db


def get_carousel(elements: list):
    return str({"type": "carousel", "elements": elements}).replace('\'', '\"')


def get_carousel_main_menu():
    number = 0
    elements = []
    categories = get_categories_from_db()
    for category in categories:
        number += 1
        element = create_element_carousel(
            category[0],
            category[1],
            [create_callback_button('ОЗНАКОМИТЬСЯ', 'primary', f'menu_button_{number}')],
            category[2]
        )
        elements.append(element)

    return get_carousel(elements)


def get_carousel_meat_menu():
    return get_products_menu(1)


def get_carousel_sweet_menu():
    return get_products_menu(2)


def get_carousel_vegetable_menu():
    return get_products_menu(3)


def get_products_menu(num: int):
    if num == 1:
        items = get_bakery_meat_from_db()
    elif num == 2:
        items = get_bakery_sweet_from_db()
    else:
        items = get_bakery_veg_from_db()

    elements = []

    for item in items:
        element = create_element_carousel(item[0], item[1], get_two_buttons(), item[2])
        elements.append(element)
    return get_carousel(elements)


def get_snack_event(text: str):
    return str({"type": "show_snackbar", "text": text}).replace('\'', '\"')


def get_two_buttons():
    return [
        create_callback_button('ВЫБРАТЬ', 'positive', 'show'),
        create_callback_button('НАЗАД', 'negative', 'back')
    ]


def create_callback_button(label: str, color, user_type: str):
    return {
        "action": {
            "label": label,
            "type": "callback",
            "payload": {
                "type": user_type
            }
        },
        "color": color
    }


def create_element_carousel(title: str, desc: str, buttons: list, photo_id: str):
    return {
        "title": title,
        "description": desc,
        "action": {
            "type": "open_photo"
        },
        "photo_id": photo_id,
        "buttons": buttons
    }


if __name__ == '__main__':
    print('Меню категорий:', get_carousel_main_menu())
    print('Меню мяса', get_carousel_meat_menu())
    print('Сладкое меню', get_carousel_sweet_menu())
    print('Овощное меню', get_carousel_vegetable_menu())
