import random
from math import gcd

def generate_keypair(p, q):
    # Step 1: Choose two large prime numbers
    n = p * q
    phi_n = (p-1) * (q-1)

    # Step 2: Choose an integer e such that 1 < e < phi_n and gcd(e, phi_n) = 1
    e = random.randrange(1, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randrange(1, phi_n)

    # Step 3: Compute the integer d such that d*e = 1 (mod phi_n)
    d = pow(e, -1, phi_n)

    # Return the public key (n, e) and the private key (n, d)
    return (n, e), (n, d)

def encrypt(public_key, message):
    # Extract the public key components n and e
    n, e = public_key

    # Convert the message to an integer
    m = int.from_bytes(message.encode(), 'big')

    # Compute the ciphertext c = m^e (mod n)
    c = pow(m, e, n)

    # Return the ciphertext as a bytes object
    return c.to_bytes((c.bit_length() + 7) // 8, 'big')

def decrypt(private_key, ciphertext):
    # Extract the private key components n and d
    n, d = private_key

    # Convert the ciphertext to an integer
    c = int.from_bytes(ciphertext, 'big')

    # Compute the plaintext m = c^d (mod n)
    m = pow(c, d, n)

    # Convert the plaintext to a string
    return m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()

# Example usage
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

message = "Hello, world!"
ciphertext = encrypt(public_key, message)
plaintext = decrypt(private_key, ciphertext)

print("Original message:", message)
print("Ciphertext:", ciphertext)
print("Plaintext:", plaintext)
