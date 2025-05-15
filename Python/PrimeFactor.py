def prime_factors(n):
    factors = set()
    p = 2  # start with the smallest prime number
    iterations = 0
    
    while n > 1:
        while n % p == 0:
            factors.add(p)
            n = n/p
            iterations += 1
        p += 1


    return factors, iterations

while True:
    user_input = input("Enter a positive integer (enter 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        n = int(user_input)
        factors, iterations = prime_factors(n)
        print(f"\nThe prime factors of {n} are: \n{factors}\n")
        print(f"The algorithm took {iterations} iterations to find them.\n")
    except ValueError:
        print("Invalid input. Please enter a positive integer or 'exit' to quit.\n")
