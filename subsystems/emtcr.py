import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0, dsrdtr=1)
string = 'Hello from Raspberry Pi'
print 'Sending "%s"' % string
ser.write('%s\n' % string)

while True:
    incoming = ser.readline()
    print 'Received %s' % incoming
    ser.write('RPi Received: %s\n' % incoming)
