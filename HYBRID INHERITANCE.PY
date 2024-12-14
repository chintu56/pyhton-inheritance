class Ramaiah:
    def mygrandfather_assets(self):
        print("Ramaiah assets")
class Govardhan(Ramaiah):
    def myfather_assets(self):
        print("imported from Ramaiah")
class Yaswanth(Ramaiah):
    def mybrother_assets(self):
        print("imported from Ramaiah")
class Bharath(Govardhan,Yaswanth):
    def my_assets(self):
        print("imported from my father and my brother")


b=Bharath()
b.my_assets()
b.myfather_assets()
b.mybrother_assets()
b.mygrandfather_assets()
