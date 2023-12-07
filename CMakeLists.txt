cmake_minimum_required(VERSION 3.0)
project(myadd VERSION 1.0.0)

set(PYTHON_LIBRARY_DIR "C:/Users/AbdulTabish/anaconda3/envs/qr-py/Lib/site-packages" CACHE PATH "Python library directory")
set(PYTHON_EXECUTABLE "C:/Users/AbdulTabish/anaconda3/envs/qr-py/python.exe" CACHE FILEPATH "Python executable")
set(pybind11_DIR "C:/Users/AbdulTabish/anaconda3/envs/qr-py/Lib/site-packages/pybind11/share/cmake/pybind11" CACHE PATH "Pybind11 directory")

# Find the required packages
find_package(pybind11 REQUIRED)

# Create the pybind11 module
pybind11_add_module(my_add SHARED add.cpp)

target_link_libraries(my_add PRIVATE #-fno-lto
    -static -static-libstdc++ -static-libgcc)