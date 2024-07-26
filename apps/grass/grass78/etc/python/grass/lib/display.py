'''Wrapper for display.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_display.7.8 C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/display.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h -o OBJ.x86_64-w64-mingw32/display.py

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

_libs["grass_display.7.8"] = load_library("grass_display.7.8")

# 1 libraries
# End libraries

# No modules

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 407
class struct_Cell_head(Structure):
    pass

struct_Cell_head.__slots__ = [
    'format',
    'compressed',
    'rows',
    'rows3',
    'cols',
    'cols3',
    'depths',
    'proj',
    'zone',
    'ew_res',
    'ew_res3',
    'ns_res',
    'ns_res3',
    'tb_res',
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
]
struct_Cell_head._fields_ = [
    ('format', c_int),
    ('compressed', c_int),
    ('rows', c_int),
    ('rows3', c_int),
    ('cols', c_int),
    ('cols3', c_int),
    ('depths', c_int),
    ('proj', c_int),
    ('zone', c_int),
    ('ew_res', c_double),
    ('ew_res3', c_double),
    ('ns_res', c_double),
    ('ns_res3', c_double),
    ('tb_res', c_double),
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
]

CELL = c_int # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 597

DCELL = c_double # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 598

FCELL = c_float # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 599

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 618
class struct__Color_Value_(Structure):
    pass

struct__Color_Value_.__slots__ = [
    'value',
    'red',
    'grn',
    'blu',
]
struct__Color_Value_._fields_ = [
    ('value', DCELL),
    ('red', c_ubyte),
    ('grn', c_ubyte),
    ('blu', c_ubyte),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 626
class struct__Color_Rule_(Structure):
    pass

struct__Color_Rule_.__slots__ = [
    'low',
    'high',
    'next',
    'prev',
]
struct__Color_Rule_._fields_ = [
    ('low', struct__Color_Value_),
    ('high', struct__Color_Value_),
    ('next', POINTER(struct__Color_Rule_)),
    ('prev', POINTER(struct__Color_Rule_)),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 638
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'red',
    'grn',
    'blu',
    'set',
    'nalloc',
    'active',
]
struct_anon_5._fields_ = [
    ('red', POINTER(c_ubyte)),
    ('grn', POINTER(c_ubyte)),
    ('blu', POINTER(c_ubyte)),
    ('set', POINTER(c_ubyte)),
    ('nalloc', c_int),
    ('active', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 648
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'vals',
    'rules',
    'nalloc',
    'active',
]
struct_anon_6._fields_ = [
    ('vals', POINTER(DCELL)),
    ('rules', POINTER(POINTER(struct__Color_Rule_))),
    ('nalloc', c_int),
    ('active', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 633
class struct__Color_Info_(Structure):
    pass

struct__Color_Info_.__slots__ = [
    'rules',
    'n_rules',
    'lookup',
    'fp_lookup',
    'min',
    'max',
]
struct__Color_Info_._fields_ = [
    ('rules', POINTER(struct__Color_Rule_)),
    ('n_rules', c_int),
    ('lookup', struct_anon_5),
    ('fp_lookup', struct_anon_6),
    ('min', DCELL),
    ('max', DCELL),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 660
class struct_Colors(Structure):
    pass

struct_Colors.__slots__ = [
    'version',
    'shift',
    'invert',
    'is_float',
    'null_set',
    'null_red',
    'null_grn',
    'null_blu',
    'undef_set',
    'undef_red',
    'undef_grn',
    'undef_blu',
    'fixed',
    'modular',
    'cmin',
    'cmax',
    'organizing',
]
struct_Colors._fields_ = [
    ('version', c_int),
    ('shift', DCELL),
    ('invert', c_int),
    ('is_float', c_int),
    ('null_set', c_int),
    ('null_red', c_ubyte),
    ('null_grn', c_ubyte),
    ('null_blu', c_ubyte),
    ('undef_set', c_int),
    ('undef_red', c_ubyte),
    ('undef_grn', c_ubyte),
    ('undef_blu', c_ubyte),
    ('fixed', struct__Color_Info_),
    ('modular', struct__Color_Info_),
    ('cmin', DCELL),
    ('cmax', DCELL),
    ('organizing', c_int),
]

RASTER_MAP_TYPE = c_int # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 25

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 27
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'color',
    'r',
    'g',
    'b',
    'fr',
    'fg',
    'fb',
]
struct_anon_8._fields_ = [
    ('color', c_int),
    ('r', c_int),
    ('g', c_int),
    ('b', c_int),
    ('fr', c_double),
    ('fg', c_double),
    ('fb', c_double),
]

SYMBCOLOR = struct_anon_8 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 27

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 35
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'count',
    'alloc',
    'x',
    'y',
]
struct_anon_9._fields_ = [
    ('count', c_int),
    ('alloc', c_int),
    ('x', POINTER(c_double)),
    ('y', POINTER(c_double)),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 40
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'clock',
    'x',
    'y',
    'r',
    'a1',
    'a2',
]
struct_anon_10._fields_ = [
    ('clock', c_int),
    ('x', c_double),
    ('y', c_double),
    ('r', c_double),
    ('a1', c_double),
    ('a2', c_double),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 33
class union_anon_11(Union):
    pass

union_anon_11.__slots__ = [
    'line',
    'arc',
]
union_anon_11._fields_ = [
    ('line', struct_anon_9),
    ('arc', struct_anon_10),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 46
class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'type',
    'coor',
]
struct_anon_12._fields_ = [
    ('type', c_int),
    ('coor', union_anon_11),
]

SYMBEL = struct_anon_12 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 46

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 55
class struct_anon_13(Structure):
    pass

struct_anon_13.__slots__ = [
    'count',
    'alloc',
    'elem',
    'scount',
    'salloc',
    'sx',
    'sy',
]
struct_anon_13._fields_ = [
    ('count', c_int),
    ('alloc', c_int),
    ('elem', POINTER(POINTER(SYMBEL))),
    ('scount', c_int),
    ('salloc', c_int),
    ('sx', POINTER(c_double)),
    ('sy', POINTER(c_double)),
]

SYMBCHAIN = struct_anon_13 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 55

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 65
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'type',
    'color',
    'fcolor',
    'count',
    'alloc',
    'chain',
]
struct_anon_14._fields_ = [
    ('type', c_int),
    ('color', SYMBCOLOR),
    ('fcolor', SYMBCOLOR),
    ('count', c_int),
    ('alloc', c_int),
    ('chain', POINTER(POINTER(SYMBCHAIN))),
]

SYMBPART = struct_anon_14 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 65

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 74
class struct_anon_15(Structure):
    pass

struct_anon_15.__slots__ = [
    'scale',
    'yscale',
    'xscale',
    'count',
    'alloc',
    'part',
]
struct_anon_15._fields_ = [
    ('scale', c_double),
    ('yscale', c_double),
    ('xscale', c_double),
    ('count', c_int),
    ('alloc', c_int),
    ('part', POINTER(POINTER(SYMBPART))),
]

SYMBOL = struct_anon_15 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/symbol.h: 74

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 8
class struct_color_rgba(Structure):
    pass

struct_color_rgba.__slots__ = [
    'r',
    'g',
    'b',
    'a',
]
struct_color_rgba._fields_ = [
    ('r', c_ubyte),
    ('g', c_ubyte),
    ('b', c_ubyte),
    ('a', c_ubyte),
]

RGBA_Color = struct_color_rgba # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 13

enum_clip_mode = c_int # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 20

M_NONE = 0 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 20

M_CULL = (M_NONE + 1) # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 20

M_CLIP = (M_CULL + 1) # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 20

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 5
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_update_conversions'):
        continue
    D_update_conversions = _lib.D_update_conversions
    D_update_conversions.argtypes = []
    D_update_conversions.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 6
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_fit_d_to_u'):
        continue
    D_fit_d_to_u = _lib.D_fit_d_to_u
    D_fit_d_to_u.argtypes = []
    D_fit_d_to_u.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 7
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_fit_u_to_d'):
        continue
    D_fit_u_to_d = _lib.D_fit_u_to_d
    D_fit_u_to_d.argtypes = []
    D_fit_u_to_d.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 8
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_show_conversions'):
        continue
    D_show_conversions = _lib.D_show_conversions
    D_show_conversions.argtypes = []
    D_show_conversions.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 10
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_do_conversions'):
        continue
    D_do_conversions = _lib.D_do_conversions
    D_do_conversions.argtypes = [POINTER(struct_Cell_head), c_double, c_double, c_double, c_double]
    D_do_conversions.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 12
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_is_lat_lon'):
        continue
    D_is_lat_lon = _lib.D_is_lat_lon
    D_is_lat_lon.argtypes = []
    D_is_lat_lon.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_d_to_a_xconv'):
        continue
    D_get_d_to_a_xconv = _lib.D_get_d_to_a_xconv
    D_get_d_to_a_xconv.argtypes = []
    D_get_d_to_a_xconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 15
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_d_to_a_yconv'):
        continue
    D_get_d_to_a_yconv = _lib.D_get_d_to_a_yconv
    D_get_d_to_a_yconv.argtypes = []
    D_get_d_to_a_yconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 16
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_d_to_u_xconv'):
        continue
    D_get_d_to_u_xconv = _lib.D_get_d_to_u_xconv
    D_get_d_to_u_xconv.argtypes = []
    D_get_d_to_u_xconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_d_to_u_yconv'):
        continue
    D_get_d_to_u_yconv = _lib.D_get_d_to_u_yconv
    D_get_d_to_u_yconv.argtypes = []
    D_get_d_to_u_yconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 18
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_a_to_u_xconv'):
        continue
    D_get_a_to_u_xconv = _lib.D_get_a_to_u_xconv
    D_get_a_to_u_xconv.argtypes = []
    D_get_a_to_u_xconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 19
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_a_to_u_yconv'):
        continue
    D_get_a_to_u_yconv = _lib.D_get_a_to_u_yconv
    D_get_a_to_u_yconv.argtypes = []
    D_get_a_to_u_yconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 20
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_a_to_d_xconv'):
        continue
    D_get_a_to_d_xconv = _lib.D_get_a_to_d_xconv
    D_get_a_to_d_xconv.argtypes = []
    D_get_a_to_d_xconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 21
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_a_to_d_yconv'):
        continue
    D_get_a_to_d_yconv = _lib.D_get_a_to_d_yconv
    D_get_a_to_d_yconv.argtypes = []
    D_get_a_to_d_yconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 22
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_u_to_d_xconv'):
        continue
    D_get_u_to_d_xconv = _lib.D_get_u_to_d_xconv
    D_get_u_to_d_xconv.argtypes = []
    D_get_u_to_d_xconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 23
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_u_to_d_yconv'):
        continue
    D_get_u_to_d_yconv = _lib.D_get_u_to_d_yconv
    D_get_u_to_d_yconv.argtypes = []
    D_get_u_to_d_yconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_u_to_a_xconv'):
        continue
    D_get_u_to_a_xconv = _lib.D_get_u_to_a_xconv
    D_get_u_to_a_xconv.argtypes = []
    D_get_u_to_a_xconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_u_to_a_yconv'):
        continue
    D_get_u_to_a_yconv = _lib.D_get_u_to_a_yconv
    D_get_u_to_a_yconv.argtypes = []
    D_get_u_to_a_yconv.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 27
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_ns_resolution'):
        continue
    D_get_ns_resolution = _lib.D_get_ns_resolution
    D_get_ns_resolution.argtypes = []
    D_get_ns_resolution.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 28
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_ew_resolution'):
        continue
    D_get_ew_resolution = _lib.D_get_ew_resolution
    D_get_ew_resolution.argtypes = []
    D_get_ew_resolution.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 30
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_u_west'):
        continue
    D_get_u_west = _lib.D_get_u_west
    D_get_u_west.argtypes = []
    D_get_u_west.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 31
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_u_east'):
        continue
    D_get_u_east = _lib.D_get_u_east
    D_get_u_east.argtypes = []
    D_get_u_east.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 32
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_u_north'):
        continue
    D_get_u_north = _lib.D_get_u_north
    D_get_u_north.argtypes = []
    D_get_u_north.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 33
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_u_south'):
        continue
    D_get_u_south = _lib.D_get_u_south
    D_get_u_south.argtypes = []
    D_get_u_south.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 34
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_a_west'):
        continue
    D_get_a_west = _lib.D_get_a_west
    D_get_a_west.argtypes = []
    D_get_a_west.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 35
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_a_east'):
        continue
    D_get_a_east = _lib.D_get_a_east
    D_get_a_east.argtypes = []
    D_get_a_east.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 36
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_a_north'):
        continue
    D_get_a_north = _lib.D_get_a_north
    D_get_a_north.argtypes = []
    D_get_a_north.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 37
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_a_south'):
        continue
    D_get_a_south = _lib.D_get_a_south
    D_get_a_south.argtypes = []
    D_get_a_south.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 38
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_d_west'):
        continue
    D_get_d_west = _lib.D_get_d_west
    D_get_d_west.argtypes = []
    D_get_d_west.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 39
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_d_east'):
        continue
    D_get_d_east = _lib.D_get_d_east
    D_get_d_east.argtypes = []
    D_get_d_east.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 40
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_d_north'):
        continue
    D_get_d_north = _lib.D_get_d_north
    D_get_d_north.argtypes = []
    D_get_d_north.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 41
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_d_south'):
        continue
    D_get_d_south = _lib.D_get_d_south
    D_get_d_south.argtypes = []
    D_get_d_south.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_region'):
        continue
    D_set_region = _lib.D_set_region
    D_set_region.argtypes = [POINTER(struct_Cell_head)]
    D_set_region.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 44
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_src'):
        continue
    D_set_src = _lib.D_set_src
    D_set_src.argtypes = [c_double, c_double, c_double, c_double]
    D_set_src.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 45
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_src'):
        continue
    D_get_src = _lib.D_get_src
    D_get_src.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    D_get_src.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 46
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_grid'):
        continue
    D_set_grid = _lib.D_set_grid
    D_set_grid.argtypes = [c_int, c_int, c_int, c_int]
    D_set_grid.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 47
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_grid'):
        continue
    D_get_grid = _lib.D_get_grid
    D_get_grid.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    D_get_grid.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 48
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_dst'):
        continue
    D_set_dst = _lib.D_set_dst
    D_set_dst.argtypes = [c_double, c_double, c_double, c_double]
    D_set_dst.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 49
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_dst'):
        continue
    D_get_dst = _lib.D_get_dst
    D_get_dst.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    D_get_dst.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 51
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_u'):
        continue
    D_get_u = _lib.D_get_u
    D_get_u.argtypes = [(c_double * 2) * 2]
    D_get_u.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 52
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_a'):
        continue
    D_get_a = _lib.D_get_a
    D_get_a.argtypes = [(c_int * 2) * 2]
    D_get_a.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 53
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_d'):
        continue
    D_get_d = _lib.D_get_d
    D_get_d.argtypes = [(c_double * 2) * 2]
    D_get_d.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 55
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_d_to_a_row'):
        continue
    D_d_to_a_row = _lib.D_d_to_a_row
    D_d_to_a_row.argtypes = [c_double]
    D_d_to_a_row.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 56
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_d_to_a_col'):
        continue
    D_d_to_a_col = _lib.D_d_to_a_col
    D_d_to_a_col.argtypes = [c_double]
    D_d_to_a_col.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 57
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_d_to_u_row'):
        continue
    D_d_to_u_row = _lib.D_d_to_u_row
    D_d_to_u_row.argtypes = [c_double]
    D_d_to_u_row.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 58
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_d_to_u_col'):
        continue
    D_d_to_u_col = _lib.D_d_to_u_col
    D_d_to_u_col.argtypes = [c_double]
    D_d_to_u_col.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 59
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_a_to_u_row'):
        continue
    D_a_to_u_row = _lib.D_a_to_u_row
    D_a_to_u_row.argtypes = [c_double]
    D_a_to_u_row.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 60
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_a_to_u_col'):
        continue
    D_a_to_u_col = _lib.D_a_to_u_col
    D_a_to_u_col.argtypes = [c_double]
    D_a_to_u_col.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 61
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_a_to_d_row'):
        continue
    D_a_to_d_row = _lib.D_a_to_d_row
    D_a_to_d_row.argtypes = [c_double]
    D_a_to_d_row.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 62
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_a_to_d_col'):
        continue
    D_a_to_d_col = _lib.D_a_to_d_col
    D_a_to_d_col.argtypes = [c_double]
    D_a_to_d_col.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 63
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_u_to_d_row'):
        continue
    D_u_to_d_row = _lib.D_u_to_d_row
    D_u_to_d_row.argtypes = [c_double]
    D_u_to_d_row.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 64
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_u_to_d_col'):
        continue
    D_u_to_d_col = _lib.D_u_to_d_col
    D_u_to_d_col.argtypes = [c_double]
    D_u_to_d_col.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 65
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_u_to_a_row'):
        continue
    D_u_to_a_row = _lib.D_u_to_a_row
    D_u_to_a_row.argtypes = [c_double]
    D_u_to_a_row.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 66
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_u_to_a_col'):
        continue
    D_u_to_a_col = _lib.D_u_to_a_col
    D_u_to_a_col.argtypes = [c_double]
    D_u_to_a_col.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 70
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_clip'):
        continue
    D_set_clip = _lib.D_set_clip
    D_set_clip.argtypes = [c_double, c_double, c_double, c_double]
    D_set_clip.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 71
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_clip_to_map'):
        continue
    D_clip_to_map = _lib.D_clip_to_map
    D_clip_to_map.argtypes = []
    D_clip_to_map.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 72
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_clip_mode'):
        continue
    D_set_clip_mode = _lib.D_set_clip_mode
    D_set_clip_mode.argtypes = [c_int]
    D_set_clip_mode.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 73
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_reduction'):
        continue
    D_set_reduction = _lib.D_set_reduction
    D_set_reduction.argtypes = [c_double]
    D_set_reduction.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 75
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_line_width'):
        continue
    D_line_width = _lib.D_line_width
    D_line_width.argtypes = [c_double]
    D_line_width.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 76
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_text_box'):
        continue
    D_get_text_box = _lib.D_get_text_box
    D_get_text_box.argtypes = [String, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    D_get_text_box.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 78
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_pos_abs'):
        continue
    D_pos_abs = _lib.D_pos_abs
    D_pos_abs.argtypes = [c_double, c_double]
    D_pos_abs.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 79
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_pos_rel'):
        continue
    D_pos_rel = _lib.D_pos_rel
    D_pos_rel.argtypes = [c_double, c_double]
    D_pos_rel.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 80
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_move_abs'):
        continue
    D_move_abs = _lib.D_move_abs
    D_move_abs.argtypes = [c_double, c_double]
    D_move_abs.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 81
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_move_rel'):
        continue
    D_move_rel = _lib.D_move_rel
    D_move_rel.argtypes = [c_double, c_double]
    D_move_rel.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 82
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_cont_abs'):
        continue
    D_cont_abs = _lib.D_cont_abs
    D_cont_abs.argtypes = [c_double, c_double]
    D_cont_abs.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 83
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_cont_rel'):
        continue
    D_cont_rel = _lib.D_cont_rel
    D_cont_rel.argtypes = [c_double, c_double]
    D_cont_rel.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 84
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_line_abs'):
        continue
    D_line_abs = _lib.D_line_abs
    D_line_abs.argtypes = [c_double, c_double, c_double, c_double]
    D_line_abs.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 85
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_line_rel'):
        continue
    D_line_rel = _lib.D_line_rel
    D_line_rel.argtypes = [c_double, c_double, c_double, c_double]
    D_line_rel.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 86
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_polydots_abs'):
        continue
    D_polydots_abs = _lib.D_polydots_abs
    D_polydots_abs.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    D_polydots_abs.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 87
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_polydots_rel'):
        continue
    D_polydots_rel = _lib.D_polydots_rel
    D_polydots_rel.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    D_polydots_rel.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 88
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_polyline_abs'):
        continue
    D_polyline_abs = _lib.D_polyline_abs
    D_polyline_abs.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    D_polyline_abs.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 89
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_polyline_rel'):
        continue
    D_polyline_rel = _lib.D_polyline_rel
    D_polyline_rel.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    D_polyline_rel.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 90
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_polygon_abs'):
        continue
    D_polygon_abs = _lib.D_polygon_abs
    D_polygon_abs.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    D_polygon_abs.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 91
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_polygon_rel'):
        continue
    D_polygon_rel = _lib.D_polygon_rel
    D_polygon_rel.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
    D_polygon_rel.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 92
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_box_abs'):
        continue
    D_box_abs = _lib.D_box_abs
    D_box_abs.argtypes = [c_double, c_double, c_double, c_double]
    D_box_abs.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 93
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_box_rel'):
        continue
    D_box_rel = _lib.D_box_rel
    D_box_rel.argtypes = [c_double, c_double]
    D_box_rel.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 95
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_begin'):
        continue
    D_begin = _lib.D_begin
    D_begin.argtypes = []
    D_begin.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 96
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_end'):
        continue
    D_end = _lib.D_end
    D_end.argtypes = []
    D_end.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 97
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_close'):
        continue
    D_close = _lib.D_close
    D_close.argtypes = []
    D_close.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 98
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_stroke'):
        continue
    D_stroke = _lib.D_stroke
    D_stroke.argtypes = []
    D_stroke.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 99
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_fill'):
        continue
    D_fill = _lib.D_fill
    D_fill.argtypes = []
    D_fill.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 100
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_dots'):
        continue
    D_dots = _lib.D_dots
    D_dots.argtypes = []
    D_dots.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 103
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_plot_icon'):
        continue
    D_plot_icon = _lib.D_plot_icon
    D_plot_icon.argtypes = [c_double, c_double, c_int, c_double, c_double]
    D_plot_icon.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 106
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_draw_raster'):
        continue
    D_draw_raster = _lib.D_draw_raster
    D_draw_raster.argtypes = [c_int, POINTER(None), POINTER(struct_Colors), RASTER_MAP_TYPE]
    D_draw_raster.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 107
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_draw_d_raster'):
        continue
    D_draw_d_raster = _lib.D_draw_d_raster
    D_draw_d_raster.argtypes = [c_int, POINTER(DCELL), POINTER(struct_Colors)]
    D_draw_d_raster.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 108
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_draw_f_raster'):
        continue
    D_draw_f_raster = _lib.D_draw_f_raster
    D_draw_f_raster.argtypes = [c_int, POINTER(FCELL), POINTER(struct_Colors)]
    D_draw_f_raster.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 109
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_draw_c_raster'):
        continue
    D_draw_c_raster = _lib.D_draw_c_raster
    D_draw_c_raster.argtypes = [c_int, POINTER(CELL), POINTER(struct_Colors)]
    D_draw_c_raster.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 110
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_raster_draw_begin'):
        continue
    D_raster_draw_begin = _lib.D_raster_draw_begin
    D_raster_draw_begin.argtypes = []
    D_raster_draw_begin.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 111
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_draw_raster_RGB'):
        continue
    D_draw_raster_RGB = _lib.D_draw_raster_RGB
    D_draw_raster_RGB.argtypes = [c_int, POINTER(None), POINTER(None), POINTER(None), POINTER(struct_Colors), POINTER(struct_Colors), POINTER(struct_Colors), RASTER_MAP_TYPE, RASTER_MAP_TYPE, RASTER_MAP_TYPE]
    D_draw_raster_RGB.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 114
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_raster_draw_end'):
        continue
    D_raster_draw_end = _lib.D_raster_draw_end
    D_raster_draw_end.argtypes = []
    D_raster_draw_end.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 117
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_overlay_mode'):
        continue
    D_set_overlay_mode = _lib.D_set_overlay_mode
    D_set_overlay_mode.argtypes = [c_int]
    D_set_overlay_mode.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 118
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_color'):
        continue
    D_color = _lib.D_color
    D_color.argtypes = [CELL, POINTER(struct_Colors)]
    D_color.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 119
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_c_color'):
        continue
    D_c_color = _lib.D_c_color
    D_c_color.argtypes = [CELL, POINTER(struct_Colors)]
    D_c_color.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 120
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_d_color'):
        continue
    D_d_color = _lib.D_d_color
    D_d_color.argtypes = [DCELL, POINTER(struct_Colors)]
    D_d_color.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 121
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_f_color'):
        continue
    D_f_color = _lib.D_f_color
    D_f_color.argtypes = [FCELL, POINTER(struct_Colors)]
    D_f_color.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 122
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_color_of_type'):
        continue
    D_color_of_type = _lib.D_color_of_type
    D_color_of_type.argtypes = [POINTER(None), POINTER(struct_Colors), RASTER_MAP_TYPE]
    D_color_of_type.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 125
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_setup'):
        continue
    D_setup = _lib.D_setup
    D_setup.argtypes = [c_int]
    D_setup.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 126
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_setup_unity'):
        continue
    D_setup_unity = _lib.D_setup_unity
    D_setup_unity.argtypes = [c_int]
    D_setup_unity.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 127
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_setup2'):
        continue
    D_setup2 = _lib.D_setup2
    D_setup2.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double]
    D_setup2.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 130
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_symbol'):
        continue
    D_symbol = _lib.D_symbol
    D_symbol.argtypes = [POINTER(SYMBOL), c_double, c_double, POINTER(RGBA_Color), POINTER(RGBA_Color)]
    D_symbol.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 132
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_symbol2'):
        continue
    D_symbol2 = _lib.D_symbol2
    D_symbol2.argtypes = [POINTER(SYMBOL), c_double, c_double, POINTER(RGBA_Color), POINTER(RGBA_Color)]
    D_symbol2.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 136
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_translate_color'):
        continue
    D_translate_color = _lib.D_translate_color
    D_translate_color.argtypes = [String]
    D_translate_color.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 137
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_parse_color'):
        continue
    D_parse_color = _lib.D_parse_color
    D_parse_color.argtypes = [String, c_int]
    D_parse_color.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 138
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_use_color'):
        continue
    D_use_color = _lib.D_use_color
    D_use_color.argtypes = [c_int]
    D_use_color.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 139
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_color_number_to_RGB'):
        continue
    D_color_number_to_RGB = _lib.D_color_number_to_RGB
    D_color_number_to_RGB.argtypes = [c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    D_color_number_to_RGB.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 140
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_RGB_color'):
        continue
    D_RGB_color = _lib.D_RGB_color
    D_RGB_color.argtypes = [c_int, c_int, c_int]
    D_RGB_color.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 143
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_erase'):
        continue
    D_erase = _lib.D_erase
    D_erase.argtypes = [String]
    D_erase.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 147
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_open_driver'):
        continue
    D_open_driver = _lib.D_open_driver
    D_open_driver.argtypes = []
    D_open_driver.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 148
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_close_driver'):
        continue
    D_close_driver = _lib.D_close_driver
    D_close_driver.argtypes = []
    D_close_driver.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 149
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_save_command'):
        continue
    D_save_command = _lib.D_save_command
    D_save_command.argtypes = [String]
    D_save_command.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 151
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D__erase'):
        continue
    D__erase = _lib.D__erase
    D__erase.argtypes = []
    D__erase.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 153
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_text_size'):
        continue
    D_text_size = _lib.D_text_size
    D_text_size.argtypes = [c_double, c_double]
    D_text_size.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 154
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_text_rotation'):
        continue
    D_text_rotation = _lib.D_text_rotation
    D_text_rotation.argtypes = [c_double]
    D_text_rotation.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 155
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_text'):
        continue
    D_text = _lib.D_text
    D_text.argtypes = [String]
    D_text.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 157
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_font'):
        continue
    D_font = _lib.D_font
    D_font.argtypes = [String]
    D_font.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 158
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_encoding'):
        continue
    D_encoding = _lib.D_encoding
    D_encoding.argtypes = [String]
    D_encoding.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 159
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_font_list'):
        continue
    D_font_list = _lib.D_font_list
    D_font_list.argtypes = [POINTER(POINTER(POINTER(c_char))), POINTER(c_int)]
    D_font_list.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 160
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_font_info'):
        continue
    D_font_info = _lib.D_font_info
    D_font_info.argtypes = [POINTER(POINTER(POINTER(c_char))), POINTER(c_int)]
    D_font_info.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 162
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_clip_window'):
        continue
    D_get_clip_window = _lib.D_get_clip_window
    D_get_clip_window.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    D_get_clip_window.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 163
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_clip_window'):
        continue
    D_set_clip_window = _lib.D_set_clip_window
    D_set_clip_window.argtypes = [c_double, c_double, c_double, c_double]
    D_set_clip_window.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 164
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_frame'):
        continue
    D_get_frame = _lib.D_get_frame
    D_get_frame.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    D_get_frame.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 165
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_screen'):
        continue
    D_get_screen = _lib.D_get_screen
    D_get_screen.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    D_get_screen.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 166
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_clip_window_to_map_window'):
        continue
    D_set_clip_window_to_map_window = _lib.D_set_clip_window_to_map_window
    D_set_clip_window_to_map_window.argtypes = []
    D_set_clip_window_to_map_window.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 167
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_set_clip_window_to_screen_window'):
        continue
    D_set_clip_window_to_screen_window = _lib.D_set_clip_window_to_screen_window
    D_set_clip_window_to_screen_window.argtypes = []
    D_set_clip_window_to_screen_window.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/display.h: 169
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'D_get_file'):
        continue
    D_get_file = _lib.D_get_file
    D_get_file.argtypes = []
    D_get_file.restype = c_char_p
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 16
try:
    RGBA_COLOR_OPAQUE = 255
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 17
try:
    RGBA_COLOR_TRANSPARENT = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 18
try:
    RGBA_COLOR_NONE = 0
except:
    pass

color_rgba = struct_color_rgba # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\display.h: 8

# No inserted files

