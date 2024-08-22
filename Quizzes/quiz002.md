# Quiz001 2024/08/21

## Paper solution
![image](https://github.com/user-attachments/assets/ae94a8a9-3586-4508-9ef1-ef727c4f59a3)


## Code
```.py
#[SL]
a = int(input())
b = int(input())
meow = False
if a == 20 or b == 20:
    meow = True
if a+b == 20:
    meow = True
print(meow)

#[HL]
list_a = input().split(", ")
list_b = input().split(", ")
woof = False
count = 0
for item in list_a:
    if int(list_a[count]) == 20 or int(list_b[count]) == 20:
        woof = True
    if int(list_a[count]) + int(list_b[count]) == 20:
        woof = True
    count += 1
print(woof)
```

## Proof of Work
