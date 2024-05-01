## ex4 演示cython如何使用c语言的静态连接库

- 2024-05-01
- 李长圣


1. 制作c语言静态库 `libcfib.a`
    ```
    gcc -c cfib.c
    ar -rc libcfib.a cfib.o
    ```

2. 编译 cython 项目
    ```
    python setup.py build
    ```

3. 运行示例
    ```
    python test.py
    ```
