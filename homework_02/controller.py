import text_ru
import view
import model
import os

FILE_PATH = 'Telephone_directory.json'


def start():
    phone_book = model.PhoneBook(FILE_PATH)
    is_running = True

    while is_running:
        view.show_main_menu()
        choice = input(text_ru.main_menu_choice)

        if choice == '1':
            file_manager = model.FileManager(FILE_PATH)
            contacts = file_manager.load_contacts()
            print(text_ru.open_file if contacts else text_ru.open_file_error)
        elif choice == '2':
            file_manager = model.FileManager(FILE_PATH)
            contacts = file_manager.load_contacts()
            phone_book.contacts = contacts
            phone_book.get_contact_list()
        elif choice == '3':
            name, phone, comment = view.user_input_contact()
            contact_manager = model.Contact(phone_book)
            contact_manager.create_contact(name, phone, comment)
        elif choice == '4':
            search_query = view.user_input_search()
            phone_book.find_contact(search_query)
        elif choice == '5':
            search_query = view.user_input_search()
            phone_book.find_contact(search_query)
            user_input_id = view.user_input_id()
            contact_to_edit = phone_book.edit_contact(user_input_id)
            view.user_refactor_contact(contact_to_edit)
        elif choice == '6':
            search_query = view.user_input_search()
            phone_book.find_contact(search_query)
            user_input_id = view.user_input_id()
            contact_to_delete = phone_book.delete_contact(user_input_id)
            view.user_delete_contact(contact_to_delete)
        elif choice == '7':
            file_manager = model.FileManager(FILE_PATH)
            file_manager.save_contacts(phone_book.contacts)
        elif choice == '8':
            if view.user_input_out() == 'да':
                file_manager = model.FileManager(FILE_PATH)
                file_manager.save_contacts(phone_book.contacts)
            print(text_ru.phone_exit)
            is_running = False
        else:
            print(text_ru.main_menu_choice_error)
