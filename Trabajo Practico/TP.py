class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, codigo, cantidad_total, cantidad_prestados, autor, titulo):
        libro = {
            "codigo": codigo,
            "cantidad_total": cantidad_total,
            "cantidad_prestados": cantidad_prestados,
            "autor": autor,
            "titulo": titulo
        }
        self.libros.append(libro)

    def buscar_libro(self, codigo):
        for libro in self.libros:
            if libro["codigo"] == codigo:
                return libro
        return None

    def gestionar_prestamo(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro is None:
            print("El libro no existe.")
        else:
            if libro["cantidad_total"] - libro["cantidad_prestados"] <= 0:
                print("No quedan ejemplares disponibles para prestar.")
            else:
                print(f"Autor: {libro['autor']}")
                print(f"Título: {libro['titulo']}")
                print(f"Ejemplares disponibles: {libro['cantidad_total'] - libro['cantidad_prestados']}")
                confirmar = input("¿Desea confirmar el préstamo? (S/N): ")
                if confirmar.lower() == "s":
                    libro["cantidad_prestados"] += 1
                    print("Préstamo confirmado. Disfrute su lectura.")

# Crear una instancia de la biblioteca
biblioteca = Biblioteca()

# Agregar algunos libros a la biblioteca
biblioteca.agregar_libro("L001", 5, 2, "Autor 1", "Libro 1")
biblioteca.agregar_libro("L002", 3, 1, "Autor 2", "Libro 2")

# Menú de opciones
while True:
    print("Menú:")
    print("1) Gestionar Préstamo")
    print("0) Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo_libro = input("Ingrese el código del libro: ")
        biblioteca.gestionar_prestamo(codigo_libro)
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
