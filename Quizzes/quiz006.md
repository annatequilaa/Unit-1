# Quiz005 2024/09/05? 2024/09/06?

## Paper solution
![image](https://github.com/user-attachments/assets/f0232d5f-d93b-44db-9453-34615d1054d7)

## Flowchart
![image](https://github.com/user-attachments/assets/2a998c51-2aa0-418b-8fe2-9cfd46fa9a4b)


## Code
```.py
def maximum(nums:list):
    m = -1
    for i in range(len(nums)):
        if nums[i] > m:
            m = nums[i]
    return m

#test case
print(maximum([3,5,10,2,15]))
```

## Proof of Work
![image](https://github.com/user-attachments/assets/d84c574d-38b6-4aef-92e2-bf3477f1a486)
