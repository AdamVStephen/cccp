# To discover : is there any kind of cmake lint like bash lint?
#
# How to verify cmake files on multiple platorms, other than Travis?
#
cmake_minimum_required(VERSION 3.10)

message("cond-build : cmake demonstration of supporting multiple build platforms and submodule collections.")

project(cond-build)
add_executable(cond-build cond-build.c)

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

message("CODAS_BUILD_TYPE is ${CODAS_BUILD_TYPE}")
message("CMAKE_BUILD_TYPE is ${CMAKE_BUILD_TYPE}")
message("CODAS_OPTIONS are ${CODAS_OPTIONS}")

message("cond-build : example ends")
