# Quiz008 2024/09/11

## Paper solution
![image](https://github.com/user-attachments/assets/83f56686-b352-4b29-8f30-dbf8e91bf08c)

## Flowchart
### SL
![image](https://github.com/user-attachments/assets/33fe0318-0d1e-43a8-b7f1-7119a93e59dd)

### HL
![image](https://github.com/user-attachments/assets/a0081488-4864-460c-9d26-5a1e692b6e2c)

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
