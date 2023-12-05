
#include <pybind11/pybind11.h>

float cpp_add(float num1, float num2) {
    float result = num1 + num2;
    return result;
}

PYBIND11_MODULE(my_add, module) {
    module.doc() = "This module adds numbers";
    module.def("cpp_add", &cpp_add);
}
