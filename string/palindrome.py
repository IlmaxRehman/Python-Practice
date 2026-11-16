text = input("enter text:")

original = text

reverse = text[::-1]

if(reverse == original):
    print(f"{original} is a palindrom")
else:
    print(f"{original} is not a palindrom")