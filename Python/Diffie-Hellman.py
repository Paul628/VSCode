import random

def diffie_hellman():
    # Choose public parameters
    g = 2
    N = 17681  # 17681 is a prime number. Prime numbers are a good chouice to make the DLP difficult.(Cyclic Group)
    
    # A chooses a random value for r
    r_a = random.randint(1, N-1)

    # A computes g^r mod N and sends it to B
    m_a = pow(g, r_a, N)
    
    # B chooses a random value for r
    r_b = random.randint(1, N-1)

    # B computes g^r mod N and sends it to party A
    m_b = pow(g, r_b, N)
    
    # Both compute the shared secret key
    k_a = pow(m_b, r_a, N)
    k_b = pow(m_a, r_b, N)
    
    # Check that the shared secret keys match
    assert k_a == k_b
    
    # Return the shared secret key
    return k_a

k = diffie_hellman()
print("Shared secret key:", k)
