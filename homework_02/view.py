import text_ru
from typing import Optional


def show_main_menu():
    """Показать меню"""
    for i, row in enumerate(text_ru.main_menu_items):
        print(f'\t{i}. {row}' if i else row)


def user_input(msg: str) -> str:
    """Запросить у пользователя ввод"""
    return user_input(msg)


def user_input_out() -> str:
    """Запросить у пользователя значение на выход"""
    exit_choice = input(text_ru.main_menu_exit).lower()
    return exit_choice


def user_menu_choice():
    """Запросить у пользователя пункт меню."""
    return user_input(text_ru.main_menu_choice), len(text_ru.main_menu_items)


def user_input_contact() -> tuple[str, str, str]:
    """Запросить у пользователя данные для нового контакта."""
    name = input(text_ru.name_input)
    phone = input(text_ru.phone_input)
    comment = input(text_ru.comment_input)
    return name, phone, comment


def user_input_search() -> str:
    """Запросить у пользователя данные для поиска контакта."""
    search_query = input(text_ru.search_input)
    return search_query


def user_input_id() -> Optional[int]:
    """ Запрашивает у пользователя данные для поиска контакта и возвращает ID как целое число или None."""
    is_running = True
    while is_running:
        contact_id_input = input(text_ru.id_choose).strip()
        if not contact_id_input.isdigit():
            print(text_ru.id_mistake)
            is_running = False
            return None
        is_running = False
        return int(contact_id_input)


def user_refactor_contact(contact_to_edit: dict) -> None:
    """Редактировать контакт с использованием сообщений из модуля."""
    if not contact_to_edit:
        print("")
        return
    contact_to_edit['name'] = (
        input(text_ru.msg_contact_input(text_ru.FIELD_NAME, contact_to_edit['name'])) or contact_to_edit['name']
    )
    contact_to_edit['phone'] = (
        input(text_ru.msg_contact_input(text_ru.FIELD_PHONE, contact_to_edit['phone'])) or contact_to_edit['phone']
    )
    contact_to_edit['comment'] = (
        input(text_ru.msg_contact_input(text_ru.FIELD_COMMENT, contact_to_edit['comment'])) or contact_to_edit['comment']
    )
    print(text_ru.msg_contact_changed(contact_to_edit))


def user_delete_contact(contact: dict) -> None:
    """Отображает сообщение пользователю после удаления контакта."""
    if contact:
        print(text_ru.msg_contact_show(contact))
        print(text_ru.success_deleted)
    else:
        print("")

