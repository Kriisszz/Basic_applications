# Creating email class containing the required objects and function

class Email:

    # Class variable created
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        self.has_been_read = True


# Filling up the inbox list.
inbox = []


def populate_inbox():
    inbox.append(Email("noreply@cogrammar.com", "Welcome to HyperionDev", "glad to see you here"))
    inbox.append(Email("noreply@cogrammar.com", "Great work on the bootcamp!", "You are doing very well"))
    inbox.append(Email("noreply@cogrammar.com", "Your excellent marks!", "Lets see your excellent marks"))
    return inbox


def list_emails(inbox):
    """Creates a function which prints the emails subject_line,
along with a corresponding number."""

    count = 0
    print("Emails")
    while count < len(inbox):
        print(count, ": ", inbox[count].subject_line)
        count = count + 1


def read_email(Email):
    """ This function is to read emails, takes in a user input
    to read the chosen email and marks the email as read
    with the "mark_as_read" function """

    list_emails(inbox)

    while True:

        try:
            user_choice = int(input("Press a number to read the selected message or 3 to Main Menu"))
            if user_choice == 0:

                """Each choice has got a while loop going through
                the list with the user asked index."""
                email_object = inbox[user_choice]
                print("The sender is:",
                      email_object.email_address,
                      "\n", "Subject: ", email_object.subject_line,
                      "\n", "Message is:", email_object.email_content)
                email_object.mark_as_read()

            elif user_choice == 1:
                email_object = inbox[user_choice]
                print("The sender is:",
                      email_object.email_address, "\n", "Subject: ",
                      email_object.subject_line, "\n", "Message is:",
                      email_object.email_content)
                email_object.mark_as_read()

            elif user_choice == 2:
                email_object = inbox[user_choice]
                print("The sender is:",
                      email_object.email_address, "\n", "Subject: ",
                      email_object.subject_line, "\n", "Message is:",
                      email_object.email_content)
                email_object.mark_as_read()

            elif user_choice == 3:
                break
            else: print("Invalid number, please choose 0, 1, 2 or 3 to go back!")
        except ValueError: print("Invalid character, please choose a number!")


# Calling populate_inbox function.
populate_inbox()

"""Menu with multiple options, loop breaks when user press number 3.
Also implemented a try and except error handling so
the values can only be an integer type."""
while True:
    try:
        user_choice = int(input('''\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: '''))

        if user_choice == 1:
            read_email(inbox)
        elif user_choice == 2:
            count = 0
            print("Unread Emails:")
            while count < len(inbox):
                unread_email = inbox[count]
                if unread_email.has_been_read == False:
                    print(unread_email.subject_line)
                else: pass
                count = count + 1

        elif user_choice == 3:
            break

        else:
            print("Oops - incorrect input.")
    except ValueError: print("Invalid character, please choose a number!")
