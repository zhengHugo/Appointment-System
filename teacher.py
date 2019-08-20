from main import correct_input


def login():
    username = input("ID:")
    password = input("Password:")
    # Query in Database
    # id = ....
    # name = ..
    # office_hour = ....
    t = Teacher(username, None, None)
    return (t, True)


class Teacher:
    def __init__(self, id, name, office_hour):
        self.id = id
        self.name = name
        self.office_hour = office_hour

    def main(self):
        print("Welcome, {}!".format(self.name))
        print("What do you want to do today?")
        option = int(correct_input(
            "1. Set office hours\n 2. View/edit my appointments\n 3. Change password", lambda x: x == '1' or x == '2' or x == '3'))
        if option == 1:
            self.setOfficeHour()
        elif option == 2:
            self.viewMyAppointments()
        else:
            self.changePassword()
        return

    def setOfficeHour(self):
        return

    def viewMyAppointments(self):
        return

    def changePassword(self):
        return
