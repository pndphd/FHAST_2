'''Wrapper for gprojects.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_gproj.7.8 -IC:/OSGeo4W64/include C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gprojects.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h -o OBJ.x86_64-w64-mingw32/proj.py

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

_libs["grass_gproj.7.8"] = load_library("grass_gproj.7.8")

# 1 libraries
# End libraries

# No modules

# C:/OSGeo4W64/include/proj.h: 188
class struct_PJconsts(Structure):
    pass

PJ = struct_PJconsts # C:/OSGeo4W64/include/proj.h: 189

OGRSpatialReferenceH = POINTER(None) # C:/OSGeo4W64/include/ogr_srs_api.h: 459

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 43
class struct_pj_info(Structure):
    pass

struct_pj_info.__slots__ = [
    'pj',
    'meters',
    'zone',
    'proj',
    '_def',
    'srid',
]
struct_pj_info._fields_ = [
    ('pj', POINTER(PJ)),
    ('meters', c_double),
    ('zone', c_int),
    ('proj', c_char * 100),
    ('_def', String),
    ('srid', String),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 57
class struct_gpj_datum(Structure):
    pass

struct_gpj_datum.__slots__ = [
    'name',
    'longname',
    'ellps',
    'dx',
    'dy',
    'dz',
]
struct_gpj_datum._fields_ = [
    ('name', String),
    ('longname', String),
    ('ellps', String),
    ('dx', c_double),
    ('dy', c_double),
    ('dz', c_double),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 63
class struct_gpj_datum_transform_list(Structure):
    pass

struct_gpj_datum_transform_list.__slots__ = [
    'count',
    'params',
    'where_used',
    'comment',
    'next',
]
struct_gpj_datum_transform_list._fields_ = [
    ('count', c_int),
    ('params', String),
    ('where_used', String),
    ('comment', String),
    ('next', POINTER(struct_gpj_datum_transform_list)),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 79
class struct_gpj_ellps(Structure):
    pass

struct_gpj_ellps.__slots__ = [
    'name',
    'longname',
    'a',
    'es',
    'rf',
]
struct_gpj_ellps._fields_ = [
    ('name', String),
    ('longname', String),
    ('a', c_double),
    ('es', c_double),
    ('rf', c_double),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 5
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_init_transform'):
    GPJ_init_transform = _libs['grass_gproj.7.8'].GPJ_init_transform
    GPJ_init_transform.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info), POINTER(struct_pj_info)]
    GPJ_init_transform.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 7
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_transform'):
    GPJ_transform = _libs['grass_gproj.7.8'].GPJ_transform
    GPJ_transform.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info), POINTER(struct_pj_info), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    GPJ_transform.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 9
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_transform_array'):
    GPJ_transform_array = _libs['grass_gproj.7.8'].GPJ_transform_array
    GPJ_transform_array.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info), POINTER(struct_pj_info), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    GPJ_transform_array.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 14
if hasattr(_libs['grass_gproj.7.8'], 'pj_do_proj'):
    pj_do_proj = _libs['grass_gproj.7.8'].pj_do_proj
    pj_do_proj.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(struct_pj_info), POINTER(struct_pj_info)]
    pj_do_proj.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 15
if hasattr(_libs['grass_gproj.7.8'], 'pj_do_transform'):
    pj_do_transform = _libs['grass_gproj.7.8'].pj_do_transform
    pj_do_transform.argtypes = [c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(struct_pj_info), POINTER(struct_pj_info)]
    pj_do_transform.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 20
class struct_Key_Value(Structure):
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 20
if hasattr(_libs['grass_gproj.7.8'], 'pj_get_kv'):
    pj_get_kv = _libs['grass_gproj.7.8'].pj_get_kv
    pj_get_kv.argtypes = [POINTER(struct_pj_info), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]
    pj_get_kv.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 21
if hasattr(_libs['grass_gproj.7.8'], 'pj_get_string'):
    pj_get_string = _libs['grass_gproj.7.8'].pj_get_string
    pj_get_string.argtypes = [POINTER(struct_pj_info), String]
    pj_get_string.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 25
if hasattr(_libs['grass_gproj.7.8'], 'set_proj_share'):
    set_proj_share = _libs['grass_gproj.7.8'].set_proj_share
    set_proj_share.argtypes = [String]
    set_proj_share.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 26
if hasattr(_libs['grass_gproj.7.8'], 'pj_print_proj_params'):
    pj_print_proj_params = _libs['grass_gproj.7.8'].pj_print_proj_params
    pj_print_proj_params.argtypes = [POINTER(struct_pj_info), POINTER(struct_pj_info)]
    pj_print_proj_params.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 29
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_grass_to_wkt'):
    GPJ_grass_to_wkt = _libs['grass_gproj.7.8'].GPJ_grass_to_wkt
    GPJ_grass_to_wkt.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), c_int, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        GPJ_grass_to_wkt.restype = ReturnString
    else:
        GPJ_grass_to_wkt.restype = String
        GPJ_grass_to_wkt.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 30
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_grass_to_wkt2'):
    GPJ_grass_to_wkt2 = _libs['grass_gproj.7.8'].GPJ_grass_to_wkt2
    GPJ_grass_to_wkt2.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value), c_int, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        GPJ_grass_to_wkt2.restype = ReturnString
    else:
        GPJ_grass_to_wkt2.restype = String
        GPJ_grass_to_wkt2.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 32
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_grass_to_osr'):
    GPJ_grass_to_osr = _libs['grass_gproj.7.8'].GPJ_grass_to_osr
    GPJ_grass_to_osr.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value)]
    GPJ_grass_to_osr.restype = OGRSpatialReferenceH

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 33
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_grass_to_osr2'):
    GPJ_grass_to_osr2 = _libs['grass_gproj.7.8'].GPJ_grass_to_osr2
    GPJ_grass_to_osr2.argtypes = [POINTER(struct_Key_Value), POINTER(struct_Key_Value), POINTER(struct_Key_Value)]
    GPJ_grass_to_osr2.restype = OGRSpatialReferenceH

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 34
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_set_csv_loc'):
    GPJ_set_csv_loc = _libs['grass_gproj.7.8'].GPJ_set_csv_loc
    GPJ_set_csv_loc.argtypes = [String]
    GPJ_set_csv_loc.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 35
class struct_Cell_head(Structure):
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 35
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_osr_to_grass'):
    GPJ_osr_to_grass = _libs['grass_gproj.7.8'].GPJ_osr_to_grass
    GPJ_osr_to_grass.argtypes = [POINTER(struct_Cell_head), POINTER(POINTER(struct_Key_Value)), POINTER(POINTER(struct_Key_Value)), OGRSpatialReferenceH, c_int]
    GPJ_osr_to_grass.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 38
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_wkt_to_grass'):
    GPJ_wkt_to_grass = _libs['grass_gproj.7.8'].GPJ_wkt_to_grass
    GPJ_wkt_to_grass.argtypes = [POINTER(struct_Cell_head), POINTER(POINTER(struct_Key_Value)), POINTER(POINTER(struct_Key_Value)), String, c_int]
    GPJ_wkt_to_grass.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 42
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_get_datum_by_name'):
    GPJ_get_datum_by_name = _libs['grass_gproj.7.8'].GPJ_get_datum_by_name
    GPJ_get_datum_by_name.argtypes = [String, POINTER(struct_gpj_datum)]
    GPJ_get_datum_by_name.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 43
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_get_default_datum_params_by_name'):
    GPJ_get_default_datum_params_by_name = _libs['grass_gproj.7.8'].GPJ_get_default_datum_params_by_name
    GPJ_get_default_datum_params_by_name.argtypes = [String, POINTER(POINTER(c_char))]
    GPJ_get_default_datum_params_by_name.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 44
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_get_datum_params'):
    GPJ_get_datum_params = _libs['grass_gproj.7.8'].GPJ_get_datum_params
    GPJ_get_datum_params.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    GPJ_get_datum_params.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 45
if hasattr(_libs['grass_gproj.7.8'], 'GPJ__get_datum_params'):
    GPJ__get_datum_params = _libs['grass_gproj.7.8'].GPJ__get_datum_params
    GPJ__get_datum_params.argtypes = [POINTER(struct_Key_Value), POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    GPJ__get_datum_params.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 46
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_free_datum'):
    GPJ_free_datum = _libs['grass_gproj.7.8'].GPJ_free_datum
    GPJ_free_datum.argtypes = [POINTER(struct_gpj_datum)]
    GPJ_free_datum.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 47
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_get_datum_transform_by_name'):
    GPJ_get_datum_transform_by_name = _libs['grass_gproj.7.8'].GPJ_get_datum_transform_by_name
    GPJ_get_datum_transform_by_name.argtypes = [String]
    GPJ_get_datum_transform_by_name.restype = POINTER(struct_gpj_datum_transform_list)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 48
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_free_datum_transform'):
    GPJ_free_datum_transform = _libs['grass_gproj.7.8'].GPJ_free_datum_transform
    GPJ_free_datum_transform.argtypes = [POINTER(struct_gpj_datum_transform_list)]
    GPJ_free_datum_transform.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 51
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_get_ellipsoid_by_name'):
    GPJ_get_ellipsoid_by_name = _libs['grass_gproj.7.8'].GPJ_get_ellipsoid_by_name
    GPJ_get_ellipsoid_by_name.argtypes = [String, POINTER(struct_gpj_ellps)]
    GPJ_get_ellipsoid_by_name.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 52
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_get_ellipsoid_params'):
    GPJ_get_ellipsoid_params = _libs['grass_gproj.7.8'].GPJ_get_ellipsoid_params
    GPJ_get_ellipsoid_params.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    GPJ_get_ellipsoid_params.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 53
if hasattr(_libs['grass_gproj.7.8'], 'GPJ__get_ellipsoid_params'):
    GPJ__get_ellipsoid_params = _libs['grass_gproj.7.8'].GPJ__get_ellipsoid_params
    GPJ__get_ellipsoid_params.argtypes = [POINTER(struct_Key_Value), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    GPJ__get_ellipsoid_params.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 55
if hasattr(_libs['grass_gproj.7.8'], 'GPJ_free_ellps'):
    GPJ_free_ellps = _libs['grass_gproj.7.8'].GPJ_free_ellps
    GPJ_free_ellps.argtypes = [POINTER(struct_gpj_ellps)]
    GPJ_free_ellps.restype = None

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 24
try:
    RAD_TO_DEG = 57.29577951308232
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 36
try:
    ELLIPSOIDTABLE = '/etc/proj/ellipse.table'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 37
try:
    DATUMTABLE = '/etc/proj/datum.table'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 38
try:
    DATUMTRANSFORMTABLE = '/etc/proj/datumtransform.table'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 40
try:
    GRIDDIR = '/etc/proj/nad'
except:
    pass

pj_info = struct_pj_info # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 43

gpj_datum = struct_gpj_datum # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 57

gpj_datum_transform_list = struct_gpj_datum_transform_list # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 63

gpj_ellps = struct_gpj_ellps # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\gprojects.h: 79

Key_Value = struct_Key_Value # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 20

Cell_head = struct_Cell_head # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/gprojects.h: 35

# No inserted files

