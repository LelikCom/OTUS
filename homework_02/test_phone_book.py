import pytest
from unittest.mock import patch
from model import PhoneBook


@pytest.fixture
def phone_book():
    """Данные для создания экземпляра PhoneBook с тестовыми данными."""
    pb = PhoneBook("test_contacts.json")
    pb.contacts = [
        {'id': 1, 'name': 'Алиса', 'phone': '1234567890', 'comment': 'Подруга'},
        {'id': 2, 'name': 'Дима', 'phone': '0987654321', 'comment': 'Коллега'}
    ]
    return pb


def test_search_contacts(phone_book):
    """Тестируем поиск контактов."""
    results = phone_book.search_contacts('Алиса')
    assert len(results) == 1
    assert results[0]['name'] == 'Алиса'


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


def test_edit_contact(phone_book):
    """Тестируем редактирование контакта по ID."""
    contact = phone_book.edit_contact(1)
    assert contact['name'] == 'Алиса'


def test_delete_contact(phone_book):
    """Тестируем удаление контакта."""
    contact = phone_book.delete_contact(1)
    assert contact['name'] == 'Алиса'
    assert len(phone_book.contacts) == 1


def test_delete_contact_not_found(phone_book):
    """Тестируем удаление контакта, которого нет в списке."""
    with patch("builtins.print") as mock_print:
        phone_book.delete_contact(99)
        mock_print.assert_called_with("Контакт с указанным ID не найден.")
