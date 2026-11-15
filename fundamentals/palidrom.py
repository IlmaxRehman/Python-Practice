num = int(input("enter number:"))
original = num
reverse = 0

while num > 0 :
    reverse = reverse*10 + num%10
    num = num//10

if( reverse == original):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")