from libc.math cimport sin as c_sin
from math import sin as py_sin

print(c_sin(3.1415926 / 3)) # 测试注释
print(py_sin(3.1415926 / 3))