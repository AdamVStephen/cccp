cmake_minimum_required (VERSION 2.6)
project (Tutorial)

# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)
 
# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
  )
 
# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

option(USE_MYMATH "Use implementation of sqrt provided by tutorial." ON)

# add the MathFunctions library?
#
if (USE_MYMATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MyMath")
  add_subdirectory (MyMath) 
  set (EXTRA_LIBS ${EXTRA_LIBS} MyMath)
endif (USE_MYMATH)

# Add the executable
add_executable(Tutorial tutorial.cpp)
target_link_libraries(Tutorial ${EXTRA_LIBS})


