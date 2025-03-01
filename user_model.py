class user:
   global email
   global password
   def init_(self, email, password):
      self.email=email
      self.password=password
   def getValues(self):
       return self.email, self.password
   def getEmail(self):
       return self.email
   def getPass(self):
       return self.password