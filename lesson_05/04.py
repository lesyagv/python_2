import sys

def print_help():
    print("usage: square.py number [-h]\n")
    print("positional arguments:")
    print("  number         display the square of a given number\n")
    print("options:")
    print("  -h | --help    show this help message and exit")

def square_number(number):
    return number ** 2

def main():
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print_help()
    elif len(sys.argv) == 2:
        try:
            number = float(sys.argv[1])
            result = square_number(number)
            print(f"The square of {number} is: {result}")
        except ValueError:
            print("Error: Please provide a valid number.")
    else:
        print("Error: Invalid number of arguments.")
        print_help()

if __name__ == "__main__":
    main()