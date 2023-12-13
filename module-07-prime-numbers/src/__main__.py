from sys import argv
from recursive_prime_numbers import is_prime


def main():
    args = len(argv)
    start = 0
    end = 11

    if args > 1:
        # => ./src {to}
        end = int(argv[1])

    if args > 2:
        # => ./src {from} {to}
        start = int(argv[1])
        end = int(argv[2])

    for i in range(start, end + 1):
        result = "is prime number" if is_prime(i) else "is not prime number"
        print(f"'{i}' {result}")


if __name__ == "__main__":
    main()
