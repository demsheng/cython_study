import pyximport
pyximport.install(language_level=3)

import cython_test

g = cython_test.Girl('古明地觉', 16, 'female')
print(g)  # <cython_test.Girl object at 0x000001C49D81B330>

g.get_info()
g.set_score([90.4, 97.3, 97.6])
print(g.get_score())  # [90.4, 97.3, 97.6]