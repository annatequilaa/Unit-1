# Quiz011 2024/09/18

## Paper solution
![image](https://github.com/user-attachments/assets/0aad57bc-08cc-4450-857a-ff5abf2fa402)

## Flowchart
![image](https://github.com/user-attachments/assets/b76c22bd-f52c-4476-aafd-13891dfd11b6)

## Code
```.py
def month(m):
    output = ""
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day_labels = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    start_days = [0,3,4,0,2,5,0,3,6,1,4,6]

    num_days = days_in_month[m-1]

    output += (f"{months[m-1]} 2024\n")


    start_day = start_days[m-1]

    for day in range(1, num_days + 1):
        output += (f"{day_labels[start_day]} {day}    ")
        start_day = (start_day + 1) % 7  # Cycle through days of the week
    return output


print(month(1))
print()#new line
print(month(3)) #my birthday month
```

## Proof of Work
![image](https://github.com/user-attachments/assets/8bbbb4e4-cf6e-48a1-874c-601efc1bcaae)

