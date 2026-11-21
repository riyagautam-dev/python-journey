number=int(input("Enter a number: "))
count=0
number=abs(number)
if number==0:
    count=1
while number>0:
    digit=number%10
    count+=1
    number=number//10
print("The number of digits in the number is:", count)
