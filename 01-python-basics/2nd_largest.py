numbers=[10,10,8,40,15]
largest = None
second_largest = None
if len(numbers) == 0:
    print("List is empty")
else:
    for i in range(len(numbers)):
        if largest is None or numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        
    else:
        if second_largest is None or numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
print("The second largest number is:", second_largest)
