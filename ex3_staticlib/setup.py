
from distutils.core import setup, Extension
from Cython.Build import cythonize

#from setuptools import setup, Extension
#from setuptools.dist import Distribution
#from setuptools.command.build_ext import build_ext
#import subprocess


# 这里我们不能在 sources 里面写上 ["fib.pyx", "libfib.a"] 这是不合法的，因为 sources 里面需要放入源文件
# 静态库和动态库需要通过 library_dirs 和 libraries 指定
ext = Extension(name="wrapper_staticlib",
                sources=["fib.pyx"],
                # 相当于 -L 参数，路径可以指定多个
                library_dirs=["./staticlib"],
                # 相当于 -l 参数，链接的库可以指定多个
                # 注意：不能写 libfib.a，直接写 fib 就行，所以命名还是需要遵循规范，要以 lib 开头、.a 结尾，
                libraries=["cfib"],
                # 如果还需要头文件的话，那么通过 include_dirs 指定
                # 只不过由于头文件就在当前目录中，所以我们不需要指定
                include_dirs=["./staticlib","./"],
                )

setup(ext_modules=cythonize(ext, language_level=3),
      )
