#!/usr/bin/env python3

import sys;
import minimalmodbus
import struct
from shutil import copyfile

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1, mode='rtu') # port name, slave address (in decimal)

#sys.stdout=open('/tmp/pwm-data.tmp', 'w')

instrument.serial.baudrate = 9600   # Baud
instrument.serial.timeout  = 1   # seconds

def convert_in_float(value1, value2):
        raw = struct.pack('>HH',value1,value2)
        ans = struct.unpack('>f', raw)[0]
        return ans

try:
        read_values1  = instrument.read_registers( 0x00, 0x4a, 4)

        # Volts
        print("voltage1=" + str(convert_in_float( read_values1[0], read_values1[1])))
        print("voltage2=" + str(convert_in_float( read_values1[2], read_values1[3])))
        print("voltage3=" + str(convert_in_float( read_values1[4], read_values1[5])))
        # Current
        print("current1=" + str(convert_in_float( read_values1[6], read_values1[7])))
        print("current2=" + str(convert_in_float( read_values1[8], read_values1[9])))
        print("current3=" + str(convert_in_float( read_values1[10], read_values1[11])))
        # Active Power
        print("power1=" + str(convert_in_float( read_values1[12], read_values1[13])))
        print("power2=" + str(convert_in_float( read_values1[14], read_values1[15])))
        print("power3=" + str(convert_in_float( read_values1[16], read_values1[17])))
        # Apparent Power
        print("powerapparent1=" + str(convert_in_float( read_values1[18], read_values1[19])))
        print("powerapparent2=" + str(convert_in_float( read_values1[20], read_values1[21])))
        print("powerapparent3=" + str(convert_in_float( read_values1[22], read_values1[23])))
        # Reactive Power
        print("powerreactive1=" + str(convert_in_float( read_values1[24], read_values1[25])))
        print("powerreactive2=" + str(convert_in_float( read_values1[26], read_values1[27])))
        print("powerreactive3=" + str(convert_in_float( read_values1[28], read_values1[29])))
        # Power Factor
        print("powerfactor1=" + str(convert_in_float( read_values1[30], read_values1[31])))
        print("powerfactor2=" + str(convert_in_float( read_values1[32], read_values1[33])))
        print("powerfactor3=" + str(convert_in_float( read_values1[34], read_values1[35])))
        # Phase Angle
        print("phaseangle1=" + str(convert_in_float( read_values1[36], read_values1[37])))
        print("phaseangle2=" + str(convert_in_float( read_values1[38], read_values1[39])))
        print("phaseangle3=" + str(convert_in_float( read_values1[40], read_values1[41])))
        # Frequency
        print("frequency=" + str(convert_in_float( read_values1[70], read_values1[71])))


except IOError:
        print("voltage1=0")
        print("current1=0")
        print("power1=0")
        print("powerapparent1=0")
        print("powerreactive1=0")
        print("powerfactor1=0")
        print("phaseangle1=0")
        print("voltage2=0")
        print("current2=0")
        print("power2=0")
        print("powerapparent2=0")
        print("powerreactive2=0")
        print("powerfactor2=0")
        print("phaseangle2=0")
        print("voltage3=0")
        print("current3=0")
        print("power3=0")
        print("powerapparent3=0")
        print("powerreactive3=0")
        print("powerfactor3=0")
        print("phaseangle3=0")
        print("frequency=0")

#sys.stdout.close()
#copyfile('/tmp/pwm-data.tmp', '/tmp/pwm-data.txt')
