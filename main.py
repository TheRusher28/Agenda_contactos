"""
No esta terminado por el momento :D
"""
ADD_CONTACT = 1
REMOVE_CONTACT = 2
SEARCH_CONTACT = 3
EXPORT_CONTACT = 4
EXIT = 5

def show_menu():
    print("1. Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Exportar contactos a un CSV")
    print("5. Salir")

def main():
    action = show_menu()
    while action != EXIT:
        if action == ADD_CONTACT:
            print("añadir contacto")
        elif action == REMOVE_CONTACT:
            print("eliminar contacto")
        elif action == SEARCH_CONTACT:
            print("buscar contacto")
        elif action == EXPORT_CONTACT:
            print("exportar contactos")

        action = show_menu()

    #Salir del programa

if __name__ == '__main__':
    pass