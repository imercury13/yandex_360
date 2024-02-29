"""Модуль функций для работы с сотрудниками. Просмотр, создание, изменение и удаление.

.. note::
    **Права доступа для работы с данными сотрудников:**

    **directory:read_users** — просмотр;
    **directory:write_users** — просмотр и изменение.


"""

from jreq.jreq import safe_request
import json

def show_users(token, orgID, url=None):
    """Функция Возвращает список сотрудников с постраничной навигацией

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param url: :term:`Ключи разбивки на страницы`
    :type url: str or None
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/?{url}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('get', url, headers)

def show_user(token, orgID, userID):
    """Функция возвращает информацию об одном сотруднике

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def update_user(token, orgID, userID, body):
    """Функция изменяет информацию о сотруднике.

    .. note::
        Изменяются значения только тех параметров, которые были переданы в запросе.

    .. code-block::
        Test

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('patch', url, headers, json.dumps(body))

def add_user(token, orgID, body):
    """Функция добавляет нового сотрудника

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict
    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}
	
    return safe_request('post', url, headers, json.dumps(body))

def delete_user(token, orgID, userID):
    """Функция удаления пользователя

    .. danger::
        **Данная операция необратима, восстановить данные будет невозможно!**
        
        Будут удалены все почтовые сообщения, а также папки и файлы на Яндекс Диске

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def add_alias_user(token, orgID, userID, body):
    """Функция добавляет сотруднику алиас почтового ящика

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}/aliases'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('post', url, headers, json.dumps(body))

def delete_alias_user(token, orgID, userID, alias):
    """Функция удаляет у сотрудника алиас почтового ящика

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :param alias: альяс
    :type alias: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}/aliases/{alias}'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def update_user_contacts(token, orgID, userID, body):
    """Функция изменяет контактную информацию сотрудника.

    .. note::
        Автоматически созданную контактную информацию (с флагом synthetic) нельзя изменить или удалить

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :param body: тело запроса
    :type body: dict
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}/contacts'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('put', url, headers, json.dumps(body))

def delete_user_contacts(token, orgID, userID):
    """Функция удаляет контактную информацию сотрудника внесенную вручную

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}/contacts'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)


def show_user_2fa(token, orgID, userID):
    """Функция возвращает информацию о статусе 2FA сотрудника

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}/2fa'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('get', url, headers)

def delete_user_2fa(token, orgID, userID):
    """Функция сбрасывает телефон для 2FA у пользователя организации

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}/2fa'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'application/json'}

    return safe_request('delete', url, headers)

def upload_user_avatar(token, orgID, userID, avatar):
    """Функция управляет потретами пользователей организации.
    
    .. note::
        Работает только для пользователей, созданных на домене организации

    :param token: :term:`Яндекс токен приложения`
    :type token: str
    :param orgID: :term:`ID организации в Яндекс 360`
    :type orgID: str
    :param userID: :term:`ID пользователя в Яндекс 360`
    :type userID: str
    :param avatar: данные картинки в binary 
    :type avatar: binary
    :return: результат запроса
    :rtype: dict

    """

    url = f'https://api360.yandex.net/directory/v1/org/{orgID}/users/{userID}/avatar'
    headers={'Authorization': f'OAuth {token}', 'Content-type': 'image/png'}

    return safe_request('put', url, headers, avatar)