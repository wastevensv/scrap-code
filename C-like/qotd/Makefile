CC=gcc
CXX=g++
RM=rm -f

#LD_LIBRARY_PATH=/lib64
CCFLAGS=-l linux-vdso.so libstdc++.so libm.so libgcc_s.so libc.so

TARGET=main
SRC=$(TARGET).cpp
OBJ=$(TARGET).o
EXE=qotd

all: main

run: main
	./$(OBJ)

main: $(OBJ)
	$(CXX) $(SRC) -o $(OBJ)

$(OBJ): $(SRC)

clean:
	$(RM) $(OBJ)
