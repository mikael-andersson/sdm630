#!/usr/bin/env python3

import sys;
import minimalmodbus
import struct
from shutil import copyfile

instrument = minimalmodbus.Instrument('/dev/ttyUSB1', 1, mode='rtu',close_port_after_each_call=False,debug=True)

instrument.serial.baudrate = 9600   # Baud
instrument.serial.timeout  = 1   # seconds

def convert_in_float(value1, value2):
        raw = struct.pack('>HH',value1,value2)
        ans = struct.unpack('>f', raw)[0]
        return ans

        read_values1  = instrument.read_registers(0, 76, 4)

        # Volts
        print("voltage1=" + str(convert_in_float( read_values1[0], read_values1[1])))
        print("voltage2=" + str(convert_in_float( read_values1[2], read_values1[3])))
        print("voltage3=" + str(convert_in_float( read_values1[4], read_values1[5])))
        # Current
        print("current1=" + str(convert_in_float( read_values1[6], read_values1[7])))
        print("current2=" + str(convert_in_float( read_values1[8], read_values1[9])))
        print("current3=" + str(convert_in_float( read_values1[10], read_values1[11])))

        print("active power 1=" + str(convert_in_float( read_values1[12], read_values1[13])))
        print("active power 2=" + str(convert_in_float( read_values1[14], read_values1[15])))
        print("active power 3=" + str(convert_in_float( read_values1[16], read_values1[17])))

        print("reactive power 1=" + str(convert_in_float( read_values1[24], read_values1[25])))
        print("reactive power 2=" + str(convert_in_float( read_values1[26], read_values1[27])))
        print("reactive power 3=" + str(convert_in_float( read_values1[28], read_values1[29])))

	# Total power
        print("total active power=" + str(convert_in_float( read_values1[52], read_values1[53])))
        print("total reactive power=" + str(convert_in_float( read_values1[60], read_values1[61])))

        print("total imported active energy=" + str(convert_in_float( read_values1[72], read_values1[73])))
        print("total exported active energy=" + str(convert_in_float( read_values1[74], read_values1[75])))
