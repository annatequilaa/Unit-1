# Quiz003 2024/08/28

## Paper solution
![image](https://github.com/user-attachments/assets/a1e89694-39c3-460b-bb9c-a5ee80fe0c2f)

## Flow Chart
### SL
![image](https://github.com/user-attachments/assets/35df39d4-7e33-4572-aeb6-dc8cc25d9209)

### HL
I realized this after I have deleted the file (due to storage running out), but the assigning variables process should be put in a rectangle and not a parallelogram. Only input or output should be in a parallelogram. 
![image](https://github.com/user-attachments/assets/c34e220c-b8ca-47ad-a942-3de0c3f34b64)


## Code
```.py
#SL
in_protein = str(input("enter a DNA protein: "))
if in_protein == "A":
    out_protein = "T"
elif in_protein == "T":
        out_protein = "A"
elif in_protein == "C":
        out_protein = "G"
elif in_protein == "G":
        out_protein = "C"
print(out_protein)

#HL
dictDNA = {"A":"T","G":"C", "T":"A", "C":"G"}
out_protein = ""
in_protein = str(input("enter a DNA protein"))
for i in range(len(in_protein)):
    out_protein += dictDNA[in_protein[i]]
print(out_protein)
```


## Proof of Work
![image](https://github.com/user-attachments/assets/7211581a-aac9-49ba-b448-5d2f5be5b4fb)
