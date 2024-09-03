# Quiz005 2024/09/02

## Paper solution

## Code
```.py
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def the_function(word):
    total = 0
    for char in word:
        for i in range(len(lower)):
            if char == lower[i] or char == upper[i]:
                total += i + 1
                break
            if char == " ":
                total -= 32
                break
    return total

print(the_function(str(input("Enter a word: "))))
```

## Proof of Work
