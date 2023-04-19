import serial
ser = serial.Serial('COM3',9600)


while True:
    input_user = input("Press Y to turn on the light \n Press N to turn off the light")
    if(input_user == 'Y'):
        ser.write(b'Y')
        
    if(input_user == 'N'):
        ser.write(b'N')    
