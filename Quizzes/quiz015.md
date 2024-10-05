# Quiz014 2024/09

## Paper solution
![image](https://github.com/user-attachments/assets/000a1c1e-bcd5-4c2b-915c-ccd3b5f19ec1)

## Flowchart
![image](https://github.com/user-attachments/assets/0da53646-0c29-411f-b6d2-4e8bf8ab29ba)

## Code
```.py
def open_doors(num_students):
    output = 0
    doors = [False]*num_students
    for i in range(num_students):
        for d in range(i, num_students, i + 1):
            doors[d] = not doors[d]
    for d in doors:
        if d == True:
            output += 1
    return output
```

## Proof of Work
![image](https://github.com/user-attachments/assets/05061978-d694-461c-a022-4cf0bf49d54d)
