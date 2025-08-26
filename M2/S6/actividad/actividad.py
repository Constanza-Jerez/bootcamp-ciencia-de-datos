# 1.Crea la clase Libro con los atributos privados _titulo, _autor y _isbn.
class Libro:

# 2.Define un constructor para Libro que inicialice estos atributos al momento de crear un objet.    
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn


# 3.Implementa métodos get_titulo(), get_autor() y get_isbn() para obtener el valor de cada atributo desde fuera de la clase.
    def get_titulo(self):
        return self._titulo
        
    def get_autor(self):
        return self._autor
    
    def get_isbn(self):
        return self._isbn        

# 4.Crea un método descripcion() en la clase Libro que retorne una cadena con los detalles del libro en el formato “Título: [titulo], Autor: [autor], ISBN: [isbn]”.
    def descripcion(self):
        return f'Título: {self._titulo}, Autor: {self._autor}, ISBN: {self._isbn}'
    
# 5.Crea una clase Biblioteca que permita gestionar una lista de libros. Define un método agregar_libro() para añadir un libro a la bibliotec.
class Biblioteca:
    
    def __init__(self):
        self.libros = [] # lista de libros vacia cada vez que se crea una biblioteca  
    
    # def __init__(self, libros):
    #     self.libros = libros # lista de libros vacia cada vez que se crea una biblioteca, ej Biblioteca([])

    def agregar_libro(self, libro):
        self.libros.append(libro)

# 6.Define un método mostrar_libro() en Biblioteca que recorra la lista de libros e imprima la descripción de cada libro.        
    def mostrar_libro(self):
        for temp in self.libros:
            print(temp)   
           
# 7.Instancia la clase Biblioteca, crea al menos dos libros y añádelos a la biblioteca. Luego, muestra los detalles de los libros almacenado.

biblioteca = Biblioteca()

biblioteca.agregar_libro(Libro('titulo1', 'autor2', 'lib123'))
libro2 = Libro('titulo2', 'autor2', 'lib234')
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libro()