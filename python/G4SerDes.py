#!/usr/bin/env python3

import pdb
import re
import struct

headerPat = """.*([0-9]+) EventId: ([a-z]+) Type: ([0-9]+)"""

def g4Des(datafile, arrayDim1, arrayDim2, elemSizeInBytes):
    headers = []
    depoEnergyTime = []
    reacEnergyTime = []
    fmt = 'i'*arrayDim2
    with open(datafile, 'rb') as fh:        
        for i in range(0,arrayDim1):
            #pdb.set_trace()
            separator=fh.readline()
            header = fh.readline()
            headers.append(header)
            rawData = fh.read(arrayDim2*elemSizeInBytes)
            intData = struct.unpack(fmt, rawData)
            depoEnergyTime.append(intData)
            rawData = fh.read(arrayDim2*elemSizeInBytes)
            intData = struct.unpack(fmt, rawData)
            reacEnergyTime.append(intData)
    return (headers, depoEnergyTime, reacEnergyTime)
        

def main():
    for (filename, dim1, dim2, elemSize) in [
            ['g4arrays.10.dat', 7, 10, 4],
            ['g4arrays.11.dat', 7, 11, 4]]:
        print('%'*40)
        print('Array size %d' % dim2)
        print('%'*40)
        headers, depoEnergyTime,reacEnergyTime = g4Des(filename, dim1, dim2, elemSize)
        for idx, det in enumerate(depoEnergyTime):
            print('%-35s : %s' % (headers[idx].strip(), det))
        print('-'*80)
        for idx, ret in enumerate(reacEnergyTime):
            print('%-35s : %s' % (headers[idx].strip(), ret))
    
if __name__ == '__main__':
    main()
