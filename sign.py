from user_model import user
l=[]
def signUp():
  email=input("Enter your emai1:").strip()
  password=input("Enter your password:").strip()
  u=user(email, password)
  print(u.getValues())
  l.append(u)
  print("Signup successfu11.")
def signIn():
  email=input("Enter your email:")
  password=input("Enter your password:")
  for user in 1:
    if user.getEmail()==email:
      if user.getPass()==password:
        print("signin successfu11")
      else:
        print("Incorrect password.")
      return
  print("Singup first, ")
def main():
    signUp()
    signIn()
if __name__=="__name__":
    main()