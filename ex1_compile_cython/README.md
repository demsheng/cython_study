## ex1 cython直接封装C源代码

- 2024-04-14
- 李长圣

1. 已经编写完成的C代码
    + cfib.h
    + cfib.c
2. 采用cython封装写好的C代码
    + fib.pyx
3. 将以上功能编译成动态链接库 `so (linux)` 或者 `pyd (windows)`
    + `python setup.py build`
4. 在python中使用动态链接库 `so (linux)` 或者 `pyd (windows)`
    + `python test.py`