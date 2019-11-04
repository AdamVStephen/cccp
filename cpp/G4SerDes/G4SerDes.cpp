#include <math.h>
#include <iostream>
#include <fstream>
// To pick up std::setw
#include <iomanip>
/**
 * Demonstration of serialisation/deserialsation for python interactivity.
 * 
 * Case Study taken from github.com:rsarwar87/geant4_liquidscintillationsimulator
 *
 */

#include "G4SerDes.h"

G4int depoEnergyTime[7][11] = {{0}};
G4int reacEnergyTime[7][11] = {{0}};

void g4sdInit() {

  for(int i=0; i<7; i++) {
    for(int j=0; j<11; j++) {
      depoEnergyTime[i][j] = i*100 + j;
      reacEnergyTime[i][j] = i*1000 + j;
    }
  }
  return;
}

void g4sdShow() {

  for(int i=0; i<7; i++) {
    fprintf(stdout, "<%1d>", i);
    for(int j=0; j<11; j++) {
      fprintf(stdout, "(%-4d) [%-4d] ",
	      depoEnergyTime[i][j],
	      reacEnergyTime[i][j]);
    }
	fprintf(stdout, "\n");
  }
  return;
}

bool g4sdSerialise(const char *filename, int asize) {
  std::ofstream fout;
  std::cout << "g4sdSerialise to g4arrays.dat" << std::endl;

  G4int gEventNumber = 42;
  std::string name = "neutron";
  
  fout.open(filename,
	    std::ios::binary | std::ios::out | std::ios::trunc);

  for(int i=0; i<7; i++) {
    fout << "\n" << std::setw(5) << gEventNumber << " EventId: " << name << " Type: " << i << "\n";
    fout.write(reinterpret_cast<char*>(depoEnergyTime[i]),
	       std::streamsize(asize*sizeof(G4int)));
    fout.write(reinterpret_cast<char*>(reacEnergyTime[i]),
	       std::streamsize(asize*sizeof(G4int)));
  }

  fout.close();
  return true;
}

bool g4sdDeserialise() {
  return true;
}
