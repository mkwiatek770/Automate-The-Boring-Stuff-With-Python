
def colatz(number: int) -> int:
    if number % 2 == 0:
        return number // 2
    return number * 3 + 1


if __name__ == "__main__":
    while True:
        try:
            user_input = int(input("Type integer: "))
            break
        except ValueError:
            print("Please type integer!")

    result = user_input
    while result != 1:
        result = colatz(result)
        print(result)
