# cython_test.pxd

ctypedef double real

cdef class Girl:

    cdef public :
        str name
        long age
        str gender
    cdef real *scores

    cpdef str get_info(self)
    cpdef set_score(self, list scores)  # 如果参数有默认值，那么在声明的时候让其等于 * 即可，比如：arg=*，表示该函数的 arg 参数有默认值
    cpdef list get_score(self)