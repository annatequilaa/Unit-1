# Quiz010 2024/09/16

## Paper solution
![image](https://github.com/user-attachments/assets/f70765ac-d483-4faf-b990-ddefeb569e22)

## Flowchart
![image](https://github.com/user-attachments/assets/3fa2f16d-6144-439d-926c-d29bead80244)

## Code
```.py
def powersTen(num: int, unit: str):
    units = {"tera": 12, "giga": 9, "mega": 6, "kilo": 3, "": 0, "mili": -3, "micro": -6, "nano": -9, "pico": -12}
    output = ""
    for i in units:
        n = units[i]//3
        a = ""
        if n < 0:
            n = -n
            a = "0.00" + (n-1)*"000" + str(num)

        elif n > 0:
            a = str(num) + "000"*n
        else:
            a = str(num)
        output += f"{a.ljust(20)}{i}{unit}\n"

    return output


print(powersTen(1, "gram of salt"))
```

## Proof of Work
![image](https://github.com/user-attachments/assets/5b4f50b2-4a6a-4c68-8561-8e527e273940)


