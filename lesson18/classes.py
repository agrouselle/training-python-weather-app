class Vehicule:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print(f"I'm moving")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


class Airplane(Vehicule):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model} {self.faa_id}")

    def moves(self):
        print(f"I'm flying like a bird")


class GolfCar(Vehicule):
    pass    # inherit from Vehicule

    def moves(self):
        print(f"I'm moving like a golf car")


mycar = Vehicule('Tesla', 'Model S')
# print(mycar.make)
# print(mycar.model)
mycar.get_make_model()
mycar.moves()

yourcar = Vehicule('Toyota', 'Corolla')
yourcar.get_make_model()
yourcar.moves()

myplane = Airplane('Boeing', '777', 'N-12345')
myplane.get_make_model()
myplane.moves()

mygoldcar = GolfCar("Golf", "car")
mygoldcar.get_make_model()
mygoldcar.moves()

print("\n")

for v in (mycar, yourcar, myplane, mygoldcar):
    v.get_make_model()
    v.moves()
