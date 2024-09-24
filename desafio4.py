# Definimos los niveles y los puntos correspondientes
niveles = ["Fácil", "Medio", "Difícil", "Experto"]
puntos_por_nivel = {"Fácil": 10, "Medio": 20, "Difícil": 30, "Experto": 50}

# Diccionario para almacenar los jugadores y sus puntuaciones
jugadores = {}

def obtener_puntos_adicionales(nivel, tiempo):
    """Determina si se otorgan puntos adicionales basados en el nivel y tiempo."""
    if nivel in ["Difícil", "Experto"] and tiempo <= 30:
        return 10  # Puntos extra por completar niveles difíciles rápidamente
    return 0

def actualizar_puntuacion(jugador, nivel, tiempo):
    """Actualiza la puntuación del jugador basado en el nivel y tiempo."""
    puntos = puntos_por_nivel[nivel]
    puntos_extra = obtener_puntos_adicionales(nivel, tiempo)
    puntos_totales = puntos + puntos_extra
    
    if jugador in jugadores:
        jugadores[jugador] += puntos_totales
    else:
        jugadores[jugador] = puntos_totales

def mostrar_lideres():
    """Muestra al líder actual del juego y maneja empates."""
    if jugadores:
        max_puntos = max(jugadores.values())
        lideres = [jugador for jugador, puntos in jugadores.items() if puntos == max_puntos]
        print("Líder(es) actual(es):")
        for lider in lideres:
            print(f"{lider}: {jugadores[lider]} puntos")
    else:
        print("No hay jugadores registrados.")

def mostrar_puntuaciones():
    """Muestra las puntuaciones actuales de todos los jugadores."""
    if jugadores:
        print("Puntuaciones actuales:")
        for jugador, puntos in jugadores.items():
            print(f"{jugador}: {puntos} puntos")
    else:
        print("No hay puntuaciones para mostrar.")

def main():
    """Función principal que gestiona el flujo del juego y las interacciones con el usuario."""
    while True:
        print("\nSistema de Puntuación Interactivo")
        print("1. Registrar ronda de juego")
        print("2. Mostrar líderes")
        print("3. Mostrar puntuaciones")
        print("4. Salir")
        
        opcion = input("Elija una opción (1-4): ")
        
        if opcion == "1":
            nombre_jugador = input("Ingrese el nombre del jugador: ").strip()
            nivel_completado = input("Ingrese el nivel completado (Fácil, Medio, Difícil, Experto): ").strip()
            
            if nivel_completado not in niveles:
                print("Nivel no válido. Intente nuevamente.")
                continue
            
            tiempo_str = input("Ingrese el tiempo en segundos que tardó en completar el nivel: ").strip()
            try:
                tiempo = float(tiempo_str)
                if tiempo <= 0:
                    print("El tiempo debe ser un número positivo. Intente nuevamente.")
                    continue
            except ValueError:
                print("El tiempo debe ser un número válido. Intente nuevamente.")
                continue
            
            actualizar_puntuacion(nombre_jugador, nivel_completado, tiempo)
            print(f"Puntuación actualizada para {nombre_jugador}.")
        
        elif opcion == "2":
            mostrar_lideres()
        
        elif opcion == "3":
            mostrar_puntuaciones()
        
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 4.")

if __name__ == "__main__":
    main()
