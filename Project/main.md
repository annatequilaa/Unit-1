# Criterion A: Planning

## Problem definition
My client is the owner of a medicine Company. His employees are suffering from security breaches, where unauthorized individuals gain access and even controls to sensitive company information and systems. This endangers many of their clients since the sensitive information are no longer secure and medicines are important. In the past, they have stored passwords physically or relied on memorization. However, this presents many limitations. When people memorize their passwords, they are prone to forgetting passwords and taking extra time to retrieve it, or setting weak and repetitive passwords for different websites, which can be easily hacked into. Furthermore, people recording the passwords physically on paper and postits have the risk of the physical objects being accessible to everyone, hence not having much security. My client is concerned about future cycber attacks. 

## Proposed Solution
I propose to create a hidden and secure password manager software for my client, this solves their problems because:
* The software isn't physical and accessible to everyone. Only a user with the secret code will be able to access the content, hence reducing the risks of getting cyber attacked. 
* The software will store the password and username in a file and cypher it so when an employee forgets their password, it is accessible but also secure. This way, people can also use stronger passwords without the fear of forgetting it.
* The software's password managing feature will be masked with a daily-use feature such as calculator or to-do list. This way, the employees could keep the software with them at all times, with the password managing feature not being accessible to anyone who has access to the device with the software. 

## Success Criteria (Be more specific than this, more specific = better)
1. The to-do list feature should accept user input to add, delete, mark as complete, and undo tasks on a list. 
1. The to-do list can handle typical errors (e.g., no input, duplicated tasks) and give appropriate feedback.
1. If the user enters the secret code ("vand3r"), the program will change modes and act as a password manager.
1. In password manager mode, the user should be able to perform CVUD operations (Create, View, Update, Delete):
   * Add a password (for example, for a website).
   * View the stored log-in information.
   * Update a stored password by entering the corresponding username.
   * Delete a stored log-in information (username + password) by entering the corresponding username..
1. Save passwords permanently and securely by cyphering it with shift 12 within a string I made. This way, people can't guess the password even if they know the alphabet shift, because the string I used isn't just alphabets: it also includes number and randomly ordered special characters.
1. User could quit the password manager mode without closing the whole program. Quitting the password manager mode will lead user back to to-do list feature.
1. Use the terminal to interact with the user, and give appropriate feedback when input is invalid. 

# Criterion B: Design

### System Diagram
![image](https://github.com/user-attachments/assets/a713a9da-746e-49e5-9e6e-779b069ee655)

### Flow diagrams for algorithms

![view_tasks drawio (1)](https://github.com/user-attachments/assets/2e5e72e5-321d-4819-809b-66aab296c0e0)


**Fig. 1** This is the flow diagram for the algorithm used to check whether a list is empty and, based on that, display the to-do list. 




![add_login drawio](https://github.com/user-attachments/assets/2eddae4c-13a2-492d-8ec4-c0dafc880854)

**Fig. 2** This is the flow diagram for the algorithm used to add login information (username and password) and save it to the database. This also checks for whether the input is valid. 




![cypher drawio](https://github.com/user-attachments/assets/07448092-f3f9-4c4a-9e4c-ae5dc780243f)

**Fig. 3** This is the flow diagram for the algorithm used to cypher the passwords by shifting each character in the password along the string I have created. 

### Data storage
I use CSV files to store data in this product for easy access. However, I encrypt the saved passwords to prevent information being insecure because of the easy access to CSV files. My two CSV files are todo_db.csv and login_db.csv. 

### Sketches of the application (wireframe diagrams)

### Test plan


## Record of Tasks
| Task Number |           Planned Action           |                                                                                                  Planned Outcome                                                                                                 | Time Estimated | Target Completion Date | Criterion |
|:-----------:|:----------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------:|:----------------------:|:---------:|
| 1           | First meeting with the client      | Obtained a problem definition, understand what the situation is in order to come up with a solution.                                                                                                             | 10 min         | Sep 10th               | A         |
| 2           | Set criteria                       | Have a detailed critieria for the solution that the program will follow to perform all the tasks.                                                                                                                | 20 min         | Sep 10th               | A         |
| 3           | Complete system diagram            | A diagram that visually represents the hardware and software components of the product.                                                                                                                          | 20 min         | Sep 16th               | B         |
| 4           | Complete test plan                 | A table specifying the process for testing the solution with the inputs and expected outputs.                                                                                                                    | 45 min         | Sep 20th               | B         |
| 5           | Complete to-do list function       | Have an interactive to-do list feature that is ran on the terminal which follows the criteria and passes the corresponding tests in the test plan.                                                               | 150 min        | Sep 24rd               | C         |
| 6           | Complete password manager function | Have a hidden password manager that is activated after a secret code is entered. It should be interactive, ran on the terminal, and follows the criteria hence passing the corresponding tests in the test plan. | 90 min         | Sep 25th               | C         |
| 7           | Complete 3 flow diagrams           | Diagrams that visually represent how some key functions in the product works.                                                                                                                                    | 45 min         | Sep 26th               | B         |
| 8           | Record a demonstration             | Offers the client a preview of the product for feedback from the client to improve the product to their request if needed.                                                                                       | 20 min         | Sep 26th               | D         |
| 9           | Finalize record of tasks           | Double check everything on record of tasks to ensure everything is completed and documented.                                                                                                                     | 10 min         | Sep 27th               | B         |


## Sources
for this part of the code in to_do.py:
```.py
from time import sleep
for i in range(10):
    print("...")
    sleep(0.5)
```
I used https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/ as reference 
