# Quiz009 2024/09/13

## Paper solution
![image](https://github.com/user-attachments/assets/b5a3e492-ba85-4102-9c53-599f83838e40)

## Flowchart
![image](https://github.com/user-attachments/assets/e395d574-b847-49cd-96d8-970fedad37a0)

## Code
```.py
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def shift(word, n):
    output = ""
    for char in word:
        for i in range(len(lower)):
            if char in lower:
                if char == lower[i]:
                    output += lower[(i + n) % len(lower)]
            elif char in upper:
                if char == upper[i]:
                    output += upper[(i + n) % len(lower)]
    return output

#print(shift("hello world", 13))
#print(shift("abcdefghijklmnopqrstuvwxyz", 13))
#print(shift("secret", -10))
```

## Proof of Work
![image](https://github.com/user-attachments/assets/556cce69-5c26-43af-b6e6-07007ccdbc13)

