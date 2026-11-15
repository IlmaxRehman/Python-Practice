num = int(input("enter number:"))

i = 2
is_prime = True

if num <= 1:
    is_prime = False

else:
    while i < num :
        if(num%i == 0):
            
            is_prime = False
            break
        else:
            is_prime = True
        i += 1
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
