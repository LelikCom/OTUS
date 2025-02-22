from typing import Union, List, Dict


FIELD_NAME = "имя"
FIELD_PHONE = "телефон"
FIELD_COMMENT = "комментарий"

main_menu_items = [
    "Телефонный справочник:",
    "Открыть файл (Telephone_directory.json)",
    "Показать все контакты",
    "Создать контакт",
    "Найти контакт",
    "Изменить контакт",
    "Удалить контакт",
    "Сохранить файл",
    "Выход",
]


main_menu_choice = f"Выберите действие (1-{len(main_menu_items)-1}): "
main_menu_choice_error = f"Неверный ввод, нужна цифра (1-{len(main_menu_items)-1})."
main_menu_exit = "Вы хотите сохранить изменения перед выходом? (да/нет): "

open_file = "Файл успешно открыт"

open_file_error = "Файл пуст или не найден"


phone_exit = "Выход из программы."

phone_book_zero = "Контакты не найдены"
no_input = "Вы ничего не ввели"

name_input = "Введите имя: "
phone_input = "Введите телефон: "
comment_input = "Введите комментарий: "
search_input = "Введите имя, телефон или комментарий для поиска: "
found_contact = "Найдены следующие контакты:"
id_choose = "Введите ID контакта, который хотите изменить: "
id_mistake = "Ошибка: ID должен быть числом."
contact_changed = "Контакт успешно изменён!"
no_id_in_contacts = "Контакт с указанным ID не найден."
success_deleted = "Успешно удален!"
zero_param = "Пусто"


def msg_contact_show(contact: Union[Dict, List[Dict]]) -> str:
    """Форматирует информацию о контакте или списке контактов для отображения."""
    if isinstance(contact, list):
        return "\n".join(
            f"ID: {c['id']} | Имя: {c['name']} | Телефон: {c['phone']} | Комментарий: {c['comment']}"
            for c in contact
        )
    elif isinstance(contact, dict):
        return f"ID: {contact['id']} | Имя: {contact['name']} | Телефон: {contact['phone']} | Комментарий: {contact['comment']}"
    else:
        return phone_book_zero


def msg_contact_create(name: str, phone: str, comment: str) -> str:
    """Генерирует сообщение о создании контакта с учетом пустых значений."""
    name = name if name else zero_param
    phone = phone if phone else zero_param
    comment = comment if comment else zero_param
    if name == zero_param and phone == zero_param and comment == zero_param:
        return "Пустой контакт создан!"
    return f"Контакт {name} | {phone} | {comment} успешно создан!"


# text_ru.py


def json_decode_error(file_path: str) -> str:
    return f"Ошибка: файл '{file_path}' содержит некорректный JSON."


def file_not_found_error(file_path: str) -> str:
    return f"Ошибка: файл '{file_path}' не найден."


def permission_error(file_path: str) -> str:
    return f"Ошибка: нет прав на чтение файла '{file_path}'."


def msg_contact_edit(contact_to_edit: dict) -> str:
    if contact_to_edit:
        return f"Контакт найден: ID {contact_to_edit['id']}"


def msg_contact_not_found(contact_to_edit: dict) -> str:
    if contact_to_edit:
        return f"Контакт c ID {contact_to_edit['id']} не найден"


def msg_contact_input(field: str, current_value: str) -> str:
    """Генерирует приглашение для ввода нового значения для указанного поля."""
    return f"Новое {field} (текущее: {current_value}): "


def msg_contact_changed(contact_to_edit: dict) -> str:
    """Возвращает сообщение об успешном изменении контакта, используя константы."""
    return (
        f"Контакт успешно изменён!\n"
        f"ID: {contact_to_edit['id']} | {FIELD_NAME.capitalize()}: {contact_to_edit['name']} | "
        f"{FIELD_PHONE.capitalize()}: {contact_to_edit['phone']} | "
        f"{FIELD_COMMENT.capitalize()}: {contact_to_edit['comment']}"
    )


def file_save(file_path: str) -> str:
    """Сообщение об успешном сохранении файла."""
    return f"Контакты успешно сохранены в файл: {file_path}."


def file_not_save(file_path: str, error: Exception) -> str:
    """Сообщение об ошибке сохранения файла."""
    return f"Контакты не сохранены в файл '{file_path}'. Ошибка: {error}"
