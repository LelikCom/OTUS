import json
import os

# Путь к файлу справочника
FILE_PATH = 'Telephone_directory.json'

# Открыть файл
def open_file():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Сохранение контактов в файл
def save_contacts(contacts):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)

# Показать все контакты
def show_contacts(contacts):
    if not contacts:
        print("Справочник пуст.")
    else:
        for contact in contacts:
            print(
                f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact['comment']}")

# Найти первый свободный ID
def get_next_id(contacts):
    if not contacts:
        return 1
    existing_ids = sorted(contact['id'] for contact in contacts)
    for i in range(1, existing_ids[-1] + 1):
        if i not in existing_ids:
            return i
    return existing_ids[-1] + 1

# Создать контакт
def create_contact(contacts):
    new_id = get_next_id(contacts)
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    comment = input("Введите комментарий: ")
    if not name:
        choice = input("Вы не ввели имя. Хотите оставить поле пустым? (да/нет): ").lower()
        if choice == 'нет':
            name = input("Введите имя: ")
    if not phone:
        choice = input("Вы не ввели телефон. Хотите оставить поле пустым? (да/нет): ").lower()
        if choice == 'нет':
            phone = input("Введите телефон: ")
    if not comment:
        choice = input("Вы не ввели комментарий. Хотите оставить поле пустым? (да/нет): ").lower()
        if choice == 'нет':
            comment = input("Введите комментарий: ")
    contacts.append({
        'id': new_id,
        'name': name,
        'phone': phone,
        'comment': comment
    })
    print(f"Контакт {name} успешно создан!")

# Найти контакт
def find_contact(contacts):
    search = input("Введите имя, телефон или комментарий для поиска: ").lower()
    results = [contact for contact in contacts if
               search in str(contact['name']).lower() or search in str(contact['phone']) or search in str(contact['comment']).lower()]
    if results:
        for contact in results:
            print(
                f"Найден контакт - ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact['comment']}")
    else:
        print("Контакт не найден.")

# Изменить контакт
def edit_contact(contacts):
    contact_id = int(input("Введите ID контакта для редактирования: "))
    contact = next((contact for contact in contacts if contact['id'] == contact_id), None)
    if contact:
        contact['name'] = input(f"Новое имя (текущие: {contact['name']}): ") or contact['name']
        contact['phone'] = input(f"Новый телефон (текущие: {contact['phone']}): ") or contact['phone']
        contact['comment'] = input(f"Новый комментарий (текущие: {contact['comment']}): ") or contact['comment']
        print("Контакт успешно изменён!")
    else:
        print("Контакт не найден.")

# Удалить контакт
def delete_contact(contacts):
    while True:
        contact_id_input = input("Введите ID контакта для удаления: ")
        if not contact_id_input.isdigit():
            print("Ошибка: ID должен быть числом. Попробуйте снова.")
            continue
        contact_id = int(contact_id_input)
        contact = next((contact for contact in contacts if contact['id'] == contact_id), None)
        if contact:
            confirm = input(f"Вы точно хотите удалить контакт с ID {contact_id} (да/нет)? ").lower()
            if confirm == 'да':
                contacts.remove(contact)
                print(f"Контакт с ID {contact_id} успешно удалён!")
            else:
                print("Удаление отменено.")
            break
        else:
            print(f"Контакт с ID {contact_id} не найден. Попробуйте снова.")

# Главное меню
def main_menu():
    contacts = []

    while True:
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
            if contacts:
                print("Файл успешно открыт!")
            else:
                print("Файл пуст или не найден.")
        elif choice == '2':
            if not contacts:
                print("Контакты не загружены. Открываем файл...")
                contacts = open_file()
            show_contacts(contacts)
        elif choice == '3':
            if not contacts:
                print("Контакты не загружены. Открываем файл...")
                contacts = open_file()
            create_contact(contacts)
        elif choice == '4':
            if not contacts:
                print("Контакты не загружены. Открываем файл...")
                contacts = open_file()
            find_contact(contacts)
        elif choice == '5':
            if not contacts:
                print("Контакты не загружены. Открываем файл...")
                contacts = open_file()
            edit_contact(contacts)
        elif choice == '6':
            if not contacts:
                print("Контакты не загружены. Открываем файл...")
                contacts = open_file()
            delete_contact(contacts)
        elif choice == '7':
            if contacts:
                save_contacts(contacts)
                print("Файл успешно сохранён!")
            else:
                print("Нет контактов для сохранения.")
        elif choice == '8':
            if contacts:
                if input("Вы хотите сохранить изменения перед выходом? (да/нет): ").lower() == 'да':
                    save_contacts(contacts)
                    print("Изменения сохранены.")
                    print("Выход из программы.")
            else:
                print('Данных для изменения нет. Выход из программы.')
            break
        else:
            print("Неверный ввод, нужна цифра (1-8).")

if __name__ == '__main__':
    main_menu()
