class Persona:
    def __init__(self, nombre, edad, color, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self, edad):
        nombre = self.nombre
        print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
 

         
class Estudiante(Persona):
    def __init__(self, nombre, edad, color, sexo, peso, altura, instituto, grado):
        super().__init__(nombre, edad, sexo, peso, altura)
        self.instituto = instituto
        self.grado = grado