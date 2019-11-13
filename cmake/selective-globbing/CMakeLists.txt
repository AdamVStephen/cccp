cmake_minimum_required(VERSION 3.6)
message("selective-globbing demo")

file(GLOB SRC_FILES ./*.c)
message("SRC_FILES is ${SRC_FILES}")

# The following does not work because ./wip.c is not in the list; `pwd`/.wip.c is in the path
#list(REMOVE_ITEM SRC_FILES ./wip.c)

# The solution is to use GLOB to generate the path to be excluded.
file(GLOB SRC_REMOVE ./wip.c)
list(REMOVE_ITEM SRC_FILES ${SRC_REMOVE})

message("SRC_FILES is ${SRC_FILES}")

add_library(Globbing SHARED ${SRC_FILES})
