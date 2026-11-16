text = input("enter text : ")

count = 0
#O(n)
for char in text :
        count += 1

print(f"the word has {count} characters")