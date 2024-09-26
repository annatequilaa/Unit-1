from os import system, name


def clear():
    #windows
    if name == 'nt':
        _ = system('cls')
    #mac
    else:
        _ = system('clear')

def n_validation(number:str):
    for letter in number:
        if letter not in "0123456789":
            print("number must be a number, try again.")
            return False
        else:
            return int(number)

def alpha_validation(word):
    for letter in word:
        if letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("input must be alphabets, try again.")
            return False
        else:
            return str(word)

#reuse these for password?
def get_tasks():
    task_dict = {}
    data_cleaned = []
    with open("todo_db.csv", mode="r") as f:
        data = f.readlines()
    for i in data:
        data_cleaned.append(i.strip())
    for i in range(len(data_cleaned)):
        task_dict[i + 1] = data[i]
    return task_dict

def view_tasks(task_dict):
    output = ""
    if len(task_dict) < 1:
        return "Your to-do list is empty."
    for n, task in task_dict.items():
        output += f"{n}. {task}"
    return output

def add_task(item):
    data_cleaned = []
    with open("todo_db.csv", mode="r") as f:
        data = f.readlines()
    for i in data:
        data_cleaned.append(i.strip())
    if item in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" or item not in data_cleaned:
        with open("todo_db.csv", mode="a") as f:
            f.write(f"{item}\n")
        return True
    else:
        return False


def delete_task(n):
    task_dict = get_tasks()
    if n in task_dict:
        del task_dict[n]
        with open("todo_db.csv", mode="w") as f:
            for task in task_dict.values():
                f.write(f"{task}")
        return True
    else:
        return False


def mark_complete(n):
    task_dict = get_tasks()
    if n in task_dict and "(completed)" not in task_dict[n]:
        task_dict[n] = "(completed) " + task_dict[n]
        with open("todo_db.csv", "w") as f:
            for task in task_dict.values():
                f.write(task)
        return True
    else:
        return False


def undo_mark_complete(n):
    task_dict = get_tasks()
    if n in task_dict and "(completed)" in task_dict[n]:
        task_dict[n] = task_dict[n].replace("(completed) ", "")
        with open("todo_db.csv", "w") as f:
            f.writelines(task_dict.values())
        return True
    else:
        return False

def get_login():
    with open('login_db.csv', mode='r') as f:
        data = f.readlines()
    dict = {}
    for item in data:
        data_cleaned = item.strip()
        data_separated = data_cleaned.split(', ')
        username = data_separated[0]
        password = data_separated[1]
        dict[username] = password
    return dict

def view_logins(dict):
    output = ""
    if len(dict) < 1:
        return "There are currently no log in info stored."
    for username, password in dict.items():
        output += f"{username}: {undo_cypher(password)}\n"
    return output

def add_login(username, password):
    data_cleaned = []
    with open("login_db.csv", mode="r") as f:
        data = f.readlines()
    for i in data:
        data_cleaned.append(i.strip())
    if username in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" or username not in data_cleaned:
        with open("login_db.csv", mode="a") as f:
            f.write(f"{username}, {cypher(password)}\n")
        return True
    else:
        return False



def delete_login(username):
    login_dict = get_login()
    if username in login_dict:
        del login_dict[username]
        with open('login_db.csv', 'w') as f:
            for username, password in login_dict.items():
                f.write(f"{username}, {password}\n")
        return True
    else:
        return False


def update_login(username, n_password):
    dict = get_login()
    if username in dict:
        dict[username] = cypher(n_password)
        with open('login_db.csv', 'w') as f:
            for username, password in dict.items():
                f.write(f"{username}, {password}\n")
        return True
    else:
        return False


def cypher(password):
    output = ""
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()<_+"
    for char in password:
        if char in string:
            i = string.index(char)
            new_index = (i + 12) % len(string)
            output += string[new_index]
    return output

def undo_cypher(c_password):
    output = ""
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()<_+"
    for char in c_password:
        if char in string:
            i = string.index(char)
            new_index = (i - 12) % len(string)
            output += string[new_index]
    return output