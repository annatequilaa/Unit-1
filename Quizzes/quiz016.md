# Quiz016 2024/10

## Paper solution
### a. get_l3tt3r function

### b. boolean circuit for: AB + not(B+C) + B(notC notA)



## Flowchart
![image](https://github.com/user-attachments/assets/8179976f-60bb-4923-a6f3-6c0998e76797)

## Code
```.py
def get_l3tt3r(word):
    output = ""
    for i in word:
        if i == "A" or i == "a":
            output += "4"
        elif i == "E" or i == "e":
            output += "3"
        elif i == "I" or i == "i":
            output += "1"
        elif i == "O" or i == "o":
            output += "0"
        elif i == " ":
            output += "_"
        else:
            output += i
    return output
```

## Proof of Work
![image](https://github.com/user-attachments/assets/b41edf99-e8ed-4e9b-b879-f4e6e6b19b45)


