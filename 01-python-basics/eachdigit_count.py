n=int(input("enter a number: "))
count=0
freq={}
while n>0:
    digit=n%10
    if digit in freq:
        freq[digit]+=1
    else:
        freq[digit]=1
    n=n//10

for digit, count in freq.items():
    print(f"Digit {digit}: {count} times")