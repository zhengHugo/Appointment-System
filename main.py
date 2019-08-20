# main function for running


def main():
    print("---------------Welcome---------------")
    print("student or teacher?")

    while True:
        try:
            identity = input("1. student \t 2. teacher\n")
            assert identity == '1' or identity == '2'
        except AssertionError:
            print("\nWrong input! Please select 1 or 2\n")
            continue
        break


if __name__ == "__main__":
    main()
