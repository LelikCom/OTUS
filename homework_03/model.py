from typing import List, Dict, Any, Optional
import os
import json
from homework_03 import text_ru


def validate_user_input(user_date: str, len_menu: int) -> bool:
    return user_date.isdigit() and (0 < int(user_date) <= len_menu)


class PhoneBook:
    def __init__(self, file_path: str):
        self.contacts: list[dict] = []
        self.file_path = file_path

    def get_contact_list(self) -> None:
        """Преобразовать список контактов в формат для печати и вывести на экран."""
        if not self.contacts:
            print(text_ru.phone_book_zero)
        else:
            for contact in self.contacts:
                print(text_ru.msg_contact_show(contact))

    def search_contacts(self, query: str) -> List[Dict[str, Any]]:
        """Ищет контакты по имени, телефону или комментарию и возвращает список найденных контактов."""
        query = query.lower()
        return [
            contact
            for contact in self.contacts
            if query in contact["name"].lower()
            or query in contact["phone"]
            or query in contact["comment"].lower()
        ]

    def find_contact(self, search_query: str) -> None:
        """Находит и выводит контакт(ы) по имени, телефону или комментарию."""
        results = self.search_contacts(search_query)
        if results:
            print(text_ru.found_contact)
            print(text_ru.msg_contact_show(results))
        else:
            print(text_ru.phone_book_zero)

    def edit_contact(self, contact_id: int) -> Optional[dict]:
        """Ищет контакт по ID и возвращает его для редактирования."""
        contact_to_edit = next(
            (contact for contact in self.contacts if contact["id"] == contact_id), None
        )
        if contact_to_edit:
            print(text_ru.msg_contact_edit(contact_to_edit))
            return contact_to_edit
        else:
            print(text_ru.no_id_in_contacts)
            return None

    def delete_contact(self, contact_id: int) -> Optional[dict]:
        """Удаляет контакт по-указанному ID."""
        contact_to_delete = next(
            (contact for contact in self.contacts if contact["id"] == contact_id), None
        )
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            return contact_to_delete
        else:
            print(text_ru.no_id_in_contacts)
            return None


class FileManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.contacts: list[dict] = []

    """Класс для работы с файлами."""

    def open_file(self) -> list[dict]:
        """Открыть файл и вернуть его содержимое."""
        if not os.path.exists(self.file_path):
            print(text_ru.file_not_found_error(self.file_path))
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)  # Попытка загрузить JSON
        except json.JSONDecodeError:
            print(text_ru.json_decode_error(self.file_path))
            return []
        except FileNotFoundError:
            print(text_ru.file_not_found_error(self.file_path))
            return []
        except PermissionError:
            print(text_ru.permission_error(self.file_path))
            return []

    def load_contacts(self) -> list[dict]:
        """Загрузить контакты из файла в атрибут `self.contacts`."""
        self.contacts = self.open_file()
        return self.contacts

    def save_contacts(self, contacts: list[dict]) -> None:
        """Сохранить контакты в файл."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(contacts, file, indent=4, ensure_ascii=False)
            print(text_ru.file_save(self.file_path))
        except Exception as e:
            print(text_ru.file_not_save(self.file_path, e))


class Contact:
    """Класс для представления контакта."""

    def __init__(self, phone_book: PhoneBook):
        """Инициализация класса Contact с привязкой к экземпляру PhoneBook."""
        self.phone_book = phone_book

    def get_next_id(self) -> int:
        """Вернуть следующий доступный ID для нового контакта."""
        existing_ids = {contact["id"] for contact in self.phone_book.contacts}
        next_id = 1
        while next_id in existing_ids:
            next_id += 1
        return next_id

    def create_contact(self, name: str, phone: str, comment: str) -> None:
        """Создать новый контакт и добавить его в список контактов."""
        new_id = self.get_next_id()

        self.phone_book.contacts.append(
            {"id": new_id, "name": name, "phone": phone, "comment": comment}
        )
        print(text_ru.msg_contact_create(name, phone, comment))
