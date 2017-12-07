#include <cassert>
#include <iostream>

#include "lodepng.h"
#include "data.h"

int main() {
    std::vector<uint8_t> decoded;
    unsigned width = 0, height = 0;
    unsigned error = lodepng::decode(decoded, width, height, PNG_DATA);
    assert(static_cast<bool>(error) == false);
    return 0;
}
