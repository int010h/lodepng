from conans import ConanFile, CMake, tools

class LodepngConan(ConanFile):
    name = "lodepng"
    version = "1.0"
    url = "https://github.com/int010h/conan-lodepng"
    description = "PNG encoder and decoder in C and C++"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.source_folder)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lodepng"]
