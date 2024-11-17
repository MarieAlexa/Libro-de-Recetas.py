import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('recetario.db')
cursor = conn.cursor()

# Crear tabla de recetas si no existe
def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            ingredientes TEXT NOT NULL,
            pasos TEXT NOT NULL
        )
    ''')
    conn.commit()

# Agregar una nueva receta
def agregar_receta(nombre, ingredientes, pasos):
    try:
        cursor.execute('INSERT INTO recetas (nombre, ingredientes, pasos) VALUES (?, ?, ?)',
                       (nombre, ingredientes, pasos))
        conn.commit()
        print("Receta agregada con éxito.")
    except sqlite3.IntegrityError:
        print("Error: Ya existe una receta con ese nombre.")

# Actualizar una receta existente
def actualizar_receta(nombre, nuevos_ingredientes, nuevos_pasos):
    cursor.execute('UPDATE recetas SET ingredientes = ?, pasos = ? WHERE nombre = ?',
                   (nuevos_ingredientes, nuevos_pasos, nombre))
    if cursor.rowcount > 0:
        conn.commit()
        print("Receta actualizada con éxito.")
    else:
        print("Error: No se encontró una receta con ese nombre.")

# Eliminar una receta
def eliminar_receta(nombre):
    cursor.execute('DELETE FROM recetas WHERE nombre = ?', (nombre,))
    if cursor.rowcount > 0:
        conn.commit()
        print("Receta eliminada con éxito.")
    else:
        print("Error: No se encontró una receta con ese nombre.")

# Ver el listado de recetas
def ver_recetas():
    cursor.execute('SELECT nombre FROM recetas')
    recetas = cursor.fetchall()
    if recetas:
        print("Listado de recetas:")
        for receta in recetas:
            print(f"- {receta[0]}")
    else:
        print("No hay recetas disponibles.")

# Buscar una receta por nombre
def buscar_receta(nombre):
    cursor.execute('SELECT ingredientes, pasos FROM recetas WHERE nombre = ?', (nombre,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"\nIngredientes:\n{resultado[0]}\n")
        print(f"Pasos:\n{resultado[1]}\n")
    else:
        print("Error: No se encontró una receta con ese nombre.")

# Menú principal
def menu():
    crear_tablas()
    while True:
        print("\n--- Libro de Recetas ---")
        print("1. Agregar nueva receta")
        print("2. Actualizar receta existente")
        print("3. Eliminar receta existente")
        print("4. Ver listado de recetas")
        print("5. Buscar ingredientes y pasos de receta")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre de la receta: ")
            ingredientes = input("Ingredientes (separados por comas): ")
            pasos = input("Pasos: ")
            agregar_receta(nombre, ingredientes, pasos)
        elif opcion == '2':
            nombre = input("Nombre de la receta a actualizar: ")
            nuevos_ingredientes = input("Nuevos ingredientes (separados por comas): ")
            nuevos_pasos = input("Nuevos pasos: ")
            actualizar_receta(nombre, nuevos_ingredientes, nuevos_pasos)
        elif opcion == '3':
            nombre = input("Nombre de la receta a eliminar: ")
            eliminar_receta(nombre)
        elif opcion == '4':
            ver_recetas()
        elif opcion == '5':
            nombre = input("Nombre de la receta a buscar: ")
            buscar_receta(nombre)
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            conn.close()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del programa
if __name__ == '__main__':
    menu()




