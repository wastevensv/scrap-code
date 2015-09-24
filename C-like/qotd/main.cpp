#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cstring>
#include <unistd.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include <signal.h>
#include <time.h>

using namespace std;

void log(string msg) {
    cerr << msg << endl;
}

void error(string msg, int code) {
    log(msg);
    exit(code);
}

void term(int s) {
    error("\nShutting down QOTD server...",0);
}

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
    int sockfd, newsockfd; // File descriptors for system calls.
    int portno; // Port number to listen on.
    int clilen; // Size of the client address.

    struct sockaddr_in serv_addr, cli_addr; // Structures to hold internet addresses

    log("QOTD Server started. Press CTRL-C to exit.");
    if(argc < 2) { // Set port number
        portno=3017;
        log("WARN, no port provided. (Default: 3017)");
    } else {
        portno=atoi(argv[1]);
    }

    sockfd = socket(AF_INET, SOCK_STREAM, 0); // Attempt to open socket
    if(sockfd < 0)
        error("ERROR, could not open socket", 1);

    memset((char *) &serv_addr, 0, sizeof(serv_addr)); // Zero serv_addr structure

    // Setup server address structure
    serv_addr.sin_family = AF_INET; // Internet address
    serv_addr.sin_port = htons(portno); // TCP port number
    serv_addr.sin_addr.s_addr = INADDR_ANY; // Bind to any host address

    if(bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
        error("ERROR, could not bind IP address.", 2);

    listen(sockfd,5); // Listen, allowing up to 5 clients waiting.
    
    ifstream qfile ("test.qotd");

   
    signal(SIGINT,term);

    while(1) {

        clilen = sizeof(cli_addr);
        newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, (socklen_t*) &clilen); // Wait for a connection
        if(newsockfd < 0)
            error("ERROR, could not accept connection", 3);

        srand(time(NULL)); // Initialize random number generator
        if (qfile.is_open()) {
            qfile.seekg(0, qfile.beg);

            int m = atoi(getQuote(qfile).c_str()) - 1; // First 'quote' is actually the number of quotes in the file.
            for(int n = rand() % m; n>=0; n--) {
                getQuote(qfile);
            }

      	    string quote = getQuote(qfile) + '\n'; // Add newline to quote
            int ret = write(newsockfd, quote.c_str(), quote.length() ); // Send quote ver socket
            if( ret < 0 ) error("ERROR, could not write message", 4);
            else log("LOG, quote sent to client");
        } else {
            error("ERROR, Opening file failed", 404);
        }
        close(newsockfd);
    }
    qfile.close();
    close(sockfd);
    return 0;
}
