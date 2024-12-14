class Bharath:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Chintu(Bharath):
  pass

x = Chintu("bharath", "kumar")
x.printname()
