#print('Holle World!')
#from Cython import __version__
#print(__version__)  # 0.29.14

import sys
sys.path.append('./build/lib.linux-x86_64-3.6')
import wrapper_staticlib

print(wrapper_staticlib.fib_with_c(20))  # 6765.0
print(wrapper_staticlib.fib_with_c.__doc__)  # 调用 C 编写的斐波那契数列
