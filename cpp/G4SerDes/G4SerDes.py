#!/usr/bin/env python3

import pdb
import struct

def g4Des(datafile, arrayDim1, arrayDim2, elemSizeInBytes):
    depoEnergyTime = []
    reacEnergyTime = []
    fmt = 'i'*arrayDim2
    with open(datafile, 'rb') as fh:        
        for i in range(0,arrayDim1):
            #pdb.set_trace()
            rawData = fh.read(arrayDim2*elemSizeInBytes)
            intData = struct.unpack(fmt, rawData)
            depoEnergyTime.append(intData)
            rawData = fh.read(arrayDim2*elemSizeInBytes)
            intData = struct.unpack(fmt, rawData)
            reacEnergyTime.append(intData)
    return (depoEnergyTime, reacEnergyTime)
        

def main():
    for (filename, dim1, dim2, elemSize) in [
            ['g4arrays.10.dat', 7, 10, 4],
            ['g4arrays.11.dat', 7, 11, 4]]:
        print('%'*40)
        print('Array size %d' % dim2)
        print('%'*40)
        depoEnergyTime,reacEnergyTime = g4Des(filename, dim1, dim2, elemSize)
        for a in depoEnergyTime:
            print(a)
        print('-'*80)
        for a in reacEnergyTime:
            print(a)
    
if __name__ == '__main__':
    main()
