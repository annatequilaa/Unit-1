# Quiz004 2024/08/30

## Paper solution
![image](https://github.com/user-attachments/assets/4401afd4-f939-4975-871f-17a4de226cf5)

## Code
```.py
num = int(input("enter a number: "))
sum = 0
for i in range(1,num-1):
    if num%i == 0:
        print(i)
        sum += i
print(sum == num)
```

## Proof of Work
