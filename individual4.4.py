class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} esta comiendo.")

class Koala(Animal):
    def __init__(self, nombre, edad, patas):
        super().__init__(nombre, edad)
        self.patas = patas

    def caminar(self):
        print(f"{self.nombre} esta caminando en {self.patas} patas.")

class Perro(Koala):
    def __init__(self, nombre, edad, crias):
        super().__init__(nombre, edad, 4)
        self.crias = crias

    def ladrar(self):
        print(f"{self.nombre} ladra. Woof woof!")

class Cat(Koala):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad, 4)
        self.color = color

    def ronronear(self):
        print(f"{self.nombre} ronrorrea. Prr prr como motor.")


animal = Animal("Generic Animal", 5)
animal.comer()

julio = Koala("julio koala", 10, 4)
julio.comer()
julio.caminar()

shera = Perro("shera", 3, "pastor aleman")
shera.comer()
shera.caminar()
shera.ladrar()

felix = Cat("felix", 2, "negro")
felix.comer()

felix.caminar()
felix.ronronear()
#errores  por dobe guion en init
#instancias a clases animal, koala, perro y gato mas respectivos metodos
# clase animal base. clase koala hereda de animal y agrega propiedad patas y metodo caminar
# clase perro hereda de koala y agrega propiedad crias y metodo ladrar.
# clase gato hereda de koala y agrega propiedad color y metodo ronronear 