LodePNG
-------

PNG encoder and decoder in C and C++.

Home page: http://lodev.org/lodepng/

Only two files are needed to allow your program to read and write PNG files: lodepng.cpp and lodepng.h.

For C, you can rename lodepng.cpp to lodepng.c and it'll work. C++ only adds extra API.

The other files in the project are just examples, unit tests, etc...

conan-lodepng
-------------

Conan.io package for LodePNG encoder and decorer

The packages generated with this conanfile can be found in conan.io.

Usage

Example conanfile.txt configuration:

[requires]
lodepng/1.0@int010h/stable
