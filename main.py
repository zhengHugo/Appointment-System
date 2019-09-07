# main function for running
import student
import teacher


def main():
    print("---------------Welcome---------------")
    print("student or teacher?")

    identity = int(correct_input(
        "1. Student \t 2. Teacher \t 3. Exit", lambda x: x == '1' or x == '2' or x == '3'))
    if identity == 1:
        while True:
            success = student.login()
            if success:
                student.main()
                break
            else:
                print("Incorrect ID or password!\n Please try again or exit\n")
                option = int(correct_input(
                    "\n1. Try again\n 2. Exit", lambda x: x == '1' or x == '2'))
                if (option == 1):
                    continue
                else:
                    return
    elif identity == 2:
        while True:
            (t, success) = teacher.login()
            if success:
                t.main()
                break
            else:
                print("Incorrect ID or password!\n Please try again or exit\n")
                option = int(correct_input(
                    "\n1. Try again\n 2. Exit", lambda x: x == '1' or x == '2'))
                if (option == 1):
                    continue
                else:
                    return
    else:
        exit(0)


def correct_input(msg, evaluate):
    while True:
        try:
            option = input(msg)
            assert evaluate(option)
        except AssertionError:
            print("\nPlease try again\n")
            continue
        break
    return option


if __name__ == "__main__":
    main()
