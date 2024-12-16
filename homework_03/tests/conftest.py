import pytest
from model import PhoneBook


@pytest.fixture
def phone_book():
    """Фикстура для тестовой книги контактов."""
    pb = PhoneBook("test_contacts.json")
    pb.contacts = [
        {'id': 1, 'name': 'Алиса', 'phone': '1234567890', 'comment': 'Подруга'},
        {'id': 2, 'name': 'Дима', 'phone': '0987654321', 'comment': 'Коллега'}
    ]
    return pb
