class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
       
    def display(self):
      print("name",self.name)
      print("age",self.age)
    
t=Person("rajesh",20)
t.display()


