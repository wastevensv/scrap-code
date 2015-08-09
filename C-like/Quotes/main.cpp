#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <time.h>

using namespace std;

string getQuote(ifstream &qfile) {
    string quote;
    char c;
    while(qfile.get(c)) {
        if(c == '*') break;
        quote += c;
    }
    return quote;
}

int main(int argc, char** argv) {
    srand(time(NULL));
    ifstream qfile ("test.qotd");
    if (qfile.is_open()) {
        char c = 0;
        while(c != 'n') {
            qfile.seekg(0, qfile.beg);
            int m = atoi(getQuote(qfile).c_str()) - 1; // First 'quote' is actually the number of quotes in the file.
            for(int n = rand() % m; n>=0; n--) {
                getQuote(qfile);
            }
            cout << endl << getQuote(qfile) << endl;
            cout << "Continue? (y/n): ";
            cin >> c;
        }
    } else {
        cerr << "File IO Error" << endl;
        return 404;
    }
    qfile.close();
    return 0;
}
