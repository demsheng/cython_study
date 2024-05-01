import sys
#sys.path.append('./build/lib.win-amd64-cpython-37')
sys.path.append('./build/lib.linux-x86_64-3.6')

# 这里不需要 pyximport 了, 因为导入的是已经编译好的 pyd 文件
# 当然即使有 pyximport, 也会优先导入 pyd 文件
from cython_relative_demo import caller

g = caller.NewGirl("古明地觉", 17, "female", "东方地灵殿")

print(g.get_info())  # name: 古明地觉, age: 17, gender: female
print(g.new_get_info())  # name: 古明地觉, age: 17, gender: female, where: 东方地灵殿
