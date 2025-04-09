#quiz Hazel

product_inventory = {
    "producto": "Zapatilas air",
    "talla": 36,
    "color": "Negro",
    "stock": 7
}

#funciona
def show_menu():
    print("\nMenú de opciones:")
    print("1. Modificar un elemento en el diccionario")
    print("2. Eliminar un elemento del diccionario")
    print("3. Mostrar el estado actual del diccionario")
    print("4. Salir")

#aun no funciona correctamente
def modify_item():
    key = input("Ingrese la clave que desea modificar: ")
    if key in product_inventory:
        nuevo_value = input("Ingrese el nuevo valor para '{}': ".format(key))
        if nuevo_value(): 
            product_inventory[key] = (nuevo_value)
            print("Elemento actualizado correctamente.")
    else:
        print("Clave no encontrada en el diccionario.")

#funciona
def delete_item():
    key = input("Ingrese la clave que desea eliminar: ")
    if key in product_inventory:
        del product_inventory[key]
        print("Elemento eliminado correctamente.")
    else:
        print("Clave no encontrada en el diccionario.")

#funciona
def show_dictionary():
    print("\nEstado actual del diccionario:")
    for key, value in product_inventory.items():
        print(f"{key}: {value}")

#funciona        
while True:
    show_menu()
    option = input("Seleccione una opción (1-4): ")
    
    if option == "1":
        modify_item()
    elif option == "2":
        delete_item()
    elif option == "3":
        show_dictionary()
    elif option == "4":
        print("¡Gracias por usar el programa! Hasta pronto.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")