byte step = 0;
bool wait = 0;
bool doonce = 0;
unsigned int current;
const unsigned char PS_128 = (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
uint8_t changedbits;
volatile uint8_t portbhistory = 0xFF;
unsigned int rotation;

void setup() {
  ADCSRA &= ~PS_128;
  ADCSRA |= (1 << ADPS1);
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1 = 0;
  TCCR1B |= (1 << WGM12) | (1 << CS11) | (1 << CS10); 
  TIMSK1 |= (1 << OCIE1A); 
  TCCR2A = 0;
  TCCR2B = 0;
  TCNT2 = 0;
  OCR2A = 100;
  OCR2B = 20;
  TCCR2A |= (1 << WGM21); 
  TCCR2B |= (1 << CS21); 
  TIMSK2 |= (1 << OCIE2A) | (1 << OCIE2B);
  PCICR |= (1 << PCIE0);    
  PCMSK0 |= (1 << PCINT0);
  sei();
  DDRD = B11110000;    //Pin 4,5,6,7 --> OUTPUT Pin3 --> INPUT
  DDRB = B00100011;    //Pin 8,9 --> OUTPUT, Pin 10,11,12 INPUT
  PORTD = B00000000;
  PORTB = B00011100;
  rotation = map(analogRead(A7), 0, 1023, 5000, 200);
  OCR1A = rotation;
}

ISR(TIMER1_COMPA_vect) {
  rotation = map(analogRead(A7), 0, 1023, 5000, 200);
  OCR1A = rotation;
  step++;
  doonce = 0;
  if (step == 6) {
    step = 0;
  }
}

ISR(TIMER2_COMPB_vect) {
  if (wait == 0) {
    wait = 1;
    doonce = 0;
  }
}

ISR(TIMER2_COMPA_vect) {
  if (wait == 1) {
    wait = 0;
    doonce = 0;
  }
}

ISR (PCINT0_vect) {
  if (rotation < 1000) {
    current = map(rotation, 1000, 200, 20, 50);
    OCR2B = current;
    changedbits = PINB ^ portbhistory;
    portbhistory = PINB;
    if ((changedbits & (1 << PINB2)) && (step == (2 || 5))) //Phase C (3)
    {
      step++;
      wait = 0;
      TCNT1 = 0;
      TCNT2 = 0;
      if (step == 6) {
        step = 0;
      }
      doonce = 0;
    }

    if ((changedbits & (1 << PINB3)) && (step == (0 || 3))) //Phase B (2)
    {
      step++;
      wait = 0;
      TCNT1 = 0;
      TCNT2 = 0;
      doonce = 0;
    }

    if ((changedbits & (1 << PINB4)) && (step == (1 || 4))) //Phase A (1)
    {
      step++;
      wait = 0;
      TCNT1 = 0;
      TCNT2 = 0;
      doonce = 0;
    }
  }
}

void loop() {
  if (doonce == 0) {
    switch (step) {
      case 0:
        if (wait == 0) {
          step0();
        }
        else {
          step01();
        }
        break;
      case 1:
        if (wait == 0) {
          step1();
        }
        else {
          step11();
        }
        break;
      case 2:
        if (wait == 0) {
          step2();
        }
        else {
          step21();
        }
        break;
      case 3:
        if (wait == 0) {
          step3();
        }
        else {
          step31();
        }
        break;
      case 4:
        if (wait == 0) {
          step4();
        }
        else {
          step41();
        }
        break;
      case 5:
        if (wait == 0) {
          step5();
        }
        else {
          step51();
        }
        break;
    }
  }
}

void step0() {
  PORTD = B00100000;
  PORTB = B00011111;
  doonce = 1;
}

void step01() {
  PORTD = B00100000;
  PORTB = B00011101;
  doonce = 1;
  TCNT2 = 0;
}

void step1() {
  PORTD = B11100000;
  PORTB = B00011100;
  doonce = 1;
}

void step11() {
  PORTB = B00011100;
  PORTD = B01100000;
  doonce = 1;
  TCNT2 = 0;
}
void step2() {
  PORTB = B00011101;
  PORTD = B11000000;
  doonce = 1;
}

void step21() {
  PORTD = B01000000;
  PORTB = B00011101;
  doonce = 1;
  TCNT2 = 0;
}

void step3() {
  PORTD = B00110000;
  PORTB = B00011101;
  doonce = 1;
}

void step31() {
  PORTD = B00100000;
  PORTB = B00011101;
  doonce = 1;
  TCNT2 = 0;
}

void step4() {
  PORTD = B01110000;
  PORTB = B00011100;
  doonce = 1;
}

void step41() {
  PORTB = B00011100;
  PORTD = B01100000;
  doonce = 1;
  TCNT2 = 0;
}

void step5() {
  PORTB = B00011111;
  PORTD = B01000000;
  doonce = 1;
}

void step51() {
  PORTD = B01000000;
  PORTB = B00011101;
  doonce = 1;
  TCNT2 = 0;
}

