#Creating email class containing the required objects and function

class Email():
    #I dont see the point "has_been_read" as a class variable but I followed the instructions.
    
    has_been_read=bool(False)
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    def mark_as_read(has_been_read,Email):
        has_been_read = True
        return bool(Email.has_been_read)
#Filling up the inbox list.

def populate_inbox(inbox,Email):
    inbox.append(Email("noreply@cogrammar.com", "Welcome to HyperionDev", "glad to see you here"))
    inbox.append(Email("noreply@cogrammar.com","Great work on the bootcamp!","You are doing very well"))
    inbox.append(Email("noreply@cogrammar.com","Your excellent marks!","Lets see your excellent marks"))
    return inbox
# Create a function which prints the emails subject_line, along with a corresponding number.

def list_emails(Email,inbox):
    count=0
    print("Unread mails")
    while count<len(inbox):
        print(count, ": ", inbox[count].subject_line)
        count = count + 1

def read_email(Email,inbox):
#Creating menu to read emails or go back if number 3 is pressed
    
    while True:
        try:
            user_choice=int(input("Press a number to read the selected message or 3 to Main Menu"))
            if user_choice == 0:
                count_sub=0
                #Each choice has got a while loop going through the list with the user asked index.
                
                while count_sub < 1:
                    print("The sender is:", inbox[user_choice].email_address, "\n", "Subject: ", inbox[user_choice].subject_line, "\n","Message is:", inbox[user_choice].email_content)
                    count_sub = count_sub+1
                    Email.mark_as_read(Email.has_been_read,Email)
            elif user_choice == 1: 
                count_sub=0
                while count_sub < 1:
                    print("The sender is:", inbox[user_choice].email_address, "\n", "Subject: ", inbox[user_choice].subject_line, "\n","Message is:", inbox[user_choice].email_content)
                    count_sub = count_sub+1
                    Email.mark_as_read(Email.has_been_read,Email)
            elif user_choice == 2: 
                count_sub=0
                while count_sub < 1:
                    print("The sender is:", inbox[user_choice].email_address, "\n", "Subject: ", inbox[user_choice].subject_line, "\n","Message is:", inbox[user_choice].email_content)
                    count_sub = count_sub+1
                    Email.mark_as_read(Email.has_been_read,Email)
            elif user_choice == 3:
                break
            else: print("invalid number, please choose 0, 1, 2 or 3 to go back!")
        except ValueError: print("Invalid character, please choose a number!")
#Creating an empty list for inbox.

inbox=[]
#Calling populate_inbox function.

inbox = populate_inbox(inbox,Email)
 
#Menu with multiple options, loop breaks when user press number 3.
#Also implemented a try and except error handling so the values can only be an integer type.
while True:
    try:
        user_choice = int(input('''\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: '''))
        
        if user_choice == 1:
            read_email(Email,inbox)
        elif user_choice == 2:
            list_emails(Email,inbox)
            
        elif user_choice == 3:
            break

        else:
            print("Oops - incorrect input.")
    except ValueError: print("Invalid character, please choose a number!")

