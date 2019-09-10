
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
