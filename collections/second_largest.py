#second largest distinct element

number = [13,56,78,43,333]

largest = None
second = None


for num in number:
    if  largest is  None or num > largest:
        second = largest
        largest = num
    elif num < largest and (second is None or num > second):
        second = num
      


print(second)