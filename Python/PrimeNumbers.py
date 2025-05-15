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

index = input("Enter the index of the prime number you want to find: ")
try:
    index = int(index)
    if index <= 0:
        raise ValueError
    primes = generate_primes(index * 20)  # generate enough primes to cover the index
    prime_number = primes[index - 1]  # index - 1 because the list is 0-indexed
    print(f"The {index}th prime number is: {prime_number}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
