# Quiz014 2024/09

## Paper solution

## Flowchart

## Code
```.py
def open_doors(num_students):
    count = 0
    doors = [False]*num_students
    for i in range(num_students):
        for d in range(i, num_students, i + 1):
            doors[d] = not doors[d]
    for d in doors:
        if d == True:
            count += 1
    output = count
    return output
```

## Proof of Work
![image](https://github.com/user-attachments/assets/05061978-d694-461c-a022-4cf0bf49d54d)
