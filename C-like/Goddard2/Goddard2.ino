#define LE 9
#define LF 11
#define LR 8

#define RE 10
#define RF 13
#define RR 12

#define I_LEFT  0
#define I_RIGHT 1
#define I_TIME  2

int incomingByte;

// Byte to indicate start of command.
byte startByte = 0x42;
// Format: [('1'-'5') Left Speed, ('1'-'5') Right Speed, ('1'-'9') Duration/100ms]
// Speeds: '1' - Full Forward, '3' - 0, '5'- Full Reverse
byte command[3];

void drive(byte left, byte right, byte time) {
  digitalWrite(LE, 0);
  digitalWrite(RE, 0);
  
  time = time - '0';
  if(time == 0) time = 10;
  byte leftSpeed  = 0;  
  byte rightSpeed = 0;  

  switch(left) {
    case '1':
      digitalWrite(LF, 1);
      digitalWrite(LR, 0);
      leftSpeed = 255;
      break;
    case '2':
      digitalWrite(LF, 1);
      digitalWrite(LR, 0);
      leftSpeed = 127;
      break;
    case '3':
      digitalWrite(LF, 0);
      digitalWrite(LR, 0);
      leftSpeed = 0;
      break;
    case '4':
      digitalWrite(LF, 0);
      digitalWrite(LR, 1);
      leftSpeed = 127;
      break;
    case '5':
      digitalWrite(LF, 0);
      digitalWrite(LR, 1);
      leftSpeed = 255;
      break;
  }

  switch(right) {
    case '1':
      digitalWrite(RF, 1);
      digitalWrite(RR, 0);
      rightSpeed = 255;
      break;
    case '2':
      digitalWrite(RF, 1);
      digitalWrite(RR, 0);
      rightSpeed = 127;
      break;
    case '3':
      digitalWrite(RF, 0);
      digitalWrite(RR, 0);
      rightSpeed = 0;
      break;
    case '4':
      digitalWrite(RF, 0);
      digitalWrite(RR, 1);
      rightSpeed = 127;
      break;
    case '5':
      digitalWrite(RF, 0);
      digitalWrite(RR, 1);
      rightSpeed = 255;
      break;
  }

  analogWrite(LE, leftSpeed);
  analogWrite(RE, rightSpeed);
  delay(time*100);
  digitalWrite(LE, 0);
  digitalWrite(RE, 0);
}

void setup() {
  pinMode(LE, OUTPUT);
  pinMode(LF, OUTPUT);
  pinMode(LR, OUTPUT);
  pinMode(RE, OUTPUT);
  pinMode(RF, OUTPUT);
  pinMode(RR, OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    if(Serial.read() == startByte) {
      // Read command.
      while (Serial.available() < 3);
      command[I_LEFT] = Serial.read();
      command[I_RIGHT] = Serial.read();
      command[I_TIME] = Serial.read();
      // Parse command.
      drive(command[I_LEFT], command[I_RIGHT], command[I_TIME]);
    }
  }
}
