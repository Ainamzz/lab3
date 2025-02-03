numbers = list(map(int, input("Enter numbers:").split()))

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, x))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)
