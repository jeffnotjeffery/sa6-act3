DigitSum = lambda x: sum(int(digit) for digit in str(x) if digit.isdigit())

def get_userinput():
    while True:
        try:
            x = int(input("Enter a positive number to see if I work."))
            if x <= 0:
                raise ValueError("Try again dood")
            return x
        except ValueError as e:
            print(e)

def main():
    input = get_userinput()

    result = (DigitSum(input))

    print(f'The sum of {input} is {result}')


if __name__ == "__main__":
    main()