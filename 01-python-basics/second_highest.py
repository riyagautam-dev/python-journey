n = int(input())
arr = list(map(int, input().split()))
highest=None;
second_highest=None;
for i in range(len(arr)) :
        if highest is None:
            highest=arr[i]
        elif(arr[i]>highest ):
            second_highest=highest
            highest=arr[i]
        elif((second_highest is None) or arr[i]<highest and arr[i]>second_highest):
            second_highest=arr[i]
print(second_highest)
        