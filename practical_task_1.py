# Parent class
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
# This method is to show contact details

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
# This method is to show the location of the head office

    def location_details(self):
        print("The head office location is: Cape Town")
# Subclass with the constructor that initializes 2 attributes.


class OopCourse(Course):
    def __init__(self, description="OOP Fundamentals",
                 trainer="Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer

    # Method to print the details of the trainer (or course)(4th instruction)
    def trainer_details(self):
        print("The course is about", self.description,
              "and the name of the trainer is ", self.trainer)

    # Method to print the Course Id
    def show_course_id(self):
        print("The course ID is #12345")


# Create an object of the subclass
course1 = OopCourse()

# Call the methods
course1.contact_details()

course1.trainer_details()

course1.show_course_id()
