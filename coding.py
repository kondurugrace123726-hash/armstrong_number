
def is_armstrong(n):
    original = n
    num_digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** num_digits
        n //= 10

    return total == original


if __name__ == "__main__":
    number = int(input().strip())

    if is_armstrong(number):
        print("Armstrong")
    else:
        print("Not Armstrong")

        