import mysql.connector
from main import correct_input
from main import main
from getpass import getpass
from teacher import dbconfig
# Student.py for handling students requests


def login():
    sid = int(input("ID:"))
    password = getpass()

    # database connection
    cnx = mysql.connector.connect(**dbconfig)
    mycursor = cnx.cursor()
    sql = "select name, password from student where sid = %s"
    mycursor.execute(sql, (sid,))
    result = mycursor.fetchall()
    mycursor.close()
    cnx.close()

    # user not found
    if not result:
        return (None, False)

    if password == result[0][1]:
        student = Student(sid, result[0][0])

    return (student, True)


class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

    def main(self):
        print("Welcome, {}!".format(self.name))
        print("What do you want to do today!")
        print("1. View/edit my appointments")
        print("2. Apply for a new appointment")
        print("3. Change my password")
        print("4. Exit")
        option = int(correct_input(
            "", lambda x: x == '1' or x == '2' or x == '3' or x == '4'))
        if option == 1:
            self.viewMyAppointments()
        elif option == 2:
            self.newAppointment()
        elif option == 3:
            self.changePassword()
        else:
            main()

        return

    def viewMyAppointments(self):
        return

    def newAppointment(self):
        return

    def changePassword(self):
        return
