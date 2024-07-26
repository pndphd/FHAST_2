'''Wrapper for gmath.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_gmath.7.8 C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gmath.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h -o OBJ.x86_64-w64-mingw32/gmath.py

Do not modify this file.
'''

__docformat__ = 'restructuredtext'


_libs = {}
_libdirs = []

from .ctypes_preamble import *
from .ctypes_preamble import _variadic_function
from .ctypes_loader import *

add_library_search_dirs([])

# Begin libraries

_libs["grass_gmath.7.8"] = load_library("grass_gmath.7.8")

# 1 libraries
# End libraries

# No modules

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 59
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'values',
    'cols',
    'index',
]
struct_anon_3._fields_ = [
    ('values', POINTER(c_double)),
    ('cols', c_uint),
    ('index', POINTER(c_uint)),
]

G_math_spvector = struct_anon_3 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 59

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 5
if hasattr(_libs['grass_gmath.7.8'], 'G_alloc_vector'):
    G_alloc_vector = _libs['grass_gmath.7.8'].G_alloc_vector
    G_alloc_vector.argtypes = [c_size_t]
    G_alloc_vector.restype = POINTER(c_double)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 6
if hasattr(_libs['grass_gmath.7.8'], 'G_alloc_matrix'):
    G_alloc_matrix = _libs['grass_gmath.7.8'].G_alloc_matrix
    G_alloc_matrix.argtypes = [c_int, c_int]
    G_alloc_matrix.restype = POINTER(POINTER(c_double))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 7
if hasattr(_libs['grass_gmath.7.8'], 'G_alloc_fvector'):
    G_alloc_fvector = _libs['grass_gmath.7.8'].G_alloc_fvector
    G_alloc_fvector.argtypes = [c_size_t]
    G_alloc_fvector.restype = POINTER(c_float)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 8
if hasattr(_libs['grass_gmath.7.8'], 'G_alloc_fmatrix'):
    G_alloc_fmatrix = _libs['grass_gmath.7.8'].G_alloc_fmatrix
    G_alloc_fmatrix.argtypes = [c_int, c_int]
    G_alloc_fmatrix.restype = POINTER(POINTER(c_float))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 9
if hasattr(_libs['grass_gmath.7.8'], 'G_free_vector'):
    G_free_vector = _libs['grass_gmath.7.8'].G_free_vector
    G_free_vector.argtypes = [POINTER(c_double)]
    G_free_vector.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 10
if hasattr(_libs['grass_gmath.7.8'], 'G_free_matrix'):
    G_free_matrix = _libs['grass_gmath.7.8'].G_free_matrix
    G_free_matrix.argtypes = [POINTER(POINTER(c_double))]
    G_free_matrix.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 11
if hasattr(_libs['grass_gmath.7.8'], 'G_free_fvector'):
    G_free_fvector = _libs['grass_gmath.7.8'].G_free_fvector
    G_free_fvector.argtypes = [POINTER(c_float)]
    G_free_fvector.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 12
if hasattr(_libs['grass_gmath.7.8'], 'G_free_fmatrix'):
    G_free_fmatrix = _libs['grass_gmath.7.8'].G_free_fmatrix
    G_free_fmatrix.argtypes = [POINTER(POINTER(c_float))]
    G_free_fmatrix.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 15
if hasattr(_libs['grass_gmath.7.8'], 'G_alloc_ivector'):
    G_alloc_ivector = _libs['grass_gmath.7.8'].G_alloc_ivector
    G_alloc_ivector.argtypes = [c_size_t]
    G_alloc_ivector.restype = POINTER(c_int)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 16
if hasattr(_libs['grass_gmath.7.8'], 'G_alloc_imatrix'):
    G_alloc_imatrix = _libs['grass_gmath.7.8'].G_alloc_imatrix
    G_alloc_imatrix.argtypes = [c_int, c_int]
    G_alloc_imatrix.restype = POINTER(POINTER(c_int))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 17
if hasattr(_libs['grass_gmath.7.8'], 'G_free_ivector'):
    G_free_ivector = _libs['grass_gmath.7.8'].G_free_ivector
    G_free_ivector.argtypes = [POINTER(c_int)]
    G_free_ivector.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 18
if hasattr(_libs['grass_gmath.7.8'], 'G_free_imatrix'):
    G_free_imatrix = _libs['grass_gmath.7.8'].G_free_imatrix
    G_free_imatrix.argtypes = [POINTER(POINTER(c_int))]
    G_free_imatrix.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 21
if hasattr(_libs['grass_gmath.7.8'], 'fft'):
    fft = _libs['grass_gmath.7.8'].fft
    fft.argtypes = [c_int, POINTER(c_double) * 2, c_int, c_int, c_int]
    fft.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 22
if hasattr(_libs['grass_gmath.7.8'], 'fft2'):
    fft2 = _libs['grass_gmath.7.8'].fft2
    fft2.argtypes = [c_int, POINTER(c_double * 2), c_int, c_int, c_int]
    fft2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 25
if hasattr(_libs['grass_gmath.7.8'], 'G_math_rand_gauss'):
    G_math_rand_gauss = _libs['grass_gmath.7.8'].G_math_rand_gauss
    G_math_rand_gauss.argtypes = [c_double]
    G_math_rand_gauss.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 28
if hasattr(_libs['grass_gmath.7.8'], 'G_math_max_pow2'):
    G_math_max_pow2 = _libs['grass_gmath.7.8'].G_math_max_pow2
    G_math_max_pow2.argtypes = [c_long]
    G_math_max_pow2.restype = c_long

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 29
if hasattr(_libs['grass_gmath.7.8'], 'G_math_min_pow2'):
    G_math_min_pow2 = _libs['grass_gmath.7.8'].G_math_min_pow2
    G_math_min_pow2.argtypes = [c_long]
    G_math_min_pow2.restype = c_long

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 32
if hasattr(_libs['grass_gmath.7.8'], 'G_math_srand'):
    G_math_srand = _libs['grass_gmath.7.8'].G_math_srand
    G_math_srand.argtypes = [c_int]
    G_math_srand.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 33
if hasattr(_libs['grass_gmath.7.8'], 'G_math_srand_auto'):
    G_math_srand_auto = _libs['grass_gmath.7.8'].G_math_srand_auto
    G_math_srand_auto.argtypes = []
    G_math_srand_auto.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 34
if hasattr(_libs['grass_gmath.7.8'], 'G_math_rand'):
    G_math_rand = _libs['grass_gmath.7.8'].G_math_rand
    G_math_rand.argtypes = []
    G_math_rand.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 37
if hasattr(_libs['grass_gmath.7.8'], 'del2g'):
    del2g = _libs['grass_gmath.7.8'].del2g
    del2g.argtypes = [POINTER(c_double) * 2, c_int, c_double]
    del2g.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 40
if hasattr(_libs['grass_gmath.7.8'], 'getg'):
    getg = _libs['grass_gmath.7.8'].getg
    getg.argtypes = [c_double, POINTER(c_double) * 2, c_int]
    getg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 43
if hasattr(_libs['grass_gmath.7.8'], 'G_math_egvorder'):
    G_math_egvorder = _libs['grass_gmath.7.8'].G_math_egvorder
    G_math_egvorder.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_long]
    G_math_egvorder.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 46
if hasattr(_libs['grass_gmath.7.8'], 'G_math_complex_mult'):
    G_math_complex_mult = _libs['grass_gmath.7.8'].G_math_complex_mult
    G_math_complex_mult.argtypes = [POINTER(c_double) * 2, c_int, POINTER(c_double) * 2, c_int, POINTER(c_double) * 2, c_int]
    G_math_complex_mult.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 49
if hasattr(_libs['grass_gmath.7.8'], 'G_ludcmp'):
    G_ludcmp = _libs['grass_gmath.7.8'].G_ludcmp
    G_ludcmp.argtypes = [POINTER(POINTER(c_double)), c_int, POINTER(c_int), POINTER(c_double)]
    G_ludcmp.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 50
if hasattr(_libs['grass_gmath.7.8'], 'G_lubksb'):
    G_lubksb = _libs['grass_gmath.7.8'].G_lubksb
    G_lubksb.argtypes = [POINTER(POINTER(c_double)), c_int, POINTER(c_int), POINTER(c_double)]
    G_lubksb.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 53
if hasattr(_libs['grass_gmath.7.8'], 'G_math_findzc'):
    G_math_findzc = _libs['grass_gmath.7.8'].G_math_findzc
    G_math_findzc.argtypes = [POINTER(c_double), c_int, POINTER(c_double), c_double, c_int]
    G_math_findzc.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 59
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solv'):
    G_math_solv = _libs['grass_gmath.7.8'].G_math_solv
    G_math_solv.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_solv.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 60
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solvps'):
    G_math_solvps = _libs['grass_gmath.7.8'].G_math_solvps
    G_math_solvps.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_solvps.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 61
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solvtd'):
    G_math_solvtd = _libs['grass_gmath.7.8'].G_math_solvtd
    G_math_solvtd.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    G_math_solvtd.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 62
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solvru'):
    G_math_solvru = _libs['grass_gmath.7.8'].G_math_solvru
    G_math_solvru.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_solvru.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 63
if hasattr(_libs['grass_gmath.7.8'], 'G_math_minv'):
    G_math_minv = _libs['grass_gmath.7.8'].G_math_minv
    G_math_minv.argtypes = [POINTER(POINTER(c_double)), c_int]
    G_math_minv.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 64
if hasattr(_libs['grass_gmath.7.8'], 'G_math_psinv'):
    G_math_psinv = _libs['grass_gmath.7.8'].G_math_psinv
    G_math_psinv.argtypes = [POINTER(POINTER(c_double)), c_int]
    G_math_psinv.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 65
if hasattr(_libs['grass_gmath.7.8'], 'G_math_ruinv'):
    G_math_ruinv = _libs['grass_gmath.7.8'].G_math_ruinv
    G_math_ruinv.argtypes = [POINTER(POINTER(c_double)), c_int]
    G_math_ruinv.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 66
if hasattr(_libs['grass_gmath.7.8'], 'G_math_eigval'):
    G_math_eigval = _libs['grass_gmath.7.8'].G_math_eigval
    G_math_eigval.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_eigval.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 67
if hasattr(_libs['grass_gmath.7.8'], 'G_math_eigen'):
    G_math_eigen = _libs['grass_gmath.7.8'].G_math_eigen
    G_math_eigen.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_eigen.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 68
if hasattr(_libs['grass_gmath.7.8'], 'G_math_evmax'):
    G_math_evmax = _libs['grass_gmath.7.8'].G_math_evmax
    G_math_evmax.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_evmax.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 69
if hasattr(_libs['grass_gmath.7.8'], 'G_math_svdval'):
    G_math_svdval = _libs['grass_gmath.7.8'].G_math_svdval
    G_math_svdval.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_int, c_int]
    G_math_svdval.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 70
if hasattr(_libs['grass_gmath.7.8'], 'G_math_sv2val'):
    G_math_sv2val = _libs['grass_gmath.7.8'].G_math_sv2val
    G_math_sv2val.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_int, c_int]
    G_math_sv2val.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 71
if hasattr(_libs['grass_gmath.7.8'], 'G_math_svduv'):
    G_math_svduv = _libs['grass_gmath.7.8'].G_math_svduv
    G_math_svduv.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, POINTER(POINTER(c_double)), c_int]
    G_math_svduv.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 72
if hasattr(_libs['grass_gmath.7.8'], 'G_math_sv2uv'):
    G_math_sv2uv = _libs['grass_gmath.7.8'].G_math_sv2uv
    G_math_sv2uv.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, POINTER(POINTER(c_double)), c_int]
    G_math_sv2uv.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 73
if hasattr(_libs['grass_gmath.7.8'], 'G_math_svdu1v'):
    G_math_svdu1v = _libs['grass_gmath.7.8'].G_math_svdu1v
    G_math_svdu1v.argtypes = [POINTER(c_double), POINTER(POINTER(c_double)), c_int, POINTER(POINTER(c_double)), c_int]
    G_math_svdu1v.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 81
if hasattr(_libs['grass_gmath.7.8'], 'G_math_alloc_spvector'):
    G_math_alloc_spvector = _libs['grass_gmath.7.8'].G_math_alloc_spvector
    G_math_alloc_spvector.argtypes = [c_int]
    G_math_alloc_spvector.restype = POINTER(G_math_spvector)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 82
if hasattr(_libs['grass_gmath.7.8'], 'G_math_alloc_spmatrix'):
    G_math_alloc_spmatrix = _libs['grass_gmath.7.8'].G_math_alloc_spmatrix
    G_math_alloc_spmatrix.argtypes = [c_int]
    G_math_alloc_spmatrix.restype = POINTER(POINTER(G_math_spvector))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 83
if hasattr(_libs['grass_gmath.7.8'], 'G_math_free_spmatrix'):
    G_math_free_spmatrix = _libs['grass_gmath.7.8'].G_math_free_spmatrix
    G_math_free_spmatrix.argtypes = [POINTER(POINTER(G_math_spvector)), c_int]
    G_math_free_spmatrix.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 84
if hasattr(_libs['grass_gmath.7.8'], 'G_math_free_spvector'):
    G_math_free_spvector = _libs['grass_gmath.7.8'].G_math_free_spvector
    G_math_free_spvector.argtypes = [POINTER(G_math_spvector)]
    G_math_free_spvector.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 85
if hasattr(_libs['grass_gmath.7.8'], 'G_math_add_spvector'):
    G_math_add_spvector = _libs['grass_gmath.7.8'].G_math_add_spvector
    G_math_add_spvector.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(G_math_spvector), c_int]
    G_math_add_spvector.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 86
if hasattr(_libs['grass_gmath.7.8'], 'G_math_A_to_Asp'):
    G_math_A_to_Asp = _libs['grass_gmath.7.8'].G_math_A_to_Asp
    G_math_A_to_Asp.argtypes = [POINTER(POINTER(c_double)), c_int, c_double]
    G_math_A_to_Asp.restype = POINTER(POINTER(G_math_spvector))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 87
if hasattr(_libs['grass_gmath.7.8'], 'G_math_Asp_to_A'):
    G_math_Asp_to_A = _libs['grass_gmath.7.8'].G_math_Asp_to_A
    G_math_Asp_to_A.argtypes = [POINTER(POINTER(G_math_spvector)), c_int]
    G_math_Asp_to_A.restype = POINTER(POINTER(c_double))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 88
if hasattr(_libs['grass_gmath.7.8'], 'G_math_Asp_to_sband_matrix'):
    G_math_Asp_to_sband_matrix = _libs['grass_gmath.7.8'].G_math_Asp_to_sband_matrix
    G_math_Asp_to_sband_matrix.argtypes = [POINTER(POINTER(G_math_spvector)), c_int, c_int]
    G_math_Asp_to_sband_matrix.restype = POINTER(POINTER(c_double))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 89
if hasattr(_libs['grass_gmath.7.8'], 'G_math_sband_matrix_to_Asp'):
    G_math_sband_matrix_to_Asp = _libs['grass_gmath.7.8'].G_math_sband_matrix_to_Asp
    G_math_sband_matrix_to_Asp.argtypes = [POINTER(POINTER(c_double)), c_int, c_int, c_double]
    G_math_sband_matrix_to_Asp.restype = POINTER(POINTER(G_math_spvector))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 90
if hasattr(_libs['grass_gmath.7.8'], 'G_math_print_spmatrix'):
    G_math_print_spmatrix = _libs['grass_gmath.7.8'].G_math_print_spmatrix
    G_math_print_spmatrix.argtypes = [POINTER(POINTER(G_math_spvector)), c_int]
    G_math_print_spmatrix.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 91
if hasattr(_libs['grass_gmath.7.8'], 'G_math_Ax_sparse'):
    G_math_Ax_sparse = _libs['grass_gmath.7.8'].G_math_Ax_sparse
    G_math_Ax_sparse.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_Ax_sparse.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 94
if hasattr(_libs['grass_gmath.7.8'], 'G_math_matrix_to_sband_matrix'):
    G_math_matrix_to_sband_matrix = _libs['grass_gmath.7.8'].G_math_matrix_to_sband_matrix
    G_math_matrix_to_sband_matrix.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]
    G_math_matrix_to_sband_matrix.restype = POINTER(POINTER(c_double))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 95
if hasattr(_libs['grass_gmath.7.8'], 'G_math_sband_matrix_to_matrix'):
    G_math_sband_matrix_to_matrix = _libs['grass_gmath.7.8'].G_math_sband_matrix_to_matrix
    G_math_sband_matrix_to_matrix.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]
    G_math_sband_matrix_to_matrix.restype = POINTER(POINTER(c_double))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 96
if hasattr(_libs['grass_gmath.7.8'], 'G_math_Ax_sband'):
    G_math_Ax_sband = _libs['grass_gmath.7.8'].G_math_Ax_sband
    G_math_Ax_sband.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_Ax_sband.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 99
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_gauss'):
    G_math_solver_gauss = _libs['grass_gmath.7.8'].G_math_solver_gauss
    G_math_solver_gauss.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_solver_gauss.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 100
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_lu'):
    G_math_solver_lu = _libs['grass_gmath.7.8'].G_math_solver_lu
    G_math_solver_lu.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_solver_lu.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 101
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_cholesky'):
    G_math_solver_cholesky = _libs['grass_gmath.7.8'].G_math_solver_cholesky
    G_math_solver_cholesky.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_solver_cholesky.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 102
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_cholesky_sband'):
    G_math_solver_cholesky_sband = _libs['grass_gmath.7.8'].G_math_solver_cholesky_sband
    G_math_solver_cholesky_sband.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_solver_cholesky_sband.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 103
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_jacobi'):
    G_math_solver_jacobi = _libs['grass_gmath.7.8'].G_math_solver_jacobi
    G_math_solver_jacobi.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]
    G_math_solver_jacobi.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 104
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_gs'):
    G_math_solver_gs = _libs['grass_gmath.7.8'].G_math_solver_gs
    G_math_solver_gs.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]
    G_math_solver_gs.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 106
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_pcg'):
    G_math_solver_pcg = _libs['grass_gmath.7.8'].G_math_solver_pcg
    G_math_solver_pcg.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_int]
    G_math_solver_pcg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 107
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_cg'):
    G_math_solver_cg = _libs['grass_gmath.7.8'].G_math_solver_cg
    G_math_solver_cg.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]
    G_math_solver_cg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 108
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_cg_sband'):
    G_math_solver_cg_sband = _libs['grass_gmath.7.8'].G_math_solver_cg_sband
    G_math_solver_cg_sband.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_int, c_double]
    G_math_solver_cg_sband.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 109
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_bicgstab'):
    G_math_solver_bicgstab = _libs['grass_gmath.7.8'].G_math_solver_bicgstab
    G_math_solver_bicgstab.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]
    G_math_solver_bicgstab.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 110
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_sparse_jacobi'):
    G_math_solver_sparse_jacobi = _libs['grass_gmath.7.8'].G_math_solver_sparse_jacobi
    G_math_solver_sparse_jacobi.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]
    G_math_solver_sparse_jacobi.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 111
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_sparse_gs'):
    G_math_solver_sparse_gs = _libs['grass_gmath.7.8'].G_math_solver_sparse_gs
    G_math_solver_sparse_gs.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_double]
    G_math_solver_sparse_gs.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 112
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_sparse_pcg'):
    G_math_solver_sparse_pcg = _libs['grass_gmath.7.8'].G_math_solver_sparse_pcg
    G_math_solver_sparse_pcg.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double, c_int]
    G_math_solver_sparse_pcg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 113
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_sparse_cg'):
    G_math_solver_sparse_cg = _libs['grass_gmath.7.8'].G_math_solver_sparse_cg
    G_math_solver_sparse_cg.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]
    G_math_solver_sparse_cg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 114
if hasattr(_libs['grass_gmath.7.8'], 'G_math_solver_sparse_bicgstab'):
    G_math_solver_sparse_bicgstab = _libs['grass_gmath.7.8'].G_math_solver_sparse_bicgstab
    G_math_solver_sparse_bicgstab.argtypes = [POINTER(POINTER(G_math_spvector)), POINTER(c_double), POINTER(c_double), c_int, c_int, c_double]
    G_math_solver_sparse_bicgstab.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 117
if hasattr(_libs['grass_gmath.7.8'], 'G_math_gauss_elimination'):
    G_math_gauss_elimination = _libs['grass_gmath.7.8'].G_math_gauss_elimination
    G_math_gauss_elimination.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_gauss_elimination.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 118
if hasattr(_libs['grass_gmath.7.8'], 'G_math_lu_decomposition'):
    G_math_lu_decomposition = _libs['grass_gmath.7.8'].G_math_lu_decomposition
    G_math_lu_decomposition.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), c_int]
    G_math_lu_decomposition.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 119
if hasattr(_libs['grass_gmath.7.8'], 'G_math_cholesky_decomposition'):
    G_math_cholesky_decomposition = _libs['grass_gmath.7.8'].G_math_cholesky_decomposition
    G_math_cholesky_decomposition.argtypes = [POINTER(POINTER(c_double)), c_int, c_int]
    G_math_cholesky_decomposition.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 120
if hasattr(_libs['grass_gmath.7.8'], 'G_math_cholesky_sband_decomposition'):
    G_math_cholesky_sband_decomposition = _libs['grass_gmath.7.8'].G_math_cholesky_sband_decomposition
    G_math_cholesky_sband_decomposition.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, c_int]
    G_math_cholesky_sband_decomposition.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 121
if hasattr(_libs['grass_gmath.7.8'], 'G_math_backward_substitution'):
    G_math_backward_substitution = _libs['grass_gmath.7.8'].G_math_backward_substitution
    G_math_backward_substitution.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_backward_substitution.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 122
if hasattr(_libs['grass_gmath.7.8'], 'G_math_forward_substitution'):
    G_math_forward_substitution = _libs['grass_gmath.7.8'].G_math_forward_substitution
    G_math_forward_substitution.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int]
    G_math_forward_substitution.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 123
if hasattr(_libs['grass_gmath.7.8'], 'G_math_cholesky_sband_substitution'):
    G_math_cholesky_sband_substitution = _libs['grass_gmath.7.8'].G_math_cholesky_sband_substitution
    G_math_cholesky_sband_substitution.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_cholesky_sband_substitution.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 128
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_x_dot_y'):
    G_math_d_x_dot_y = _libs['grass_gmath.7.8'].G_math_d_x_dot_y
    G_math_d_x_dot_y.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_x_dot_y.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 129
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_asum_norm'):
    G_math_d_asum_norm = _libs['grass_gmath.7.8'].G_math_d_asum_norm
    G_math_d_asum_norm.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_asum_norm.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 130
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_euclid_norm'):
    G_math_d_euclid_norm = _libs['grass_gmath.7.8'].G_math_d_euclid_norm
    G_math_d_euclid_norm.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_euclid_norm.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 131
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_max_norm'):
    G_math_d_max_norm = _libs['grass_gmath.7.8'].G_math_d_max_norm
    G_math_d_max_norm.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_max_norm.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 132
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_ax_by'):
    G_math_d_ax_by = _libs['grass_gmath.7.8'].G_math_d_ax_by
    G_math_d_ax_by.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double, c_double, c_int]
    G_math_d_ax_by.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 133
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_copy'):
    G_math_d_copy = _libs['grass_gmath.7.8'].G_math_d_copy
    G_math_d_copy.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_d_copy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 135
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_x_dot_y'):
    G_math_f_x_dot_y = _libs['grass_gmath.7.8'].G_math_f_x_dot_y
    G_math_f_x_dot_y.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_x_dot_y.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 136
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_asum_norm'):
    G_math_f_asum_norm = _libs['grass_gmath.7.8'].G_math_f_asum_norm
    G_math_f_asum_norm.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_asum_norm.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 137
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_euclid_norm'):
    G_math_f_euclid_norm = _libs['grass_gmath.7.8'].G_math_f_euclid_norm
    G_math_f_euclid_norm.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_euclid_norm.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 138
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_max_norm'):
    G_math_f_max_norm = _libs['grass_gmath.7.8'].G_math_f_max_norm
    G_math_f_max_norm.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_max_norm.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 139
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_ax_by'):
    G_math_f_ax_by = _libs['grass_gmath.7.8'].G_math_f_ax_by
    G_math_f_ax_by.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(c_float), c_float, c_float, c_int]
    G_math_f_ax_by.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 140
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_copy'):
    G_math_f_copy = _libs['grass_gmath.7.8'].G_math_f_copy
    G_math_f_copy.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_f_copy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 142
if hasattr(_libs['grass_gmath.7.8'], 'G_math_i_x_dot_y'):
    G_math_i_x_dot_y = _libs['grass_gmath.7.8'].G_math_i_x_dot_y
    G_math_i_x_dot_y.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_double), c_int]
    G_math_i_x_dot_y.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 143
if hasattr(_libs['grass_gmath.7.8'], 'G_math_i_asum_norm'):
    G_math_i_asum_norm = _libs['grass_gmath.7.8'].G_math_i_asum_norm
    G_math_i_asum_norm.argtypes = [POINTER(c_int), POINTER(c_double), c_int]
    G_math_i_asum_norm.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 144
if hasattr(_libs['grass_gmath.7.8'], 'G_math_i_euclid_norm'):
    G_math_i_euclid_norm = _libs['grass_gmath.7.8'].G_math_i_euclid_norm
    G_math_i_euclid_norm.argtypes = [POINTER(c_int), POINTER(c_double), c_int]
    G_math_i_euclid_norm.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 145
if hasattr(_libs['grass_gmath.7.8'], 'G_math_i_max_norm'):
    G_math_i_max_norm = _libs['grass_gmath.7.8'].G_math_i_max_norm
    G_math_i_max_norm.argtypes = [POINTER(c_int), POINTER(c_int), c_int]
    G_math_i_max_norm.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 146
if hasattr(_libs['grass_gmath.7.8'], 'G_math_i_ax_by'):
    G_math_i_ax_by = _libs['grass_gmath.7.8'].G_math_i_ax_by
    G_math_i_ax_by.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), c_int, c_int, c_int]
    G_math_i_ax_by.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 147
if hasattr(_libs['grass_gmath.7.8'], 'G_math_i_copy'):
    G_math_i_copy = _libs['grass_gmath.7.8'].G_math_i_copy
    G_math_i_copy.argtypes = [POINTER(c_int), POINTER(c_int), c_int]
    G_math_i_copy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 150
if hasattr(_libs['grass_gmath.7.8'], 'G_math_ddot'):
    G_math_ddot = _libs['grass_gmath.7.8'].G_math_ddot
    G_math_ddot.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_ddot.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 151
if hasattr(_libs['grass_gmath.7.8'], 'G_math_sdot'):
    G_math_sdot = _libs['grass_gmath.7.8'].G_math_sdot
    G_math_sdot.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_sdot.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 152
if hasattr(_libs['grass_gmath.7.8'], 'G_math_sdsdot'):
    G_math_sdsdot = _libs['grass_gmath.7.8'].G_math_sdsdot
    G_math_sdsdot.argtypes = [POINTER(c_float), POINTER(c_float), c_float, c_int]
    G_math_sdsdot.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 153
if hasattr(_libs['grass_gmath.7.8'], 'G_math_dnrm2'):
    G_math_dnrm2 = _libs['grass_gmath.7.8'].G_math_dnrm2
    G_math_dnrm2.argtypes = [POINTER(c_double), c_int]
    G_math_dnrm2.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 154
if hasattr(_libs['grass_gmath.7.8'], 'G_math_dasum'):
    G_math_dasum = _libs['grass_gmath.7.8'].G_math_dasum
    G_math_dasum.argtypes = [POINTER(c_double), c_int]
    G_math_dasum.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 155
if hasattr(_libs['grass_gmath.7.8'], 'G_math_idamax'):
    G_math_idamax = _libs['grass_gmath.7.8'].G_math_idamax
    G_math_idamax.argtypes = [POINTER(c_double), c_int]
    G_math_idamax.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 156
if hasattr(_libs['grass_gmath.7.8'], 'G_math_snrm2'):
    G_math_snrm2 = _libs['grass_gmath.7.8'].G_math_snrm2
    G_math_snrm2.argtypes = [POINTER(c_float), c_int]
    G_math_snrm2.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 157
if hasattr(_libs['grass_gmath.7.8'], 'G_math_sasum'):
    G_math_sasum = _libs['grass_gmath.7.8'].G_math_sasum
    G_math_sasum.argtypes = [POINTER(c_float), c_int]
    G_math_sasum.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 158
if hasattr(_libs['grass_gmath.7.8'], 'G_math_isamax'):
    G_math_isamax = _libs['grass_gmath.7.8'].G_math_isamax
    G_math_isamax.argtypes = [POINTER(c_float), c_int]
    G_math_isamax.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 159
if hasattr(_libs['grass_gmath.7.8'], 'G_math_dscal'):
    G_math_dscal = _libs['grass_gmath.7.8'].G_math_dscal
    G_math_dscal.argtypes = [POINTER(c_double), c_double, c_int]
    G_math_dscal.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 160
if hasattr(_libs['grass_gmath.7.8'], 'G_math_sscal'):
    G_math_sscal = _libs['grass_gmath.7.8'].G_math_sscal
    G_math_sscal.argtypes = [POINTER(c_float), c_float, c_int]
    G_math_sscal.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 161
if hasattr(_libs['grass_gmath.7.8'], 'G_math_dcopy'):
    G_math_dcopy = _libs['grass_gmath.7.8'].G_math_dcopy
    G_math_dcopy.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    G_math_dcopy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 162
if hasattr(_libs['grass_gmath.7.8'], 'G_math_scopy'):
    G_math_scopy = _libs['grass_gmath.7.8'].G_math_scopy
    G_math_scopy.argtypes = [POINTER(c_float), POINTER(c_float), c_int]
    G_math_scopy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 163
if hasattr(_libs['grass_gmath.7.8'], 'G_math_daxpy'):
    G_math_daxpy = _libs['grass_gmath.7.8'].G_math_daxpy
    G_math_daxpy.argtypes = [POINTER(c_double), POINTER(c_double), c_double, c_int]
    G_math_daxpy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 164
if hasattr(_libs['grass_gmath.7.8'], 'G_math_saxpy'):
    G_math_saxpy = _libs['grass_gmath.7.8'].G_math_saxpy
    G_math_saxpy.argtypes = [POINTER(c_float), POINTER(c_float), c_float, c_int]
    G_math_saxpy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 167
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_Ax'):
    G_math_d_Ax = _libs['grass_gmath.7.8'].G_math_d_Ax
    G_math_d_Ax.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_int, c_int]
    G_math_d_Ax.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 168
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_Ax'):
    G_math_f_Ax = _libs['grass_gmath.7.8'].G_math_f_Ax
    G_math_f_Ax.argtypes = [POINTER(POINTER(c_float)), POINTER(c_float), POINTER(c_float), c_int, c_int]
    G_math_f_Ax.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 169
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_x_dyad_y'):
    G_math_d_x_dyad_y = _libs['grass_gmath.7.8'].G_math_d_x_dyad_y
    G_math_d_x_dyad_y.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(POINTER(c_double)), c_int, c_int]
    G_math_d_x_dyad_y.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 170
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_x_dyad_y'):
    G_math_f_x_dyad_y = _libs['grass_gmath.7.8'].G_math_f_x_dyad_y
    G_math_f_x_dyad_y.argtypes = [POINTER(c_float), POINTER(c_float), POINTER(POINTER(c_float)), c_int, c_int]
    G_math_f_x_dyad_y.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 171
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_aAx_by'):
    G_math_d_aAx_by = _libs['grass_gmath.7.8'].G_math_d_aAx_by
    G_math_d_aAx_by.argtypes = [POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), c_double, c_double, POINTER(c_double), c_int, c_int]
    G_math_d_aAx_by.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 172
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_aAx_by'):
    G_math_f_aAx_by = _libs['grass_gmath.7.8'].G_math_f_aAx_by
    G_math_f_aAx_by.argtypes = [POINTER(POINTER(c_float)), POINTER(c_float), POINTER(c_float), c_float, c_float, POINTER(c_float), c_int, c_int]
    G_math_f_aAx_by.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 173
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_A_T'):
    G_math_d_A_T = _libs['grass_gmath.7.8'].G_math_d_A_T
    G_math_d_A_T.argtypes = [POINTER(POINTER(c_double)), c_int]
    G_math_d_A_T.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 174
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_A_T'):
    G_math_f_A_T = _libs['grass_gmath.7.8'].G_math_f_A_T
    G_math_f_A_T.argtypes = [POINTER(POINTER(c_float)), c_int]
    G_math_f_A_T.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 177
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_aA_B'):
    G_math_d_aA_B = _libs['grass_gmath.7.8'].G_math_d_aA_B
    G_math_d_aA_B.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_double, POINTER(POINTER(c_double)), c_int, c_int]
    G_math_d_aA_B.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 178
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_aA_B'):
    G_math_f_aA_B = _libs['grass_gmath.7.8'].G_math_f_aA_B
    G_math_f_aA_B.argtypes = [POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), c_float, POINTER(POINTER(c_float)), c_int, c_int]
    G_math_f_aA_B.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 179
if hasattr(_libs['grass_gmath.7.8'], 'G_math_d_AB'):
    G_math_d_AB = _libs['grass_gmath.7.8'].G_math_d_AB
    G_math_d_AB.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, c_int, c_int]
    G_math_d_AB.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gmath.h: 180
if hasattr(_libs['grass_gmath.7.8'], 'G_math_f_AB'):
    G_math_f_AB = _libs['grass_gmath.7.8'].G_math_f_AB
    G_math_f_AB.argtypes = [POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), POINTER(POINTER(c_float)), c_int, c_int, c_int]
    G_math_f_AB.restype = None

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 36
try:
    G_MATH_SOLVER_DIRECT_GAUSS = 'gauss'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 37
try:
    G_MATH_SOLVER_DIRECT_LU = 'lu'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 38
try:
    G_MATH_SOLVER_DIRECT_CHOLESKY = 'cholesky'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 39
try:
    G_MATH_SOLVER_ITERATIVE_JACOBI = 'jacobi'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 40
try:
    G_MATH_SOLVER_ITERATIVE_SOR = 'sor'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 41
try:
    G_MATH_SOLVER_ITERATIVE_CG = 'cg'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 42
try:
    G_MATH_SOLVER_ITERATIVE_PCG = 'pcg'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 43
try:
    G_MATH_SOLVER_ITERATIVE_BICGSTAB = 'bicgstab'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 46
try:
    G_MATH_DIAGONAL_PRECONDITION = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 47
try:
    G_MATH_ROWSCALE_ABSSUMNORM_PRECONDITION = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 48
try:
    G_MATH_ROWSCALE_EUKLIDNORM_PRECONDITION = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gmath.h: 49
try:
    G_MATH_ROWSCALE_MAXNORM_PRECONDITION = 4
except:
    pass

# No inserted files

