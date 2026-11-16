text = input(" enter text :")

for char in text:
    if text.count(char) > 1:
        print(char)
        break