import pytest
from unittest.mock import patch, mock_open
from homework_03.model import Contact, FileManager
import json
import view


@pytest.mark.parametrize("name, phone, comment, expected_count", [
    ("Олег", "1122334455", "Друг", 3),
    ("", "", "", 3),
    ("Олег", "", "", 3),
    ("", "1122334455", "", 3),
])
def test_create_contact_parametrized(phone_book, name, phone, comment, expected_count):
    """Тестируем создание контактов с разными входными данными."""
    contact = Contact(phone_book)
    contact.create_contact(name=name, phone=phone, comment=comment)

    assert len(phone_book.contacts) == expected_count
    assert phone_book.contacts[-1]['name'] == name
    assert phone_book.contacts[-1]['phone'] == phone
    assert phone_book.contacts[-1]['comment'] == comment


@pytest.mark.parametrize(
    "search_query, expected_prints",
    [
        ("Алиса", [
            "Найдены следующие контакты:",
            "ID: 1 | Имя: Алиса | Телефон: 1234567890 | Комментарий: Подруга"
        ]),
        ("Дима", [
            "Найдены следующие контакты:",
            "ID: 2 | Имя: Дима | Телефон: 0987654321 | Комментарий: Коллега"
        ]),
        ("", [
            "Найдены следующие контакты:",
            "ID: 1 | Имя: Алиса | Телефон: 1234567890 | Комментарий: Подруга\n"
            "ID: 2 | Имя: Дима | Телефон: 0987654321 | Комментарий: Коллега"
        ]),
        ("Кнопка", [
            "Контакты не найдены"
        ])
    ]
)
def test_find_contact_parametrized(phone_book, search_query, expected_prints):
    """Параметризованный тест для find_contact."""
    with patch("builtins.print") as mock_print:
        phone_book.find_contact(search_query)

        for message in expected_prints:
            mock_print.assert_any_call(message)


@pytest.mark.parametrize("contact_id, expected_messages, expected_count", [
    (1, [
        "ID: 1 | Имя: Алиса | Телефон: 1234567890 | Комментарий: Подруга",
        "Успешно удален!"
    ], 1),
    (99, [
        "Контакт с указанным ID не найден."
    ], 2),
])
def test_delete_contact_parametrized(phone_book, contact_id, expected_messages, expected_count):
    """Тестируем удаление контактов с разными ID."""
    with patch("builtins.print") as mock_print:
        contact_to_delete = phone_book.delete_contact(contact_id)

        view.user_delete_contact(contact_to_delete)

        for message in expected_messages:
            print(f"Ожидаемое сообщение: {message}")
            print(f"Фактические вызовы print: {mock_print.mock_calls}")
            mock_print.assert_any_call(message)

        assert len(phone_book.contacts) == expected_count


def test_open_file():
    """Тестируем открытие файла с контактами через FileManager."""
    test_data = [
        {'id': 1, 'name': 'Алиса', 'phone': '1234567890', 'comment': 'Подруга'},
        {'id': 2, 'name': 'Дима', 'phone': '0987654321', 'comment': 'Коллега'}
    ]
    file_manager = FileManager("test_contacts.json")
    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))), \
         patch("os.path.exists", return_value=True):
        contacts = file_manager.open_file()
    assert len(contacts) == 2
    assert contacts[0]['name'] == 'Алиса'
    assert contacts[1]['phone'] == '0987654321'


def test_save_contacts():
    """Тестируем сохранение контактов через FileManager."""
    test_data = [
        {'id': 1, 'name': 'Алиса', 'phone': '1234567890', 'comment': 'Подруга'},
        {'id': 2, 'name': 'Дима', 'phone': '0987654321', 'comment': 'Коллега'}
    ]

    file_manager = FileManager("test_contacts.json")

    with patch("builtins.open", mock_open()) as mocked_open:
        file_manager.save_contacts(test_data)
        mocked_open.assert_called_once_with("test_contacts.json", "w", encoding="utf-8")
        handle = mocked_open()
        written_data = "".join(call.args[0] for call in handle.write.mock_calls)
        assert json.loads(written_data) == test_data


def test_save_contacts_with_error():
    """Тестируем поведение при ошибке сохранения контактов."""
    test_data = [
        {'id': 1, 'name': 'Алиса', 'phone': '1234567890', 'comment': 'Подруга'}
    ]

    file_manager = FileManager("test_contacts.json")

    with patch("builtins.open", side_effect=PermissionError):
        with patch("builtins.print") as mock_print:
            file_manager.save_contacts(test_data)

            mock_print.assert_called_with(
                f"Контакты не сохранены в файл 'test_contacts.json'. Ошибка: "
            )


def test_get_next_id(phone_book):
    """Тестируем получение следующего ID."""
    contact = Contact(phone_book)
    assert contact.get_next_id() == 3
    phone_book.contacts.pop(0)
    assert contact.get_next_id() == 1


def test_find_contact(phone_book):
    """Тестируем нахождение контакта по поисковому запросу."""
    with patch("builtins.print") as mock_print:
        phone_book.find_contact('Дима')
        mock_print.assert_called_with("ID: 2 | Имя: Дима | Телефон: 0987654321 | Комментарий: Коллега")


def test_find_contact_not_found(phone_book):
    """Тестируем ситуацию, когда контакт не найден."""
    with patch("builtins.print") as mock_print:
        phone_book.find_contact('Кнопка')
        mock_print.assert_called_with("Контакты не найдены")


@pytest.mark.parametrize("contact_id, new_data, expected_output, expected_contact", [
    (
        1,
        {'name': 'Иван', 'phone': '5555555555', 'comment': 'Друг'},
        ["Контакт найден: ID 1"],
        {'id': 1, 'name': 'Иван', 'phone': '5555555555', 'comment': 'Друг'}
    ),
    (
        99,
        None,
        ["Контакт с указанным ID не найден."],
        None
    )
])
def test_edit_contact_parametrized(phone_book, contact_id, new_data, expected_output, expected_contact):
    """Тестируем редактирование контактов с разными ID и новыми данными."""
    with patch("builtins.print") as mock_print:
        contact_to_edit = phone_book.edit_contact(contact_id)

        for message in expected_output:
            mock_print.assert_any_call(message)

        if contact_to_edit:
            contact_to_edit.update(new_data)

            assert contact_to_edit['name'] == new_data['name']
            assert contact_to_edit['phone'] == new_data['phone']
            assert contact_to_edit['comment'] == new_data['comment']

            updated_contact = next(c for c in phone_book.contacts if c['id'] == contact_id)
            assert updated_contact == expected_contact
        else:
            assert contact_to_edit is None
