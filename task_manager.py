#=====importing libraries===========
'''This is the section where you will import libraries'''
import math
import datetime
#====== End of importing ============

# we are openning text files for reading and writing:
today = str(datetime.date.today())


user_tasks = open("tasks.txt","r+",encoding="utf-8")

user_credentials = open("user.txt","r+",encoding="utf-8")

# Reading text files so we can manipulate them and use data:
user_task_read = user_tasks.readlines()


user_credential_read = user_credentials.readlines()


username_list = []

password_list = []

#====Login Section====#
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
print("In order to login you will need to enter your credentials:\n\n")



# Checking if username and password entered are matching one in our database(user.txt file)
# For each line in user.txt file separating username and password in two separate elements in the list so we can use them in our program

# Iteratinh through the usernames and passwords and appending them to 2 separate lists
for name in user_credential_read:
    user_split = name.strip("\n").split(", ")
    username_list.append(user_split[0])
    password_list.append(user_split[1])

# Counting number of tasks so we can display them later
for count, line in enumerate(user_task_read):
    pass
number_of_tasks = (count + 1)

# Using while loop to validate username and password if we can find them in username_list and password_list
while True:
    username = input("Please enter your username:\n\n")

    password = input("Please enter your password:\n\n")

    if username not in username_list or password not in password_list:
        print("You entered incorrect username and/or password")
    elif username in username_list and password in password_list:
        print("You logged in sucessfully")
        break
   
#=====End of Login Section====#


while True:
    #presenting the menu to the user and once we are logged in
    # making sure that the user input is coneverted to lower case
    menu = input('''Select one of the following Options below:

r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds - Display statistics
e - Exit
: \n''').lower()
    #======= Option r =======#
    # If user chose r then means registering new user
    if menu == 'r' and username == "admin":

        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        # Making sure only admin can register users:


        # Requesting new username from the user
        new_username = input("Please enter your new username:\n\n")
        # Requesting new password from the user
        new_password = input("Please enter your new password\n\n")
        #confirming the password
        confirm_password = input("Please confirm your password\n\n")

        # Checking if user confirmed password they entered correctly and writing it to our data file if True
        # We are doing error handling and outputing error message if new password doesn't match
        if new_password != confirm_password:
            print("You entered the wrong password,Please confirm new user's details again")
        else:
            print("You sucessfully registered new user")
            user_credentials.write(f"\n{new_username}, {new_password}")
        break

    #========= End of option r ======#

    #========= Option a ==========#
    elif menu == 'a':
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        
        # Asking user for the username of the person task is assigned to:
        task_username = input("What is the username of the person that will be assigned with this task?\n\n")

        # Asking for task title
        task_title = input("Please enter the task title:\n\n")

        # Asking for description of the task
        task_description = input("Please describe the task:\n\n")

        #Assigning due date to the task
        due_date = input("Please assign due date:\n\n")

        # Getting current date:
        current_date = today

        # Including completion indicator for the new task which is NO by defaulkt when task is being created:
        completion_indicator = "No"

        # Writing new task to the tasks.txt file
        user_tasks.write(f"\n{task_username}, {task_title}, {task_description}, {due_date}, {current_date}, {completion_indicator}")
        
        
        break
    #========== End of option a ===========#

    #========== Option va =============#
    elif menu == 'va':
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        # Reading a line from the tasks.txt file and separating lines into elements in the list
        for pos, line in enumerate(user_task_read,1):
            split_line = line.split(", ")
           
            # Printing formatted task to the console
            output = f"------------[{pos}]---------------\n"
            output += f"Assigned to:\t\t{split_line[0]}\n"
            output += f"Task:\t\t\t{split_line[1]}\n"
            output += f"Description:\t\t{split_line[2]}\n"
            output += f"Assigned Date:\t\t{split_line[3]}\n"
            output += f"Due Date:\t\t{split_line[4]}\n"
            output += f"Is completed\t\t{split_line[5]}\n"
            output += "n"
            output += "------------------------------------"
            
            print(output)
        
    #=========== End of option va ========#

    #=========== Option vm =============#
    elif menu == 'vm':
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        # Reading a line from the tasks.txt file and separating lines into elements in the list
        for pos, line in enumerate(user_task_read,1):
            split_line = line.split(", ")
            # Checking if username of the person logged in is the same as the username we read from the file 
            if username == split_line[0]:
                # Printing formatted task to the console
                output = f"------------[{pos}]---------------\n"
                output += f"Assigned to:\t\t{split_line[0]}\n"
                output += f"Task:\t\t\t{split_line[1]}\n"
                output += f"Description:\t\t{split_line[2]}\n"
                output += f"Assigned Date:\t\t{split_line[3]}\n"
                output += f"Due Date:\t\t{split_line[4]}\n"
                output += f"Is completed\t\t{split_line[5]}\n"
                output += "\n"
                output += "------------------------------------"

                print(output)
        
    #================== End of option vm=======#

    #==================Option ds ===============#
    elif menu == "ds" and username == "admin":
        # Displaying total number of tasks:
        output = f"====================================================\n"
        output += f"Total number of tasks is:\t\t{number_of_tasks}\n"
        output += "\n"
        output += f"Total number of users is:\t\t{len(username_list)}\n"
        output += f"====================================================\n"
        print(output)
    #================= End of option ds =========#

    #================= Exit menu ================#
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    #================= End of exit menu =========#
    else:
        print("You have made a wrong choice,or you need to be administrator in order to use this option.Please Try again")


user_credentials.close()