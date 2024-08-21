# Quiz001 2024/08/21

## Paper solution
![image](https://github.com/user-attachments/assets/5ab074ec-f7fe-4351-98e3-018bfebeb883)


## Code
```.py
#goal: print first letter + len(word)-2 + last letter
#conditionals: if word has less than 3 letters then just print original

#split by spaces into a list
sentence = str(input()).split(" ")

output = []

for word in sentence:
    if not len(word) < 3:
        #len(word)-2 because doesn't include the first and last letter
        #str() because len(word)-2 is integer and cannot be connected with str
        output.append(word[0]+str(len(word)-2)+word[-1])
    else:
        #add unprocessed string to list
        output.append(word)

#make the output list into a sentence, with each word being separated by a space
to_print = ' '.join(output)

print(to_print)
```


## Proof of work
![image](https://github.com/user-attachments/assets/68929e29-b54c-4a69-93e9-3023695b23f1)
![image](https://github.com/user-attachments/assets/89abecc8-4cbd-4c41-a2c8-4582476721a9)
![image](https://github.com/user-attachments/assets/d8cac056-ba4c-4a5e-b416-81cabc5ce6d3)
![image](https://github.com/user-attachments/assets/f5e22472-cb62-4bb8-9c8d-52d2d41ded69)



