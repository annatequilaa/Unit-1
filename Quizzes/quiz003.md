# Quiz003 2024/08/28

## Paper solution
![image](https://github.com/user-attachments/assets/a1e89694-39c3-460b-bb9c-a5ee80fe0c2f)


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
