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
1. In password manager mode, the user should be able to perform CVUD operations (Create, View, Update, Delete) after entering the secret code:
   * Add a password (for example, for a website).
   * View the stored log-in information.
   * Update a stored password by entering the corresponding username.
   * Delete a stored log-in information (username + password) by entering the corresponding username.
1. The terminal will be cleared every time after the secret code is entered to ensure that the secret code is safe. 
1. Save passwords permanently and securely in a csv file by cyphering it with shift 12 within a string I made. This way, people can't guess the password even if they know the alphabet shift, because the string I used isn't just alphabets: it also includes number and randomly ordered special characters.
1. User could quit the password manager mode without closing the whole program. Quitting the password manager mode will lead user back to to-do list feature.
1. Use the terminal to interact with the user, and give appropriate feedback when input is invalid. 

# Criterion B: Design

### System Diagram
![image](https://github.com/user-attachments/assets/e5fe1227-028c-40d4-9ff6-4573296e778c)


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
| Description                                  | Success Criteria | Input                                                                                                                                 | Output                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accepting user input to select what to do    | 1                | 1. user enters one of these letters: A,V,D,M,U,S,Q 2. user enters something else                                                      | 1. the corresponding task is activated 2. feedback "input invalid, try again"                                                                                                                                                                                                                                                                                       |
| Adding a task                                | 1                | 1. user enters A or a, and then enters the name of the task                                                                           | 1. a or A triggers the adding task function, which will print the numbered and updated task list with the new task added at the bottom provided that the task entered isn't blank.                                                                                                                                                                                  |
| Deleting a task                              | 1                | 1. user enters D or d, and then enters the number of the task                                                                         | 1. d or D triggers the deleting task function, which will first print the current numbered to-do list, then ask the user to enter the number of the task. After that, an updated numbered to-do list will be printed without the to-do with the number that was deleted.                                                                                            |
| Marking a task as complete                   | 1                | 1. user enters M or m, and then enters the number of the task                                                                         | 1. m or M triggers the mark task as complete function, which will first print the current numbered to-do list, then ask the user to enter the number of the task. After that, an updated numbered to-do list will be printed with the to-do with the number formatted as "(completed) task_name". This will only work if the to-do number isn't already completed.  |
| Undo marking a task as complete              | 1                | 1. user enters U or u, and then enters the number of the task                                                                         | 1. u or U triggers the undo mark task as complete function, which will first print the current numbered to-do list, then ask the user to enter the number of the task. After that, an updated numbered to-do list will be printed with the to-do with the number formatted as "task_name". This will only work if the to-do number is already marked as completed.  |
| Handling errors of user input                | 2                | 1. user enters nothing 2. user enters something invalid listed in rows above such as trying to mark complete task as complete again.  | error message is printed, and prompts user to try again; returns to options page                                                                                                                                                                                                                                                                                    |
| Activating the password manager mode         | 3                | 1. user enters "vand3r" 2. user enters something else                                                                                 | 1. password manager mode is activated 2. error message is printed and user is denied access and stays in to-do list mode                                                                                                                                                                                                                                            |
| Creating log-in information                  | 4                | 1. user enters c or C, then "vand3r", then username, then password 2. ditto, user enters a blank username or password                 | 1. create login mode activated, screen cleared after "vand3r" is entered, after username and password are entered, an updated list of log-in information will be displayed.  2. error message is printed and user is directed back to the options page of password manager.                                                                                         |
| Viewing log-in information                   | 4                | 1. user enters v or V, then "vand3r"                                                                                                  | 1. view login mode activated, screen cleared after "vand3r" is enetered, a list of currently saved log-in information will be displayed.                                                                                                                                                                                                                            |
| Updating a password                          | 4                | 1. user enters u or U, then "vand3r", then username, then new password 2. ditto, user enters a blank username or password             | 1. update password mode activated, screen cleared after "vand3r" is entered, after username and new password are entered, an updated list of log-in information will be displayed.  2. error message is printed and user is directed back to the options page of password manager.                                                                                  |
| Delete log-in information                    | 4                | 1. user enters d or D, then "vand3r", then username 2. ditto, user enters a blank username                                            | 1. delete login mode activated, screen cleared after "vand3r" is entered, after username is entered, an updated list of log-in information, with the login with number entered deleted, will be displayed.  2. error message is printed and user is directed back to the options page of password manager.                                                          |
| Clearing terminal after entering secret code | 5                | 1. user enters "vand3r"                                                                                                               | 1. terminal is cleared                                                                                                                                                                                                                                                                                                                                              |
| Cypher password when storing into csv file   | 6                | 1. user creates a log-in detail via success criteria 4                                                                                | 1. in the file, the passwords are encrypted, but in the view login feature, the passwords displayed are not encrypted                                                                                                                                                                                                                                               |
| Quitting password manager mode               | 7                | 1. user enters q or Q                                                                                                                 | 1. user is directed back to the to-do list mode                                                                                                                                                                                                                                                                                                                     |
| Using the terminal to interact with the user | 8                | 1. Run the program file in terminal and input anything.                                                                               | 1. The program runs properly, and input is received and appropriate feedback is given when input is empty or not one of the options.                                                                                                                                                                                                                                |                                                                                                             |


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


# Criterion C: Development

## Video demonstration
(there is voiceover in this video, and it is quite loud)
https://drive.google.com/file/d/1Wmh9NT_Pyl914XW4IidZXmc86s3_y0_y/view?usp=sharing

## Sources
For this part of the code in to_do.py:
```.py
from time import sleep
for i in range(10):
    print("...")
    sleep(0.5)
```
I used https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/ as reference 

For the  ```.py clear()``` function in mylib.py:
```.py
from os import system, name
def clear():
    #windows
    if name == 'nt':
        _ = system('cls')
    #mac
    else:
        _ = system('clear')
```
I used code from https://stackoverflow.com/questions/27241268/clear-pycharm-run-window answered by Mahak Khurmi (2021) and edited by vayana (2023). 
