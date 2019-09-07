from getpass import getpass
import mysql.connector
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

        return
    # studentbussi1 = input(
    #     'what do you want to do today? \n 1. View/edit my appointments \n 2. Apply for a new appointment \n 3. Change password \n')
    # if studentbussi1 == 1:
    #             # view pr edit appointment
    # elif studentbussi1 == 2:
    #             # apply #
    #     elif studentbussi1 == 3:
    #             #change#
