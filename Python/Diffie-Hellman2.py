import random

def generate_public_key(g, N, private_key):
    # Compute the public key as g^private_key mod N
    public_key = pow(g, private_key, N)
    return public_key

def generate_shared_secret(public_key, N, private_key):
    # Compute the shared secret as public_key^private_key mod N
    shared_secret = pow(public_key, private_key, N)
    return shared_secret

# Example usage
g = 2   # Public parameter
N = 17681  # Public parameter

# Party A chooses a random secret exponent
private_key_a = random.randint(1, N-1)

# Party A generates their public key and sends it to party B
public_key_a = generate_public_key(g, N, private_key_a)
print("Party A public key:", public_key_a)

# Party B chooses a random secret exponent
private_key_b = random.randint(1, N-1)

# Party B generates their public key and sends it to party A
public_key_b = generate_public_key(g, N, private_key_b)
print("Party B public key:", public_key_b)

# Party A computes the shared secret using their private key and party B's public key
shared_secret_a = generate_shared_secret(public_key_b, N, private_key_a)
print("Party A shared secret:", shared_secret_a)

# Party B computes the shared secret using their private key and party A's public key
shared_secret_b = generate_shared_secret(public_key_a, N, private_key_b)
print("Party B shared secret:", shared_secret_b)
