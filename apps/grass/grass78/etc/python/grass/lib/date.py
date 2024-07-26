'''Wrapper for datetime.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_datetime.7.8 C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/datetime.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h -o OBJ.x86_64-w64-mingw32/date.py

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

_libs["grass_datetime.7.8"] = load_library("grass_datetime.7.8")

# 1 libraries
# End libraries

# No modules

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 27
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

DateTime = struct_DateTime # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 27

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 5
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_between'):
    datetime_is_between = _libs['grass_datetime.7.8'].datetime_is_between
    datetime_is_between.argtypes = [c_int, c_int, c_int]
    datetime_is_between.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 8
if hasattr(_libs['grass_datetime.7.8'], 'datetime_change_from_to'):
    datetime_change_from_to = _libs['grass_datetime.7.8'].datetime_change_from_to
    datetime_change_from_to.argtypes = [POINTER(DateTime), c_int, c_int, c_int]
    datetime_change_from_to.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 11
if hasattr(_libs['grass_datetime.7.8'], 'datetime_copy'):
    datetime_copy = _libs['grass_datetime.7.8'].datetime_copy
    datetime_copy.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_copy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 14
if hasattr(_libs['grass_datetime.7.8'], 'datetime_difference'):
    datetime_difference = _libs['grass_datetime.7.8'].datetime_difference
    datetime_difference.argtypes = [POINTER(DateTime), POINTER(DateTime), POINTER(DateTime)]
    datetime_difference.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 18
if hasattr(_libs['grass_datetime.7.8'], 'datetime_error'):
    datetime_error = _libs['grass_datetime.7.8'].datetime_error
    datetime_error.argtypes = [c_int, String]
    datetime_error.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 19
if hasattr(_libs['grass_datetime.7.8'], 'datetime_error_code'):
    datetime_error_code = _libs['grass_datetime.7.8'].datetime_error_code
    datetime_error_code.argtypes = []
    datetime_error_code.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 20
if hasattr(_libs['grass_datetime.7.8'], 'datetime_error_msg'):
    datetime_error_msg = _libs['grass_datetime.7.8'].datetime_error_msg
    datetime_error_msg.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        datetime_error_msg.restype = ReturnString
    else:
        datetime_error_msg.restype = String
        datetime_error_msg.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 21
if hasattr(_libs['grass_datetime.7.8'], 'datetime_clear_error'):
    datetime_clear_error = _libs['grass_datetime.7.8'].datetime_clear_error
    datetime_clear_error.argtypes = []
    datetime_clear_error.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 24
if hasattr(_libs['grass_datetime.7.8'], 'datetime_format'):
    datetime_format = _libs['grass_datetime.7.8'].datetime_format
    datetime_format.argtypes = [POINTER(DateTime), String]
    datetime_format.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 27
if hasattr(_libs['grass_datetime.7.8'], 'datetime_increment'):
    datetime_increment = _libs['grass_datetime.7.8'].datetime_increment
    datetime_increment.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_increment.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 30
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_valid_increment'):
    datetime_is_valid_increment = _libs['grass_datetime.7.8'].datetime_is_valid_increment
    datetime_is_valid_increment.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_is_valid_increment.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 31
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_increment'):
    datetime_check_increment = _libs['grass_datetime.7.8'].datetime_check_increment
    datetime_check_increment.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_check_increment.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 34
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_increment_type'):
    datetime_get_increment_type = _libs['grass_datetime.7.8'].datetime_get_increment_type
    datetime_get_increment_type.argtypes = [POINTER(DateTime), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    datetime_get_increment_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 36
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_increment_type'):
    datetime_set_increment_type = _libs['grass_datetime.7.8'].datetime_set_increment_type
    datetime_set_increment_type.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_set_increment_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 39
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_local_timezone'):
    datetime_get_local_timezone = _libs['grass_datetime.7.8'].datetime_get_local_timezone
    datetime_get_local_timezone.argtypes = [POINTER(c_int)]
    datetime_get_local_timezone.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 40
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_local_time'):
    datetime_get_local_time = _libs['grass_datetime.7.8'].datetime_get_local_time
    datetime_get_local_time.argtypes = [POINTER(DateTime)]
    datetime_get_local_time.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 43
if hasattr(_libs['grass_datetime.7.8'], 'datetime_days_in_month'):
    datetime_days_in_month = _libs['grass_datetime.7.8'].datetime_days_in_month
    datetime_days_in_month.argtypes = [c_int, c_int, c_int]
    datetime_days_in_month.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 44
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_leap_year'):
    datetime_is_leap_year = _libs['grass_datetime.7.8'].datetime_is_leap_year
    datetime_is_leap_year.argtypes = [c_int, c_int]
    datetime_is_leap_year.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 45
if hasattr(_libs['grass_datetime.7.8'], 'datetime_days_in_year'):
    datetime_days_in_year = _libs['grass_datetime.7.8'].datetime_days_in_year
    datetime_days_in_year.argtypes = [c_int, c_int]
    datetime_days_in_year.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 48
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_same'):
    datetime_is_same = _libs['grass_datetime.7.8'].datetime_is_same
    datetime_is_same.argtypes = [POINTER(DateTime), POINTER(DateTime)]
    datetime_is_same.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 51
if hasattr(_libs['grass_datetime.7.8'], 'datetime_scan'):
    datetime_scan = _libs['grass_datetime.7.8'].datetime_scan
    datetime_scan.argtypes = [POINTER(DateTime), String]
    datetime_scan.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 54
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_positive'):
    datetime_is_positive = _libs['grass_datetime.7.8'].datetime_is_positive
    datetime_is_positive.argtypes = [POINTER(DateTime)]
    datetime_is_positive.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 55
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_negative'):
    datetime_is_negative = _libs['grass_datetime.7.8'].datetime_is_negative
    datetime_is_negative.argtypes = [POINTER(DateTime)]
    datetime_is_negative.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 56
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_positive'):
    datetime_set_positive = _libs['grass_datetime.7.8'].datetime_set_positive
    datetime_set_positive.argtypes = [POINTER(DateTime)]
    datetime_set_positive.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 57
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_negative'):
    datetime_set_negative = _libs['grass_datetime.7.8'].datetime_set_negative
    datetime_set_negative.argtypes = [POINTER(DateTime)]
    datetime_set_negative.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 58
if hasattr(_libs['grass_datetime.7.8'], 'datetime_invert_sign'):
    datetime_invert_sign = _libs['grass_datetime.7.8'].datetime_invert_sign
    datetime_invert_sign.argtypes = [POINTER(DateTime)]
    datetime_invert_sign.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 61
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_type'):
    datetime_set_type = _libs['grass_datetime.7.8'].datetime_set_type
    datetime_set_type.argtypes = [POINTER(DateTime), c_int, c_int, c_int, c_int]
    datetime_set_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 62
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_type'):
    datetime_get_type = _libs['grass_datetime.7.8'].datetime_get_type
    datetime_get_type.argtypes = [POINTER(DateTime), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    datetime_get_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 64
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_valid_type'):
    datetime_is_valid_type = _libs['grass_datetime.7.8'].datetime_is_valid_type
    datetime_is_valid_type.argtypes = [POINTER(DateTime)]
    datetime_is_valid_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 65
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_type'):
    datetime_check_type = _libs['grass_datetime.7.8'].datetime_check_type
    datetime_check_type.argtypes = [POINTER(DateTime)]
    datetime_check_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 66
if hasattr(_libs['grass_datetime.7.8'], 'datetime_in_interval_year_month'):
    datetime_in_interval_year_month = _libs['grass_datetime.7.8'].datetime_in_interval_year_month
    datetime_in_interval_year_month.argtypes = [c_int]
    datetime_in_interval_year_month.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 67
if hasattr(_libs['grass_datetime.7.8'], 'datetime_in_interval_day_second'):
    datetime_in_interval_day_second = _libs['grass_datetime.7.8'].datetime_in_interval_day_second
    datetime_in_interval_day_second.argtypes = [c_int]
    datetime_in_interval_day_second.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 68
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_absolute'):
    datetime_is_absolute = _libs['grass_datetime.7.8'].datetime_is_absolute
    datetime_is_absolute.argtypes = [POINTER(DateTime)]
    datetime_is_absolute.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 69
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_relative'):
    datetime_is_relative = _libs['grass_datetime.7.8'].datetime_is_relative
    datetime_is_relative.argtypes = [POINTER(DateTime)]
    datetime_is_relative.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 72
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_timezone'):
    datetime_check_timezone = _libs['grass_datetime.7.8'].datetime_check_timezone
    datetime_check_timezone.argtypes = [POINTER(DateTime), c_int]
    datetime_check_timezone.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 73
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_timezone'):
    datetime_get_timezone = _libs['grass_datetime.7.8'].datetime_get_timezone
    datetime_get_timezone.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_timezone.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 74
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_timezone'):
    datetime_set_timezone = _libs['grass_datetime.7.8'].datetime_set_timezone
    datetime_set_timezone.argtypes = [POINTER(DateTime), c_int]
    datetime_set_timezone.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 75
if hasattr(_libs['grass_datetime.7.8'], 'datetime_unset_timezone'):
    datetime_unset_timezone = _libs['grass_datetime.7.8'].datetime_unset_timezone
    datetime_unset_timezone.argtypes = [POINTER(DateTime)]
    datetime_unset_timezone.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 76
if hasattr(_libs['grass_datetime.7.8'], 'datetime_is_valid_timezone'):
    datetime_is_valid_timezone = _libs['grass_datetime.7.8'].datetime_is_valid_timezone
    datetime_is_valid_timezone.argtypes = [c_int]
    datetime_is_valid_timezone.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 79
if hasattr(_libs['grass_datetime.7.8'], 'datetime_change_timezone'):
    datetime_change_timezone = _libs['grass_datetime.7.8'].datetime_change_timezone
    datetime_change_timezone.argtypes = [POINTER(DateTime), c_int]
    datetime_change_timezone.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 80
if hasattr(_libs['grass_datetime.7.8'], 'datetime_change_to_utc'):
    datetime_change_to_utc = _libs['grass_datetime.7.8'].datetime_change_to_utc
    datetime_change_to_utc.argtypes = [POINTER(DateTime)]
    datetime_change_to_utc.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 81
if hasattr(_libs['grass_datetime.7.8'], 'datetime_decompose_timezone'):
    datetime_decompose_timezone = _libs['grass_datetime.7.8'].datetime_decompose_timezone
    datetime_decompose_timezone.argtypes = [c_int, POINTER(c_int), POINTER(c_int)]
    datetime_decompose_timezone.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 84
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_year'):
    datetime_check_year = _libs['grass_datetime.7.8'].datetime_check_year
    datetime_check_year.argtypes = [POINTER(DateTime), c_int]
    datetime_check_year.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 85
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_month'):
    datetime_check_month = _libs['grass_datetime.7.8'].datetime_check_month
    datetime_check_month.argtypes = [POINTER(DateTime), c_int]
    datetime_check_month.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 86
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_day'):
    datetime_check_day = _libs['grass_datetime.7.8'].datetime_check_day
    datetime_check_day.argtypes = [POINTER(DateTime), c_int]
    datetime_check_day.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 87
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_hour'):
    datetime_check_hour = _libs['grass_datetime.7.8'].datetime_check_hour
    datetime_check_hour.argtypes = [POINTER(DateTime), c_int]
    datetime_check_hour.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 88
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_minute'):
    datetime_check_minute = _libs['grass_datetime.7.8'].datetime_check_minute
    datetime_check_minute.argtypes = [POINTER(DateTime), c_int]
    datetime_check_minute.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 89
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_second'):
    datetime_check_second = _libs['grass_datetime.7.8'].datetime_check_second
    datetime_check_second.argtypes = [POINTER(DateTime), c_double]
    datetime_check_second.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 90
if hasattr(_libs['grass_datetime.7.8'], 'datetime_check_fracsec'):
    datetime_check_fracsec = _libs['grass_datetime.7.8'].datetime_check_fracsec
    datetime_check_fracsec.argtypes = [POINTER(DateTime), c_int]
    datetime_check_fracsec.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 91
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_year'):
    datetime_get_year = _libs['grass_datetime.7.8'].datetime_get_year
    datetime_get_year.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_year.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 92
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_year'):
    datetime_set_year = _libs['grass_datetime.7.8'].datetime_set_year
    datetime_set_year.argtypes = [POINTER(DateTime), c_int]
    datetime_set_year.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 93
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_month'):
    datetime_get_month = _libs['grass_datetime.7.8'].datetime_get_month
    datetime_get_month.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_month.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 94
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_month'):
    datetime_set_month = _libs['grass_datetime.7.8'].datetime_set_month
    datetime_set_month.argtypes = [POINTER(DateTime), c_int]
    datetime_set_month.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 95
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_day'):
    datetime_get_day = _libs['grass_datetime.7.8'].datetime_get_day
    datetime_get_day.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_day.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 96
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_day'):
    datetime_set_day = _libs['grass_datetime.7.8'].datetime_set_day
    datetime_set_day.argtypes = [POINTER(DateTime), c_int]
    datetime_set_day.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 97
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_hour'):
    datetime_get_hour = _libs['grass_datetime.7.8'].datetime_get_hour
    datetime_get_hour.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_hour.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 98
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_hour'):
    datetime_set_hour = _libs['grass_datetime.7.8'].datetime_set_hour
    datetime_set_hour.argtypes = [POINTER(DateTime), c_int]
    datetime_set_hour.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 99
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_minute'):
    datetime_get_minute = _libs['grass_datetime.7.8'].datetime_get_minute
    datetime_get_minute.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_minute.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 100
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_minute'):
    datetime_set_minute = _libs['grass_datetime.7.8'].datetime_set_minute
    datetime_set_minute.argtypes = [POINTER(DateTime), c_int]
    datetime_set_minute.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 101
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_second'):
    datetime_get_second = _libs['grass_datetime.7.8'].datetime_get_second
    datetime_get_second.argtypes = [POINTER(DateTime), POINTER(c_double)]
    datetime_get_second.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 102
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_second'):
    datetime_set_second = _libs['grass_datetime.7.8'].datetime_set_second
    datetime_set_second.argtypes = [POINTER(DateTime), c_double]
    datetime_set_second.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 103
if hasattr(_libs['grass_datetime.7.8'], 'datetime_get_fracsec'):
    datetime_get_fracsec = _libs['grass_datetime.7.8'].datetime_get_fracsec
    datetime_get_fracsec.argtypes = [POINTER(DateTime), POINTER(c_int)]
    datetime_get_fracsec.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/datetime.h: 104
if hasattr(_libs['grass_datetime.7.8'], 'datetime_set_fracsec'):
    datetime_set_fracsec = _libs['grass_datetime.7.8'].datetime_set_fracsec
    datetime_set_fracsec.argtypes = [POINTER(DateTime), c_int]
    datetime_set_fracsec.restype = c_int

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 4
try:
    DATETIME_ABSOLUTE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 5
try:
    DATETIME_RELATIVE = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 10
try:
    DATETIME_YEAR = 101
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 11
try:
    DATETIME_MONTH = 102
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 12
try:
    DATETIME_DAY = 103
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 13
try:
    DATETIME_HOUR = 104
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 14
try:
    DATETIME_MINUTE = 105
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 15
try:
    DATETIME_SECOND = 106
except:
    pass

DateTime = struct_DateTime # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\datetime.h: 27

# No inserted files

