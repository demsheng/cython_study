from libc.stdlib cimport malloc, free

cdef class Girl:

    def __cinit__(self, *args, **kwargs):
        self.scores = < real * > malloc(3 * sizeof(real))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __dealloc__(self):
        if self.scores != NULL:
            free(self.scores)

    cpdef str get_info(self):
        return f"name: {self.name}, age: {self.age}, gender: {self.gender}"

    cpdef set_score(self, list scores):
        # 虽然 not None 也可以写在参数后面, 但是它只适用于 Python 函数, 也就是 def 定义的函数
        assert scores is not None and len(scores) == 3
        cdef real score
        cdef long idx
        for idx, score in enumerate(scores):
            self.scores[idx] = score

    cpdef list get_score(self):
        cdef list res = [self.scores[0], self.scores[1], self.scores[2]]
        return res