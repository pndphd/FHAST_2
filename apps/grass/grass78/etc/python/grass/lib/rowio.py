'''Wrapper for rowio.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_rowio.7.8 C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rowio.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/rowio.h -o OBJ.x86_64-w64-mingw32/rowio.py

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

_libs["grass_rowio.7.8"] = load_library("grass_rowio.7.8")

# 1 libraries
# End libraries

# No modules

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\rowio.h: 14
class struct_ROWIO_RCB(Structure):
    pass

struct_ROWIO_RCB.__slots__ = [
    'buf',
    'age',
    'row',
    'dirty',
]
struct_ROWIO_RCB._fields_ = [
    ('buf', POINTER(None)),
    ('age', c_int),
    ('row', c_int),
    ('dirty', c_int),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\rowio.h: 21
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    'fd',
    'nrows',
    'len',
    'cur',
    'buf',
    'getrow',
    'putrow',
    'rcb',
]
struct_anon_1._fields_ = [
    ('fd', c_int),
    ('nrows', c_int),
    ('len', c_int),
    ('cur', c_int),
    ('buf', POINTER(None)),
    ('getrow', CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), c_int, c_int)),
    ('putrow', CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), c_int, c_int)),
    ('rcb', POINTER(struct_ROWIO_RCB)),
]

ROWIO = struct_anon_1 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\rowio.h: 21

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/rowio.h: 4
if hasattr(_libs['grass_rowio.7.8'], 'Rowio_fileno'):
    Rowio_fileno = _libs['grass_rowio.7.8'].Rowio_fileno
    Rowio_fileno.argtypes = [POINTER(ROWIO)]
    Rowio_fileno.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/rowio.h: 5
if hasattr(_libs['grass_rowio.7.8'], 'Rowio_forget'):
    Rowio_forget = _libs['grass_rowio.7.8'].Rowio_forget
    Rowio_forget.argtypes = [POINTER(ROWIO), c_int]
    Rowio_forget.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/rowio.h: 6
if hasattr(_libs['grass_rowio.7.8'], 'Rowio_get'):
    Rowio_get = _libs['grass_rowio.7.8'].Rowio_get
    Rowio_get.argtypes = [POINTER(ROWIO), c_int]
    Rowio_get.restype = POINTER(c_ubyte)
    Rowio_get.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/rowio.h: 7
if hasattr(_libs['grass_rowio.7.8'], 'Rowio_flush'):
    Rowio_flush = _libs['grass_rowio.7.8'].Rowio_flush
    Rowio_flush.argtypes = [POINTER(ROWIO)]
    Rowio_flush.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/rowio.h: 8
if hasattr(_libs['grass_rowio.7.8'], 'Rowio_put'):
    Rowio_put = _libs['grass_rowio.7.8'].Rowio_put
    Rowio_put.argtypes = [POINTER(ROWIO), POINTER(None), c_int]
    Rowio_put.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/rowio.h: 9
if hasattr(_libs['grass_rowio.7.8'], 'Rowio_release'):
    Rowio_release = _libs['grass_rowio.7.8'].Rowio_release
    Rowio_release.argtypes = [POINTER(ROWIO)]
    Rowio_release.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/rowio.h: 10
if hasattr(_libs['grass_rowio.7.8'], 'Rowio_setup'):
    Rowio_setup = _libs['grass_rowio.7.8'].Rowio_setup
    Rowio_setup.argtypes = [POINTER(ROWIO), c_int, c_int, c_int, CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), c_int, c_int), CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), c_int, c_int)]
    Rowio_setup.restype = c_int

ROWIO_RCB = struct_ROWIO_RCB # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\rowio.h: 14

# No inserted files

