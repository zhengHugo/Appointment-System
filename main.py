# main function for running


def main():
    print("---------------welcome---------------")
    print("student or teacher?")
    # while(identity != '1' or identity != '2'):
    #     # print(identity)
    #     identity = input("1. student \t 2. teacher\n")
    # if (identity == 1):
    #     print(1)
    # elif (identity == 2):
    #     print(2)

    while True:
        try:
            identity = input("1. student \t 2. teacher \n")
            assert identity == '1' or identity == '2'
        except AssertionError:
            print("\nWrong input! Please select 1 or 2\n")
            continue
        break
    if identity ==1:
        studentbussi1 = input('what do you want to do today? \n 1. View/edit my appointments \n 2. Apply for a new appointment \n 3. Change password \n')
        if studentbuss1 == 1:
                # view pr edit appointment
        elif studentbussi1 == 2 :
                # apply #
        elif studentbussi1 ==3 :
                #change#

        #search system#
    else:
        teacherbussi1 = input('what do you what to do taday? \n 1.Set office hours \n 2. View/edit my appointments \n 3.Change password')



if __name__ == "__main__":
    main()
