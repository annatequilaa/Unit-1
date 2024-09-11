# Quiz008 2024/09/11

## Paper solution
![image](https://github.com/user-attachments/assets/83f56686-b352-4b29-8f30-dbf8e91bf08c)

## Flowchart

## Code
```.py
def SL():
    lst = []
    for i in range(100):
        for j in range(10):
            for k in range(10):
                lst.append(f"{i+1}-Room {j+1}F{k+1:02d}")
    output = "\n".join(lst)
    return output

def HL(room:int):
    lst = []
    for i in range(100):
        for j in range(10):
            for k in range(10):
                lst.append(f"Room {j+1}F{k+1:02d}")
    output = lst[room-1]
    return output

#test cases
print(SL())
print(HL(100))
print(HL(13))
```

## Proof of Work
![image](https://github.com/user-attachments/assets/27c1076e-b865-4b23-b858-e00f793bf4cf)
