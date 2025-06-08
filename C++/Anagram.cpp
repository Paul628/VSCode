// C++ Program to generate all unique
// permutations of a string
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <chrono>
using namespace std;
using namespace std::chrono;

// Recursive function to generate 
// all permutations of string s
void recurPermute(int index, string &s,
                    vector<string> &ans) {

    // Base Case
    if (index == s.size()) {
        ans.push_back(s);
        return;
    }

    // Swap the current index with all
    // possible indices and recur
    for (int i = index; i < s.size(); i++) {
        swap(s[index], s[i]);
        recurPermute(index + 1, s, ans);
        swap(s[index], s[i]);
    }
}

// Function to find all unique permutations
set<string> findPermutation(string &s) {

    // Stores the final answer
    vector<string> ans;

    recurPermute(0, s, ans);

    // sort the resultant vector
    sort(ans.begin(), ans.end());

    // Insert all elements of ans into a set
    set<string> finalAns;
    for (auto x : ans) {
        finalAns.insert(x);
    }

    return finalAns;
}


int main() {
    string s = "Spellblade";
    auto start = high_resolution_clock::now();
    set<string> res = findPermutation(s);
    auto stop = high_resolution_clock::now();
    cout << "Time taken: "
         << duration_cast<microseconds>(stop - start).count()
         << " microseconds" << endl
         << "Number of unique permutations: "
         << res.size() << endl;
    /*for(auto x: res) {
        cout << x << " ";
    }*/
    return 0;
}