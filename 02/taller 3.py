class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    def describir(self):
        return f"{self.nombre} es un {self.especie} de {self.edad} años."
    
    def envejecer(self, años=1):
        self.edad += años
        return f"{self.nombre} ahora tiene {self.edad} años."

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def info_vehiculo(self):
        return f"{self.marca} {self.modelo} del año {self.año}"
    
    def antiguedad(self, año_actual):
        return f"Tiene {año_actual - self.año} años de antigüedad."

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def descripcion(self):
        return f"'{self.titulo}' por {self.autor}, {self.paginas} páginas."
    
    def leer_paginas(self, paginas_leidas):
        if paginas_leidas <= self.paginas:
            self.paginas -= paginas_leidas
            return f"Quedan {self.paginas} páginas por leer."
        return "¡Ya terminaste el libro!"

if __name__ == "__main__":
    animales = [
        Animal("Max", "perro", 3),
        Animal("Luna", "gato", 2),
        Animal("Piolín", "canario", 1),
        Animal("Bugs", "conejo", 4),
        Animal("Nemo", "pez", 1)
    ]
    
    vehiculos = [
        Vehiculo("Toyota", "Corolla", 2020),
        Vehiculo("Honda", "Civic", 2018),
        Vehiculo("Ford", "Fiesta", 2015),
        Vehiculo("Chevrolet", "Spark", 2019),
        Vehiculo("Volkswagen", "Golf", 2017)
    ]
    
    libros = [
        Libro("Cien años de soledad", "Gabriel García Márquez", 432),
        Libro("1984", "George Orwell", 328),
        Libro("El principito", "Antoine de Saint-Exupéry", 96),
        Libro("Don Quijote", "Miguel de Cervantes", 863),
        Libro("Orgullo y prejuicio", "Jane Austen", 279)
    ]
    
    print(animales[0].describir())
    print(vehiculos[1].info_vehiculo())
    print(libros[2].descripcion())
    
    print(animales[0].envejecer())
    print(vehiculos[1].antiguedad(2025))
    print(libros[2].leer_paginas(20))