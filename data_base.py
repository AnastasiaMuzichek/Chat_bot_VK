import sqlite3 as sqlite


NAME_BASE = '../bakery.db'
TABLE_TOKEN = 'Token_table'
TABLE_CATEGORY = 'Bakery_category'
TABLE_BAKERY_MEAT = 'Bakery_meat'
TABLE_BAKERY_VEGETABLE = 'Bakery_vegetables'
TABLE_BAKERY_SWEET = 'Bakery_sweet'

KEYS_AUTH = 'Token, Version_api, Group_id'
KEYS_BAKERY = 'Title, Description, Photo_id'


def get_parameters_from_db(name, var, table_name):
    try:
        connection = sqlite.connect(name)
        print("Успешное подключение к базе данных")
        cursor = connection.cursor()
        print("Успешное получение курсора")
        return send_query(cursor, f"SELECT {var} FROM {table_name};")
    except sqlite.Error:
        print(f'Не удалось подключиться к базе данных и запросить {var} из таблицы {table_name}. Ошибка: {sqlite.Error}')
        return []
    finally:
        if(connection):
            connection.close()
            print('Соединение с базой данных закрыто')


def get_settings_from_db():
    return get_parameters_from_db(NAME_BASE, KEYS_AUTH, TABLE_TOKEN)


def get_categories_from_db():
    return get_parameters_from_db(NAME_BASE, KEYS_BAKERY, TABLE_CATEGORY)


def get_bakery_meat_from_db():
    return get_parameters_from_db(NAME_BASE, KEYS_BAKERY, TABLE_BAKERY_MEAT)


def get_bakery_veg_from_db():
    return get_parameters_from_db(NAME_BASE, KEYS_BAKERY, TABLE_BAKERY_VEGETABLE)


def get_bakery_sweet_from_db():
    return get_parameters_from_db(NAME_BASE, KEYS_BAKERY, TABLE_BAKERY_SWEET)


def send_query(cursor, query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite.Error:
        print('Error from query', sqlite.Error)
        return False


if __name__ == '__main__':
    print('Результат запроса 1:', get_settings_from_db())
    print('Результат запроса 2:', get_categories_from_db())
    print('Результат запроса 3:', get_bakery_meat_from_db())
    print('Результат запроса 4:', get_bakery_veg_from_db())
    print('Результат запроса 5:', get_bakery_sweet_from_db())
