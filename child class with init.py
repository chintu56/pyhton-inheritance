"""Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

 The __init__() function is called automatically every time the class is being used to create a new object.
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

Example
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

"""




class Bharath:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname,self.lastname)

class Chintu(Bharath):
  def init(self,fname,lname):
    Bharath.__init__(self,fname,lname)

x = Chintu("bharath", "kumar")
x.printname()
