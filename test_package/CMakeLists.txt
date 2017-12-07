project(PackageTest CXX)
cmake_minimum_required(VERSION 3.5)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp data.cpp)
target_link_libraries(example ${CONAN_LIBS})
