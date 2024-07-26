'''Wrapper for imagery.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_imagery.7.8 C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/imagery.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h -o OBJ.x86_64-w64-mingw32/imagery.py

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

_libs["grass_imagery.7.8"] = load_library("grass_imagery.7.8")

# 1 libraries
# End libraries

# No modules

# C:/msys64/mingw64/x86_64-w64-mingw32/include/stdio.h: 24
class struct__iobuf(Structure):
    pass

struct__iobuf.__slots__ = [
    '_ptr',
    '_cnt',
    '_base',
    '_flag',
    '_file',
    '_charbuf',
    '_bufsiz',
    '_tmpfname',
]
struct__iobuf._fields_ = [
    ('_ptr', String),
    ('_cnt', c_int),
    ('_base', String),
    ('_flag', c_int),
    ('_file', c_int),
    ('_charbuf', c_int),
    ('_bufsiz', c_int),
    ('_tmpfname', String),
]

FILE = struct__iobuf # C:/msys64/mingw64/x86_64-w64-mingw32/include/stdio.h: 34

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

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 10
class struct_Ref_Color(Structure):
    pass

struct_Ref_Color.__slots__ = [
    'table',
    'index',
    'buf',
    'fd',
    'min',
    'max',
    'n',
]
struct_Ref_Color._fields_ = [
    ('table', POINTER(c_ubyte)),
    ('index', POINTER(c_ubyte)),
    ('buf', POINTER(c_ubyte)),
    ('fd', c_int),
    ('min', CELL),
    ('max', CELL),
    ('n', c_int),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 20
class struct_Ref_Files(Structure):
    pass

struct_Ref_Files.__slots__ = [
    'name',
    'mapset',
]
struct_Ref_Files._fields_ = [
    ('name', c_char * 256),
    ('mapset', c_char * 256),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 26
class struct_Ref(Structure):
    pass

struct_Ref.__slots__ = [
    'nfiles',
    'file',
    'red',
    'grn',
    'blu',
]
struct_Ref._fields_ = [
    ('nfiles', c_int),
    ('file', POINTER(struct_Ref_Files)),
    ('red', struct_Ref_Color),
    ('grn', struct_Ref_Color),
    ('blu', struct_Ref_Color),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 33
class struct_Tape_Info(Structure):
    pass

struct_Tape_Info.__slots__ = [
    'title',
    'id',
    'desc',
]
struct_Tape_Info._fields_ = [
    ('title', c_char * 75),
    ('id', (c_char * 75) * 2),
    ('desc', (c_char * 75) * 5),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 40
class struct_Control_Points(Structure):
    pass

struct_Control_Points.__slots__ = [
    'count',
    'e1',
    'n1',
    'z1',
    'e2',
    'n2',
    'z2',
    'status',
]
struct_Control_Points._fields_ = [
    ('count', c_int),
    ('e1', POINTER(c_double)),
    ('n1', POINTER(c_double)),
    ('z1', POINTER(c_double)),
    ('e2', POINTER(c_double)),
    ('n2', POINTER(c_double)),
    ('z2', POINTER(c_double)),
    ('status', POINTER(c_int)),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 52
class struct_One_Sig(Structure):
    pass

struct_One_Sig.__slots__ = [
    'desc',
    'npoints',
    'mean',
    'var',
    'status',
    'r',
    'g',
    'b',
    'have_color',
]
struct_One_Sig._fields_ = [
    ('desc', c_char * 100),
    ('npoints', c_int),
    ('mean', POINTER(c_double)),
    ('var', POINTER(POINTER(c_double))),
    ('status', c_int),
    ('r', c_float),
    ('g', c_float),
    ('b', c_float),
    ('have_color', c_int),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 63
class struct_Signature(Structure):
    pass

struct_Signature.__slots__ = [
    'nbands',
    'nsigs',
    'title',
    'sig',
]
struct_Signature._fields_ = [
    ('nbands', c_int),
    ('nsigs', c_int),
    ('title', c_char * 100),
    ('sig', POINTER(struct_One_Sig)),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 71
class struct_SubSig(Structure):
    pass

struct_SubSig.__slots__ = [
    'N',
    'pi',
    'means',
    'R',
    'Rinv',
    'cnst',
    'used',
]
struct_SubSig._fields_ = [
    ('N', c_double),
    ('pi', c_double),
    ('means', POINTER(c_double)),
    ('R', POINTER(POINTER(c_double))),
    ('Rinv', POINTER(POINTER(c_double))),
    ('cnst', c_double),
    ('used', c_int),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 82
class struct_ClassData(Structure):
    pass

struct_ClassData.__slots__ = [
    'npixels',
    'count',
    'x',
    'p',
]
struct_ClassData._fields_ = [
    ('npixels', c_int),
    ('count', c_int),
    ('x', POINTER(POINTER(c_double))),
    ('p', POINTER(POINTER(c_double))),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 90
class struct_ClassSig(Structure):
    pass

struct_ClassSig.__slots__ = [
    'classnum',
    'title',
    'used',
    'type',
    'nsubclasses',
    'SubSig',
    'ClassData',
]
struct_ClassSig._fields_ = [
    ('classnum', c_long),
    ('title', String),
    ('used', c_int),
    ('type', c_int),
    ('nsubclasses', c_int),
    ('SubSig', POINTER(struct_SubSig)),
    ('ClassData', struct_ClassData),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 101
class struct_SigSet(Structure):
    pass

struct_SigSet.__slots__ = [
    'nbands',
    'nclasses',
    'title',
    'ClassSig',
]
struct_SigSet._fields_ = [
    ('nbands', c_int),
    ('nclasses', c_int),
    ('title', String),
    ('ClassSig', POINTER(struct_ClassSig)),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 138
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'cat',
    'name',
    'color',
    'nbands',
    'ncells',
    'band_min',
    'band_max',
    'band_sum',
    'band_mean',
    'band_stddev',
    'band_product',
    'band_histo',
    'band_range_min',
    'band_range_max',
    'nstd',
]
struct_anon_8._fields_ = [
    ('cat', c_int),
    ('name', String),
    ('color', String),
    ('nbands', c_int),
    ('ncells', c_int),
    ('band_min', POINTER(c_int)),
    ('band_max', POINTER(c_int)),
    ('band_sum', POINTER(c_float)),
    ('band_mean', POINTER(c_float)),
    ('band_stddev', POINTER(c_float)),
    ('band_product', POINTER(POINTER(c_float))),
    ('band_histo', POINTER(POINTER(c_int))),
    ('band_range_min', POINTER(c_int)),
    ('band_range_max', POINTER(c_int)),
    ('nstd', c_float),
]

IClass_statistics = struct_anon_8 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 138

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 171
class struct_scScatts(Structure):
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 149
class struct_scCats(Structure):
    pass

struct_scCats.__slots__ = [
    'type',
    'n_cats',
    'n_bands',
    'n_scatts',
    'n_a_cats',
    'cats_ids',
    'cats_idxs',
    'cats_arr',
]
struct_scCats._fields_ = [
    ('type', c_int),
    ('n_cats', c_int),
    ('n_bands', c_int),
    ('n_scatts', c_int),
    ('n_a_cats', c_int),
    ('cats_ids', POINTER(c_int)),
    ('cats_idxs', POINTER(c_int)),
    ('cats_arr', POINTER(POINTER(struct_scScatts))),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 186
class struct_scdScattData(Structure):
    pass

struct_scScatts.__slots__ = [
    'n_a_scatts',
    'scatts_bands',
    'scatt_idxs',
    'scatts_arr',
]
struct_scScatts._fields_ = [
    ('n_a_scatts', c_int),
    ('scatts_bands', POINTER(c_int)),
    ('scatt_idxs', POINTER(c_int)),
    ('scatts_arr', POINTER(POINTER(struct_scdScattData))),
]

struct_scdScattData.__slots__ = [
    'n_vals',
    'b_conds_arr',
    'scatt_vals_arr',
]
struct_scdScattData._fields_ = [
    ('n_vals', c_int),
    ('b_conds_arr', POINTER(c_ubyte)),
    ('scatt_vals_arr', POINTER(c_uint)),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 5
if hasattr(_libs['grass_imagery.7.8'], 'I_malloc'):
    I_malloc = _libs['grass_imagery.7.8'].I_malloc
    I_malloc.argtypes = [c_size_t]
    I_malloc.restype = POINTER(c_ubyte)
    I_malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 6
if hasattr(_libs['grass_imagery.7.8'], 'I_realloc'):
    I_realloc = _libs['grass_imagery.7.8'].I_realloc
    I_realloc.argtypes = [POINTER(None), c_size_t]
    I_realloc.restype = POINTER(c_ubyte)
    I_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 7
if hasattr(_libs['grass_imagery.7.8'], 'I_free'):
    I_free = _libs['grass_imagery.7.8'].I_free
    I_free.argtypes = [POINTER(None)]
    I_free.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 8
if hasattr(_libs['grass_imagery.7.8'], 'I_alloc_double2'):
    I_alloc_double2 = _libs['grass_imagery.7.8'].I_alloc_double2
    I_alloc_double2.argtypes = [c_int, c_int]
    I_alloc_double2.restype = POINTER(POINTER(c_double))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 9
if hasattr(_libs['grass_imagery.7.8'], 'I_alloc_int'):
    I_alloc_int = _libs['grass_imagery.7.8'].I_alloc_int
    I_alloc_int.argtypes = [c_int]
    I_alloc_int.restype = POINTER(c_int)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 10
if hasattr(_libs['grass_imagery.7.8'], 'I_alloc_int2'):
    I_alloc_int2 = _libs['grass_imagery.7.8'].I_alloc_int2
    I_alloc_int2.argtypes = [c_int, c_int]
    I_alloc_int2.restype = POINTER(POINTER(c_int))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 11
if hasattr(_libs['grass_imagery.7.8'], 'I_free_int2'):
    I_free_int2 = _libs['grass_imagery.7.8'].I_free_int2
    I_free_int2.argtypes = [POINTER(POINTER(c_int))]
    I_free_int2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 12
if hasattr(_libs['grass_imagery.7.8'], 'I_free_double2'):
    I_free_double2 = _libs['grass_imagery.7.8'].I_free_double2
    I_free_double2.argtypes = [POINTER(POINTER(c_double))]
    I_free_double2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 13
if hasattr(_libs['grass_imagery.7.8'], 'I_alloc_double3'):
    I_alloc_double3 = _libs['grass_imagery.7.8'].I_alloc_double3
    I_alloc_double3.argtypes = [c_int, c_int, c_int]
    I_alloc_double3.restype = POINTER(POINTER(POINTER(c_double)))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 14
if hasattr(_libs['grass_imagery.7.8'], 'I_free_double3'):
    I_free_double3 = _libs['grass_imagery.7.8'].I_free_double3
    I_free_double3.argtypes = [POINTER(POINTER(POINTER(c_double)))]
    I_free_double3.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 17
if hasattr(_libs['grass_imagery.7.8'], 'I_get_to_eol'):
    I_get_to_eol = _libs['grass_imagery.7.8'].I_get_to_eol
    I_get_to_eol.argtypes = [String, c_int, POINTER(FILE)]
    I_get_to_eol.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 20
if hasattr(_libs['grass_imagery.7.8'], 'I_find_group'):
    I_find_group = _libs['grass_imagery.7.8'].I_find_group
    I_find_group.argtypes = [String]
    I_find_group.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 21
if hasattr(_libs['grass_imagery.7.8'], 'I_find_group2'):
    I_find_group2 = _libs['grass_imagery.7.8'].I_find_group2
    I_find_group2.argtypes = [String, String]
    I_find_group2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 22
if hasattr(_libs['grass_imagery.7.8'], 'I_find_group_file'):
    I_find_group_file = _libs['grass_imagery.7.8'].I_find_group_file
    I_find_group_file.argtypes = [String, String]
    I_find_group_file.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 23
if hasattr(_libs['grass_imagery.7.8'], 'I_find_group_file2'):
    I_find_group_file2 = _libs['grass_imagery.7.8'].I_find_group_file2
    I_find_group_file2.argtypes = [String, String, String]
    I_find_group_file2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 24
if hasattr(_libs['grass_imagery.7.8'], 'I_find_subgroup'):
    I_find_subgroup = _libs['grass_imagery.7.8'].I_find_subgroup
    I_find_subgroup.argtypes = [String, String]
    I_find_subgroup.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 25
if hasattr(_libs['grass_imagery.7.8'], 'I_find_subgroup2'):
    I_find_subgroup2 = _libs['grass_imagery.7.8'].I_find_subgroup2
    I_find_subgroup2.argtypes = [String, String, String]
    I_find_subgroup2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 26
if hasattr(_libs['grass_imagery.7.8'], 'I_find_subgroup_file'):
    I_find_subgroup_file = _libs['grass_imagery.7.8'].I_find_subgroup_file
    I_find_subgroup_file.argtypes = [String, String, String]
    I_find_subgroup_file.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 27
if hasattr(_libs['grass_imagery.7.8'], 'I_find_subgroup_file2'):
    I_find_subgroup_file2 = _libs['grass_imagery.7.8'].I_find_subgroup_file2
    I_find_subgroup_file2.argtypes = [String, String, String, String]
    I_find_subgroup_file2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 28
if hasattr(_libs['grass_imagery.7.8'], 'I_find_signature_file'):
    I_find_signature_file = _libs['grass_imagery.7.8'].I_find_signature_file
    I_find_signature_file.argtypes = [String, String, String, String]
    I_find_signature_file.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 31
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_group_file_new'):
    I_fopen_group_file_new = _libs['grass_imagery.7.8'].I_fopen_group_file_new
    I_fopen_group_file_new.argtypes = [String, String]
    I_fopen_group_file_new.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 32
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_group_file_append'):
    I_fopen_group_file_append = _libs['grass_imagery.7.8'].I_fopen_group_file_append
    I_fopen_group_file_append.argtypes = [String, String]
    I_fopen_group_file_append.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 33
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_group_file_old'):
    I_fopen_group_file_old = _libs['grass_imagery.7.8'].I_fopen_group_file_old
    I_fopen_group_file_old.argtypes = [String, String]
    I_fopen_group_file_old.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 34
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_group_file_old2'):
    I_fopen_group_file_old2 = _libs['grass_imagery.7.8'].I_fopen_group_file_old2
    I_fopen_group_file_old2.argtypes = [String, String, String]
    I_fopen_group_file_old2.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 35
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_subgroup_file_new'):
    I_fopen_subgroup_file_new = _libs['grass_imagery.7.8'].I_fopen_subgroup_file_new
    I_fopen_subgroup_file_new.argtypes = [String, String, String]
    I_fopen_subgroup_file_new.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 36
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_subgroup_file_append'):
    I_fopen_subgroup_file_append = _libs['grass_imagery.7.8'].I_fopen_subgroup_file_append
    I_fopen_subgroup_file_append.argtypes = [String, String, String]
    I_fopen_subgroup_file_append.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 37
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_subgroup_file_old'):
    I_fopen_subgroup_file_old = _libs['grass_imagery.7.8'].I_fopen_subgroup_file_old
    I_fopen_subgroup_file_old.argtypes = [String, String, String]
    I_fopen_subgroup_file_old.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 38
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_subgroup_file_old2'):
    I_fopen_subgroup_file_old2 = _libs['grass_imagery.7.8'].I_fopen_subgroup_file_old2
    I_fopen_subgroup_file_old2.argtypes = [String, String, String, String]
    I_fopen_subgroup_file_old2.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 41
if hasattr(_libs['grass_imagery.7.8'], 'I_compute_georef_equations'):
    I_compute_georef_equations = _libs['grass_imagery.7.8'].I_compute_georef_equations
    I_compute_georef_equations.argtypes = [POINTER(struct_Control_Points), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    I_compute_georef_equations.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 43
if hasattr(_libs['grass_imagery.7.8'], 'I_georef'):
    I_georef = _libs['grass_imagery.7.8'].I_georef
    I_georef.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    I_georef.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 46
if hasattr(_libs['grass_imagery.7.8'], 'I_compute_georef_equations_tps'):
    I_compute_georef_equations_tps = _libs['grass_imagery.7.8'].I_compute_georef_equations_tps
    I_compute_georef_equations_tps.argtypes = [POINTER(struct_Control_Points), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(POINTER(c_double))]
    I_compute_georef_equations_tps.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 48
if hasattr(_libs['grass_imagery.7.8'], 'I_georef_tps'):
    I_georef_tps = _libs['grass_imagery.7.8'].I_georef_tps
    I_georef_tps.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(struct_Control_Points), c_int]
    I_georef_tps.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 52
if hasattr(_libs['grass_imagery.7.8'], 'I_get_group'):
    I_get_group = _libs['grass_imagery.7.8'].I_get_group
    I_get_group.argtypes = [String]
    I_get_group.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 53
if hasattr(_libs['grass_imagery.7.8'], 'I_put_group'):
    I_put_group = _libs['grass_imagery.7.8'].I_put_group
    I_put_group.argtypes = [String]
    I_put_group.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 54
if hasattr(_libs['grass_imagery.7.8'], 'I_get_subgroup'):
    I_get_subgroup = _libs['grass_imagery.7.8'].I_get_subgroup
    I_get_subgroup.argtypes = [String, String]
    I_get_subgroup.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 55
if hasattr(_libs['grass_imagery.7.8'], 'I_put_subgroup'):
    I_put_subgroup = _libs['grass_imagery.7.8'].I_put_subgroup
    I_put_subgroup.argtypes = [String, String]
    I_put_subgroup.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 56
if hasattr(_libs['grass_imagery.7.8'], 'I_get_group_ref'):
    I_get_group_ref = _libs['grass_imagery.7.8'].I_get_group_ref
    I_get_group_ref.argtypes = [String, POINTER(struct_Ref)]
    I_get_group_ref.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 57
if hasattr(_libs['grass_imagery.7.8'], 'I_get_group_ref2'):
    I_get_group_ref2 = _libs['grass_imagery.7.8'].I_get_group_ref2
    I_get_group_ref2.argtypes = [String, String, POINTER(struct_Ref)]
    I_get_group_ref2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 58
if hasattr(_libs['grass_imagery.7.8'], 'I_get_subgroup_ref'):
    I_get_subgroup_ref = _libs['grass_imagery.7.8'].I_get_subgroup_ref
    I_get_subgroup_ref.argtypes = [String, String, POINTER(struct_Ref)]
    I_get_subgroup_ref.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 59
if hasattr(_libs['grass_imagery.7.8'], 'I_get_subgroup_ref2'):
    I_get_subgroup_ref2 = _libs['grass_imagery.7.8'].I_get_subgroup_ref2
    I_get_subgroup_ref2.argtypes = [String, String, String, POINTER(struct_Ref)]
    I_get_subgroup_ref2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 60
if hasattr(_libs['grass_imagery.7.8'], 'I_init_ref_color_nums'):
    I_init_ref_color_nums = _libs['grass_imagery.7.8'].I_init_ref_color_nums
    I_init_ref_color_nums.argtypes = [POINTER(struct_Ref)]
    I_init_ref_color_nums.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 61
if hasattr(_libs['grass_imagery.7.8'], 'I_put_group_ref'):
    I_put_group_ref = _libs['grass_imagery.7.8'].I_put_group_ref
    I_put_group_ref.argtypes = [String, POINTER(struct_Ref)]
    I_put_group_ref.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 62
if hasattr(_libs['grass_imagery.7.8'], 'I_put_subgroup_ref'):
    I_put_subgroup_ref = _libs['grass_imagery.7.8'].I_put_subgroup_ref
    I_put_subgroup_ref.argtypes = [String, String, POINTER(struct_Ref)]
    I_put_subgroup_ref.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 63
if hasattr(_libs['grass_imagery.7.8'], 'I_add_file_to_group_ref'):
    I_add_file_to_group_ref = _libs['grass_imagery.7.8'].I_add_file_to_group_ref
    I_add_file_to_group_ref.argtypes = [String, String, POINTER(struct_Ref)]
    I_add_file_to_group_ref.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 64
if hasattr(_libs['grass_imagery.7.8'], 'I_transfer_group_ref_file'):
    I_transfer_group_ref_file = _libs['grass_imagery.7.8'].I_transfer_group_ref_file
    I_transfer_group_ref_file.argtypes = [POINTER(struct_Ref), c_int, POINTER(struct_Ref)]
    I_transfer_group_ref_file.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 65
if hasattr(_libs['grass_imagery.7.8'], 'I_init_group_ref'):
    I_init_group_ref = _libs['grass_imagery.7.8'].I_init_group_ref
    I_init_group_ref.argtypes = [POINTER(struct_Ref)]
    I_init_group_ref.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 66
if hasattr(_libs['grass_imagery.7.8'], 'I_free_group_ref'):
    I_free_group_ref = _libs['grass_imagery.7.8'].I_free_group_ref
    I_free_group_ref.argtypes = [POINTER(struct_Ref)]
    I_free_group_ref.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 69
class struct_Map_info(Structure):
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 70
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_analysis'):
    I_iclass_analysis = _libs['grass_imagery.7.8'].I_iclass_analysis
    I_iclass_analysis.argtypes = [POINTER(IClass_statistics), POINTER(struct_Ref), POINTER(struct_Map_info), String, String, String]
    I_iclass_analysis.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 71
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_init_group'):
    I_iclass_init_group = _libs['grass_imagery.7.8'].I_iclass_init_group
    I_iclass_init_group.argtypes = [String, String, POINTER(struct_Ref)]
    I_iclass_init_group.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 72
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_create_raster'):
    I_iclass_create_raster = _libs['grass_imagery.7.8'].I_iclass_create_raster
    I_iclass_create_raster.argtypes = [POINTER(IClass_statistics), POINTER(struct_Ref), String]
    I_iclass_create_raster.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 75
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_nbands'):
    I_iclass_statistics_get_nbands = _libs['grass_imagery.7.8'].I_iclass_statistics_get_nbands
    I_iclass_statistics_get_nbands.argtypes = [POINTER(IClass_statistics), POINTER(c_int)]
    I_iclass_statistics_get_nbands.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 76
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_cat'):
    I_iclass_statistics_get_cat = _libs['grass_imagery.7.8'].I_iclass_statistics_get_cat
    I_iclass_statistics_get_cat.argtypes = [POINTER(IClass_statistics), POINTER(c_int)]
    I_iclass_statistics_get_cat.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 77
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_name'):
    I_iclass_statistics_get_name = _libs['grass_imagery.7.8'].I_iclass_statistics_get_name
    I_iclass_statistics_get_name.argtypes = [POINTER(IClass_statistics), POINTER(POINTER(c_char))]
    I_iclass_statistics_get_name.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 78
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_color'):
    I_iclass_statistics_get_color = _libs['grass_imagery.7.8'].I_iclass_statistics_get_color
    I_iclass_statistics_get_color.argtypes = [POINTER(IClass_statistics), POINTER(POINTER(c_char))]
    I_iclass_statistics_get_color.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 79
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_ncells'):
    I_iclass_statistics_get_ncells = _libs['grass_imagery.7.8'].I_iclass_statistics_get_ncells
    I_iclass_statistics_get_ncells.argtypes = [POINTER(IClass_statistics), POINTER(c_int)]
    I_iclass_statistics_get_ncells.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 80
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_max'):
    I_iclass_statistics_get_max = _libs['grass_imagery.7.8'].I_iclass_statistics_get_max
    I_iclass_statistics_get_max.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_int)]
    I_iclass_statistics_get_max.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 81
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_range_max'):
    I_iclass_statistics_get_range_max = _libs['grass_imagery.7.8'].I_iclass_statistics_get_range_max
    I_iclass_statistics_get_range_max.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_int)]
    I_iclass_statistics_get_range_max.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 82
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_min'):
    I_iclass_statistics_get_min = _libs['grass_imagery.7.8'].I_iclass_statistics_get_min
    I_iclass_statistics_get_min.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_int)]
    I_iclass_statistics_get_min.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 83
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_range_min'):
    I_iclass_statistics_get_range_min = _libs['grass_imagery.7.8'].I_iclass_statistics_get_range_min
    I_iclass_statistics_get_range_min.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_int)]
    I_iclass_statistics_get_range_min.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 84
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_sum'):
    I_iclass_statistics_get_sum = _libs['grass_imagery.7.8'].I_iclass_statistics_get_sum
    I_iclass_statistics_get_sum.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_float)]
    I_iclass_statistics_get_sum.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 85
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_mean'):
    I_iclass_statistics_get_mean = _libs['grass_imagery.7.8'].I_iclass_statistics_get_mean
    I_iclass_statistics_get_mean.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_float)]
    I_iclass_statistics_get_mean.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 86
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_stddev'):
    I_iclass_statistics_get_stddev = _libs['grass_imagery.7.8'].I_iclass_statistics_get_stddev
    I_iclass_statistics_get_stddev.argtypes = [POINTER(IClass_statistics), c_int, POINTER(c_float)]
    I_iclass_statistics_get_stddev.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 87
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_nstd'):
    I_iclass_statistics_get_nstd = _libs['grass_imagery.7.8'].I_iclass_statistics_get_nstd
    I_iclass_statistics_get_nstd.argtypes = [POINTER(IClass_statistics), POINTER(c_float)]
    I_iclass_statistics_get_nstd.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 88
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_set_nstd'):
    I_iclass_statistics_set_nstd = _libs['grass_imagery.7.8'].I_iclass_statistics_set_nstd
    I_iclass_statistics_set_nstd.argtypes = [POINTER(IClass_statistics), c_float]
    I_iclass_statistics_set_nstd.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 89
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_histo'):
    I_iclass_statistics_get_histo = _libs['grass_imagery.7.8'].I_iclass_statistics_get_histo
    I_iclass_statistics_get_histo.argtypes = [POINTER(IClass_statistics), c_int, c_int, POINTER(c_int)]
    I_iclass_statistics_get_histo.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 90
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_statistics_get_product'):
    I_iclass_statistics_get_product = _libs['grass_imagery.7.8'].I_iclass_statistics_get_product
    I_iclass_statistics_get_product.argtypes = [POINTER(IClass_statistics), c_int, c_int, POINTER(c_float)]
    I_iclass_statistics_get_product.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 91
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_init_statistics'):
    I_iclass_init_statistics = _libs['grass_imagery.7.8'].I_iclass_init_statistics
    I_iclass_init_statistics.argtypes = [POINTER(IClass_statistics), c_int, String, String, c_float]
    I_iclass_init_statistics.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 92
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_free_statistics'):
    I_iclass_free_statistics = _libs['grass_imagery.7.8'].I_iclass_free_statistics
    I_iclass_free_statistics.argtypes = [POINTER(IClass_statistics)]
    I_iclass_free_statistics.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 95
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_init_signatures'):
    I_iclass_init_signatures = _libs['grass_imagery.7.8'].I_iclass_init_signatures
    I_iclass_init_signatures.argtypes = [POINTER(struct_Signature), POINTER(struct_Ref)]
    I_iclass_init_signatures.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 96
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_add_signature'):
    I_iclass_add_signature = _libs['grass_imagery.7.8'].I_iclass_add_signature
    I_iclass_add_signature.argtypes = [POINTER(struct_Signature), POINTER(IClass_statistics)]
    I_iclass_add_signature.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 97
if hasattr(_libs['grass_imagery.7.8'], 'I_iclass_write_signatures'):
    I_iclass_write_signatures = _libs['grass_imagery.7.8'].I_iclass_write_signatures
    I_iclass_write_signatures.argtypes = [POINTER(struct_Signature), String, String, String]
    I_iclass_write_signatures.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 100
if hasattr(_libs['grass_imagery.7.8'], 'I_list_group'):
    I_list_group = _libs['grass_imagery.7.8'].I_list_group
    I_list_group.argtypes = [String, POINTER(struct_Ref), POINTER(FILE)]
    I_list_group.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 101
if hasattr(_libs['grass_imagery.7.8'], 'I_list_group_simple'):
    I_list_group_simple = _libs['grass_imagery.7.8'].I_list_group_simple
    I_list_group_simple.argtypes = [POINTER(struct_Ref), POINTER(FILE)]
    I_list_group_simple.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 104
if hasattr(_libs['grass_imagery.7.8'], 'I_list_subgroups'):
    I_list_subgroups = _libs['grass_imagery.7.8'].I_list_subgroups
    I_list_subgroups.argtypes = [String, POINTER(c_int)]
    I_list_subgroups.restype = POINTER(POINTER(c_char))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 105
if hasattr(_libs['grass_imagery.7.8'], 'I_list_subgroups2'):
    I_list_subgroups2 = _libs['grass_imagery.7.8'].I_list_subgroups2
    I_list_subgroups2.argtypes = [String, String, POINTER(c_int)]
    I_list_subgroups2.restype = POINTER(POINTER(c_char))

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 106
if hasattr(_libs['grass_imagery.7.8'], 'I_list_subgroup'):
    I_list_subgroup = _libs['grass_imagery.7.8'].I_list_subgroup
    I_list_subgroup.argtypes = [String, String, POINTER(struct_Ref), POINTER(FILE)]
    I_list_subgroup.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 107
if hasattr(_libs['grass_imagery.7.8'], 'I_list_subgroup_simple'):
    I_list_subgroup_simple = _libs['grass_imagery.7.8'].I_list_subgroup_simple
    I_list_subgroup_simple.argtypes = [POINTER(struct_Ref), POINTER(FILE)]
    I_list_subgroup_simple.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 110
if hasattr(_libs['grass_imagery.7.8'], 'I_location_info'):
    I_location_info = _libs['grass_imagery.7.8'].I_location_info
    I_location_info.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        I_location_info.restype = ReturnString
    else:
        I_location_info.restype = String
        I_location_info.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 113
if hasattr(_libs['grass_imagery.7.8'], 'I_new_control_point'):
    I_new_control_point = _libs['grass_imagery.7.8'].I_new_control_point
    I_new_control_point.argtypes = [POINTER(struct_Control_Points), c_double, c_double, c_double, c_double, c_int]
    I_new_control_point.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 115
if hasattr(_libs['grass_imagery.7.8'], 'I_get_control_points'):
    I_get_control_points = _libs['grass_imagery.7.8'].I_get_control_points
    I_get_control_points.argtypes = [String, POINTER(struct_Control_Points)]
    I_get_control_points.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 116
if hasattr(_libs['grass_imagery.7.8'], 'I_put_control_points'):
    I_put_control_points = _libs['grass_imagery.7.8'].I_put_control_points
    I_put_control_points.argtypes = [String, POINTER(struct_Control_Points)]
    I_put_control_points.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 119
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_group_ref_new'):
    I_fopen_group_ref_new = _libs['grass_imagery.7.8'].I_fopen_group_ref_new
    I_fopen_group_ref_new.argtypes = [String]
    I_fopen_group_ref_new.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 120
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_group_ref_old'):
    I_fopen_group_ref_old = _libs['grass_imagery.7.8'].I_fopen_group_ref_old
    I_fopen_group_ref_old.argtypes = [String]
    I_fopen_group_ref_old.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 121
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_group_ref_old2'):
    I_fopen_group_ref_old2 = _libs['grass_imagery.7.8'].I_fopen_group_ref_old2
    I_fopen_group_ref_old2.argtypes = [String, String]
    I_fopen_group_ref_old2.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 122
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_subgroup_ref_new'):
    I_fopen_subgroup_ref_new = _libs['grass_imagery.7.8'].I_fopen_subgroup_ref_new
    I_fopen_subgroup_ref_new.argtypes = [String, String]
    I_fopen_subgroup_ref_new.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 123
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_subgroup_ref_old'):
    I_fopen_subgroup_ref_old = _libs['grass_imagery.7.8'].I_fopen_subgroup_ref_old
    I_fopen_subgroup_ref_old.argtypes = [String, String]
    I_fopen_subgroup_ref_old.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 124
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_subgroup_ref_old2'):
    I_fopen_subgroup_ref_old2 = _libs['grass_imagery.7.8'].I_fopen_subgroup_ref_old2
    I_fopen_subgroup_ref_old2.argtypes = [String, String, String]
    I_fopen_subgroup_ref_old2.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 127
if hasattr(_libs['grass_imagery.7.8'], 'I_sc_init_cats'):
    I_sc_init_cats = _libs['grass_imagery.7.8'].I_sc_init_cats
    I_sc_init_cats.argtypes = [POINTER(struct_scCats), c_int, c_int]
    I_sc_init_cats.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 128
if hasattr(_libs['grass_imagery.7.8'], 'I_sc_free_cats'):
    I_sc_free_cats = _libs['grass_imagery.7.8'].I_sc_free_cats
    I_sc_free_cats.argtypes = [POINTER(struct_scCats)]
    I_sc_free_cats.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 129
if hasattr(_libs['grass_imagery.7.8'], 'I_sc_add_cat'):
    I_sc_add_cat = _libs['grass_imagery.7.8'].I_sc_add_cat
    I_sc_add_cat.argtypes = [POINTER(struct_scCats)]
    I_sc_add_cat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 130
if hasattr(_libs['grass_imagery.7.8'], 'I_sc_insert_scatt_data'):
    I_sc_insert_scatt_data = _libs['grass_imagery.7.8'].I_sc_insert_scatt_data
    I_sc_insert_scatt_data.argtypes = [POINTER(struct_scCats), POINTER(struct_scdScattData), c_int, c_int]
    I_sc_insert_scatt_data.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 132
if hasattr(_libs['grass_imagery.7.8'], 'I_scd_init_scatt_data'):
    I_scd_init_scatt_data = _libs['grass_imagery.7.8'].I_scd_init_scatt_data
    I_scd_init_scatt_data.argtypes = [POINTER(struct_scdScattData), c_int, c_int, POINTER(None)]
    I_scd_init_scatt_data.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 135
if hasattr(_libs['grass_imagery.7.8'], 'I_compute_scatts'):
    I_compute_scatts = _libs['grass_imagery.7.8'].I_compute_scatts
    I_compute_scatts.argtypes = [POINTER(struct_Cell_head), POINTER(struct_scCats), POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), c_int, POINTER(struct_scCats), POINTER(POINTER(c_char))]
    I_compute_scatts.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 138
if hasattr(_libs['grass_imagery.7.8'], 'I_create_cat_rast'):
    I_create_cat_rast = _libs['grass_imagery.7.8'].I_create_cat_rast
    I_create_cat_rast.argtypes = [POINTER(struct_Cell_head), String]
    I_create_cat_rast.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 139
if hasattr(_libs['grass_imagery.7.8'], 'I_insert_patch_to_cat_rast'):
    I_insert_patch_to_cat_rast = _libs['grass_imagery.7.8'].I_insert_patch_to_cat_rast
    I_insert_patch_to_cat_rast.argtypes = [String, POINTER(struct_Cell_head), String]
    I_insert_patch_to_cat_rast.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 141
if hasattr(_libs['grass_imagery.7.8'], 'I_id_scatt_to_bands'):
    I_id_scatt_to_bands = _libs['grass_imagery.7.8'].I_id_scatt_to_bands
    I_id_scatt_to_bands.argtypes = [c_int, c_int, POINTER(c_int), POINTER(c_int)]
    I_id_scatt_to_bands.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 142
if hasattr(_libs['grass_imagery.7.8'], 'I_bands_to_id_scatt'):
    I_bands_to_id_scatt = _libs['grass_imagery.7.8'].I_bands_to_id_scatt
    I_bands_to_id_scatt.argtypes = [c_int, c_int, c_int, POINTER(c_int)]
    I_bands_to_id_scatt.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 144
if hasattr(_libs['grass_imagery.7.8'], 'I_merge_arrays'):
    I_merge_arrays = _libs['grass_imagery.7.8'].I_merge_arrays
    I_merge_arrays.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, c_uint, c_double]
    I_merge_arrays.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 145
if hasattr(_libs['grass_imagery.7.8'], 'I_apply_colormap'):
    I_apply_colormap = _libs['grass_imagery.7.8'].I_apply_colormap
    I_apply_colormap.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_uint, POINTER(c_ubyte), POINTER(c_ubyte)]
    I_apply_colormap.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 146
if hasattr(_libs['grass_imagery.7.8'], 'I_rasterize'):
    I_rasterize = _libs['grass_imagery.7.8'].I_rasterize
    I_rasterize.argtypes = [POINTER(c_double), c_int, c_ubyte, POINTER(struct_Cell_head), POINTER(c_ubyte)]
    I_rasterize.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 149
if hasattr(_libs['grass_imagery.7.8'], 'I_init_signatures'):
    I_init_signatures = _libs['grass_imagery.7.8'].I_init_signatures
    I_init_signatures.argtypes = [POINTER(struct_Signature), c_int]
    I_init_signatures.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 150
if hasattr(_libs['grass_imagery.7.8'], 'I_new_signature'):
    I_new_signature = _libs['grass_imagery.7.8'].I_new_signature
    I_new_signature.argtypes = [POINTER(struct_Signature)]
    I_new_signature.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 151
if hasattr(_libs['grass_imagery.7.8'], 'I_free_signatures'):
    I_free_signatures = _libs['grass_imagery.7.8'].I_free_signatures
    I_free_signatures.argtypes = [POINTER(struct_Signature)]
    I_free_signatures.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 152
if hasattr(_libs['grass_imagery.7.8'], 'I_read_one_signature'):
    I_read_one_signature = _libs['grass_imagery.7.8'].I_read_one_signature
    I_read_one_signature.argtypes = [POINTER(FILE), POINTER(struct_Signature)]
    I_read_one_signature.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 153
if hasattr(_libs['grass_imagery.7.8'], 'I_read_signatures'):
    I_read_signatures = _libs['grass_imagery.7.8'].I_read_signatures
    I_read_signatures.argtypes = [POINTER(FILE), POINTER(struct_Signature)]
    I_read_signatures.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 154
if hasattr(_libs['grass_imagery.7.8'], 'I_write_signatures'):
    I_write_signatures = _libs['grass_imagery.7.8'].I_write_signatures
    I_write_signatures.argtypes = [POINTER(FILE), POINTER(struct_Signature)]
    I_write_signatures.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 157
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_signature_file_new'):
    I_fopen_signature_file_new = _libs['grass_imagery.7.8'].I_fopen_signature_file_new
    I_fopen_signature_file_new.argtypes = [String, String, String]
    I_fopen_signature_file_new.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 158
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_signature_file_old'):
    I_fopen_signature_file_old = _libs['grass_imagery.7.8'].I_fopen_signature_file_old
    I_fopen_signature_file_old.argtypes = [String, String, String]
    I_fopen_signature_file_old.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 161
if hasattr(_libs['grass_imagery.7.8'], 'I_SigSetNClasses'):
    I_SigSetNClasses = _libs['grass_imagery.7.8'].I_SigSetNClasses
    I_SigSetNClasses.argtypes = [POINTER(struct_SigSet)]
    I_SigSetNClasses.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 162
if hasattr(_libs['grass_imagery.7.8'], 'I_AllocClassData'):
    I_AllocClassData = _libs['grass_imagery.7.8'].I_AllocClassData
    I_AllocClassData.argtypes = [POINTER(struct_SigSet), POINTER(struct_ClassSig), c_int]
    I_AllocClassData.restype = POINTER(struct_ClassData)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 163
if hasattr(_libs['grass_imagery.7.8'], 'I_InitSigSet'):
    I_InitSigSet = _libs['grass_imagery.7.8'].I_InitSigSet
    I_InitSigSet.argtypes = [POINTER(struct_SigSet)]
    I_InitSigSet.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 164
if hasattr(_libs['grass_imagery.7.8'], 'I_SigSetNBands'):
    I_SigSetNBands = _libs['grass_imagery.7.8'].I_SigSetNBands
    I_SigSetNBands.argtypes = [POINTER(struct_SigSet), c_int]
    I_SigSetNBands.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 165
if hasattr(_libs['grass_imagery.7.8'], 'I_NewClassSig'):
    I_NewClassSig = _libs['grass_imagery.7.8'].I_NewClassSig
    I_NewClassSig.argtypes = [POINTER(struct_SigSet)]
    I_NewClassSig.restype = POINTER(struct_ClassSig)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 166
if hasattr(_libs['grass_imagery.7.8'], 'I_NewSubSig'):
    I_NewSubSig = _libs['grass_imagery.7.8'].I_NewSubSig
    I_NewSubSig.argtypes = [POINTER(struct_SigSet), POINTER(struct_ClassSig)]
    I_NewSubSig.restype = POINTER(struct_SubSig)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 167
if hasattr(_libs['grass_imagery.7.8'], 'I_ReadSigSet'):
    I_ReadSigSet = _libs['grass_imagery.7.8'].I_ReadSigSet
    I_ReadSigSet.argtypes = [POINTER(FILE), POINTER(struct_SigSet)]
    I_ReadSigSet.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 168
if hasattr(_libs['grass_imagery.7.8'], 'I_SetSigTitle'):
    I_SetSigTitle = _libs['grass_imagery.7.8'].I_SetSigTitle
    I_SetSigTitle.argtypes = [POINTER(struct_SigSet), String]
    I_SetSigTitle.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 169
if hasattr(_libs['grass_imagery.7.8'], 'I_GetSigTitle'):
    I_GetSigTitle = _libs['grass_imagery.7.8'].I_GetSigTitle
    I_GetSigTitle.argtypes = [POINTER(struct_SigSet)]
    I_GetSigTitle.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 170
if hasattr(_libs['grass_imagery.7.8'], 'I_SetClassTitle'):
    I_SetClassTitle = _libs['grass_imagery.7.8'].I_SetClassTitle
    I_SetClassTitle.argtypes = [POINTER(struct_ClassSig), String]
    I_SetClassTitle.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 171
if hasattr(_libs['grass_imagery.7.8'], 'I_GetClassTitle'):
    I_GetClassTitle = _libs['grass_imagery.7.8'].I_GetClassTitle
    I_GetClassTitle.argtypes = [POINTER(struct_ClassSig)]
    I_GetClassTitle.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 172
if hasattr(_libs['grass_imagery.7.8'], 'I_WriteSigSet'):
    I_WriteSigSet = _libs['grass_imagery.7.8'].I_WriteSigSet
    I_WriteSigSet.argtypes = [POINTER(FILE), POINTER(struct_SigSet)]
    I_WriteSigSet.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 175
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_sigset_file_new'):
    I_fopen_sigset_file_new = _libs['grass_imagery.7.8'].I_fopen_sigset_file_new
    I_fopen_sigset_file_new.argtypes = [String, String, String]
    I_fopen_sigset_file_new.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 176
if hasattr(_libs['grass_imagery.7.8'], 'I_fopen_sigset_file_old'):
    I_fopen_sigset_file_old = _libs['grass_imagery.7.8'].I_fopen_sigset_file_old
    I_fopen_sigset_file_old.argtypes = [String, String, String]
    I_fopen_sigset_file_old.restype = POINTER(FILE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 179
if hasattr(_libs['grass_imagery.7.8'], 'I_get_target'):
    I_get_target = _libs['grass_imagery.7.8'].I_get_target
    I_get_target.argtypes = [String, String, String]
    I_get_target.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 180
if hasattr(_libs['grass_imagery.7.8'], 'I_put_target'):
    I_put_target = _libs['grass_imagery.7.8'].I_put_target
    I_put_target.argtypes = [String, String, String]
    I_put_target.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 183
if hasattr(_libs['grass_imagery.7.8'], 'I_get_group_title'):
    I_get_group_title = _libs['grass_imagery.7.8'].I_get_group_title
    I_get_group_title.argtypes = [String, String, c_int]
    I_get_group_title.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 184
if hasattr(_libs['grass_imagery.7.8'], 'I_put_group_title'):
    I_put_group_title = _libs['grass_imagery.7.8'].I_put_group_title
    I_put_group_title.argtypes = [String, String]
    I_put_group_title.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 187
if hasattr(_libs['grass_imagery.7.8'], 'I_variance'):
    I_variance = _libs['grass_imagery.7.8'].I_variance
    I_variance.argtypes = [c_double, c_double, c_int]
    I_variance.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 188
if hasattr(_libs['grass_imagery.7.8'], 'I_stddev'):
    I_stddev = _libs['grass_imagery.7.8'].I_stddev
    I_stddev.argtypes = [c_double, c_double, c_int]
    I_stddev.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 162
try:
    GNAME_MAX = 256
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 8
try:
    INAME_LEN = GNAME_MAX
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 142
try:
    SC_SCATT_DATA = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 143
try:
    SC_SCATT_CONDITIONS = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 197
try:
    SIGNATURE_TYPE_MIXED = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 199
try:
    GROUPFILE = 'CURGROUP'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 200
try:
    SUBGROUPFILE = 'CURSUBGROUP'
except:
    pass

Ref_Color = struct_Ref_Color # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 10

Ref_Files = struct_Ref_Files # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 20

Ref = struct_Ref # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 26

Tape_Info = struct_Tape_Info # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 33

Control_Points = struct_Control_Points # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 40

One_Sig = struct_One_Sig # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 52

Signature = struct_Signature # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 63

SubSig = struct_SubSig # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 71

ClassData = struct_ClassData # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 82

ClassSig = struct_ClassSig # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 90

SigSet = struct_SigSet # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 101

scScatts = struct_scScatts # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 171

scCats = struct_scCats # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 149

scdScattData = struct_scdScattData # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\imagery.h: 186

Map_info = struct_Map_info # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/imagery.h: 69

# No inserted files

