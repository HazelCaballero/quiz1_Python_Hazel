#solo base, falta para probar
def mostrar_mensaje():
    
    mensajes = [
        "¡Sigue adelante! ¡El éxito está a tu alcance!",
        "La perseverancia es la clave del éxito.",
    ]
    
    print("\nSeleccione el mensaje que desea leer:")
   
    for i, mensaje in enumerate(mensajes, 1):
        
        print(f"{i}. {mensaje[:20]}...")
    

def mostrar_nombres():
    
    nombres = ["Diana", "Hazel", "Enrique", "Onil", "Chipper"]
    print("\nLista de nombres:")
    
    print("\n".join(nombres)) 