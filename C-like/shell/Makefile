TARGET=wsh
SOURCES := $(wildcard *.c)
OBJECTS=$(SOURCES:.c=.o)

CFLAGS=-Wall

all: $(TARGET) $(OBJECTS)

$(TARGET): $(OBJECTS)
	cc -s $(CFLAGS) -o $(TARGET) $(OBJECTS)

debug: $(TARGET) $(OBJECTS)
	cc -g $(CFLAGS) -o $(TARGET) $(OBJECTS)

clean:
	rm -v *.o $(TARGET)

.c.o:
	cc -c -g $(CFLAGS) $< -o $@
