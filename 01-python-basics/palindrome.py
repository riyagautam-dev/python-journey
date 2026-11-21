number=int(input("enter a number:"))
reverse=0
original_number=number
while(number>0):
    digit=number%10
   
    reverse=reverse*10+digit
    number=number//10
print("the reverse of the number is:", reverse)
if reverse==original_number:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")