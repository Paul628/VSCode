def generate_primes(limit):
    # Generate a sequence of prime numbers using the Sieve of Eratosthenes algorithm
    primes = []
    is_prime = [True] * limit  # initialize all numbers as potentially prime
    for n in range(2, len(is_prime)):
        if is_prime[n]:
            primes.append(n)
            for multiple in range(n * n, len(is_prime), n):
                is_prime[multiple] = False
    return primes

prime_number = int(input("Enter a prime number: "))
try:
    primes = generate_primes(prime_number * 20)  # generate enough primes to cover the input
    index = primes.index(prime_number) + 1  # add 1 because the list is 0-indexed
    print(f"The index of {prime_number} is: {index}")
except ValueError:
    print(f"{prime_number} is not a prime number.")
