import json
import os
from typing import List, Dict, Any

FILE_PATH = 'Telephone_directory.json'


def open_file() -> List[Dict[str, Any]]:
    """Открыть файл справочника и вернуть список контактов. Если файла нет, возвращается пустой список."""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_contacts(contacts: List[Dict[str, Any]]) -> None:
    """Сохранить контакты в файл."""
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)


def show_contacts(contacts: List[Dict[str, Any]]) -> None:
    """Вывести все контакты на экран."""
    if not contacts:
        print("Справочник пуст.")
    else:
        for contact in contacts:
            print(
                f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, "
                f"Комментарий: {contact['comment']}"
            )


def get_next_id(contacts: List[Dict[str, Any]]) -> int:
    """Вернуть следующий доступный ID для нового контакта."""
    if not contacts:
        return 1
    existing_ids = sorted(contact['id'] for contact in contacts)
    for i in range(1, existing_ids[-1] + 1):
        if i not in existing_ids:
            return i
    return existing_ids[-1] + 1


def create_contact(contacts: List[Dict[str, Any]]) -> None:
    """Создать новый контакт и добавить его в список контактов."""
    new_id = get_next_id(contacts)
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    comment = input("Введите комментарий: ")

    if not name:
        name = input("Вы не ввели имя. Повторите ввод имени: ")
    if not phone:
        phone = input("Вы не ввели телефон. Повторите ввод телефона: ")
    if not comment:
        comment = input("Вы не ввели комментарий. Повторите ввод комментария: ")

    contacts.append({
        'id': new_id,
        'name': name,
        'phone': phone,
        'comment': comment
    })
    print(f"Контакт {name} успешно создан!")


def search_contacts(contacts: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    """Ищет контакты по имени, телефону или комментарию и возвращает список найденных контактов."""
    query = query.lower()
    return [
        contact for contact in contacts
        if query in contact['name'].lower() or query in contact['phone'] or query in contact['comment'].lower()
    ]


def find_contact(contacts: List[Dict[str, Any]]) -> None:
    """Находит и выводит контакт(ы) по имени, телефону или комментарию."""
    search_query = input("Введите имя, телефон или комментарий для поиска: ")
    results = search_contacts(contacts, search_query)

    if results:
        print("Найдены следующие контакты:")
        for contact in results:
            print(
                f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, "
                f"Комментарий: {contact['comment']}"
            )
    else:
        print("Контакт не найден.")


def edit_contact(contacts: List[Dict[str, Any]]) -> None:
    """Редактировать контакт после поиска и выбора ID."""
    search_query = input("Введите имя, телефон или комментарий для поиска контакта для редактирования: ")
    results = search_contacts(contacts, search_query)

    if results:
        print("Найдены следующие контакты:")
        for contact in results:
            print(
                f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, "
                f"Комментарий: {contact['comment']}"
            )

        contact_id_input = input("Введите ID контакта, который хотите изменить: ")
        if not contact_id_input.isdigit():
            print("Ошибка: ID должен быть числом.")
            return

        contact_id = int(contact_id_input)
        contact_to_edit = next((contact for contact in contacts if contact['id'] == contact_id), None)

        if contact_to_edit:
            contact_to_edit['name'] = input(f"Новое имя (текущие: {contact_to_edit['name']}): ") or contact_to_edit['name']
            contact_to_edit['phone'] = input(f"Новый телефон (текущие: {contact_to_edit['phone']}): ") or contact_to_edit['phone']
            contact_to_edit['comment'] = input(f"Новый комментарий (текущие: {contact_to_edit['comment']}): ") or contact_to_edit['comment']
            print("Контакт успешно изменён!")
        else:
            print("Контакт с указанным ID не найден.")
    else:
        print("Контакт для редактирования не найден.")


def delete_contact(contacts: List[Dict[str, Any]]) -> None:
    """Удалить контакт после поиска и выбора ID."""
    search_query = input("Введите имя, телефон или комментарий для поиска контакта для удаления: ")
    results = search_contacts(contacts, search_query)

    if results:
        print("Найдены следующие контакты:")
        for contact in results:
            print(
                f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, "
                f"Комментарий: {contact['comment']}"
            )

        contact_id_input = input("Введите ID контакта, который хотите удалить: ")
        if not contact_id_input.isdigit():
            print("Ошибка: ID должен быть числом.")
            return

        contact_id = int(contact_id_input)
        contact_to_delete = next((contact for contact in contacts if contact['id'] == contact_id), None)

        if contact_to_delete:
            confirm = input(f"Вы точно хотите удалить контакт с ID {contact_id} (да/нет)? ").lower()
            if confirm == 'да':
                contacts.remove(contact_to_delete)
                print(f"Контакт с ID {contact_id} успешно удалён!")
            else:
                print("Удаление отменено.")
        else:
            print("Контакт с указанным ID не найден.")
    else:
        print("Контакт для удаления не найден.")


def main_menu() -> None:
    """Главное меню программы."""
    contacts = open_file()
    is_running = True

    while is_running:
        print("\nТелефонный справочник:")
        print("1. Открыть файл (Telephone_directory.json)")
        print("2. Показать все контакты")
        print("3. Создать контакт")
        print("4. Найти контакт")
        print("5. Изменить контакт")
        print("6. Удалить контакт")
        print("7. Сохранить файл")
        print("8. Выход")

        choice = input("Выберите действие (1-8): ")

        if choice == '1':
            contacts = open_file()
            print("Файл успешно открыт!" if contacts else "Файл пуст или не найден.")
        elif choice == '2':
            show_contacts(contacts)
        elif choice == '3':
            create_contact(contacts)
        elif choice == '4':
            find_contact(contacts)
        elif choice == '5':
            edit_contact(contacts)
        elif choice == '6':
            delete_contact(contacts)
        elif choice == '7':
            save_contacts(contacts)
            print("Файл успешно сохранён!")
        elif choice == '8':
            if input("Вы хотите сохранить изменения перед выходом? (да/нет): ").lower() == 'да':
                save_contacts(contacts)
                print("Изменения сохранены.")
            print("Выход из программы.")
            is_running = False
        else:
            print("Неверный ввод, нужна цифра (1-8).")


if __name__ == '__main__':
    main_menu()
