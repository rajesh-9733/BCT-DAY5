x=int(input("x="))
y=int(input("y="))
try:
    z=x/y
    print(z)
except  Exception as e:
   print("value=",e)