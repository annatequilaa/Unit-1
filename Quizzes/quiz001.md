# Quiz001 2024/08/21

## Paper solution
![image](https://github.com/user-attachments/assets/56723ade-bb17-425d-be14-9cef29f6ba5e)

## flow chart
![fc001 drawio](https://github.com/user-attachments/assets/4f73fb8d-5b38-499c-a494-fa8fd3357088)

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
![image](https://github.com/user-attachments/assets/39f0c79e-54dd-4746-acb4-f24d1e2ff0da)
![image](https://github.com/user-attachments/assets/ca679ec7-f2d6-414b-8cbd-8b3e137e2c16)
![image](https://github.com/user-attachments/assets/3cd57bea-70bc-4ebe-8809-58f6d4ba9acf)
![image](https://github.com/user-attachments/assets/4f50965c-938f-4fd8-936d-d1b032700046)





