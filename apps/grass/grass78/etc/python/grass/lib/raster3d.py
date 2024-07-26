'''Wrapper for raster3d.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_g3d.7.8 C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster3d.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h -o OBJ.x86_64-w64-mingw32/raster3d.py

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

_libs["grass_g3d.7.8"] = load_library("grass_g3d.7.8")

# 1 libraries
# End libraries

# No modules

NULL = None # <built-in>

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

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 496
class struct_Key_Value(Structure):
    pass

struct_Key_Value.__slots__ = [
    'nitems',
    'nalloc',
    'key',
    'value',
]
struct_Key_Value._fields_ = [
    ('nitems', c_int),
    ('nalloc', c_int),
    ('key', POINTER(POINTER(c_char))),
    ('value', POINTER(POINTER(c_char))),
]

CELL = c_int # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 597

DCELL = c_double # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 598

grass_int64 = c_int64 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 606

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

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 76
class struct_Quant_table(Structure):
    pass

struct_Quant_table.__slots__ = [
    'dLow',
    'dHigh',
    'cLow',
    'cHigh',
]
struct_Quant_table._fields_ = [
    ('dLow', DCELL),
    ('dHigh', DCELL),
    ('cLow', CELL),
    ('cHigh', CELL),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 109
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'vals',
    'rules',
    'nalloc',
    'active',
    'inf_dmin',
    'inf_dmax',
    'inf_min',
    'inf_max',
]
struct_anon_7._fields_ = [
    ('vals', POINTER(DCELL)),
    ('rules', POINTER(POINTER(struct_Quant_table))),
    ('nalloc', c_int),
    ('active', c_int),
    ('inf_dmin', DCELL),
    ('inf_dmax', DCELL),
    ('inf_min', CELL),
    ('inf_max', CELL),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 84
class struct_Quant(Structure):
    pass

struct_Quant.__slots__ = [
    'truncate_only',
    'round_only',
    'defaultDRuleSet',
    'defaultCRuleSet',
    'infiniteLeftSet',
    'infiniteRightSet',
    'cRangeSet',
    'maxNofRules',
    'nofRules',
    'defaultDMin',
    'defaultDMax',
    'defaultCMin',
    'defaultCMax',
    'infiniteDLeft',
    'infiniteDRight',
    'infiniteCLeft',
    'infiniteCRight',
    'dMin',
    'dMax',
    'cMin',
    'cMax',
    'table',
    'fp_lookup',
]
struct_Quant._fields_ = [
    ('truncate_only', c_int),
    ('round_only', c_int),
    ('defaultDRuleSet', c_int),
    ('defaultCRuleSet', c_int),
    ('infiniteLeftSet', c_int),
    ('infiniteRightSet', c_int),
    ('cRangeSet', c_int),
    ('maxNofRules', c_int),
    ('nofRules', c_int),
    ('defaultDMin', DCELL),
    ('defaultDMax', DCELL),
    ('defaultCMin', CELL),
    ('defaultCMax', CELL),
    ('infiniteDLeft', DCELL),
    ('infiniteDRight', DCELL),
    ('infiniteCLeft', CELL),
    ('infiniteCRight', CELL),
    ('dMin', DCELL),
    ('dMax', DCELL),
    ('cMin', CELL),
    ('cMax', CELL),
    ('table', POINTER(struct_Quant_table)),
    ('fp_lookup', struct_anon_7),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 127
class struct_Categories(Structure):
    pass

struct_Categories.__slots__ = [
    'ncats',
    'num',
    'title',
    'fmt',
    'm1',
    'a1',
    'm2',
    'a2',
    'q',
    'labels',
    'marks',
    'nalloc',
    'last_marked_rule',
]
struct_Categories._fields_ = [
    ('ncats', CELL),
    ('num', CELL),
    ('title', String),
    ('fmt', String),
    ('m1', c_float),
    ('a1', c_float),
    ('m2', c_float),
    ('a2', c_float),
    ('q', struct_Quant),
    ('labels', POINTER(POINTER(c_char))),
    ('marks', POINTER(c_int)),
    ('nalloc', c_int),
    ('last_marked_rule', c_int),
]

HIST_MAPID = 0 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_TITLE = (HIST_MAPID + 1) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_MAPSET = (HIST_TITLE + 1) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_CREATOR = (HIST_MAPSET + 1) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_MAPTYPE = (HIST_CREATOR + 1) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_DATSRC_1 = (HIST_MAPTYPE + 1) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_DATSRC_2 = (HIST_DATSRC_1 + 1) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_KEYWRD = (HIST_DATSRC_2 + 1) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

HIST_NUM_FIELDS = (HIST_KEYWRD + 1) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 157

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 180
class struct_History(Structure):
    pass

struct_History.__slots__ = [
    'fields',
    'nlines',
    'lines',
]
struct_History._fields_ = [
    ('fields', POINTER(c_char) * HIST_NUM_FIELDS),
    ('nlines', c_int),
    ('lines', POINTER(POINTER(c_char))),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 218
class struct_R_stats(Structure):
    pass

struct_R_stats.__slots__ = [
    'sum',
    'sumsq',
    'count',
]
struct_R_stats._fields_ = [
    ('sum', DCELL),
    ('sumsq', DCELL),
    ('count', grass_int64),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/raster.h: 233
class struct_FPRange(Structure):
    pass

struct_FPRange.__slots__ = [
    'min',
    'max',
    'first_time',
    'rstats',
]
struct_FPRange._fields_ = [
    ('min', DCELL),
    ('max', DCELL),
    ('first_time', c_int),
    ('rstats', struct_R_stats),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 62
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
    'rows',
    'cols',
    'depths',
    'ns_res',
    'ew_res',
    'tb_res',
    'proj',
    'zone',
]
struct_anon_8._fields_ = [
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
    ('rows', c_int),
    ('cols', c_int),
    ('depths', c_int),
    ('ns_res', c_double),
    ('ew_res', c_double),
    ('tb_res', c_double),
    ('proj', c_int),
    ('zone', c_int),
]

RASTER3D_Region = struct_anon_8 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 62

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 72
class struct_RASTER3D_Map(Structure):
    pass

resample_fn = CFUNCTYPE(UNCHECKED(None), POINTER(struct_RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int) # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 68

struct_RASTER3D_Map.__slots__ = [
    'version',
    'fileName',
    'tempName',
    'mapset',
    'operation',
    'region',
    'window',
    'resampleFun',
    'unit',
    'vertical_unit',
    'tileX',
    'tileY',
    'tileZ',
    'nx',
    'ny',
    'nz',
    'data_fd',
    'type',
    'precision',
    'compression',
    'useLzw',
    'useRle',
    'useXdr',
    'offset',
    'indexOffset',
    'indexLongNbytes',
    'indexNbytesUsed',
    'fileEndPtr',
    'hasIndex',
    'index',
    'tileLength',
    'typeIntern',
    'data',
    'currentIndex',
    'useCache',
    'cache',
    'cacheFD',
    'cacheFileName',
    'cachePosLast',
    'range',
    'numLengthExtern',
    'numLengthIntern',
    'clipX',
    'clipY',
    'clipZ',
    'tileXY',
    'tileSize',
    'nxy',
    'nTiles',
    'useMask',
]
struct_RASTER3D_Map._fields_ = [
    ('version', c_int),
    ('fileName', String),
    ('tempName', String),
    ('mapset', String),
    ('operation', c_int),
    ('region', RASTER3D_Region),
    ('window', RASTER3D_Region),
    ('resampleFun', POINTER(resample_fn)),
    ('unit', String),
    ('vertical_unit', c_int),
    ('tileX', c_int),
    ('tileY', c_int),
    ('tileZ', c_int),
    ('nx', c_int),
    ('ny', c_int),
    ('nz', c_int),
    ('data_fd', c_int),
    ('type', c_int),
    ('precision', c_int),
    ('compression', c_int),
    ('useLzw', c_int),
    ('useRle', c_int),
    ('useXdr', c_int),
    ('offset', c_int),
    ('indexOffset', c_long),
    ('indexLongNbytes', c_int),
    ('indexNbytesUsed', c_int),
    ('fileEndPtr', c_int),
    ('hasIndex', c_int),
    ('index', POINTER(c_long)),
    ('tileLength', POINTER(c_int)),
    ('typeIntern', c_int),
    ('data', String),
    ('currentIndex', c_int),
    ('useCache', c_int),
    ('cache', POINTER(None)),
    ('cacheFD', c_int),
    ('cacheFileName', String),
    ('cachePosLast', c_long),
    ('range', struct_FPRange),
    ('numLengthExtern', c_int),
    ('numLengthIntern', c_int),
    ('clipX', c_int),
    ('clipY', c_int),
    ('clipZ', c_int),
    ('tileXY', c_int),
    ('tileSize', c_int),
    ('nxy', c_int),
    ('nTiles', c_int),
    ('useMask', c_int),
]

RASTER3D_Map = struct_RASTER3D_Map # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 186

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 221
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'elts',
    'nofElts',
    'eltSize',
    'names',
    'locks',
    'autoLock',
    'nofUnlocked',
    'minUnlocked',
    'next',
    'prev',
    'first',
    'last',
    'eltRemoveFun',
    'eltRemoveFunData',
    'eltLoadFun',
    'eltLoadFunData',
    'hash',
]
struct_anon_9._fields_ = [
    ('elts', String),
    ('nofElts', c_int),
    ('eltSize', c_int),
    ('names', POINTER(c_int)),
    ('locks', String),
    ('autoLock', c_int),
    ('nofUnlocked', c_int),
    ('minUnlocked', c_int),
    ('next', POINTER(c_int)),
    ('prev', POINTER(c_int)),
    ('first', c_int),
    ('last', c_int),
    ('eltRemoveFun', CFUNCTYPE(UNCHECKED(c_int), )),
    ('eltRemoveFunData', POINTER(None)),
    ('eltLoadFun', CFUNCTYPE(UNCHECKED(c_int), )),
    ('eltLoadFunData', POINTER(None)),
    ('hash', POINTER(None)),
]

RASTER3D_cache = struct_anon_9 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 221

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 235
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'nofNames',
    'index',
    'active',
    'lastName',
    'lastIndex',
    'lastIndexActive',
]
struct_anon_10._fields_ = [
    ('nofNames', c_int),
    ('index', POINTER(c_int)),
    ('active', String),
    ('lastName', c_int),
    ('lastIndex', c_int),
    ('lastIndexActive', c_int),
]

Rast3d_cache_hash = struct_anon_10 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 235

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 240
class struct__d_interval(Structure):
    pass

struct__d_interval.__slots__ = [
    'low',
    'high',
    'inf',
    'next',
]
struct__d_interval._fields_ = [
    ('low', c_double),
    ('high', c_double),
    ('inf', c_int),
    ('next', POINTER(struct__d_interval)),
]

d_Interval = struct__d_interval # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 245

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 250
class struct__d_mask(Structure):
    pass

struct__d_mask.__slots__ = [
    'list',
]
struct__d_mask._fields_ = [
    ('list', POINTER(d_Interval)),
]

d_Mask = struct__d_mask # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 250

write_fn = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), POINTER(None)) # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 254

read_fn = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(None), POINTER(None)) # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 255

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 266
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'array',
    'sx',
    'sy',
    'sz',
]
struct_anon_11._fields_ = [
    ('array', POINTER(DCELL)),
    ('sx', c_int),
    ('sy', c_int),
    ('sz', c_int),
]

RASTER3D_Array_double = struct_anon_11 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 266

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 5
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_reset'):
    Rast3d_cache_reset = _libs['grass_g3d.7.8'].Rast3d_cache_reset
    Rast3d_cache_reset.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_reset.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 6
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_dispose'):
    Rast3d_cache_dispose = _libs['grass_g3d.7.8'].Rast3d_cache_dispose
    Rast3d_cache_dispose.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_dispose.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 7
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_new'):
    Rast3d_cache_new = _libs['grass_g3d.7.8'].Rast3d_cache_new
    Rast3d_cache_new.argtypes = [c_int, c_int, c_int, POINTER(write_fn), POINTER(None), POINTER(read_fn), POINTER(None)]
    Rast3d_cache_new.restype = POINTER(c_ubyte)
    Rast3d_cache_new.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 8
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_set_remove_fun'):
    Rast3d_cache_set_remove_fun = _libs['grass_g3d.7.8'].Rast3d_cache_set_remove_fun
    Rast3d_cache_set_remove_fun.argtypes = [POINTER(RASTER3D_cache), POINTER(write_fn), POINTER(None)]
    Rast3d_cache_set_remove_fun.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 9
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_set_load_fun'):
    Rast3d_cache_set_load_fun = _libs['grass_g3d.7.8'].Rast3d_cache_set_load_fun
    Rast3d_cache_set_load_fun.argtypes = [POINTER(RASTER3D_cache), POINTER(read_fn), POINTER(None)]
    Rast3d_cache_set_load_fun.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 10
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_new_read'):
    Rast3d_cache_new_read = _libs['grass_g3d.7.8'].Rast3d_cache_new_read
    Rast3d_cache_new_read.argtypes = [c_int, c_int, c_int, POINTER(read_fn), POINTER(None)]
    Rast3d_cache_new_read.restype = POINTER(c_ubyte)
    Rast3d_cache_new_read.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 11
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_lock'):
    Rast3d_cache_lock = _libs['grass_g3d.7.8'].Rast3d_cache_lock
    Rast3d_cache_lock.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_lock.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 12
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_lock_intern'):
    Rast3d_cache_lock_intern = _libs['grass_g3d.7.8'].Rast3d_cache_lock_intern
    Rast3d_cache_lock_intern.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_lock_intern.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 13
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_unlock'):
    Rast3d_cache_unlock = _libs['grass_g3d.7.8'].Rast3d_cache_unlock
    Rast3d_cache_unlock.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_unlock.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 14
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_unlock_all'):
    Rast3d_cache_unlock_all = _libs['grass_g3d.7.8'].Rast3d_cache_unlock_all
    Rast3d_cache_unlock_all.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_unlock_all.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 15
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_lock_all'):
    Rast3d_cache_lock_all = _libs['grass_g3d.7.8'].Rast3d_cache_lock_all
    Rast3d_cache_lock_all.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_lock_all.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 16
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_autolock_on'):
    Rast3d_cache_autolock_on = _libs['grass_g3d.7.8'].Rast3d_cache_autolock_on
    Rast3d_cache_autolock_on.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_autolock_on.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 17
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_autolock_off'):
    Rast3d_cache_autolock_off = _libs['grass_g3d.7.8'].Rast3d_cache_autolock_off
    Rast3d_cache_autolock_off.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_autolock_off.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 18
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_set_min_unlock'):
    Rast3d_cache_set_min_unlock = _libs['grass_g3d.7.8'].Rast3d_cache_set_min_unlock
    Rast3d_cache_set_min_unlock.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_set_min_unlock.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 19
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_remove_elt'):
    Rast3d_cache_remove_elt = _libs['grass_g3d.7.8'].Rast3d_cache_remove_elt
    Rast3d_cache_remove_elt.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_remove_elt.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 20
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_flush'):
    Rast3d_cache_flush = _libs['grass_g3d.7.8'].Rast3d_cache_flush
    Rast3d_cache_flush.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_flush.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 21
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_remove_all'):
    Rast3d_cache_remove_all = _libs['grass_g3d.7.8'].Rast3d_cache_remove_all
    Rast3d_cache_remove_all.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_remove_all.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 22
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_flush_all'):
    Rast3d_cache_flush_all = _libs['grass_g3d.7.8'].Rast3d_cache_flush_all
    Rast3d_cache_flush_all.argtypes = [POINTER(RASTER3D_cache)]
    Rast3d_cache_flush_all.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 23
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_elt_ptr'):
    Rast3d_cache_elt_ptr = _libs['grass_g3d.7.8'].Rast3d_cache_elt_ptr
    Rast3d_cache_elt_ptr.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_elt_ptr.restype = POINTER(c_ubyte)
    Rast3d_cache_elt_ptr.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 24
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_load'):
    Rast3d_cache_load = _libs['grass_g3d.7.8'].Rast3d_cache_load
    Rast3d_cache_load.argtypes = [POINTER(RASTER3D_cache), c_int]
    Rast3d_cache_load.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 25
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_get_elt'):
    Rast3d_cache_get_elt = _libs['grass_g3d.7.8'].Rast3d_cache_get_elt
    Rast3d_cache_get_elt.argtypes = [POINTER(RASTER3D_cache), c_int, POINTER(None)]
    Rast3d_cache_get_elt.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 26
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_put_elt'):
    Rast3d_cache_put_elt = _libs['grass_g3d.7.8'].Rast3d_cache_put_elt
    Rast3d_cache_put_elt.argtypes = [POINTER(RASTER3D_cache), c_int, POINTER(None)]
    Rast3d_cache_put_elt.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 29
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_hash_reset'):
    Rast3d_cache_hash_reset = _libs['grass_g3d.7.8'].Rast3d_cache_hash_reset
    Rast3d_cache_hash_reset.argtypes = [POINTER(Rast3d_cache_hash)]
    Rast3d_cache_hash_reset.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 30
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_hash_dispose'):
    Rast3d_cache_hash_dispose = _libs['grass_g3d.7.8'].Rast3d_cache_hash_dispose
    Rast3d_cache_hash_dispose.argtypes = [POINTER(Rast3d_cache_hash)]
    Rast3d_cache_hash_dispose.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 31
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_hash_new'):
    Rast3d_cache_hash_new = _libs['grass_g3d.7.8'].Rast3d_cache_hash_new
    Rast3d_cache_hash_new.argtypes = [c_int]
    Rast3d_cache_hash_new.restype = POINTER(c_ubyte)
    Rast3d_cache_hash_new.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 32
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_hash_remove_name'):
    Rast3d_cache_hash_remove_name = _libs['grass_g3d.7.8'].Rast3d_cache_hash_remove_name
    Rast3d_cache_hash_remove_name.argtypes = [POINTER(Rast3d_cache_hash), c_int]
    Rast3d_cache_hash_remove_name.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 33
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_hash_load_name'):
    Rast3d_cache_hash_load_name = _libs['grass_g3d.7.8'].Rast3d_cache_hash_load_name
    Rast3d_cache_hash_load_name.argtypes = [POINTER(Rast3d_cache_hash), c_int, c_int]
    Rast3d_cache_hash_load_name.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 34
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_hash_name2index'):
    Rast3d_cache_hash_name2index = _libs['grass_g3d.7.8'].Rast3d_cache_hash_name2index
    Rast3d_cache_hash_name2index.argtypes = [POINTER(Rast3d_cache_hash), c_int]
    Rast3d_cache_hash_name2index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 37
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_change_precision'):
    Rast3d_change_precision = _libs['grass_g3d.7.8'].Rast3d_change_precision
    Rast3d_change_precision.argtypes = [POINTER(None), c_int, String]
    Rast3d_change_precision.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 40
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_change_type'):
    Rast3d_change_type = _libs['grass_g3d.7.8'].Rast3d_change_type
    Rast3d_change_type.argtypes = [POINTER(None), String]
    Rast3d_change_type.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 43
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_compare_files'):
    Rast3d_compare_files = _libs['grass_g3d.7.8'].Rast3d_compare_files
    Rast3d_compare_files.argtypes = [String, String, String, String]
    Rast3d_compare_files.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 46
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_filename'):
    Rast3d_filename = _libs['grass_g3d.7.8'].Rast3d_filename
    Rast3d_filename.argtypes = [String, String, String, String]
    Rast3d_filename.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 49
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_fpcompress_print_binary'):
    Rast3d_fpcompress_print_binary = _libs['grass_g3d.7.8'].Rast3d_fpcompress_print_binary
    Rast3d_fpcompress_print_binary.argtypes = [String, c_int]
    Rast3d_fpcompress_print_binary.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 50
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_fpcompress_dissect_xdr_double'):
    Rast3d_fpcompress_dissect_xdr_double = _libs['grass_g3d.7.8'].Rast3d_fpcompress_dissect_xdr_double
    Rast3d_fpcompress_dissect_xdr_double.argtypes = [POINTER(c_ubyte)]
    Rast3d_fpcompress_dissect_xdr_double.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 51
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_fpcompress_write_xdr_nums'):
    Rast3d_fpcompress_write_xdr_nums = _libs['grass_g3d.7.8'].Rast3d_fpcompress_write_xdr_nums
    Rast3d_fpcompress_write_xdr_nums.argtypes = [c_int, String, c_int, c_int, String, c_int]
    Rast3d_fpcompress_write_xdr_nums.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 52
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_fpcompress_read_xdr_nums'):
    Rast3d_fpcompress_read_xdr_nums = _libs['grass_g3d.7.8'].Rast3d_fpcompress_read_xdr_nums
    Rast3d_fpcompress_read_xdr_nums.argtypes = [c_int, String, c_int, c_int, c_int, String, c_int]
    Rast3d_fpcompress_read_xdr_nums.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 55
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_malloc'):
    Rast3d_malloc = _libs['grass_g3d.7.8'].Rast3d_malloc
    Rast3d_malloc.argtypes = [c_int]
    Rast3d_malloc.restype = POINTER(c_ubyte)
    Rast3d_malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 56
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_realloc'):
    Rast3d_realloc = _libs['grass_g3d.7.8'].Rast3d_realloc
    Rast3d_realloc.argtypes = [POINTER(None), c_int]
    Rast3d_realloc.restype = POINTER(c_ubyte)
    Rast3d_realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 57
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_free'):
    Rast3d_free = _libs['grass_g3d.7.8'].Rast3d_free
    Rast3d_free.argtypes = [POINTER(None)]
    Rast3d_free.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 60
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_init_cache'):
    Rast3d_init_cache = _libs['grass_g3d.7.8'].Rast3d_init_cache
    Rast3d_init_cache.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_cache.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 61
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_dispose_cache'):
    Rast3d_dispose_cache = _libs['grass_g3d.7.8'].Rast3d_dispose_cache
    Rast3d_dispose_cache.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_dispose_cache.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 62
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_flush_all_tiles'):
    Rast3d_flush_all_tiles = _libs['grass_g3d.7.8'].Rast3d_flush_all_tiles
    Rast3d_flush_all_tiles.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_flush_all_tiles.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 65
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_cats'):
    Rast3d_write_cats = _libs['grass_g3d.7.8'].Rast3d_write_cats
    Rast3d_write_cats.argtypes = [String, POINTER(struct_Categories)]
    Rast3d_write_cats.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 66
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_cats'):
    Rast3d_read_cats = _libs['grass_g3d.7.8'].Rast3d_read_cats
    Rast3d_read_cats.argtypes = [String, String, POINTER(struct_Categories)]
    Rast3d_read_cats.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 69
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_close'):
    Rast3d_close = _libs['grass_g3d.7.8'].Rast3d_close
    Rast3d_close.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_close.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 72
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_remove_color'):
    Rast3d_remove_color = _libs['grass_g3d.7.8'].Rast3d_remove_color
    Rast3d_remove_color.argtypes = [String]
    Rast3d_remove_color.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 73
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_colors'):
    Rast3d_read_colors = _libs['grass_g3d.7.8'].Rast3d_read_colors
    Rast3d_read_colors.argtypes = [String, String, POINTER(struct_Colors)]
    Rast3d_read_colors.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 74
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_colors'):
    Rast3d_write_colors = _libs['grass_g3d.7.8'].Rast3d_write_colors
    Rast3d_write_colors.argtypes = [String, String, POINTER(struct_Colors)]
    Rast3d_write_colors.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 77
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_compression_mode'):
    Rast3d_set_compression_mode = _libs['grass_g3d.7.8'].Rast3d_set_compression_mode
    Rast3d_set_compression_mode.argtypes = [c_int, c_int]
    Rast3d_set_compression_mode.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 78
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_compression_mode'):
    Rast3d_get_compression_mode = _libs['grass_g3d.7.8'].Rast3d_get_compression_mode
    Rast3d_get_compression_mode.argtypes = [POINTER(c_int), POINTER(c_int)]
    Rast3d_get_compression_mode.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 79
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_cache_size'):
    Rast3d_set_cache_size = _libs['grass_g3d.7.8'].Rast3d_set_cache_size
    Rast3d_set_cache_size.argtypes = [c_int]
    Rast3d_set_cache_size.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 80
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_cache_size'):
    Rast3d_get_cache_size = _libs['grass_g3d.7.8'].Rast3d_get_cache_size
    Rast3d_get_cache_size.argtypes = []
    Rast3d_get_cache_size.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 81
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_cache_limit'):
    Rast3d_set_cache_limit = _libs['grass_g3d.7.8'].Rast3d_set_cache_limit
    Rast3d_set_cache_limit.argtypes = [c_int]
    Rast3d_set_cache_limit.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 82
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_cache_limit'):
    Rast3d_get_cache_limit = _libs['grass_g3d.7.8'].Rast3d_get_cache_limit
    Rast3d_get_cache_limit.argtypes = []
    Rast3d_get_cache_limit.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 83
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_file_type'):
    Rast3d_set_file_type = _libs['grass_g3d.7.8'].Rast3d_set_file_type
    Rast3d_set_file_type.argtypes = [c_int]
    Rast3d_set_file_type.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 84
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_file_type'):
    Rast3d_get_file_type = _libs['grass_g3d.7.8'].Rast3d_get_file_type
    Rast3d_get_file_type.argtypes = []
    Rast3d_get_file_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 85
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_tile_dimension'):
    Rast3d_set_tile_dimension = _libs['grass_g3d.7.8'].Rast3d_set_tile_dimension
    Rast3d_set_tile_dimension.argtypes = [c_int, c_int, c_int]
    Rast3d_set_tile_dimension.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 86
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_tile_dimension'):
    Rast3d_get_tile_dimension = _libs['grass_g3d.7.8'].Rast3d_get_tile_dimension
    Rast3d_get_tile_dimension.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_tile_dimension.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 87
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_error_fun'):
    Rast3d_set_error_fun = _libs['grass_g3d.7.8'].Rast3d_set_error_fun
    Rast3d_set_error_fun.argtypes = [CFUNCTYPE(UNCHECKED(None), String)]
    Rast3d_set_error_fun.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 88
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_init_defaults'):
    Rast3d_init_defaults = _libs['grass_g3d.7.8'].Rast3d_init_defaults
    Rast3d_init_defaults.argtypes = []
    Rast3d_init_defaults.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 91
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_doubles'):
    Rast3d_write_doubles = _libs['grass_g3d.7.8'].Rast3d_write_doubles
    Rast3d_write_doubles.argtypes = [c_int, c_int, POINTER(c_double), c_int]
    Rast3d_write_doubles.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 92
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_doubles'):
    Rast3d_read_doubles = _libs['grass_g3d.7.8'].Rast3d_read_doubles
    Rast3d_read_doubles.argtypes = [c_int, c_int, POINTER(c_double), c_int]
    Rast3d_read_doubles.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 95
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_skip_error'):
    Rast3d_skip_error = _libs['grass_g3d.7.8'].Rast3d_skip_error
    Rast3d_skip_error.argtypes = [String]
    Rast3d_skip_error.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 96
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_print_error'):
    Rast3d_print_error = _libs['grass_g3d.7.8'].Rast3d_print_error
    Rast3d_print_error.argtypes = [String]
    Rast3d_print_error.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 97
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_fatal_error'):
    _func = _libs['grass_g3d.7.8'].Rast3d_fatal_error
    _restype = None
    _errcheck = None
    _argtypes = [String]
    Rast3d_fatal_error = _variadic_function(_func,_restype,_argtypes,_errcheck)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 99
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_fatal_error_noargs'):
    Rast3d_fatal_error_noargs = _libs['grass_g3d.7.8'].Rast3d_fatal_error_noargs
    Rast3d_fatal_error_noargs.argtypes = [String]
    Rast3d_fatal_error_noargs.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 100
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_error'):
    _func = _libs['grass_g3d.7.8'].Rast3d_error
    _restype = None
    _errcheck = None
    _argtypes = [String]
    Rast3d_error = _variadic_function(_func,_restype,_argtypes,_errcheck)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 103
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_is_xdr_null_num'):
    Rast3d_is_xdr_null_num = _libs['grass_g3d.7.8'].Rast3d_is_xdr_null_num
    Rast3d_is_xdr_null_num.argtypes = [POINTER(None), c_int]
    Rast3d_is_xdr_null_num.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 104
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_is_xdr_null_float'):
    Rast3d_is_xdr_null_float = _libs['grass_g3d.7.8'].Rast3d_is_xdr_null_float
    Rast3d_is_xdr_null_float.argtypes = [POINTER(c_float)]
    Rast3d_is_xdr_null_float.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 105
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_is_xdr_null_double'):
    Rast3d_is_xdr_null_double = _libs['grass_g3d.7.8'].Rast3d_is_xdr_null_double
    Rast3d_is_xdr_null_double.argtypes = [POINTER(c_double)]
    Rast3d_is_xdr_null_double.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 106
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_xdr_null_num'):
    Rast3d_set_xdr_null_num = _libs['grass_g3d.7.8'].Rast3d_set_xdr_null_num
    Rast3d_set_xdr_null_num.argtypes = [POINTER(None), c_int]
    Rast3d_set_xdr_null_num.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 107
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_xdr_null_double'):
    Rast3d_set_xdr_null_double = _libs['grass_g3d.7.8'].Rast3d_set_xdr_null_double
    Rast3d_set_xdr_null_double.argtypes = [POINTER(c_double)]
    Rast3d_set_xdr_null_double.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 108
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_xdr_null_float'):
    Rast3d_set_xdr_null_float = _libs['grass_g3d.7.8'].Rast3d_set_xdr_null_float
    Rast3d_set_xdr_null_float.argtypes = [POINTER(c_float)]
    Rast3d_set_xdr_null_float.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 109
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_init_fp_xdr'):
    Rast3d_init_fp_xdr = _libs['grass_g3d.7.8'].Rast3d_init_fp_xdr
    Rast3d_init_fp_xdr.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_fp_xdr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 110
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_init_copy_to_xdr'):
    Rast3d_init_copy_to_xdr = _libs['grass_g3d.7.8'].Rast3d_init_copy_to_xdr
    Rast3d_init_copy_to_xdr.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_copy_to_xdr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 111
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_copy_to_xdr'):
    Rast3d_copy_to_xdr = _libs['grass_g3d.7.8'].Rast3d_copy_to_xdr
    Rast3d_copy_to_xdr.argtypes = [POINTER(None), c_int]
    Rast3d_copy_to_xdr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 112
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_init_copy_from_xdr'):
    Rast3d_init_copy_from_xdr = _libs['grass_g3d.7.8'].Rast3d_init_copy_from_xdr
    Rast3d_init_copy_from_xdr.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_copy_from_xdr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 113
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_copy_from_xdr'):
    Rast3d_copy_from_xdr = _libs['grass_g3d.7.8'].Rast3d_copy_from_xdr
    Rast3d_copy_from_xdr.argtypes = [c_int, POINTER(None)]
    Rast3d_copy_from_xdr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 116
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_gradient_double'):
    Rast3d_gradient_double = _libs['grass_g3d.7.8'].Rast3d_gradient_double
    Rast3d_gradient_double.argtypes = [POINTER(RASTER3D_Array_double), POINTER(c_double), POINTER(RASTER3D_Array_double), POINTER(RASTER3D_Array_double), POINTER(RASTER3D_Array_double)]
    Rast3d_gradient_double.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 121
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_history'):
    Rast3d_write_history = _libs['grass_g3d.7.8'].Rast3d_write_history
    Rast3d_write_history.argtypes = [String, POINTER(struct_History)]
    Rast3d_write_history.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 122
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_history'):
    Rast3d_read_history = _libs['grass_g3d.7.8'].Rast3d_read_history
    Rast3d_read_history.argtypes = [String, String, POINTER(struct_History)]
    Rast3d_read_history.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 125
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_ints'):
    Rast3d_write_ints = _libs['grass_g3d.7.8'].Rast3d_write_ints
    Rast3d_write_ints.argtypes = [c_int, c_int, POINTER(c_int), c_int]
    Rast3d_write_ints.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 126
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_ints'):
    Rast3d_read_ints = _libs['grass_g3d.7.8'].Rast3d_read_ints
    Rast3d_read_ints.argtypes = [c_int, c_int, POINTER(c_int), c_int]
    Rast3d_read_ints.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 129
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_key_get_int'):
    Rast3d_key_get_int = _libs['grass_g3d.7.8'].Rast3d_key_get_int
    Rast3d_key_get_int.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_int)]
    Rast3d_key_get_int.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 130
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_key_get_double'):
    Rast3d_key_get_double = _libs['grass_g3d.7.8'].Rast3d_key_get_double
    Rast3d_key_get_double.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_double)]
    Rast3d_key_get_double.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 131
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_key_get_string'):
    Rast3d_key_get_string = _libs['grass_g3d.7.8'].Rast3d_key_get_string
    Rast3d_key_get_string.argtypes = [POINTER(struct_Key_Value), String, POINTER(POINTER(c_char))]
    Rast3d_key_get_string.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 132
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_key_get_value'):
    Rast3d_key_get_value = _libs['grass_g3d.7.8'].Rast3d_key_get_value
    Rast3d_key_get_value.argtypes = [POINTER(struct_Key_Value), String, String, String, c_int, c_int, POINTER(c_int)]
    Rast3d_key_get_value.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 134
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_key_set_int'):
    Rast3d_key_set_int = _libs['grass_g3d.7.8'].Rast3d_key_set_int
    Rast3d_key_set_int.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_int)]
    Rast3d_key_set_int.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 135
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_key_set_double'):
    Rast3d_key_set_double = _libs['grass_g3d.7.8'].Rast3d_key_set_double
    Rast3d_key_set_double.argtypes = [POINTER(struct_Key_Value), String, POINTER(c_double)]
    Rast3d_key_set_double.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 136
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_key_set_string'):
    Rast3d_key_set_string = _libs['grass_g3d.7.8'].Rast3d_key_set_string
    Rast3d_key_set_string.argtypes = [POINTER(struct_Key_Value), String, POINTER(POINTER(c_char))]
    Rast3d_key_set_string.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 137
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_key_set_value'):
    Rast3d_key_set_value = _libs['grass_g3d.7.8'].Rast3d_key_set_value
    Rast3d_key_set_value.argtypes = [POINTER(struct_Key_Value), String, String, String, c_int, c_int, POINTER(c_int)]
    Rast3d_key_set_value.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 140
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_long_encode'):
    Rast3d_long_encode = _libs['grass_g3d.7.8'].Rast3d_long_encode
    Rast3d_long_encode.argtypes = [POINTER(c_long), POINTER(c_ubyte), c_int]
    Rast3d_long_encode.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 141
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_long_decode'):
    Rast3d_long_decode = _libs['grass_g3d.7.8'].Rast3d_long_decode
    Rast3d_long_decode.argtypes = [POINTER(c_ubyte), POINTER(c_long), c_int, c_int]
    Rast3d_long_decode.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 144
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_make_mapset_map_directory'):
    Rast3d_make_mapset_map_directory = _libs['grass_g3d.7.8'].Rast3d_make_mapset_map_directory
    Rast3d_make_mapset_map_directory.argtypes = [String]
    Rast3d_make_mapset_map_directory.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 147
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_close'):
    Rast3d_mask_close = _libs['grass_g3d.7.8'].Rast3d_mask_close
    Rast3d_mask_close.argtypes = []
    Rast3d_mask_close.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 148
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_file_exists'):
    Rast3d_mask_file_exists = _libs['grass_g3d.7.8'].Rast3d_mask_file_exists
    Rast3d_mask_file_exists.argtypes = []
    Rast3d_mask_file_exists.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 149
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_open_old'):
    Rast3d_mask_open_old = _libs['grass_g3d.7.8'].Rast3d_mask_open_old
    Rast3d_mask_open_old.argtypes = []
    Rast3d_mask_open_old.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 150
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_reopen'):
    Rast3d_mask_reopen = _libs['grass_g3d.7.8'].Rast3d_mask_reopen
    Rast3d_mask_reopen.argtypes = [c_int]
    Rast3d_mask_reopen.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 151
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_is_masked'):
    Rast3d_is_masked = _libs['grass_g3d.7.8'].Rast3d_is_masked
    Rast3d_is_masked.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_is_masked.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 152
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_num'):
    Rast3d_mask_num = _libs['grass_g3d.7.8'].Rast3d_mask_num
    Rast3d_mask_num.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_mask_num.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 153
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_float'):
    Rast3d_mask_float = _libs['grass_g3d.7.8'].Rast3d_mask_float
    Rast3d_mask_float.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_float)]
    Rast3d_mask_float.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 154
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_double'):
    Rast3d_mask_double = _libs['grass_g3d.7.8'].Rast3d_mask_double
    Rast3d_mask_double.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_double)]
    Rast3d_mask_double.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 155
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_tile'):
    Rast3d_mask_tile = _libs['grass_g3d.7.8'].Rast3d_mask_tile
    Rast3d_mask_tile.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None), c_int]
    Rast3d_mask_tile.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 156
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_on'):
    Rast3d_mask_on = _libs['grass_g3d.7.8'].Rast3d_mask_on
    Rast3d_mask_on.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_mask_on.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 157
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_off'):
    Rast3d_mask_off = _libs['grass_g3d.7.8'].Rast3d_mask_off
    Rast3d_mask_off.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_mask_off.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 158
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_is_on'):
    Rast3d_mask_is_on = _libs['grass_g3d.7.8'].Rast3d_mask_is_on
    Rast3d_mask_is_on.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_mask_is_on.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 159
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_is_off'):
    Rast3d_mask_is_off = _libs['grass_g3d.7.8'].Rast3d_mask_is_off
    Rast3d_mask_is_off.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_mask_is_off.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 160
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_file'):
    Rast3d_mask_file = _libs['grass_g3d.7.8'].Rast3d_mask_file
    Rast3d_mask_file.argtypes = []
    Rast3d_mask_file.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 161
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_map_exists'):
    Rast3d_mask_map_exists = _libs['grass_g3d.7.8'].Rast3d_mask_map_exists
    Rast3d_mask_map_exists.argtypes = []
    Rast3d_mask_map_exists.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 164
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_d_select'):
    Rast3d_mask_d_select = _libs['grass_g3d.7.8'].Rast3d_mask_d_select
    Rast3d_mask_d_select.argtypes = [POINTER(DCELL), POINTER(d_Mask)]
    Rast3d_mask_d_select.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 165
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_mask_match_d_interval'):
    Rast3d_mask_match_d_interval = _libs['grass_g3d.7.8'].Rast3d_mask_match_d_interval
    Rast3d_mask_match_d_interval.argtypes = [DCELL, POINTER(d_Interval)]
    Rast3d_mask_match_d_interval.restype = DCELL

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 166
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_parse_vallist'):
    Rast3d_parse_vallist = _libs['grass_g3d.7.8'].Rast3d_parse_vallist
    Rast3d_parse_vallist.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(d_Mask))]
    Rast3d_parse_vallist.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 169
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_g3d_type2cell_type'):
    Rast3d_g3d_type2cell_type = _libs['grass_g3d.7.8'].Rast3d_g3d_type2cell_type
    Rast3d_g3d_type2cell_type.argtypes = [c_int]
    Rast3d_g3d_type2cell_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 170
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_copy_float2Double'):
    Rast3d_copy_float2Double = _libs['grass_g3d.7.8'].Rast3d_copy_float2Double
    Rast3d_copy_float2Double.argtypes = [POINTER(c_float), c_int, POINTER(c_double), c_int, c_int]
    Rast3d_copy_float2Double.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 171
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_copy_double2Float'):
    Rast3d_copy_double2Float = _libs['grass_g3d.7.8'].Rast3d_copy_double2Float
    Rast3d_copy_double2Float.argtypes = [POINTER(c_double), c_int, POINTER(c_float), c_int, c_int]
    Rast3d_copy_double2Float.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 172
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_copy_values'):
    Rast3d_copy_values = _libs['grass_g3d.7.8'].Rast3d_copy_values
    Rast3d_copy_values.argtypes = [POINTER(None), c_int, c_int, POINTER(None), c_int, c_int, c_int]
    Rast3d_copy_values.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 173
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_length'):
    Rast3d_length = _libs['grass_g3d.7.8'].Rast3d_length
    Rast3d_length.argtypes = [c_int]
    Rast3d_length.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 174
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_extern_length'):
    Rast3d_extern_length = _libs['grass_g3d.7.8'].Rast3d_extern_length
    Rast3d_extern_length.argtypes = [c_int]
    Rast3d_extern_length.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 177
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_is_null_value_num'):
    Rast3d_is_null_value_num = _libs['grass_g3d.7.8'].Rast3d_is_null_value_num
    Rast3d_is_null_value_num.argtypes = [POINTER(None), c_int]
    Rast3d_is_null_value_num.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 178
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_null_value'):
    Rast3d_set_null_value = _libs['grass_g3d.7.8'].Rast3d_set_null_value
    Rast3d_set_null_value.argtypes = [POINTER(None), c_int, c_int]
    Rast3d_set_null_value.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 181
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_open_new_param'):
    Rast3d_open_new_param = _libs['grass_g3d.7.8'].Rast3d_open_new_param
    Rast3d_open_new_param.argtypes = [String, c_int, c_int, POINTER(RASTER3D_Region), c_int, c_int, c_int, c_int, c_int, c_int]
    Rast3d_open_new_param.restype = POINTER(c_ubyte)
    Rast3d_open_new_param.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 183
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_open_cell_old_no_header'):
    Rast3d_open_cell_old_no_header = _libs['grass_g3d.7.8'].Rast3d_open_cell_old_no_header
    Rast3d_open_cell_old_no_header.argtypes = [String, String]
    Rast3d_open_cell_old_no_header.restype = POINTER(c_ubyte)
    Rast3d_open_cell_old_no_header.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 184
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_open_cell_old'):
    Rast3d_open_cell_old = _libs['grass_g3d.7.8'].Rast3d_open_cell_old
    Rast3d_open_cell_old.argtypes = [String, String, POINTER(RASTER3D_Region), c_int, c_int]
    Rast3d_open_cell_old.restype = POINTER(c_ubyte)
    Rast3d_open_cell_old.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 185
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_open_cell_new'):
    Rast3d_open_cell_new = _libs['grass_g3d.7.8'].Rast3d_open_cell_new
    Rast3d_open_cell_new.argtypes = [String, c_int, c_int, POINTER(RASTER3D_Region)]
    Rast3d_open_cell_new.restype = POINTER(c_ubyte)
    Rast3d_open_cell_new.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 186
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_open_new_opt_tile_size'):
    Rast3d_open_new_opt_tile_size = _libs['grass_g3d.7.8'].Rast3d_open_new_opt_tile_size
    Rast3d_open_new_opt_tile_size.argtypes = [String, c_int, POINTER(RASTER3D_Region), c_int, c_int]
    Rast3d_open_new_opt_tile_size.restype = POINTER(c_ubyte)
    Rast3d_open_new_opt_tile_size.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 189
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_standard3d_input_params'):
    Rast3d_set_standard3d_input_params = _libs['grass_g3d.7.8'].Rast3d_set_standard3d_input_params
    Rast3d_set_standard3d_input_params.argtypes = []
    Rast3d_set_standard3d_input_params.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 190
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_standard3d_params'):
    Rast3d_get_standard3d_params = _libs['grass_g3d.7.8'].Rast3d_get_standard3d_params
    Rast3d_get_standard3d_params.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_standard3d_params.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 192
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_window_params'):
    Rast3d_set_window_params = _libs['grass_g3d.7.8'].Rast3d_set_window_params
    Rast3d_set_window_params.argtypes = []
    Rast3d_set_window_params.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 193
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_window_params'):
    Rast3d_get_window_params = _libs['grass_g3d.7.8'].Rast3d_get_window_params
    Rast3d_get_window_params.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        Rast3d_get_window_params.restype = ReturnString
    else:
        Rast3d_get_window_params.restype = String
        Rast3d_get_window_params.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 196
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_range_update_from_tile'):
    Rast3d_range_update_from_tile = _libs['grass_g3d.7.8'].Rast3d_range_update_from_tile
    Rast3d_range_update_from_tile.argtypes = [POINTER(RASTER3D_Map), POINTER(None), c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int]
    Rast3d_range_update_from_tile.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 198
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_range'):
    Rast3d_read_range = _libs['grass_g3d.7.8'].Rast3d_read_range
    Rast3d_read_range.argtypes = [String, String, POINTER(struct_FPRange)]
    Rast3d_read_range.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 199
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_range_load'):
    Rast3d_range_load = _libs['grass_g3d.7.8'].Rast3d_range_load
    Rast3d_range_load.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_range_load.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 200
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_range_min_max'):
    Rast3d_range_min_max = _libs['grass_g3d.7.8'].Rast3d_range_min_max
    Rast3d_range_min_max.argtypes = [POINTER(RASTER3D_Map), POINTER(c_double), POINTER(c_double)]
    Rast3d_range_min_max.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 201
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_range_write'):
    Rast3d_range_write = _libs['grass_g3d.7.8'].Rast3d_range_write
    Rast3d_range_write.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_range_write.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 202
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_range_init'):
    Rast3d_range_init = _libs['grass_g3d.7.8'].Rast3d_range_init
    Rast3d_range_init.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_range_init.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 205
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_region_value'):
    Rast3d_get_region_value = _libs['grass_g3d.7.8'].Rast3d_get_region_value
    Rast3d_get_region_value.argtypes = [POINTER(RASTER3D_Map), c_double, c_double, c_double, POINTER(None), c_int]
    Rast3d_get_region_value.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 206
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_adjust_region'):
    Rast3d_adjust_region = _libs['grass_g3d.7.8'].Rast3d_adjust_region
    Rast3d_adjust_region.argtypes = [POINTER(RASTER3D_Region)]
    Rast3d_adjust_region.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 207
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_region_copy'):
    Rast3d_region_copy = _libs['grass_g3d.7.8'].Rast3d_region_copy
    Rast3d_region_copy.argtypes = [POINTER(RASTER3D_Region), POINTER(RASTER3D_Region)]
    Rast3d_region_copy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 208
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_incorporate2d_region'):
    Rast3d_incorporate2d_region = _libs['grass_g3d.7.8'].Rast3d_incorporate2d_region
    Rast3d_incorporate2d_region.argtypes = [POINTER(struct_Cell_head), POINTER(RASTER3D_Region)]
    Rast3d_incorporate2d_region.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 209
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_region_from_to_cell_head'):
    Rast3d_region_from_to_cell_head = _libs['grass_g3d.7.8'].Rast3d_region_from_to_cell_head
    Rast3d_region_from_to_cell_head.argtypes = [POINTER(struct_Cell_head), POINTER(RASTER3D_Region)]
    Rast3d_region_from_to_cell_head.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 210
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_adjust_region_res'):
    Rast3d_adjust_region_res = _libs['grass_g3d.7.8'].Rast3d_adjust_region_res
    Rast3d_adjust_region_res.argtypes = [POINTER(RASTER3D_Region)]
    Rast3d_adjust_region_res.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 211
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_extract2d_region'):
    Rast3d_extract2d_region = _libs['grass_g3d.7.8'].Rast3d_extract2d_region
    Rast3d_extract2d_region.argtypes = [POINTER(RASTER3D_Region), POINTER(struct_Cell_head)]
    Rast3d_extract2d_region.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 212
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_region_to_cell_head'):
    Rast3d_region_to_cell_head = _libs['grass_g3d.7.8'].Rast3d_region_to_cell_head
    Rast3d_region_to_cell_head.argtypes = [POINTER(RASTER3D_Region), POINTER(struct_Cell_head)]
    Rast3d_region_to_cell_head.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 213
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_region_map'):
    Rast3d_read_region_map = _libs['grass_g3d.7.8'].Rast3d_read_region_map
    Rast3d_read_region_map.argtypes = [String, String, POINTER(RASTER3D_Region)]
    Rast3d_read_region_map.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 214
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_is_valid_location'):
    Rast3d_is_valid_location = _libs['grass_g3d.7.8'].Rast3d_is_valid_location
    Rast3d_is_valid_location.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double]
    Rast3d_is_valid_location.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 215
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_location2coord'):
    Rast3d_location2coord = _libs['grass_g3d.7.8'].Rast3d_location2coord
    Rast3d_location2coord.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_location2coord.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 216
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_location2coord_double'):
    Rast3d_location2coord_double = _libs['grass_g3d.7.8'].Rast3d_location2coord_double
    Rast3d_location2coord_double.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Rast3d_location2coord_double.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 217
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_location2coord2'):
    Rast3d_location2coord2 = _libs['grass_g3d.7.8'].Rast3d_location2coord2
    Rast3d_location2coord2.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_location2coord2.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 218
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_coord2location'):
    Rast3d_coord2location = _libs['grass_g3d.7.8'].Rast3d_coord2location
    Rast3d_coord2location.argtypes = [POINTER(RASTER3D_Region), c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Rast3d_coord2location.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 220
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_nearest_neighbor'):
    Rast3d_nearest_neighbor = _libs['grass_g3d.7.8'].Rast3d_nearest_neighbor
    Rast3d_nearest_neighbor.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_nearest_neighbor.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 221
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_resampling_fun'):
    Rast3d_set_resampling_fun = _libs['grass_g3d.7.8'].Rast3d_set_resampling_fun
    Rast3d_set_resampling_fun.argtypes = [POINTER(RASTER3D_Map), CFUNCTYPE(UNCHECKED(None), )]
    Rast3d_set_resampling_fun.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 222
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_resampling_fun'):
    Rast3d_get_resampling_fun = _libs['grass_g3d.7.8'].Rast3d_get_resampling_fun
    Rast3d_get_resampling_fun.argtypes = [POINTER(RASTER3D_Map), POINTER(CFUNCTYPE(UNCHECKED(None), ))]
    Rast3d_get_resampling_fun.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 223
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_nearest_neighbor_fun_ptr'):
    Rast3d_get_nearest_neighbor_fun_ptr = _libs['grass_g3d.7.8'].Rast3d_get_nearest_neighbor_fun_ptr
    Rast3d_get_nearest_neighbor_fun_ptr.argtypes = [POINTER(CFUNCTYPE(UNCHECKED(None), ))]
    Rast3d_get_nearest_neighbor_fun_ptr.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 226
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_volume_a'):
    Rast3d_get_volume_a = _libs['grass_g3d.7.8'].Rast3d_get_volume_a
    Rast3d_get_volume_a.argtypes = [POINTER(None), (((c_double * 3) * 2) * 2) * 2, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_volume_a.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 227
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_volume'):
    Rast3d_get_volume = _libs['grass_g3d.7.8'].Rast3d_get_volume
    Rast3d_get_volume.argtypes = [POINTER(None), c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_volume.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 230
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_aligned_volume'):
    Rast3d_get_aligned_volume = _libs['grass_g3d.7.8'].Rast3d_get_aligned_volume
    Rast3d_get_aligned_volume.argtypes = [POINTER(None), c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_aligned_volume.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 232
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_make_aligned_volume_file'):
    Rast3d_make_aligned_volume_file = _libs['grass_g3d.7.8'].Rast3d_make_aligned_volume_file
    Rast3d_make_aligned_volume_file.argtypes = [POINTER(None), String, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int]
    Rast3d_make_aligned_volume_file.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 235
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_value'):
    Rast3d_get_value = _libs['grass_g3d.7.8'].Rast3d_get_value
    Rast3d_get_value.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_value.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 236
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_float'):
    Rast3d_get_float = _libs['grass_g3d.7.8'].Rast3d_get_float
    Rast3d_get_float.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_get_float.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 237
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_double'):
    Rast3d_get_double = _libs['grass_g3d.7.8'].Rast3d_get_double
    Rast3d_get_double.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_get_double.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 238
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_window_value'):
    Rast3d_get_window_value = _libs['grass_g3d.7.8'].Rast3d_get_window_value
    Rast3d_get_window_value.argtypes = [POINTER(RASTER3D_Map), c_double, c_double, c_double, POINTER(None), c_int]
    Rast3d_get_window_value.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 241
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_window_ptr'):
    Rast3d_window_ptr = _libs['grass_g3d.7.8'].Rast3d_window_ptr
    Rast3d_window_ptr.argtypes = []
    Rast3d_window_ptr.restype = POINTER(RASTER3D_Region)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 242
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_window'):
    Rast3d_set_window = _libs['grass_g3d.7.8'].Rast3d_set_window
    Rast3d_set_window.argtypes = [POINTER(RASTER3D_Region)]
    Rast3d_set_window.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 243
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_window_map'):
    Rast3d_set_window_map = _libs['grass_g3d.7.8'].Rast3d_set_window_map
    Rast3d_set_window_map.argtypes = [POINTER(RASTER3D_Map), POINTER(RASTER3D_Region)]
    Rast3d_set_window_map.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 244
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_window'):
    Rast3d_get_window = _libs['grass_g3d.7.8'].Rast3d_get_window
    Rast3d_get_window.argtypes = [POINTER(RASTER3D_Region)]
    Rast3d_get_window.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 247
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_use_window_params'):
    Rast3d_use_window_params = _libs['grass_g3d.7.8'].Rast3d_use_window_params
    Rast3d_use_window_params.argtypes = []
    Rast3d_use_window_params.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 248
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_window'):
    Rast3d_read_window = _libs['grass_g3d.7.8'].Rast3d_read_window
    Rast3d_read_window.argtypes = [POINTER(RASTER3D_Region), String]
    Rast3d_read_window.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 252
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_block_nocache'):
    Rast3d_get_block_nocache = _libs['grass_g3d.7.8'].Rast3d_get_block_nocache
    Rast3d_get_block_nocache.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_block_nocache.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 254
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_block'):
    Rast3d_get_block = _libs['grass_g3d.7.8'].Rast3d_get_block
    Rast3d_get_block.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_block.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 257
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_header'):
    Rast3d_read_header = _libs['grass_g3d.7.8'].Rast3d_read_header
    Rast3d_read_header.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(POINTER(c_char)), POINTER(c_int), POINTER(c_int)]
    Rast3d_read_header.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 261
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_header'):
    Rast3d_write_header = _libs['grass_g3d.7.8'].Rast3d_write_header
    Rast3d_write_header.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_double, c_double, c_double, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, String, c_int, c_int]
    Rast3d_write_header.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 265
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_rewrite_header'):
    Rast3d_rewrite_header = _libs['grass_g3d.7.8'].Rast3d_rewrite_header
    Rast3d_rewrite_header.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_rewrite_header.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 266
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_cache_size_encode'):
    Rast3d_cache_size_encode = _libs['grass_g3d.7.8'].Rast3d_cache_size_encode
    Rast3d_cache_size_encode.argtypes = [c_int, c_int]
    Rast3d_cache_size_encode.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 267
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d__compute_cache_size'):
    Rast3d__compute_cache_size = _libs['grass_g3d.7.8'].Rast3d__compute_cache_size
    Rast3d__compute_cache_size.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d__compute_cache_size.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 268
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_fill_header'):
    Rast3d_fill_header = _libs['grass_g3d.7.8'].Rast3d_fill_header
    Rast3d_fill_header.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_double, c_double, c_double, String, c_int, c_int]
    Rast3d_fill_header.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 273
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_coords_map'):
    Rast3d_get_coords_map = _libs['grass_g3d.7.8'].Rast3d_get_coords_map
    Rast3d_get_coords_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_coords_map.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 274
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_coords_map_window'):
    Rast3d_get_coords_map_window = _libs['grass_g3d.7.8'].Rast3d_get_coords_map_window
    Rast3d_get_coords_map_window.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_coords_map_window.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 275
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_nof_tiles_map'):
    Rast3d_get_nof_tiles_map = _libs['grass_g3d.7.8'].Rast3d_get_nof_tiles_map
    Rast3d_get_nof_tiles_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_nof_tiles_map.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 276
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_region_map'):
    Rast3d_get_region_map = _libs['grass_g3d.7.8'].Rast3d_get_region_map
    Rast3d_get_region_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Rast3d_get_region_map.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 278
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_window_map'):
    Rast3d_get_window_map = _libs['grass_g3d.7.8'].Rast3d_get_window_map
    Rast3d_get_window_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Rast3d_get_window_map.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 280
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_tile_dimensions_map'):
    Rast3d_get_tile_dimensions_map = _libs['grass_g3d.7.8'].Rast3d_get_tile_dimensions_map
    Rast3d_get_tile_dimensions_map.argtypes = [POINTER(RASTER3D_Map), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_get_tile_dimensions_map.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 281
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile_type_map'):
    Rast3d_tile_type_map = _libs['grass_g3d.7.8'].Rast3d_tile_type_map
    Rast3d_tile_type_map.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_tile_type_map.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 282
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_file_type_map'):
    Rast3d_file_type_map = _libs['grass_g3d.7.8'].Rast3d_file_type_map
    Rast3d_file_type_map.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_file_type_map.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 283
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile_precision_map'):
    Rast3d_tile_precision_map = _libs['grass_g3d.7.8'].Rast3d_tile_precision_map
    Rast3d_tile_precision_map.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_tile_precision_map.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 284
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile_use_cache_map'):
    Rast3d_tile_use_cache_map = _libs['grass_g3d.7.8'].Rast3d_tile_use_cache_map
    Rast3d_tile_use_cache_map.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_tile_use_cache_map.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 285
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_print_header'):
    Rast3d_print_header = _libs['grass_g3d.7.8'].Rast3d_print_header
    Rast3d_print_header.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_print_header.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 286
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_region_struct_map'):
    Rast3d_get_region_struct_map = _libs['grass_g3d.7.8'].Rast3d_get_region_struct_map
    Rast3d_get_region_struct_map.argtypes = [POINTER(RASTER3D_Map), POINTER(RASTER3D_Region)]
    Rast3d_get_region_struct_map.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 287
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_unit'):
    Rast3d_get_unit = _libs['grass_g3d.7.8'].Rast3d_get_unit
    Rast3d_get_unit.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_get_unit.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 288
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_vertical_unit2'):
    Rast3d_get_vertical_unit2 = _libs['grass_g3d.7.8'].Rast3d_get_vertical_unit2
    Rast3d_get_vertical_unit2.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_get_vertical_unit2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 289
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_vertical_unit'):
    Rast3d_get_vertical_unit = _libs['grass_g3d.7.8'].Rast3d_get_vertical_unit
    Rast3d_get_vertical_unit.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_get_vertical_unit.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 290
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_unit'):
    Rast3d_set_unit = _libs['grass_g3d.7.8'].Rast3d_set_unit
    Rast3d_set_unit.argtypes = [POINTER(RASTER3D_Map), String]
    Rast3d_set_unit.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 291
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_vertical_unit'):
    Rast3d_set_vertical_unit = _libs['grass_g3d.7.8'].Rast3d_set_vertical_unit
    Rast3d_set_vertical_unit.argtypes = [POINTER(RASTER3D_Map), String]
    Rast3d_set_vertical_unit.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 292
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_vertical_unit2'):
    Rast3d_set_vertical_unit2 = _libs['grass_g3d.7.8'].Rast3d_set_vertical_unit2
    Rast3d_set_vertical_unit2.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_set_vertical_unit2.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 295
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_flush_index'):
    Rast3d_flush_index = _libs['grass_g3d.7.8'].Rast3d_flush_index
    Rast3d_flush_index.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_flush_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 296
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_init_index'):
    Rast3d_init_index = _libs['grass_g3d.7.8'].Rast3d_init_index
    Rast3d_init_index.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_init_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 299
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_retile'):
    Rast3d_retile = _libs['grass_g3d.7.8'].Rast3d_retile
    Rast3d_retile.argtypes = [POINTER(None), String, c_int, c_int, c_int]
    Rast3d_retile.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 302
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_rle_count_only'):
    Rast3d_rle_count_only = _libs['grass_g3d.7.8'].Rast3d_rle_count_only
    Rast3d_rle_count_only.argtypes = [String, c_int, c_int]
    Rast3d_rle_count_only.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 303
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_rle_encode'):
    Rast3d_rle_encode = _libs['grass_g3d.7.8'].Rast3d_rle_encode
    Rast3d_rle_encode.argtypes = [String, String, c_int, c_int]
    Rast3d_rle_encode.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 304
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_rle_decode'):
    Rast3d_rle_decode = _libs['grass_g3d.7.8'].Rast3d_rle_decode
    Rast3d_rle_decode.argtypes = [String, String, c_int, c_int, POINTER(c_int), POINTER(c_int)]
    Rast3d_rle_decode.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 307
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_alloc_tiles_type'):
    Rast3d_alloc_tiles_type = _libs['grass_g3d.7.8'].Rast3d_alloc_tiles_type
    Rast3d_alloc_tiles_type.argtypes = [POINTER(RASTER3D_Map), c_int, c_int]
    Rast3d_alloc_tiles_type.restype = POINTER(c_ubyte)
    Rast3d_alloc_tiles_type.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 308
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_alloc_tiles'):
    Rast3d_alloc_tiles = _libs['grass_g3d.7.8'].Rast3d_alloc_tiles
    Rast3d_alloc_tiles.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_alloc_tiles.restype = POINTER(c_ubyte)
    Rast3d_alloc_tiles.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 309
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_free_tiles'):
    Rast3d_free_tiles = _libs['grass_g3d.7.8'].Rast3d_free_tiles
    Rast3d_free_tiles.argtypes = [POINTER(None)]
    Rast3d_free_tiles.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 312
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_tile_ptr'):
    Rast3d_get_tile_ptr = _libs['grass_g3d.7.8'].Rast3d_get_tile_ptr
    Rast3d_get_tile_ptr.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_get_tile_ptr.restype = POINTER(c_ubyte)
    Rast3d_get_tile_ptr.errcheck = lambda v,*a : cast(v, c_void_p)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 313
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile_load'):
    Rast3d_tile_load = _libs['grass_g3d.7.8'].Rast3d_tile_load
    Rast3d_tile_load.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_tile_load.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 314
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d__remove_tile'):
    Rast3d__remove_tile = _libs['grass_g3d.7.8'].Rast3d__remove_tile
    Rast3d__remove_tile.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d__remove_tile.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 315
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_float_region'):
    Rast3d_get_float_region = _libs['grass_g3d.7.8'].Rast3d_get_float_region
    Rast3d_get_float_region.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_get_float_region.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 316
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_double_region'):
    Rast3d_get_double_region = _libs['grass_g3d.7.8'].Rast3d_get_double_region
    Rast3d_get_double_region.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_get_double_region.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 317
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_get_value_region'):
    Rast3d_get_value_region = _libs['grass_g3d.7.8'].Rast3d_get_value_region
    Rast3d_get_value_region.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_get_value_region.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 320
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_compute_optimal_tile_dimension'):
    Rast3d_compute_optimal_tile_dimension = _libs['grass_g3d.7.8'].Rast3d_compute_optimal_tile_dimension
    Rast3d_compute_optimal_tile_dimension.argtypes = [POINTER(RASTER3D_Region), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), c_int]
    Rast3d_compute_optimal_tile_dimension.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 321
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile_index2tile'):
    Rast3d_tile_index2tile = _libs['grass_g3d.7.8'].Rast3d_tile_index2tile
    Rast3d_tile_index2tile.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_tile_index2tile.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 322
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile2tile_index'):
    Rast3d_tile2tile_index = _libs['grass_g3d.7.8'].Rast3d_tile2tile_index
    Rast3d_tile2tile_index.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_tile2tile_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 323
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile_coord_origin'):
    Rast3d_tile_coord_origin = _libs['grass_g3d.7.8'].Rast3d_tile_coord_origin
    Rast3d_tile_coord_origin.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_tile_coord_origin.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 324
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile_index_origin'):
    Rast3d_tile_index_origin = _libs['grass_g3d.7.8'].Rast3d_tile_index_origin
    Rast3d_tile_index_origin.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_tile_index_origin.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 325
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_coord2tile_coord'):
    Rast3d_coord2tile_coord = _libs['grass_g3d.7.8'].Rast3d_coord2tile_coord
    Rast3d_coord2tile_coord.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_coord2tile_coord.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 327
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_coord2tile_index'):
    Rast3d_coord2tile_index = _libs['grass_g3d.7.8'].Rast3d_coord2tile_index
    Rast3d_coord2tile_index.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(c_int), POINTER(c_int)]
    Rast3d_coord2tile_index.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 328
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_coord_in_range'):
    Rast3d_coord_in_range = _libs['grass_g3d.7.8'].Rast3d_coord_in_range
    Rast3d_coord_in_range.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_coord_in_range.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 329
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile_index_in_range'):
    Rast3d_tile_index_in_range = _libs['grass_g3d.7.8'].Rast3d_tile_index_in_range
    Rast3d_tile_index_in_range.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_tile_index_in_range.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 330
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_tile_in_range'):
    Rast3d_tile_in_range = _libs['grass_g3d.7.8'].Rast3d_tile_in_range
    Rast3d_tile_in_range.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int]
    Rast3d_tile_in_range.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 331
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_compute_clipped_tile_dimensions'):
    Rast3d_compute_clipped_tile_dimensions = _libs['grass_g3d.7.8'].Rast3d_compute_clipped_tile_dimensions
    Rast3d_compute_clipped_tile_dimensions.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Rast3d_compute_clipped_tile_dimensions.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 335
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_null_tile_type'):
    Rast3d_set_null_tile_type = _libs['grass_g3d.7.8'].Rast3d_set_null_tile_type
    Rast3d_set_null_tile_type.argtypes = [POINTER(RASTER3D_Map), POINTER(None), c_int]
    Rast3d_set_null_tile_type.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 336
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_set_null_tile'):
    Rast3d_set_null_tile = _libs['grass_g3d.7.8'].Rast3d_set_null_tile
    Rast3d_set_null_tile.argtypes = [POINTER(RASTER3D_Map), POINTER(None)]
    Rast3d_set_null_tile.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 339
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_tile'):
    Rast3d_read_tile = _libs['grass_g3d.7.8'].Rast3d_read_tile
    Rast3d_read_tile.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None), c_int]
    Rast3d_read_tile.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 340
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_tile_float'):
    Rast3d_read_tile_float = _libs['grass_g3d.7.8'].Rast3d_read_tile_float
    Rast3d_read_tile_float.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None)]
    Rast3d_read_tile_float.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 341
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_read_tile_double'):
    Rast3d_read_tile_double = _libs['grass_g3d.7.8'].Rast3d_read_tile_double
    Rast3d_read_tile_double.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None)]
    Rast3d_read_tile_double.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 342
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_lock_tile'):
    Rast3d_lock_tile = _libs['grass_g3d.7.8'].Rast3d_lock_tile
    Rast3d_lock_tile.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_lock_tile.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 343
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_unlock_tile'):
    Rast3d_unlock_tile = _libs['grass_g3d.7.8'].Rast3d_unlock_tile
    Rast3d_unlock_tile.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_unlock_tile.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 344
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_unlock_all'):
    Rast3d_unlock_all = _libs['grass_g3d.7.8'].Rast3d_unlock_all
    Rast3d_unlock_all.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_unlock_all.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 345
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_autolock_on'):
    Rast3d_autolock_on = _libs['grass_g3d.7.8'].Rast3d_autolock_on
    Rast3d_autolock_on.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_autolock_on.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 346
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_autolock_off'):
    Rast3d_autolock_off = _libs['grass_g3d.7.8'].Rast3d_autolock_off
    Rast3d_autolock_off.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_autolock_off.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 347
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_min_unlocked'):
    Rast3d_min_unlocked = _libs['grass_g3d.7.8'].Rast3d_min_unlocked
    Rast3d_min_unlocked.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_min_unlocked.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 348
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_begin_cycle'):
    Rast3d_begin_cycle = _libs['grass_g3d.7.8'].Rast3d_begin_cycle
    Rast3d_begin_cycle.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_begin_cycle.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 349
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_end_cycle'):
    Rast3d_end_cycle = _libs['grass_g3d.7.8'].Rast3d_end_cycle
    Rast3d_end_cycle.argtypes = [POINTER(RASTER3D_Map)]
    Rast3d_end_cycle.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 352
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_tile'):
    Rast3d_write_tile = _libs['grass_g3d.7.8'].Rast3d_write_tile
    Rast3d_write_tile.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None), c_int]
    Rast3d_write_tile.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 353
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_tile_float'):
    Rast3d_write_tile_float = _libs['grass_g3d.7.8'].Rast3d_write_tile_float
    Rast3d_write_tile_float.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None)]
    Rast3d_write_tile_float.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 354
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_tile_double'):
    Rast3d_write_tile_double = _libs['grass_g3d.7.8'].Rast3d_write_tile_double
    Rast3d_write_tile_double.argtypes = [POINTER(RASTER3D_Map), c_int, POINTER(None)]
    Rast3d_write_tile_double.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 355
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_flush_tile'):
    Rast3d_flush_tile = _libs['grass_g3d.7.8'].Rast3d_flush_tile
    Rast3d_flush_tile.argtypes = [POINTER(RASTER3D_Map), c_int]
    Rast3d_flush_tile.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 356
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_flush_tile_cube'):
    Rast3d_flush_tile_cube = _libs['grass_g3d.7.8'].Rast3d_flush_tile_cube
    Rast3d_flush_tile_cube.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int]
    Rast3d_flush_tile_cube.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 357
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_flush_tiles_in_cube'):
    Rast3d_flush_tiles_in_cube = _libs['grass_g3d.7.8'].Rast3d_flush_tiles_in_cube
    Rast3d_flush_tiles_in_cube.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_int, c_int, c_int]
    Rast3d_flush_tiles_in_cube.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 358
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_put_float'):
    Rast3d_put_float = _libs['grass_g3d.7.8'].Rast3d_put_float
    Rast3d_put_float.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_float]
    Rast3d_put_float.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 359
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_put_double'):
    Rast3d_put_double = _libs['grass_g3d.7.8'].Rast3d_put_double
    Rast3d_put_double.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, c_double]
    Rast3d_put_double.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 360
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_put_value'):
    Rast3d_put_value = _libs['grass_g3d.7.8'].Rast3d_put_value
    Rast3d_put_value.argtypes = [POINTER(RASTER3D_Map), c_int, c_int, c_int, POINTER(None), c_int]
    Rast3d_put_value.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/raster3d.h: 363
if hasattr(_libs['grass_g3d.7.8'], 'Rast3d_write_ascii'):
    Rast3d_write_ascii = _libs['grass_g3d.7.8'].Rast3d_write_ascii
    Rast3d_write_ascii.argtypes = [POINTER(None), String]
    Rast3d_write_ascii.restype = None

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 7
try:
    RASTER3D_MAP_VERSION = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 12
try:
    RASTER3D_TILE_SAME_AS_FILE = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 14
try:
    RASTER3D_NO_COMPRESSION = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 15
try:
    RASTER3D_COMPRESSION = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 17
try:
    RASTER3D_MAX_PRECISION = (-1)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 19
try:
    RASTER3D_NO_CACHE = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 20
try:
    RASTER3D_USE_CACHE_DEFAULT = (-1)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 21
try:
    RASTER3D_USE_CACHE_X = (-2)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 22
try:
    RASTER3D_USE_CACHE_Y = (-3)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 23
try:
    RASTER3D_USE_CACHE_Z = (-4)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 24
try:
    RASTER3D_USE_CACHE_XY = (-5)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 25
try:
    RASTER3D_USE_CACHE_XZ = (-6)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 26
try:
    RASTER3D_USE_CACHE_YZ = (-7)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 27
try:
    RASTER3D_USE_CACHE_XYZ = (-8)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 29
try:
    RASTER3D_DEFAULT_WINDOW = NULL
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 31
try:
    RASTER3D_DIRECTORY = 'grid3'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 32
try:
    RASTER3D_CELL_ELEMENT = 'cell'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 33
try:
    RASTER3D_CATS_ELEMENT = 'cats'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 34
try:
    RASTER3D_RANGE_ELEMENT = 'range'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 35
try:
    RASTER3D_HEADER_ELEMENT = 'cellhd'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 36
try:
    RASTER3D_HISTORY_ELEMENT = 'hist'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 37
try:
    RASTER3D_COLOR_ELEMENT = 'color'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 38
try:
    RASTER3D_COLOR2_DIRECTORY = 'colr2'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 39
try:
    RASTER3D_MASK_MAP = 'RASTER3D_MASK'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 40
try:
    RASTER3D_WINDOW_ELEMENT = 'WIND3'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 41
try:
    RASTER3D_DEFAULT_WINDOW_ELEMENT = 'DEFAULT_WIND3'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 42
try:
    RASTER3D_WINDOW_DATABASE = 'windows3d'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 43
try:
    RASTER3D_PERMANENT_MAPSET = 'PERMANENT'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 268
def RASTER3D_ARRAY_ACCESS(arr, x, y, z):
    return ((arr.contents.array) [((((((arr.contents.sx).value) * ((arr.contents.sy).value)) * z) + (((arr.contents.sx).value) * y)) + x)])

RASTER3D_Map = struct_RASTER3D_Map # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 72

_d_interval = struct__d_interval # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 240

_d_mask = struct__d_mask # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\raster3d.h: 250

# No inserted files

