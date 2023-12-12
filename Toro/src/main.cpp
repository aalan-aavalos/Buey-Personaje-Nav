#include <Arduino.h>

#include <Adafruit_Sensor.h>

#include <ESP32Servo.h> 
#include <HCSR04.h> //Sensor
#include <Stepper.h>

const int stepsPerRevolution = 2048;  // change this to fit the number of steps per revolution

// ULN2003 Motor Driver Pins
#define IN1 26
#define IN2 25
#define IN3 33
#define IN4 32

#define BUZZZER_PIN 4

int ledRojo = 2;
int ledsAmarillo = 23;
int ledsVerde = 22;

//Proximidad
int trigPin = 12;
int echoPin = 13;

int servoPin = 18;

float dist = 0;

Servo myservo;  // create servo object to control a servo
HCSR04 hc(trigPin, echoPin); //Objeto del sensor de distancia
Stepper myStepper(stepsPerRevolution, IN1, IN3, IN2, IN4);

void setup() {
  Serial.begin(115200);

  myservo.setPeriodHertz(50); // Standard 50hz servo
  myservo.attach(servoPin, 500, 2400); 

  myStepper.setSpeed(15); //Stepper
  
  pinMode(ledRojo, OUTPUT);

  pinMode(ledsAmarillo, OUTPUT);
  pinMode(ledsVerde, OUTPUT);
}

void loop() {  
  dist = hc.dist();
  Serial.println(dist);
  digitalWrite(ledRojo, HIGH);
  
  if(dist < 5.00){
    //nojao
    digitalWrite(ledRojo, LOW);
    delay(100);
    digitalWrite(ledRojo, HIGH);
    delay(100);
    digitalWrite(ledRojo, LOW);
    delay(100);
    digitalWrite(ledRojo, HIGH);
    delay(100);
    digitalWrite(ledRojo, LOW);
    delay(100);
    digitalWrite(ledRojo, HIGH);
    delay(100);
    digitalWrite(ledRojo, LOW);
    delay(100);
    digitalWrite(ledRojo, HIGH);
    delay(100);
    digitalWrite(ledRojo, LOW);
    delay(100);
    digitalWrite(ledRojo, HIGH);
    delay(100);
  
    myservo.write(0);
    delay(500);  
    myservo.write(180);
    delay(500);  

    myservo.write(0);
    delay(500);  
    myservo.write(180);
    delay(500);

    myservo.write(0);
    delay(500);  
    myservo.write(180);
    delay(500);
  }
  else{    
    myStepper.step(-stepsPerRevolution);
    delay(2000);
    myStepper.step(stepsPerRevolution);  
    myservo.write(40);
    delay(250);  
    myservo.write(180);
    delay(250);
  }
  delay(50);
}