# To discover : is there any kind of cmake lint like bash lint?
#
# How to verify cmake files on multiple platorms, other than Travis?
#
cmake_minimum_required(VERSION 3.1)

message("cond-build : cmake demonstration of supporting multiple build platforms and submodule collections.")

project(cond-build)
add_executable(cond-build cond-build.c)

# Demonstration of branching the build type based on a -DCODAS_BUILD_TYPE=foo

set(SUPPORTED_BUILD_TYPES "Debug;Release;Commissioning")

if (CODAS_BUILD_TYPE STREQUAL "Debug")
  message("CODAS_BUILD_TYPE = Debug")
  SET(CMAKE_BUILD_TYPE Debug)
  include(cmake.options.debug)
elseif(CODAS_BUILD_TYPE STREQUAL "Release")
  message("CODAS_BUILD_TYPE = Release")
  SET(CMAKE_BUILD_TYPE Release)
  include(cmake.options.release)
elseif(CODAS_BUILD_TYPE STREQUAL "Commissioning")
  message("CODAS_BUILD_TYPE = Commissioning")
  SET(CMAKE_BUILD_TYPE RelwithDebInfo)
  include(cmake.options.commissioning)
else()
  message("CODAS_BUILD_TYPE incorrectly specified")
  message("Supported CODAS_BUILD_TYPE values are :")
  foreach(BUILD_TYPE ${SUPPORTED_BUILD_TYPES})
    message("\t${BUILD_TYPE}")
  endforeach()
  message("Rerun cmake ../ -DCODAS_BUILD_TYPE=<CODAS_BUILD_TYPE>")
  message(FATAL_ERROR "Without a valid CODAS_BUILD_TYPE, this build cannot proceed")
endif()

# Demonstration of the use of options for ccmake

OPTION(COND_BUILD_HW_EXE "Build the cond-build-hw executable" OFF)
SET(COND_BUILD_HW_EXE_branch "master" CACHE STRING "Branch for cond-build-hw")

if( ${COND_BUILD_HW_EXE} )
  message("Building the cond-build-hw executable")
  add_executable(cond-build-hw cond-build-hw.c)
  OPTION(COND_BUILD_HW_LIBS "Build cond-build-hw with libraries" ON)
  OPTION(POS_NESTED_OPTION "Demonstrate nested option in positive path" ON)	
else()
  OPTION(COND_BUILD_HW_LIBS "Build cond-build-hw with libraries" OFF)
  OPTION(NEG_NESTED_OPTOIN "Demonstrate nested option in the negative path" ON)
message("NOT building the cond-build-hw executable")
endif()

message("CODAS_BUILD_TYPE is ${CODAS_BUILD_TYPE}")
message("CMAKE_BUILD_TYPE is ${CMAKE_BUILD_TYPE}")
message("CODAS_OPTIONS are ${CODAS_OPTIONS}")

message("cond-build : example ends")
