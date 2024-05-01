# 文件名: caller.pyx
from .cython_test cimport Girl


cdef class NewGirl(Girl):

    cdef public str where

    def __init__(self, name, age, gender, where):
        self.where = where
        super().__init__(name, age, gender)

    def new_get_info(self):
        return super(NewGirl, self).get_info() + f", where: {self.where}"