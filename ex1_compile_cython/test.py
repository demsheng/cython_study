#print('Holle World!')
#from Cython import __version__
#print(__version__)  # 0.29.14

import sys
#sys.path.append('./ex1_compile_cython/build/lib.win-amd64-cpython-37')
sys.path.append('./build/lib.linux-x86_64-3.6')

import wrapper_cfib

print(wrapper_cfib.fib_with_c(20))  # 6765.0
print(wrapper_cfib.fib_with_c.__doc__)  # 调用 C 编写的斐波那契数列
