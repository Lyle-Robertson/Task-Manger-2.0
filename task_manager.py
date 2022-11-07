from datetime import date
from collections import Counter
import os.path


def main():  # function in order to use -1 more effectivel
    while True:
        if username == "admin":  # admin menu
            menu = input('''\nSelect one of the following Options below:
r\t-\tRegistering a user
a\t-\tAdding a task
va\t-\tView all tasks
vm\t-\tview my task
gr\t-\tGenerate reports
ds\t-\tDisplay statistics
e\t-\tExit
: ''').lower()

        else:  # non-admin menu
            menu = input('''\nSelect one of the following Options below:
r\t-\tRegistering a user
a\t-\tAdding a task
va\t-\tView all tasks
vm\t-\tview my task
e\t-\tExit
: ''').lower()

        if menu == 'r' and username == 'admin':
            pass

            while 0 == 0:  # loop input for new username
                new_user = input("Enter new username:\t")
                search_file = open("user.txt", "r")
                contents = searchfile.read()
                if new_user not in contents:  # if username is not found in file
                    while new_user == new_user:
                        new_password = input("Enter password:\t")
                        confirm_password = input("Confirm password:\t")
                        if confirm_password != new_password:  # password match conditional statement
                            print("Password do not match. Try again\n")

                        else:
                            new_user_pass = "\n" + new_user + ", " + new_password
                            ammendfile = open("user.txt", "a")  # adding user and password to file
                            ammendfile.write(new_user_pass)
                            ammendfile.close()
                            print("\n" + new_user + " has been registered!\n")
                            break
                    break
                elif new_user in contents:  # if username is found
                    print("\nuser exists, try a different username\n")
            search_file.close()  # close file

        elif menu == 'a':
            pass

            task_file = open("tasks.txt", "r")
            task_num = len(task_file.readlines())
            task_file.close()

            task_title = input("Task:\t\t\t\t\t\t")
            task_user = input("Assigned to:\t\t\t\t")

            date_assigned = date.today()
            date_assigned = date_assigned.strftime("%d/%m/%Y")
            print("Date Assigned:\t\t\t\t" + date_assigned)

            due_date = input("Due date (dd-mm-yyyy):\t\t")

            task_complete = "Task complete:\t\t\t\tNo"
            print(task_complete)

            task_description = input("Task description:\t\t\t")

            taskfile = open("tasks.txt", "a")  # writing data to task file
            taskfile.write(f'\nTask Number:\t\t\t\t{task_num},'
                           f'Task:\t\t\t\t\t\t{task_title},Assigned to:\t\t\t\t{task_user},'
                           f'Date Assigned:\t\t\t\t{date_assigned},'
                           f'Due date (dd/mm/yyyy):\t\t{due_date},{task_complete},'
                           f'Task description:\t\t\t{task_description}')
            taskfile.close()

            empty_line = ""  # removing empty lines
            task_file = open("tasks.txt", "r")
            lines = task_file.readlines()
            for line in lines:
                if not line.isspace():
                    empty_line += line
            task_file.close()

            task_file = open("tasks.txt", "w")
            task_file.write(empty_line)
            task_file.close()

        elif menu == 'va':
            pass

            task_file = open('tasks.txt', 'r')  # displays data in task file
            contents = task_file.readlines()
            for line in contents:
                print(*line.split(",")[0:6], sep="\n")
                print("")
            task_file.close()

        elif menu == 'vm':
            pass

            while 0 == 0:
                task_file = open("tasks.txt", "r")  # displaying specific user tasks
                lines = task_file.readlines()
                for line in lines:
                    if username in line:
                        print(*line.split(",")[0:7], sep="\n")
                task_file.close()

                task_num = int(input("\nTo select a task, input the task number or to return to the previous"
                                     " menu input '-1':\t"))

                task_file = open("tasks.txt", 'r')
                contents = task_file.read()
                if task_num == -1:
                    main()
                    break

                elif f'Task Number:\t\t\t\t{task_num}' not in contents:
                    print('Number entered does not match any task. try again\n')
                    task_file.close()

                else:
                    print(f"\nTask selected:\n")
                    task_file = open("tasks.txt", "r")
                    lines = task_file.readlines()
                    line_number = 0
                    for line in lines:
                        line_number += 1
                        if f'Task Number:\t\t\t\t{task_num}' in line:
                            print(*line.split(",")[0:7], sep="\n")
                            menu1 = input('''\nSelect one of the options below:
edt\t-\tEdit task
com\t-\tMark as complete
-1\t-\tTo return to previous menu
:''').lower()
                            if menu1 == "edt":

                                if 'Task complete:\t\t\t\tYes' in lines[line_number - 1]:
                                    print("\nTask is has already been completed, Try a different task number\n")
                                    task_file.close()
                                    break

                                else:
                                    menu2 = input('''\nSelect one of the option below:
date\t-\tChange The Due Date
ass\t\t-\tChange who the task is assigned to
:''').lower()
                                    if menu2 == 'date':
                                        pass

                                        new_date = input("\nEnter the new date in the format (dd/mm/yyyy):\t")
                                        line_to_edit = lines[line_number - 1]
                                        date_to_replace = lines[line_number - 1].split(",")[4]
                                        new_line = line_to_edit.replace(date_to_replace,
                                                                        f'Due date (dd/mm/yyyy):\t\t{new_date}')
                                        task_file.close()
                                        del lines[line_number - 1]  # delete original task from file

                                        task_file = open("tasks.txt", "w")  # add completed task to task file
                                        for line in lines:
                                            task_file.write(line)
                                        task_file.write("\n" + new_line)
                                        task_file.close()

                                        empty_line = ""  # removing empty lines
                                        task_file = open("tasks.txt", "r")
                                        lines = task_file.readlines()
                                        for line in lines:
                                            if not line.isspace():
                                                empty_line += line
                                        task_file.close()

                                        task_file = open("tasks.txt", "w")
                                        task_file.write(empty_line)
                                        task_file.close()

                                        print('\nDate changed successfully!\n')

                                    if menu2 == 'ass':
                                        pass

                                        assign_to = input("Who should the task be reassigned to?:\t")
                                        line_to_edit = lines[line_number - 1]
                                        name_to_replace = lines[line_number - 1].split(",")[2]
                                        new_line = line_to_edit.replace(name_to_replace,
                                                                        f'Assigned to:\t\t\t\t{assign_to}')
                                        task_file.close()
                                        del lines[line_number - 1]  # delete original task from file

                                        task_file = open("tasks.txt", "w")  # add completed task to task file
                                        for line in lines:
                                            task_file.write(line)
                                        task_file.write("\n" + new_line)
                                        task_file.close()

                                        empty_line = ""  # removing empty lines
                                        task_file = open("tasks.txt", "r")
                                        lines = task_file.readlines()
                                        for line in lines:
                                            if not line.isspace():
                                                empty_line += line
                                        task_file.close()

                                        task_file = open("tasks.txt", "w")
                                        task_file.write(empty_line)
                                        task_file.close()

                            elif menu1 == 'com':

                                line_to_edit = lines[line_number - 1]
                                task_file.close()  # delete original task from file
                                del lines[line_number - 1]

                                task_file = open("tasks.txt", "w")  # add completed task to task file
                                for line in lines:
                                    task_file.write(line)
                                new_line = line_to_edit.replace("No", "Yes")
                                task_file.write("\n" + new_line)
                                task_file.close()

                                empty_line = ""  # removing empty lines
                                task_file = open("tasks.txt", "r")
                                lines = task_file.readlines()
                                for line in lines:
                                    if not line.isspace():
                                        empty_line += line
                                task_file.close()

                                task_file = open("tasks.txt", "w")
                                task_file.write(empty_line)
                                task_file.close()

                                print(f'\nTask Number {task_num} complete!\n')

                            elif menu1 == '-1':
                                break

        elif menu == 'r' and username != 'admin':  # allowing only admin to register new users
            print("Only admin is allowed to register new users, Please make another choice")

        elif menu == 'ds':  # accessible only by admin user
            user_overview_exist = os.path.exists('user_overview.txt')
            task_overview_exist = os.path.exists('task_overview.txt')
            if user_overview_exist == True and task_overview_exist == True:
                user_overview = open('user_overview.txt', 'r')
                lines = user_overview.readlines()
                print(*lines, sep = "")
                user_overview.close()

                task_overview = open('task_overview.txt', 'r')
                lines = task_overview.readlines()
                print(*lines, sep="")
                task_overview.close()

            else:
                print('The reports have not been generated. They will now be Generated...')
                generate_reports()

        elif menu == 'gr':
            generate_reports()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")


def generate_reports():
    num_overdue = 0
    completed_tasks = 0

    task_file = open("tasks.txt", 'r')
    lines = task_file.readlines()
    num_tasks = len(lines)
    for line in lines:
        if "Task complete:\t\t\t\tYes" in line:  # if complete
            completed_tasks += 1

        else:
            split_line = line.split(",")
            date_section = split_line[4]
            date_due = date_section[24:34]

            if date_due < str(date.today().strftime("%d/%m/%Y")):  # compare due date to current date if incomplete
                num_overdue += 1
    task_file.close()

    incomplete_tasks = num_tasks - completed_tasks
    percent_incomplete = round((incomplete_tasks / num_tasks) * 100)
    percent_overdue = round((num_overdue / num_tasks) * 100)

    task_overview = open("task_overview.txt", 'w')  # write data to file created
    task_overview.write(f'Total number of tasks :\t\t\t\t{num_tasks}\n'
                        f'Total number of task complete:\t\t{completed_tasks}\n'
                        f'Total number of task incomplete:\t{incomplete_tasks}\n'
                        f'Percentage of tasks incomplete:\t\t{percent_incomplete}%\n'
                        f'Percentage of tasks overdue:\t\t{percent_overdue}%'
                        )
    task_overview.close()

    i = 0
    user_file = open("user.txt", "r")
    users = user_file.readlines()
    user_file.close()

    tasks_per_user = []  # list to determine tasks per user
    incomplete_tasks_per_user = []  # list to determine incomplete tasks per user
    overdue_tasks = []  # list to determine overdue tasks per user

    task_file = open("tasks.txt", "r")
    lines = task_file.readlines()
    while i < len(users):
        for line in lines:
            if users[i].split(",")[0] in line:
                employee = line.split(",")[2][15:121]
                tasks_per_user.append(employee)

                if "Task complete:\t\t\t\tNo" in line:
                    incomplete_tasks_per_user.append(employee)
                    split_line = line.split(",")
                    date_section = split_line[4]
                    date_due = date_section[24:34]

                    if date_due < str(date.today().strftime("%d/%m/%Y")):  # compare due date to current
                        overdue_tasks.append(employee)
        i += 1
    task_file.close()

    user_overview = open('user_overview.txt', 'w')
    user_overview.write(f'Number of users registered:\t{len(users)}\n'
                        f'Number of tasks generated:\t{num_tasks}\n\n')
    user_overview.close()

    i = 0
    while i < len(users):
        employee = f'\t{users[i].split(",")[0]}'
        percentage_assigned = round(Counter(tasks_per_user)[employee] / num_tasks * 100)
        percentage_complete = round((Counter(tasks_per_user)[employee]
                                     - Counter(incomplete_tasks_per_user)[employee])
                                    / Counter(tasks_per_user)[employee] * 100)
        percentage_incomplete = round(Counter(incomplete_tasks_per_user)[employee] / Counter(tasks_per_user)[employee]
                                      * 100)
        percentage_overdue = round(Counter(overdue_tasks)[employee] / Counter(tasks_per_user)[employee] * 100)

        user_overview = open('user_overview.txt', 'a')
        user_overview.write(f'\n{users[i].split(",")[0]}:\n'  # Write data to new file
                            f'Tasks assigned:\t\t\t\t\t\t{Counter(tasks_per_user)[employee]}\n'
                            f'Percentage of tasks assigned:\t\t{percentage_assigned}%\n'
                            f'Percentage of task completed:\t\t{percentage_complete}%\n'
                            f'Percentage of tasks incomplete:\t\t{percentage_incomplete}%\n'
                            f'Percentage of tasks overdue:\t\t{percentage_overdue}%\n'
                            )
        i += 1
    print("Reports have been Generated!!\n")
    user_overview.close()


searchfile = open("user.txt", "r")
content = searchfile.readlines()
found = False
''
while not found:
    username = input("Enter your username:\t")
    password = input("Enter your password:\t")
    user_pass = username + ", " + password  # username, password combination

    for line in content:  # search for username,password combination
        if user_pass in line:  # if found
            found = True
            searchfile.close()
            break

    if not bool(found):  # if not found
        print("Username, Password or combination of two is incorrect. Try again\n")

main()
