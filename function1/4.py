def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime():
    numbers = list(map(int, input("Enter numbers: ").split()))
    primes = list(filter(prime, numbers))
    print("Prime numbers:", primes)

filter_prime()
