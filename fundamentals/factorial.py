num = int(input("enter number: "))
fact = 1

if num < 1 :
    print("factorial is not defined")
else:
  while num > 1 :
     fact = fact *num 
     num -= 1

print(fact)
