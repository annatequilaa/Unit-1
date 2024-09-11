# Quiz001 2024/08/22

## Paper solution
![image](https://github.com/user-attachments/assets/ae94a8a9-3586-4508-9ef1-ef727c4f59a3)

## Flow Chart
### SL
![image](https://github.com/user-attachments/assets/f975fc2f-ffc3-443b-8e88-334dee8523a8)

### HL
(the "END" is written because I had a typo and didn't save the flowchart so writing it is the only way I can fix it)

![image](https://github.com/user-attachments/assets/bb4cc7b0-1d29-4735-a45f-029bae336897)



## Code
```.py
#[SL]
#note for next time: have meaningful variable names.
#note for next time 2.0: have a messege prompt for input. 
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
## SL
![image](https://github.com/user-attachments/assets/21a78186-fc9e-4fd2-bd7c-abf647c29cb5)
![image](https://github.com/user-attachments/assets/c441650e-f84f-4f70-a0cc-dc4ea6d18696)
![image](https://github.com/user-attachments/assets/bf551a46-48cb-4f16-884c-65a4a21caa81)
![image](https://github.com/user-attachments/assets/f0ec1e1c-d8d7-4d3f-8923-c17bd27394c8)


## HL
![image](https://github.com/user-attachments/assets/3c20911a-13ac-4eb7-9ba5-3e440aab6de3)




