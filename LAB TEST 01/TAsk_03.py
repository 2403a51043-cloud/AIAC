def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    first = int(input("Enter the first number: "))
    last = int(input("Enter the last number: "))
    primes = []
    for num in range(first, last+1):
        if is_prime(num):
            primes.append(num)
    if primes:
        print("Prime numbers between {} and {}:".format(first, last))
        print(", ".join(str(p) for p in primes))
    else:
        print("No prime numbers found in the given range.")
