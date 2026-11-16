text = input("enter text:")

target = "m"
count = 0
for char in text :
    if char == target:
        count += 1

print(count)