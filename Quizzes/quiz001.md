# Quiz001 2024/08/21

## Paper solution
(insert image by upload)

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
