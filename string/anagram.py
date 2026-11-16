text = input("enter text : ")
text2 = input("enter text : ")

if sorted(text) == sorted(text2):
    print("Anagrams")
else:
    print("not anagram")