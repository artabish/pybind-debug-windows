import os

from setuptools import Extension, setup
from pybind11.setup_helpers import Pybind11Extension

setup(name="myadd",
      version="1.0.0",
      ext_modules=[Pybind11Extension("my_add", ["add.cpp"], extra_compile_args=["-O0", "-g3", "-UNDEBUG"], extra_link_args=["-O0", "-g3", "-UNDEBUG"])],
      )

