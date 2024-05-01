## cython 封装C语言示例

- 2024-05-01
- 李长圣

### 配置环境

1. 创建激活虚拟环境
    ```
    sudo yum install python3-devel
    sudo yum install python3
    python3 -m venv venvcython
    source venvcython/bin/activate
    ```
2. 安装 cython 编译器 `3.0.10`
    ```
    pip install cython
    ```
    
### 示例

- ex1_compile_cython cython直接封装C源代码
- ex2_pyximport 直接运行py
- ex3_staticlib 打包c代码为静态链接库, cython创建接口，生成一个动态链接库 wrapper_*.so,供python调用
- ex4_pxd_multifile 引入cython的头文件pxd，实现pyx多文件编译
- ex5_pyinstaller cython生成的动态链接库 wrapper_*.so (由ex3生成) ，与python代码一起打包为一个 exe
