# Quiz007 2024/09/10
## Paper Solution


## Code
```.py
#SL
import random
options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
options_special = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~"

def SL():
    output = ""
    for i in range(20):
        n = random.randint(0,len(options))
        output = output + options[n]
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
