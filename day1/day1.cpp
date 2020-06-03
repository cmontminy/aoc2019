// DAY 1: Fuel required to launch a given module is based on its mass. 
// Specifically, to find the fuel required for a module, take its mass, 
// divide by three, round down, and subtract 2.

#include <iostream>  
#include <fstream>
  
using namespace std;

void part_one(ifstream&);
void part_two(ifstream&);

int main() { 
    ifstream input ("input.txt");
    if (input.is_open()) {
        //part_one(input);
        part_two(input);
    }
    input.close();
    return 0;
} 

void part_one(ifstream& input) {
    int sum = 0;
    int line;

    while (input >> line) {
        sum += (line / 3) - 2;
    }

    cout << sum << "\n";
}

void part_two(ifstream& input) {
    int sum = 0;
    int line;

    while (input >> line) {
        line = (line / 3) - 2;
        while (line > 0) {
            sum += line;
            line = (line / 3) - 2;
        }
    }

    cout << sum << "\n";
}
