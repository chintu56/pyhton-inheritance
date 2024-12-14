class Ramaiah:
    def mygrandfather_assets(self):
        print("my grand father assets")
class Govardhan:
    def myfather_assets(self):
        print("my father assets")
class Yaswanth:
    def mybrother_assets(self):
        print("my brother assets")

class Bharath(Ramaiah,Govardhan,Yaswanth):
    def my_assets(self):
        print("my assets imported from my father,grand father and my brother")

b=Bharath()
b.my_assets()
b.mybrother_assets()
b.myfather_assets()
b.mygrandfather_assets()