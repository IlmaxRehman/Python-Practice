num = int(input("enter number of terms :"))

a = 0
b = 1
count = 0
while count < num:
   print(a, end=" ")

   next = a+b
   a =b
   b = next

   count +=1
   


 