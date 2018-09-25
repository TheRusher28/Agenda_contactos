"""
No esta terminado por el momento :D
"""
from time import sleep

ADD_CONTACT = 1
REMOVE_CONTACT = 2
SEARCH_CONTACT = 3
EXPORT_CONTACT = 4
EXIT = 5

MENU_OPTIONS = [ADD_CONTACT, REMOVE_CONTACT, SEARCH_CONTACT, EXPORT_CONTACT]

def show_menu():
    print("1. Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Exportar contactos a un CSV")
    print("5. Salir")

    selected_action = ''

    while not selected_action.isdigit() or (selected_action.isdigit() not in MENU_OPTIONS):
        selected_action = input('¿Qué opcion escoges?')

    return int(selected_action)

def add_contact(contacts):
    print('Añadir contacto')
    contact = [{'name': input('Nombre: ')}, {'phone': input('Telefono: ')}, {'email': input('Email: ')}]
    contacts.append(contact)
    print('Se ha añadido un nuevo contacto')
    sleep(2)

def remove_contact(contacts):
    print('Eliminando')

def search_contact(contacts):
    print('Buscando')

def export_contact(contacts):
    print('Exportando')

def main():
    contacts = []
    action = show_menu()
    while action != EXIT:
        if action == ADD_CONTACT:
            add_contact(contacts)
        elif action == REMOVE_CONTACT:
            remove_contact()
        elif action == SEARCH_CONTACT:
            search_contact()
        elif action == EXPORT_CONTACT:
            export_contact()

        action = show_menu()

    print('Saliendo del programa...')

if __name__ == '__main__':
    main()