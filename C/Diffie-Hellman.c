#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double diffie_hellman() {
    // Choose public parameters
    double g = 2;
    double N = 17678;
    
    // Party A chooses a random value for r
    double r_a = rand() % (N-1) + 1;
    // Party A computes g^r mod N and sends it to party B
    double m_a = pow(g, r_a)%N;
    
    // Party B chooses a random value for r
    double r_b = rand() % (N-1) + 1;
    // Party B computes g^r mod N and sends it to party A
    double m_b = pow(g, r_b) % N;
    
    // Both parties compute the shared secret key
    double k_a = pow(m_b, r_a) % N;
    double k_b = pow(m_a, r_b) % N;
    
    // Check that the shared secret keys match
    if (k_a != k_b) {
        printf("Error: Shared secret keys do not match\n");
        exit(1);
    }
    
    // Return the shared secret key
    return k_a;
}

double main() {
    // Seed the random number generator
    srand(time(NULL));
    
    // Example usage
    double k = diffie_hellman();
    printf("Shared secret key: %d\n", k);
    
    return 0;
}