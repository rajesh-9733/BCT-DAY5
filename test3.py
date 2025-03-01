class Person:
  def __init__(self, n, a):
    self.name=n
    self.age =a
  def showName(self):
    print("Name ", self.name) 
  def showAge(self):
    print("Age =",self.age)
class Student(Person):
  def __init__(self, n, a, r):
    super().__init__(n,a) 
    self.r=r
  def showRollno(self): 
    print("Roll number =",self.r)
s1 = Student("rajesh", 20, 100) 
s1.showName()
s1.showAge()
s1.showRollno()