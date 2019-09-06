from main import correct_input
from enum import Enum, auto
from getpass import getpass
import mysql.connector
import time


dbconfig = {
    'user': 'hugo',
    'password': '123456',
    'host': 'localhost',
    'database': 'appointment_system',
    'raise_on_warnings': True
}


def login():
    while True:
        # user input
        tid = int(input("ID:"))
        password = getpass()

        # database connection
        cnx = mysql.connector.connect(**dbconfig)
        mycursor = cnx.cursor()
        sql = "select password from teacher where tid = %s"
        mycursor.execute(sql, (tid,))
        result = mycursor.fetchall()

        # user not found
        if not result:
            print("User not found! Please check your ID.")
            continue

        # password correct
        if password == result[0][0]:
            # get name and address from table teacher
            sql = "select (name, address) from teacher where tid = {}".format(
                tid)
            mycursor.execute(sql)
            result = mycursor.fetchall()
            (name, address) = result[0]

            # get office hour from table teacher_officehour
            sql = "select (weekday, stime, etime) from teacher_officehour where tid = {}".format(
                tid)
            mycursor.execute(sql)
            result = mycursor.fetchall()
            # for row in result:

        mycursor.close()
        cnx.close()
        t = Teacher(tid, name, None, address)
        return (t, True)


class Teacher:
    def __init__(self, tid, name, office_hour, address):
        self.id = tid
        self.name = name
        self.office_hour = office_hour
        self.address = address

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


class OfficeHour:
    class Weekday(Enum):
        SUN = 0
        MON = 1
        TUE = 2
        WED = 3
        THU = 4
        FRI = 5
        SAT = 6

    def __init__(self, weekday, stime, etime):
        self.weekday = weekday
        self.stime = stime
        self.etime = etime
