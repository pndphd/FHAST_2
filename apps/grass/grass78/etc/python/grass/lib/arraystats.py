'''Wrapper for arraystats.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_arraystats.7.8 C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/arraystats.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h -o OBJ.x86_64-w64-mingw32/arraystats.py

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

_libs["grass_arraystats.7.8"] = load_library("grass_arraystats.7.8")

# 1 libraries
# End libraries

# No modules

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 526
class struct_Option(Structure):
    pass

struct_Option.__slots__ = [
    'key',
    'type',
    'required',
    'multiple',
    'options',
    'opts',
    'key_desc',
    'label',
    'description',
    'descriptions',
    'descs',
    'answer',
    '_def',
    'answers',
    'next_opt',
    'gisprompt',
    'guisection',
    'guidependency',
    'checker',
    'count',
]
struct_Option._fields_ = [
    ('key', String),
    ('type', c_int),
    ('required', c_int),
    ('multiple', c_int),
    ('options', String),
    ('opts', POINTER(POINTER(c_char))),
    ('key_desc', String),
    ('label', String),
    ('description', String),
    ('descriptions', String),
    ('descs', POINTER(POINTER(c_char))),
    ('answer', String),
    ('_def', String),
    ('answers', POINTER(POINTER(c_char))),
    ('next_opt', POINTER(struct_Option)),
    ('gisprompt', String),
    ('guisection', String),
    ('guidependency', String),
    ('checker', CFUNCTYPE(UNCHECKED(c_int), String)),
    ('count', c_int),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 11
class struct_GASTATS(Structure):
    pass

struct_GASTATS.__slots__ = [
    'count',
    'min',
    'max',
    'sum',
    'sumsq',
    'sumabs',
    'mean',
    'meanabs',
    'var',
    'stdev',
]
struct_GASTATS._fields_ = [
    ('count', c_double),
    ('min', c_double),
    ('max', c_double),
    ('sum', c_double),
    ('sumsq', c_double),
    ('sumabs', c_double),
    ('mean', c_double),
    ('meanabs', c_double),
    ('var', c_double),
    ('stdev', c_double),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 5
if hasattr(_libs['grass_arraystats.7.8'], 'AS_eqdrt'):
    AS_eqdrt = _libs['grass_arraystats.7.8'].AS_eqdrt
    AS_eqdrt.argtypes = [POINTER(c_double), POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_eqdrt.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 6
if hasattr(_libs['grass_arraystats.7.8'], 'AS_basic_stats'):
    AS_basic_stats = _libs['grass_arraystats.7.8'].AS_basic_stats
    AS_basic_stats.argtypes = [POINTER(c_double), c_int, POINTER(struct_GASTATS)]
    AS_basic_stats.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 9
if hasattr(_libs['grass_arraystats.7.8'], 'AS_option_to_algorithm'):
    AS_option_to_algorithm = _libs['grass_arraystats.7.8'].AS_option_to_algorithm
    AS_option_to_algorithm.argtypes = [POINTER(struct_Option)]
    AS_option_to_algorithm.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 10
if hasattr(_libs['grass_arraystats.7.8'], 'AS_class_apply_algorithm'):
    AS_class_apply_algorithm = _libs['grass_arraystats.7.8'].AS_class_apply_algorithm
    AS_class_apply_algorithm.argtypes = [c_int, POINTER(c_double), c_int, POINTER(c_int), POINTER(c_double)]
    AS_class_apply_algorithm.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 11
if hasattr(_libs['grass_arraystats.7.8'], 'AS_class_interval'):
    AS_class_interval = _libs['grass_arraystats.7.8'].AS_class_interval
    AS_class_interval.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_class_interval.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 12
if hasattr(_libs['grass_arraystats.7.8'], 'AS_class_quant'):
    AS_class_quant = _libs['grass_arraystats.7.8'].AS_class_quant
    AS_class_quant.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_class_quant.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 13
if hasattr(_libs['grass_arraystats.7.8'], 'AS_class_discont'):
    AS_class_discont = _libs['grass_arraystats.7.8'].AS_class_discont
    AS_class_discont.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_class_discont.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 14
if hasattr(_libs['grass_arraystats.7.8'], 'AS_class_stdev'):
    AS_class_stdev = _libs['grass_arraystats.7.8'].AS_class_stdev
    AS_class_stdev.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double)]
    AS_class_stdev.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 15
if hasattr(_libs['grass_arraystats.7.8'], 'AS_class_equiprob'):
    AS_class_equiprob = _libs['grass_arraystats.7.8'].AS_class_equiprob
    AS_class_equiprob.argtypes = [POINTER(c_double), c_int, POINTER(c_int), POINTER(c_double)]
    AS_class_equiprob.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/arraystats.h: 16
if hasattr(_libs['grass_arraystats.7.8'], 'AS_class_frequencies'):
    AS_class_frequencies = _libs['grass_arraystats.7.8'].AS_class_frequencies
    AS_class_frequencies.argtypes = [POINTER(c_double), c_int, c_int, POINTER(c_double), POINTER(c_int)]
    AS_class_frequencies.restype = c_int

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 25
try:
    CLASS_INTERVAL = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 26
try:
    CLASS_STDEV = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 27
try:
    CLASS_QUANT = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 28
try:
    CLASS_EQUIPROB = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 29
try:
    CLASS_DISCONT = 5
except:
    pass

GASTATS = struct_GASTATS # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\arraystats.h: 11

# No inserted files

