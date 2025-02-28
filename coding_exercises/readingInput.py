# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if __name__ == "__main__":
    n = int(input().strip())

    phone_book = {}

    # Read phone book entries
    for _ in range(n):
        entry = input().strip().split(' ')
        phone_book[entry[0]] = entry[1]

    # Read names and look up numbers
    try:
        for line in sys.stdin:
            name = line.strip()
            if name in phone_book:
                print(f"{name}={phone_book[name]}")
            else:
                print("Not found")
    except EOFError:
        pass  # Handles end-of-input gracefully
