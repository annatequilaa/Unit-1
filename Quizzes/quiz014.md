# Quiz014 2024/09

## Paper solution
![image](https://github.com/user-attachments/assets/943b7e81-13db-4bd2-a44b-c09d013db0f5)

## Flowchart
### SL


### HL


## Code
```.py
def average(words):
    l_count = 0
    w_count = 0
    for i in words:
        l_count += 1
        for char in i:
            if not char == " ":
                w_count += 1
    avg = w_count/l_count
    output ='{0:.1f}'.format(avg)
    return output

print(average(["hello","main"]))
print(average(["Peru", "France", "Nepal"]))
print(average(["Computer Science","Art"]))
print("for the above one, space isn't counted so it's different from the slides since this is HL")
print(average(["one", "two"]))

```

## Proof of Work
![image](https://github.com/user-attachments/assets/d2f1361e-4849-46e3-979b-8377e4f1d21e)

