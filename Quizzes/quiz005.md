# Quiz005 2024/09/02

## Paper solution
![image](https://github.com/user-attachments/assets/802478e6-744f-478e-af6d-630098716acc)

## Flow Chart
I realized this after I have deleted the file (due to storage running out), but the assigning variables process should be put in a rectangle and not a parallelogram. Only input or output should be in a parallelogram. (it will be fixed after this)

### SL
![image](https://github.com/user-attachments/assets/ac683e49-ad0e-403a-b17c-32dd912493ca)

### HL
![image](https://github.com/user-attachments/assets/f13448d6-43da-4d37-9eb5-d7996174edd6)


## Code
```.py
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def SL(word):
    total = 0
    for char in word:
        for i in range(len(lower)):
            if char == lower[i] or char == upper[i]:
                total += i + 1
                break
            elif char == " ":
                total -= 32
                break
    return total

def HL(word):
    total = 0
    for char in word:
        for i in range(len(lower)):
            if char == lower[i]:
                total += i + 1
                break
            elif char == upper[i]:
                total += i + 1344
                break
            elif char == " ":
                total -= 32
                break
    return total

#test cases
print(SL("Math"))
print(SL("maTH"))
print(SL("Hello world"))
print(SL("Computer SCIENCE"))
print(HL("Math"))
```

## Proof of Work
![image](https://github.com/user-attachments/assets/92864d84-6079-4c36-96e2-b454107ef34b)

