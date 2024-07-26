'''Wrapper for temporal.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_temporal.7.8 C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/temporal.h -o OBJ.x86_64-w64-mingw32/temporal.py

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

_libs["grass_temporal.7.8"] = load_library("grass_temporal.7.8")

# 1 libraries
# End libraries

# No modules

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/datetime.h: 27
class struct_DateTime(Structure):
    pass

struct_DateTime.__slots__ = [
    'mode',
    '_from',
    'to',
    'fracsec',
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'second',
    'positive',
    'tz',
]
struct_DateTime._fields_ = [
    ('mode', c_int),
    ('_from', c_int),
    ('to', c_int),
    ('fracsec', c_int),
    ('year', c_int),
    ('month', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('minute', c_int),
    ('second', c_double),
    ('positive', c_int),
    ('tz', c_int),
]

DateTime = struct_DateTime # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/datetime.h: 27

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 582
class struct_TimeStamp(Structure):
    pass

struct_TimeStamp.__slots__ = [
    'dt',
    'count',
]
struct_TimeStamp._fields_ = [
    ('dt', DateTime * 2),
    ('count', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dbmi.h: 304
class struct__db_connection(Structure):
    pass

struct__db_connection.__slots__ = [
    'driverName',
    'hostName',
    'databaseName',
    'schemaName',
    'port',
    'user',
    'password',
    'keycol',
    'group',
]
struct__db_connection._fields_ = [
    ('driverName', String),
    ('hostName', String),
    ('databaseName', String),
    ('schemaName', String),
    ('port', String),
    ('user', String),
    ('password', String),
    ('keycol', String),
    ('group', String),
]

dbConnection = struct__db_connection # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dbmi.h: 304

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 14
if hasattr(_libs['grass_temporal.7.8'], 'tgis_set_connection'):
    tgis_set_connection = _libs['grass_temporal.7.8'].tgis_set_connection
    tgis_set_connection.argtypes = [POINTER(dbConnection)]
    tgis_set_connection.restype = c_int

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 15
if hasattr(_libs['grass_temporal.7.8'], 'tgis_get_connection'):
    tgis_get_connection = _libs['grass_temporal.7.8'].tgis_get_connection
    tgis_get_connection.argtypes = [POINTER(dbConnection)]
    tgis_get_connection.restype = c_int

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 16
if hasattr(_libs['grass_temporal.7.8'], 'tgis_get_default_driver_name'):
    tgis_get_default_driver_name = _libs['grass_temporal.7.8'].tgis_get_default_driver_name
    tgis_get_default_driver_name.argtypes = []
    tgis_get_default_driver_name.restype = c_char_p

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 17
if hasattr(_libs['grass_temporal.7.8'], 'tgis_get_default_database_name'):
    tgis_get_default_database_name = _libs['grass_temporal.7.8'].tgis_get_default_database_name
    tgis_get_default_database_name.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        tgis_get_default_database_name.restype = ReturnString
    else:
        tgis_get_default_database_name.restype = String
        tgis_get_default_database_name.errcheck = ReturnString

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 18
if hasattr(_libs['grass_temporal.7.8'], 'tgis_get_driver_name'):
    tgis_get_driver_name = _libs['grass_temporal.7.8'].tgis_get_driver_name
    tgis_get_driver_name.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        tgis_get_driver_name.restype = ReturnString
    else:
        tgis_get_driver_name.restype = String
        tgis_get_driver_name.errcheck = ReturnString

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 19
if hasattr(_libs['grass_temporal.7.8'], 'tgis_get_database_name'):
    tgis_get_database_name = _libs['grass_temporal.7.8'].tgis_get_database_name
    tgis_get_database_name.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        tgis_get_database_name.restype = ReturnString
    else:
        tgis_get_database_name.restype = String
        tgis_get_database_name.errcheck = ReturnString

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 20
if hasattr(_libs['grass_temporal.7.8'], 'tgis_get_mapset_driver_name'):
    tgis_get_mapset_driver_name = _libs['grass_temporal.7.8'].tgis_get_mapset_driver_name
    tgis_get_mapset_driver_name.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        tgis_get_mapset_driver_name.restype = ReturnString
    else:
        tgis_get_mapset_driver_name.restype = String
        tgis_get_mapset_driver_name.errcheck = ReturnString

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 21
if hasattr(_libs['grass_temporal.7.8'], 'tgis_get_mapset_database_name'):
    tgis_get_mapset_database_name = _libs['grass_temporal.7.8'].tgis_get_mapset_database_name
    tgis_get_mapset_database_name.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        tgis_get_mapset_database_name.restype = ReturnString
    else:
        tgis_get_mapset_database_name.restype = String
        tgis_get_mapset_database_name.errcheck = ReturnString

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 22
if hasattr(_libs['grass_temporal.7.8'], 'tgis_set_default_connection'):
    tgis_set_default_connection = _libs['grass_temporal.7.8'].tgis_set_default_connection
    tgis_set_default_connection.argtypes = []
    tgis_set_default_connection.restype = c_int

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 49
class struct__tgisMap(Structure):
    pass

struct__tgisMap.__slots__ = [
    'name',
    'mapset',
    'ts',
]
struct__tgisMap._fields_ = [
    ('name', String),
    ('mapset', String),
    ('ts', struct_TimeStamp),
]

tgisMap = struct__tgisMap # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 49

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 71
class struct__tgisMapList(Structure):
    pass

struct__tgisMapList.__slots__ = [
    'values',
    'n_values',
    'alloc_values',
]
struct__tgisMapList._fields_ = [
    ('values', POINTER(POINTER(tgisMap))),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

tgisMapList = struct__tgisMapList # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 71

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 74
if hasattr(_libs['grass_temporal.7.8'], 'tgis_init_map_list'):
    tgis_init_map_list = _libs['grass_temporal.7.8'].tgis_init_map_list
    tgis_init_map_list.argtypes = [POINTER(tgisMapList)]
    tgis_init_map_list.restype = None

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 75
if hasattr(_libs['grass_temporal.7.8'], 'tgis_free_map_list'):
    tgis_free_map_list = _libs['grass_temporal.7.8'].tgis_free_map_list
    tgis_free_map_list.argtypes = [POINTER(tgisMapList)]
    tgis_free_map_list.restype = None

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 76
if hasattr(_libs['grass_temporal.7.8'], 'tgis_new_map_list'):
    tgis_new_map_list = _libs['grass_temporal.7.8'].tgis_new_map_list
    tgis_new_map_list.argtypes = []
    tgis_new_map_list.restype = POINTER(tgisMapList)

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 78
if hasattr(_libs['grass_temporal.7.8'], 'tgis_map_list_insert'):
    tgis_map_list_insert = _libs['grass_temporal.7.8'].tgis_map_list_insert
    tgis_map_list_insert.argtypes = [POINTER(tgisMapList), String, String, POINTER(struct_TimeStamp)]
    tgis_map_list_insert.restype = None

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 80
if hasattr(_libs['grass_temporal.7.8'], 'tgis_map_list_add'):
    tgis_map_list_add = _libs['grass_temporal.7.8'].tgis_map_list_add
    tgis_map_list_add.argtypes = [POINTER(tgisMapList), POINTER(tgisMap)]
    tgis_map_list_add.restype = None

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 103
class struct__tgisExtent(Structure):
    pass

struct__tgisExtent.__slots__ = [
    'start',
    'end',
    'has_end',
    'north',
    'south',
    'east',
    'west',
    'top',
    'bottom',
]
struct__tgisExtent._fields_ = [
    ('start', c_double),
    ('end', c_double),
    ('has_end', c_char),
    ('north', c_double),
    ('south', c_double),
    ('east', c_double),
    ('west', c_double),
    ('top', c_double),
    ('bottom', c_double),
]

tgisExtent = struct__tgisExtent # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 103

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 133
class struct__tgisDataset(Structure):
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 128
class struct__tgisDatasetList(Structure):
    pass

struct__tgisDatasetList.__slots__ = [
    'values',
    'n_values',
    'alloc_values',
]
struct__tgisDatasetList._fields_ = [
    ('values', POINTER(POINTER(struct__tgisDataset))),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

tgisDatasetList = struct__tgisDatasetList # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 128

struct__tgisDataset.__slots__ = [
    'name',
    'mapset',
    'creator',
    'creation_time',
    'temporal_type',
    'ts',
    'extent',
    'metadata',
    'dataset_type',
    'is_stds',
    'next',
    'prev',
    'equal',
    'follows',
    'precedes',
    'overlaps',
    'overlapped',
    'during',
    'contains',
    'starts',
    'started',
    'finishes',
    'finished',
    'equivalent',
    'cover',
    'covered',
    'overlap',
    '_in',
    'contain',
    'meet',
]
struct__tgisDataset._fields_ = [
    ('name', String),
    ('mapset', String),
    ('creator', String),
    ('creation_time', DateTime),
    ('temporal_type', c_char),
    ('ts', struct_TimeStamp),
    ('extent', tgisExtent),
    ('metadata', POINTER(None)),
    ('dataset_type', c_char),
    ('is_stds', c_char),
    ('next', POINTER(struct__tgisDataset)),
    ('prev', POINTER(struct__tgisDataset)),
    ('equal', tgisDatasetList),
    ('follows', tgisDatasetList),
    ('precedes', tgisDatasetList),
    ('overlaps', tgisDatasetList),
    ('overlapped', tgisDatasetList),
    ('during', tgisDatasetList),
    ('contains', tgisDatasetList),
    ('starts', tgisDatasetList),
    ('started', tgisDatasetList),
    ('finishes', tgisDatasetList),
    ('finished', tgisDatasetList),
    ('equivalent', tgisDatasetList),
    ('cover', tgisDatasetList),
    ('covered', tgisDatasetList),
    ('overlap', tgisDatasetList),
    ('_in', tgisDatasetList),
    ('contain', tgisDatasetList),
    ('meet', tgisDatasetList),
]

tgisDataset = struct__tgisDataset # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 174

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 178
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_init_dataset_list'):
        continue
    tgis_init_dataset_list = _lib.tgis_init_dataset_list
    tgis_init_dataset_list.argtypes = [POINTER(tgisDatasetList)]
    tgis_init_dataset_list.restype = None
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 179
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_free_dataset_list'):
        continue
    tgis_free_dataset_list = _lib.tgis_free_dataset_list
    tgis_free_dataset_list.argtypes = [POINTER(tgisDatasetList)]
    tgis_free_dataset_list.restype = None
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 180
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_new_dataset_list'):
        continue
    tgis_new_dataset_list = _lib.tgis_new_dataset_list
    tgis_new_dataset_list.argtypes = []
    tgis_new_dataset_list.restype = POINTER(tgisDatasetList)
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 182
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_dataset_list_insert'):
        continue
    tgis_dataset_list_insert = _lib.tgis_dataset_list_insert
    tgis_dataset_list_insert.argtypes = [POINTER(tgisDatasetList), String, String, String, POINTER(DateTime), c_char, POINTER(struct_TimeStamp), POINTER(tgisExtent), POINTER(None), c_char, c_char]
    tgis_dataset_list_insert.restype = None
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 187
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_dataset_list_add'):
        continue
    tgis_dataset_list_add = _lib.tgis_dataset_list_add
    tgis_dataset_list_add.argtypes = [POINTER(tgisDataset)]
    tgis_dataset_list_add.restype = None
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 191
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_build_topology'):
        continue
    tgis_build_topology = _lib.tgis_build_topology
    tgis_build_topology.argtypes = [POINTER(tgisDatasetList), c_char]
    tgis_build_topology.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 194
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_build_topology2'):
        continue
    tgis_build_topology2 = _lib.tgis_build_topology2
    tgis_build_topology2.argtypes = [POINTER(tgisDatasetList), POINTER(tgisDatasetList), c_char]
    tgis_build_topology2.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 202
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_create_stds'):
        continue
    tgis_create_stds = _lib.tgis_create_stds
    tgis_create_stds.argtypes = [String, c_char, c_char, String, String, String, String]
    tgis_create_stds.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 206
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_modify_stds'):
        continue
    tgis_modify_stds = _lib.tgis_modify_stds
    tgis_modify_stds.argtypes = [String, c_char, String, String, String, String]
    tgis_modify_stds.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 211
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_remove_stds'):
        continue
    tgis_remove_stds = _lib.tgis_remove_stds
    tgis_remove_stds.argtypes = [String, c_char, c_char]
    tgis_remove_stds.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 214
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_update_stds'):
        continue
    tgis_update_stds = _lib.tgis_update_stds
    tgis_update_stds.argtypes = [String, c_char]
    tgis_update_stds.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 218
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_register_map'):
        continue
    tgis_register_map = _lib.tgis_register_map
    tgis_register_map.argtypes = [POINTER(tgisMap), c_char, String]
    tgis_register_map.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 221
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_unregister_map'):
        continue
    tgis_unregister_map = _lib.tgis_unregister_map
    tgis_unregister_map.argtypes = [POINTER(tgisMap), c_char, String]
    tgis_unregister_map.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 224
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_register_maps'):
        continue
    tgis_register_maps = _lib.tgis_register_maps
    tgis_register_maps.argtypes = [POINTER(tgisMapList), c_char, String]
    tgis_register_maps.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 227
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_unregister_maps'):
        continue
    tgis_unregister_maps = _lib.tgis_unregister_maps
    tgis_unregister_maps.argtypes = [POINTER(tgisMapList), c_char, String]
    tgis_unregister_maps.restype = c_int
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 230
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_get_registered_maps'):
        continue
    tgis_get_registered_maps = _lib.tgis_get_registered_maps
    tgis_get_registered_maps.argtypes = [String, String, c_char, String, String]
    tgis_get_registered_maps.restype = POINTER(tgisDatasetList)
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 236
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_get_registered_stds'):
        continue
    tgis_get_registered_stds = _lib.tgis_get_registered_stds
    tgis_get_registered_stds.argtypes = [String, String, c_char, c_char, String, String]
    tgis_get_registered_stds.restype = POINTER(tgisDatasetList)
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 241
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'tgis_get_stds_info'):
        continue
    tgis_get_stds_info = _lib.tgis_get_stds_info
    tgis_get_stds_info.argtypes = [String, String, c_char]
    tgis_get_stds_info.restype = POINTER(tgisDataset)
    break

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 9
try:
    TGISDB_DEFAULT_DRIVER = 'sqlite'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 11
try:
    TGISDB_DEFAULT_SQLITE_PATH = 'tgis/sqlite.db'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 31
try:
    TGIS_TYPE_MAP = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 32
try:
    TGIS_TYPE_STDS = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 34
try:
    TGIS_RASTER_MAP = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 35
try:
    TGIS_RASTER3D_MAP = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 36
try:
    TGIS_VECTOR_MAP = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 37
try:
    TGIS_STRDS = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 38
try:
    TGIS_STR3DS = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 39
try:
    TGIS_STVDS = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 41
try:
    TGIS_ABSOLUTE_TIME = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 42
try:
    TGIS_RELATIVE_TIME = 1
except:
    pass

_tgisMap = struct__tgisMap # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 49

_tgisMapList = struct__tgisMapList # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 71

_tgisExtent = struct__tgisExtent # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 103

_tgisDataset = struct__tgisDataset # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 133

_tgisDatasetList = struct__tgisDatasetList # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\temporal.h: 128

# No inserted files

