def mostrar_mensaje():
    # Lista de mensajes motivacionales
    mensajes = [
        "¡Sigue adelante! ¡El éxito está a tu alcance!",
        "La perseverancia es la clave del éxito.",
        "Nunca es tarde para empezar de nuevo.",
        "Lo único imposible es aquello que no intentas.",
        "Hoy es un buen día para comenzar algo nuevo."
    ]

    print("\nMensajes motivacionales disponibles:\n")

    # Mostrar los mensajes resumidos
    for i, mensaje in enumerate(mensajes, 1):
        print(f"{i}. {mensaje[:20]}...")  # Mostramos los primeros 20 caracteres

    # Solicitar una opción al usuario
    opcion = int(input("\nElige un número (1-5) o 0 para volver al menú: "))

    if opcion == "0":
        print("Regresando al menú principal...")
        return

    # Validamos que la opción sea válida
    if opcion:
        indice = (opcion)
        if 1 <= indice <= len(mensajes):
            print(f"\nMensaje completo: {mensajes[indice - 1]}")
        else:
            print("Número no valido. Elige entre 1 y 5.")
    else:
        print("Volviendo al menú.")

def mostrar_nombres():
    nombres = ["Diana", "Hazel", "Enrique", "Onil", "Chipper"]
    print("\nLista de nombres disponibles:\n")

    for nombre in nombres:
        print(f"- {nombre}")

def mostrar_menu():
    print("\nMenú interactivo:")
    print("1. Mostrar mensaje motivacional")
    print("2. Mostrar lista de nombres")
    print("3. Salir del programa")

def main():
    opciones = {
        "1": mostrar_mensaje,
        "2": mostrar_nombres,
        "3": "salir"
    }

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ").strip()

        # Si se elige la opción "3", mostramos el mensaje de despedida y salimos
        if opcion == "3":
            print("\nGracias por usar el programa. ¡Has salido!")
            break

        # Si se elige una opción válida, ejecutamos la función correspondiente
        accion = opciones.get(opcion)
        if accion == "salir":
            print("\nGracias por usar el programa. ¡Has salido!")
            break
        elif accion:
            try:
                accion()
            except Exception as error:
                print(f"Error inesperado: {error}")
        else:
            print("Opción no válida. Intenta de nuevo.")


main()
