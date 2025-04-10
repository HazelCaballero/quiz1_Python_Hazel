# Este es un diccionario que almacena información sobre un producto
product_inventory = {
    "producto": "Zapatillas air",  # La clave "producto" tiene el valor "Zapatillas air"
    "talla": 36,                   # La clave "talla" tiene el valor 36 
    "color": "Morado",              # La clave "color" tiene el valor "Morado" 
    "stock": 7                     # La clave "stock" tiene el valor 7 
}

# Función que muestra un menú de opciones para que el usuario elija lo que desea hacer
def show_menu():
    print("\nMenú de opciones:")
    print("1. Modificar un elemento en el diccionario")  
    print("2. Eliminar un elemento del diccionario")    
    print("3. Mostrar el estado actual del diccionario") 
    print("4. Salir")  

# Función que permite al usuario modificar un valor en el diccionario
def modify_item():
    # Pedimos al usuario que ingrese la clave
    key = input("Ingrese la clave que desea modificar: ")
    # Verificamos si la clave ingresada existe en el diccionario
    if key in product_inventory:
        # Si existe, pedimos al usuario que ingrese el nuevo valor para esa clave
        new_value = input("Ingrese el nuevo valor para '{}': ".format(key))
        
        if new_value: 
            product_inventory[key] = new_value  # Actualizamos el valor 
            print("Elemento actualizado correctamente.")  # Confirmamos que la modificación se realizó
        else:
            print("El valor no puede estar vacío.")  # Si el valor está vacío, mostramos un error
    else:
        if product_inventory.get(key):  # El metodo get() devuelve None si la clave no existe
            new_value = input("Ingrese el nuevo valor para '{}': ".format(key))
            if new_value:
                product_inventory[key] = new_value
                print("Elemento actualizado correctamente.")
        else:
            print("Clave no encontrada en el diccionario.")

# Función que permite al usuario eliminar un elemento del diccionario
def delete_item():
    # Pedimos al usuario que ingrese la clave del elemento que desea eliminar
    key = input("Ingrese la clave que desea eliminar: ")
    # Verificamos si la clave existe en el diccionario
    if key in product_inventory:
        removed_value = product_inventory.pop(key)  # Esto eliminará el elemento y devolverá el valor 
        #(lo practique primero con del y ahora con pop)
        print(f"Elemento '{key}' con valor '{removed_value}' eliminado correctamente.")        
    else:
        # Si la clave no existe en el diccionario, mostramos un mensaje indicando que no se encontró
        print("Clave no encontrada en el diccionario.")

# Función que muestra el estado actual del diccionario
def show_dictionary():
    print("\nEstado actual del diccionario:")
    # Recorremos todas las claves y valores del diccionario
    for key, value in product_inventory.items():
        # Mostramos la clave y su valor asociado en el diccionario
        print(f"{key}: {value}")
    
# Este es el bucle principal del programa. Se ejecuta continuamente hasta que el usuario decida salir
while True:
    show_menu() 
    # Pedimos al usuario que seleccione una opción del menú
    option = input("Seleccione una opción (1-4): ")
    
    menu_options = {
        "1": modify_item,
        "2": delete_item,
        "3": show_dictionary,
        "4": exit
    }

    try:
        # Si la opción está en el diccionario de opciones, ejecutamos la función asociada y si no manejamos el error
        menu_options.get(option, lambda: print("Opción no válida. Intente nuevamente."))()
    except ValueError:
        print("Opción no válida. Intente nuevamente.")