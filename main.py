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

    try:
        identity = input("1. student \t 2. teacher\n")
        assert identity == '1' or identity == '2'
        print(identity)
    except AssertionError:
        print("\nWrong input! Please select 1 or 2\n")


if __name__ == "__main__":
    main()
