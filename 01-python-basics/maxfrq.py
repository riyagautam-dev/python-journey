n=int(input("enter a number: "))
max_freq=0
max_digit=0
freq={}
while n>0:
    digit=n%10
    if digit in freq:
        freq[digit]+=1
    else:
        freq[digit]=1
    n=n//10

for digit, count in freq.items():
    if count>max_freq:
        max_freq=count
        max_digit=digit

print(f"Digit {max_digit} has the highest frequency with {max_freq} occurrences.")