#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;

int diffie_hellman() {
    // Choose public parameters
    int g = 2;
    int N = 17678;
    
    // Party A chooses a random value for r
    int r_a = rand() % (N-1) + 1;
    // Party A computes g^r mod N and sends it to party B
    int m_a = pow(g, r_a) % N;
    
    // Party B chooses a random value for r
    int r_b = rand() % (N-1) + 1;
    // Party B computes g^r mod N and sends it to party A
    int m_b = pow(g, r_b) % N;
    
    // Both parties compute the shared secret key
    int k_a = pow(m_b, r_a) % N;
    int k_b = pow(m_a, r_b) % N;
    
    // Check that the shared secret keys match
    assert(k_a == k_b);
    
    // Return the shared secret key
    return k_a;
}

int main() {
    // Seed the random number generator
    srand(time(NULL));
    
    // Example usage
    int k = diffie_hellman();
    cout << "Shared secret key: " << k << endl;
    
    return 0;
}