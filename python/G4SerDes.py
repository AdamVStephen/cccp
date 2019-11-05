#!/usr/bin/env python3

import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import pdb
import re
import struct

headerPat = """.*([0-9]+) EventId: ([a-z]+) Type: ([0-9]+)"""

def g4Read(datafile, arrayDim1, arrayDim2, elemSizeInBytes):
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
        

def g4Show():
    for (filename, dim1, dim2, elemSize) in [
            ['g4arrays.10.dat', 7, 10, 4],
            ['g4arrays.11.dat', 7, 11, 4]]:
        print('%'*40)
        print('Array size %d' % dim2)
        print('%'*40)
        headers, depoEnergyTime,reacEnergyTime = g4Read(filename, dim1, dim2, elemSize)
        for idx, det in enumerate(depoEnergyTime):
            print('%-35s : %s' % (headers[idx].strip(), det))
        print('-'*80)
        for idx, ret in enumerate(reacEnergyTime):
            print('%-35s : %s' % (headers[idx].strip(), ret))


def g4Plot(writePdf = False, pdfFileName = 'g4.waves.pdf'):
    with PdfPages(pdfFileName) as pdf:
        (headers, g4sines, g4cosines) = g4Read('g4.waves.dat', 7, 5000, 4)
        for (row, sin) in enumerate(g4sines):
            t = np.arange(len(sin))
            nsin = np.array(sin)
            plt.subplot(7,2,(2+2*row))
            plt.plot(t,nsin)
            plt.ylabel('g4 Sin %d' % row)
            plt.xlabel('t')
        for (row, cos) in enumerate(g4cosines):
            t = np.arange(len(cos))
            nsin = np.array(cos)
            plt.subplot(7,2,(1+2*row))
            plt.plot(t,nsin)
            plt.ylabel('g4 Cos %d' % row)
            plt.xlabel('t')
        if writePdf:
            pdf.savefig()
            print("Saved plots to %s" % pdfFileName)
        else:
            plt.show()
        pdf.savefig()
        # Metadata for fun
        d = pdf.infodict()
        d['Title'] = 'cccp matplotlib demo of subplot with G4 style data'
        d['Author'] = 'Adam Vercingetorix Stephen'
        d['CreationDate'] = datetime.datetime.today()
        
    
def main():
    g4Show()
    g4Plot(True)
    
if __name__ == '__main__':
    main()
