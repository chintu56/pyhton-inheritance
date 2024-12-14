class Ramaiah:
    def assets(self):
        print("Ramaiah assets")


class Govardhan(Ramaiah):
    def myfather_assets(self):
        print("imported from his father Ramaiah")


class Bharath(Govardhan):
    def my_assets(self):
        print("imported from my father Govardhan ")

b=Bharath()
b.my_assets()
b.myfather_assets()
b.assets()