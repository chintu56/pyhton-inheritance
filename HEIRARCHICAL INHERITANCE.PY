class Ramaiah:
    def mygrandfather_assets(self):
        print("Ramaiah assets")
class Govardhan(Ramaiah):
    def myfather_assets(self):
        print("imported from Ramaiah")
class Yaswanth(Ramaiah):
    def mybrother_assets(self):
        print("imported from Ramaiah")
class Bharath(Ramaiah):
    def my_assets(self):
        print("imported from ramaiah")

g=Govardhan()
g.myfather_assets()
g.mygrandfather_assets()
y=Yaswanth()
y.mybrother_assets()
y.mygrandfather_assets()
b=Bharath()
b.my_assets()
b.mygrandfather_assets()
    