# Quiz001 2024/08/21

## Paper solution
[![image](https://github.com/user-attachments/assets/5ab074ec-f7fe-4351-98e3-018bfebeb883)](https://private-user-images.githubusercontent.com/124410631/359797994-5ab074ec-f7fe-4351-98e3-018bfebeb883.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQ2NzI5MzQsIm5iZiI6MTcyNDY3MjYzNCwicGF0aCI6Ii8xMjQ0MTA2MzEvMzU5Nzk3OTk0LTVhYjA3NGVjLWY3ZmUtNDM1MS05OGUzLTAxOGJmZWJlYjg4My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgyNlQxMTQzNTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00Y2I5ZThlMGVmZTNhNDAwYTMxYjQ0NTc3OWU4YmQ5OGNmOTAzNmE2N2E5ODAxMjZjM2M4NWY2Yzg1MmNiMTEyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.yoEvWlFHxCfaSDq8sprSzSA7GdO7H3fQjyzTO9BSiws)


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





