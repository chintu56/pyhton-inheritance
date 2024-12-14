class Govardhan():
    def assets(self):
        print("Govardhan assets")



class Bharath(Govardhan):
    def my_assets(self):
        print("imported from my father")

b=Bharath()
b.assets()
b.my_assets()

