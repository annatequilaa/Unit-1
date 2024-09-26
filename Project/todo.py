
#import functions
from mylib import *
from time import sleep

#colors
end_code = "\033[00m"
red = "\33[0;31m"
yellow = "\33[0;33m"
green = "\033[0;32m"
blue = "\33[0;34m"
purple = "\33[0;35m"
cyan = "\33[0;36m"

#dictionary
catalog = {}


#start screen
def todo_app():
    print(f"{green}Welcome to your personal to-do list, what would you like to do?\n")
    while True:
        print(f"{red}add task (A)    {yellow}view task list (V)    {green}delete task (D)\n{cyan}mark as complete (M)    {blue}undo mark as complete (U)    {purple}something (S)    {end_code}quit (Q)\n")
        u_option = input(f"{green}Enter the letter in the brackets to select: {end_code}")
        option = alpha_validation(u_option)
        if option == False:
            print(f"{end_code}_____________________________\n")
            continue

        if option == "a" or option == "A":
            task = input(f"{red}Enter the task you want to add: ")
            validness = add_task(task)
            if not validness == False:
                print(f"{yellow}\nHere's your updated to-do list: \n{view_tasks(get_tasks())}")
            else:
                print(f"{red}task cannot be added because it either already exists or the format is wrong")
                print(f"{end_code}_____________________________\n")
                continue

        elif option == "v" or option == "V":
            print(f"{yellow}\nHere's your current to-do list: \n{view_tasks(get_tasks())}")

        elif option == "d" or option == "D":
            print(f"{yellow}\nHere's your current to-do list: \n{view_tasks(get_tasks())}")
            delete = n_validation(input(f"{green}Enter the no. of the task you want to delete: "))
            validness = delete_task(delete)
            if not validness == False:
                print(f"{yellow}\nHere's your updated to-do list: \n{view_tasks(get_tasks())}")
            else:
                print(f"{end_code}Entered task does not exist")

        elif option == "m" or option == "M":
            print(f"{yellow}\nHere's your current to-do list: \n{view_tasks(get_tasks())}")
            n = n_validation(input(f"{green}Enter the no. of the task you want to mark as complete: "))
            validness = mark_complete(n)
            if not validness == False:
                print(f"{yellow}\nHere's your updated to-do list: \n{view_tasks(get_tasks())}")
            else:
                print(f"{end_code}Entered task does not exist or is already completed")

        elif option == "u" or option == "U":
            print(f"{yellow}\nHere's your current to-do list: \n{view_tasks(get_tasks())}")
            n = n_validation(input(f"{green}Enter the no. of the task you want to undo mark as complete: "))
            validness = undo_mark_complete(n)
            if not validness == False:
                print(f"{yellow}\nHere's your updated to-do list: \n{view_tasks(get_tasks())}")
            else:
                print(f"{end_code}Entered task either does not exist or is not marked complete")

        elif option == "s" or option == "S":
            code_input = input(f"{purple}Enter a code: ")
            if code_input == "vand3r":
                break
            else:
                print(f"\n{end_code}Invalid, try again or {red} GET LOST. {green}\n")
                continue

        elif option == "q" or option == "Q":
            return False
            break

        else:
            print(f"{end_code}Input invalid, try again")
        print(f"{end_code}_____________________________\n")


def password_manager():
    clear()
    print(f"{end_code}processing...")
    for i in range(10):
        print("...")
        sleep(0.5)
    print(f"\nWelcome to the password manager.")
    while True:
        # Create, Replace, Update, Delete
        print(f"{red}create login(C)    {yellow}view logins (V)    {green}update password (U)    {blue}delete login (D)    {purple}quit (Q){end_code}")
        u_pswd_option = input("Enter the letter in the brackets to select what you want to do: ")
        p_option = alpha_validation(u_pswd_option)
        if p_option == "Q" or p_option == "q":
            clear()
            print(f"{end_code}_____________________________\n")
            break
        elif p_option not in "CVUDQcvudq":
            print(f"{end_code}Input invalid...")
            print(f"{end_code}_____________________________\n")
            continue
        code_input = input(f"{end_code}Enter the code again to continue: ")
        if code_input != "vand3r":
            print(f"\n{end_code}Invalid, try again. {blue} (How did you even get in here?) {green}\n")
        else:
            clear()
            if p_option == False:
                print(f"{end_code}_____________________________\n")
                continue

            elif p_option == "c" or p_option == "C":
                username = input(f"{red}Enter the username you want to store: ")
                if username == "":
                    print(f"{end_code}Username cannot be blank!")
                    continue
                password = input(f"{red}Enter the password you want to store: ")
                if username == "":
                    print(f"{end_code}Password cannot be blank!")
                    continue
                validness = add_login(username, password)
                if not validness == False:
                    print(f"{yellow}\nHere's your updated list of log-in infos: \n{view_logins(get_login())}")

            elif p_option == "v" or p_option == "V":
                print(f"\n{yellow}Here's the current list of log-in infos: \n{view_logins(get_login())}")


            elif p_option == "d" or p_option == "D":
                print(f"{yellow}\nHere's your current list of log-in infos: \n{view_logins(get_login())}")
                if len(get_login()) < 1:
                    continue
                delete = input(f"{blue}Enter the username of the log-in info you want to delete: ")
                validness = delete_login(delete)
                if validness == True:
                    print(f"{yellow}\nHere's your updated list of log-in infos: \n{view_logins(get_login())}")
                else:
                    print(f"{end_code}Username entered is blank or doesn't exist")

            elif p_option == "u" or p_option == "U":
                print(f"{yellow}\nHere's your current list of log-in infos: \n{view_logins(get_login())}")
                if len(get_login()) < 1:
                    continue
                username = input(f"{green}Enter the username of the password you want to update: ")
                n_password = input("Enter the new password: ")
                validness = update_login(username,n_password)
                if not validness == False:
                    print(f"{yellow}\nHere's your updated list of log-in infos: \n{view_logins(get_login())}")
                else:
                    print(f"{end_code}Username entered is blank or doesn't exist")



            print(f"{end_code}_____________________________\n")

while True:
    check = todo_app()
    if check == False:
        print(f"{red}GOODBYE.")
        exit(1)
    password_manager()




