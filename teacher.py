from tabulate import tabulate
from enum import Enum
from getpass import getpass
from util import correct_input
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
    # user input
    # TODO: try convert input into integer directly
    tid = input("ID:")
    password = getpass()

    # database connection
    cnx = mysql.connector.connect(**dbconfig)
    mycursor = cnx.cursor()
    sql = "select password from teacher where tid = %s"
    mycursor.execute(sql, (tid,))
    result = mycursor.fetchall()

    # user not found
    if not result:
        return (None, False)

    # password correct
    if password == result[0][0]:
        # get name and address from table teacher
        sql = "select name, address from teacher where tid = {}".format(
            tid)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        (name, address) = result[0]

        # get office hour from table teacher_officehour
        sql = "select weekday, stime, etime from teacher_officehour where tid = {}".format(
            tid)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        officeHour = []
        for row in result:
            officeHour = officeHour.append(
                OfficeHour(OfficeHour.Weekday(row[0]), row[1], row[2]))
    else:
        return (None, False)

    mycursor.close()
    cnx.close()
    t = Teacher(tid, name, officeHour, address)
    return (t, True)


class Teacher:
    def __init__(self, tid, name, office_hour, address):
        self.tid = tid
        self.name = name
        self.office_hour = office_hour
        self.address = address

    def main(self):
        print("What do you want to do today?")
        print("1. Set office hours")
        print("2. View edit my appointments")
        print("3. Change password")
        print("4. Exit")
        option = int(correct_input(
            "", lambda x: x == '1' or x == '2' or x == '3' or x == '4'))
        if option == 1:
            self.setOfficeHour()
        elif option == 2:
            self.viewMyAppointments()
        elif option == 3:
            self.changePassword()
        else:
            print("Bye!")
        return

    def setOfficeHour(self):
        return

    def viewMyAppointments(self):

        # fetch data from database
        cnx = mysql.connector.connect(**dbconfig)
        cursor = cnx.cursor()
        sql = "select id, student.sid, name, date, stime, etime, status from appointment join student on student.sid = appointment.sid"
        cursor.execute(sql)
        appointments = cursor.fetchall()
        cursor.close()
        cnx.close()

        # prepare data for presentation
        appointments = [list(row) for row in appointments]
        aids = [row[0] for row in appointments]  # appointment true id
        statuses = ['Initiated', 'Approved',
                    'Completed', 'Refused', 'Canceled', 'Missed']
        for i in range(len(appointments)):
            # parse status
            appointments[i][6] = statuses[appointments[i][6]]

            # add fake id to appointment (for user to select)
            appointments[i][0] = i + 1

            # Trim off seconds in time
            appointments[i][4] = str(appointments[i][4])[:5]
            appointments[i][5] = str(appointments[i][5])[:5]
        print(tabulate(appointments, headers=[
              '', 'Student ID', 'Student name', 'Date', 'From', 'To', 'Status'], tablefmt='orgtbl'))

        # Let user select
        print(
            "Select which appointment you want to edit, or type 0 to go back to main menu")
        option = correct_input("", lambda x: x in list(
            map(str, range(len(appointments)+1))))
        if option == '0':
            self.main()
        else:
            self.editAppointment(aids[int(option)-1])
        return

    def changePassword(self):
        return

    def editAppointment(self, aid):
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
