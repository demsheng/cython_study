from distutils.core import setup, Extension
from Cython.Build import cythonize

# 注意: Extension 的第一个参数, 首先我们这个文件叫做 setup.py, 当前的目录层级如下
"""
当前目录:
    cython_relative_demo:
        caller.pyx
        cython_test.pxd
        cython_test.pyx
    setup.py  
"""
# 所以我们的 build_ext.py 和 cython_relative_demo 是同级的
# 然后我们在编译的时候, name(Extension 的第一个参数) 不可以指定为 caller、cython_test
# 如果这么做的话, 当代码中涉及到相对导入的时候, 在编译时就会报错: relative cimport beyond main package is not allowed
# cython 编译器要求, 你在编译 pyx 文件、指定模块名的时候, 也需要把该 pyx 文件所在的目录也带上
ext = [
    Extension("cython_relative_demo.caller", sources=["cython_relative_demo/caller.pyx"]),
    Extension("cython_relative_demo.cython_test", sources=["cython_relative_demo/cython_test.pyx"])
]

setup(ext_modules=cythonize(ext, language_level=3))
