# Quiz007 2024/09/10
## Paper Solution
![image](https://github.com/user-attachments/assets/de0e09ff-a3b2-498f-bc06-4d7efd1685f0)

## Flowchart
### SL
![image](https://github.com/user-attachments/assets/d3dacd29-7009-4d20-b3a0-caaa29c40657)

### HL
![image](https://github.com/user-attachments/assets/a52398c7-9f51-4a2c-85da-d03358296f4d)

## Code
```.py
import random
options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
options_special = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~"

def SL():
    output = ""
    for i in range(20):
        n = random.randint(0,len(options))
        output = += options[n]
    return output

def HL(length:int, boo):
    output = ""
    for i in range(0,length):
        if boo == True:
            n = random.randint(0, len(options_special))
            output += options_special[n]
        else:
            n = random.randint(0, len(options))
            output += options[n]
    return output

#test cases
print(SL())
print(SL())
print(HL(20, True))
print(HL(5,False))
print(HL(10,True))
```

## Proof of Work
![image](https://github.com/user-attachments/assets/d06bb2cf-f3c5-4e47-81b6-6a32c04a45b5)
