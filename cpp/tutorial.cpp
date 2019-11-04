// совместимость
// A simple program that computes the square root of a number
//
// Taken from https://cmake.org/cmake-tutorial/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "TutorialConfig.h"

#ifdef USE_MYMATH
#include "MyMath.h"
#endif

#ifdef USE_G4SERDES
#include "G4SerDes.h"
#endif

void g4sd_test () {
  g4sdInit();
  g4sdShow();
  g4sdSerialise("g4arrays.10.dat", 10);
  g4sdSerialise("g4arrays.11.dat", 11);
  g4sdDeserialise();
}

int main (int argc, char *argv[])
{
  if (argc < 2)
    {
      fprintf(stdout,"Usage Version %d.%d: %s number\n",Tutorial_VERSION_MAJOR, Tutorial_VERSION_MINOR, argv[0]);
      return 1;
    }
  
  double inputValue = atof(argv[1]);

#ifdef USE_MYMATH
  double outputValue = mysqrt(inputValue);
#else
  double outputValue = sqrt(inputValue);
#endif
  
  fprintf(stdout,"The square root of %g is %g\n",
          inputValue, outputValue);



  #ifdef USE_G4SERDES
  fprintf(stdout, "g4serdes\n");
  g4sd_test();
#else
  	fprintf(stdout, "NO G4SERDES\n");
  #endif

  return 0;
}
