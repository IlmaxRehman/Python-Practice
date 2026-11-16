text = input("enter text: ")

reverse = ""

for char in text:
    reverse =  char + reverse 

print(reverse)