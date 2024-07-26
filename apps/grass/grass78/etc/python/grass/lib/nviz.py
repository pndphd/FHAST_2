'''Wrapper for nviz.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_nviz.7.8 C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/nviz.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h -o OBJ.x86_64-w64-mingw32/nviz.py

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

_libs["grass_nviz.7.8"] = load_library("grass_nviz.7.8")

# 1 libraries
# End libraries

# No modules

# C:/msys64/mingw64/x86_64-w64-mingw32/include/windef.h: 46
class struct_HDC__(Structure):
    pass

struct_HDC__.__slots__ = [
    'unused',
]
struct_HDC__._fields_ = [
    ('unused', c_int),
]

HDC = POINTER(struct_HDC__) # C:/msys64/mingw64/x86_64-w64-mingw32/include/windef.h: 46

# C:/msys64/mingw64/x86_64-w64-mingw32/include/windef.h: 47
class struct_HGLRC__(Structure):
    pass

struct_HGLRC__.__slots__ = [
    'unused',
]
struct_HGLRC__._fields_ = [
    ('unused', c_int),
]

HGLRC = POINTER(struct_HGLRC__) # C:/msys64/mingw64/x86_64-w64-mingw32/include/windef.h: 47

GLubyte = c_ubyte # C:/msys64/mingw64/x86_64-w64-mingw32/include/GL/gl.h: 29

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 76
class struct_anon_316(Structure):
    pass

struct_anon_316.__slots__ = [
    'id',
    'brt',
    'r',
    'g',
    'b',
    'ar',
    'ag',
    'ab',
    'x',
    'y',
    'z',
    'w',
]
struct_anon_316._fields_ = [
    ('id', c_int),
    ('brt', c_float),
    ('r', c_float),
    ('g', c_float),
    ('b', c_float),
    ('ar', c_float),
    ('ag', c_float),
    ('ab', c_float),
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('w', c_float),
]

light_data = struct_anon_316 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 76

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 78
class struct_fringe_data(Structure):
    pass

struct_fringe_data.__slots__ = [
    'id',
    'color',
    'elev',
    'where',
]
struct_fringe_data._fields_ = [
    ('id', c_int),
    ('color', c_ulong),
    ('elev', c_float),
    ('where', c_int * 4),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 86
class struct_arrow_data(Structure):
    pass

struct_arrow_data.__slots__ = [
    'color',
    'size',
    'where',
]
struct_arrow_data._fields_ = [
    ('color', c_ulong),
    ('size', c_float),
    ('where', c_float * 3),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 93
class struct_scalebar_data(Structure):
    pass

struct_scalebar_data.__slots__ = [
    'id',
    'color',
    'size',
    'where',
]
struct_scalebar_data._fields_ = [
    ('id', c_int),
    ('color', c_ulong),
    ('size', c_float),
    ('where', c_float * 3),
]

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 130
class struct_anon_317(Structure):
    pass

struct_anon_317.__slots__ = [
    'zrange',
    'xyrange',
    'num_cplanes',
    'cur_cplane',
    'cp_on',
    'cp_trans',
    'cp_rot',
    'light',
    'num_fringes',
    'fringe',
    'draw_arrow',
    'arrow',
    'num_scalebars',
    'scalebar',
    'bgcolor',
]
struct_anon_317._fields_ = [
    ('zrange', c_float),
    ('xyrange', c_float),
    ('num_cplanes', c_int),
    ('cur_cplane', c_int),
    ('cp_on', c_int * 6),
    ('cp_trans', (c_float * 3) * 6),
    ('cp_rot', (c_float * 3) * 6),
    ('light', light_data * 3),
    ('num_fringes', c_int),
    ('fringe', POINTER(POINTER(struct_fringe_data))),
    ('draw_arrow', c_int),
    ('arrow', POINTER(struct_arrow_data)),
    ('num_scalebars', c_int),
    ('scalebar', POINTER(POINTER(struct_scalebar_data))),
    ('bgcolor', c_int),
]

nv_data = struct_anon_317 # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 130

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 132
class struct_render_window(Structure):
    pass

struct_render_window.__slots__ = [
    'displayId',
    'contextId',
    'width',
    'height',
]
struct_render_window._fields_ = [
    ('displayId', HDC),
    ('contextId', HGLRC),
    ('width', c_int),
    ('height', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 5
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_resize_window'):
    Nviz_resize_window = _libs['grass_nviz.7.8'].Nviz_resize_window
    Nviz_resize_window.argtypes = [c_int, c_int]
    Nviz_resize_window.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 6
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_update_ranges'):
    Nviz_update_ranges = _libs['grass_nviz.7.8'].Nviz_update_ranges
    Nviz_update_ranges.argtypes = [POINTER(nv_data)]
    Nviz_update_ranges.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 7
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_viewpoint_position'):
    Nviz_set_viewpoint_position = _libs['grass_nviz.7.8'].Nviz_set_viewpoint_position
    Nviz_set_viewpoint_position.argtypes = [c_double, c_double]
    Nviz_set_viewpoint_position.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 8
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_viewpoint_position'):
    Nviz_get_viewpoint_position = _libs['grass_nviz.7.8'].Nviz_get_viewpoint_position
    Nviz_get_viewpoint_position.argtypes = [POINTER(c_double), POINTER(c_double)]
    Nviz_get_viewpoint_position.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 9
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_viewpoint_height'):
    Nviz_set_viewpoint_height = _libs['grass_nviz.7.8'].Nviz_set_viewpoint_height
    Nviz_set_viewpoint_height.argtypes = [c_double]
    Nviz_set_viewpoint_height.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 10
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_viewpoint_height'):
    Nviz_get_viewpoint_height = _libs['grass_nviz.7.8'].Nviz_get_viewpoint_height
    Nviz_get_viewpoint_height.argtypes = [POINTER(c_double)]
    Nviz_get_viewpoint_height.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 11
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_viewpoint_persp'):
    Nviz_set_viewpoint_persp = _libs['grass_nviz.7.8'].Nviz_set_viewpoint_persp
    Nviz_set_viewpoint_persp.argtypes = [c_int]
    Nviz_set_viewpoint_persp.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 12
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_viewpoint_twist'):
    Nviz_set_viewpoint_twist = _libs['grass_nviz.7.8'].Nviz_set_viewpoint_twist
    Nviz_set_viewpoint_twist.argtypes = [c_int]
    Nviz_set_viewpoint_twist.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 13
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_change_exag'):
    Nviz_change_exag = _libs['grass_nviz.7.8'].Nviz_change_exag
    Nviz_change_exag.argtypes = [POINTER(nv_data), c_double]
    Nviz_change_exag.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 14
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_look_here'):
    Nviz_look_here = _libs['grass_nviz.7.8'].Nviz_look_here
    Nviz_look_here.argtypes = [c_double, c_double]
    Nviz_look_here.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 15
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_modelview'):
    Nviz_get_modelview = _libs['grass_nviz.7.8'].Nviz_get_modelview
    Nviz_get_modelview.argtypes = [POINTER(c_double)]
    Nviz_get_modelview.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 16
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_rotation'):
    Nviz_set_rotation = _libs['grass_nviz.7.8'].Nviz_set_rotation
    Nviz_set_rotation.argtypes = [c_double, c_double, c_double, c_double]
    Nviz_set_rotation.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 17
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_unset_rotation'):
    Nviz_unset_rotation = _libs['grass_nviz.7.8'].Nviz_unset_rotation
    Nviz_unset_rotation.argtypes = []
    Nviz_unset_rotation.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 18
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_init_rotation'):
    Nviz_init_rotation = _libs['grass_nviz.7.8'].Nviz_init_rotation
    Nviz_init_rotation.argtypes = []
    Nviz_init_rotation.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 19
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_flythrough'):
    Nviz_flythrough = _libs['grass_nviz.7.8'].Nviz_flythrough
    Nviz_flythrough.argtypes = [POINTER(nv_data), POINTER(c_float), POINTER(c_int), c_int]
    Nviz_flythrough.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 22
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_new_cplane'):
    Nviz_new_cplane = _libs['grass_nviz.7.8'].Nviz_new_cplane
    Nviz_new_cplane.argtypes = [POINTER(nv_data), c_int]
    Nviz_new_cplane.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 23
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_on_cplane'):
    Nviz_on_cplane = _libs['grass_nviz.7.8'].Nviz_on_cplane
    Nviz_on_cplane.argtypes = [POINTER(nv_data), c_int]
    Nviz_on_cplane.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 24
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_off_cplane'):
    Nviz_off_cplane = _libs['grass_nviz.7.8'].Nviz_off_cplane
    Nviz_off_cplane.argtypes = [POINTER(nv_data), c_int]
    Nviz_off_cplane.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 25
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_cplane'):
    Nviz_draw_cplane = _libs['grass_nviz.7.8'].Nviz_draw_cplane
    Nviz_draw_cplane.argtypes = [POINTER(nv_data), c_int, c_int]
    Nviz_draw_cplane.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 26
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_num_cplanes'):
    Nviz_num_cplanes = _libs['grass_nviz.7.8'].Nviz_num_cplanes
    Nviz_num_cplanes.argtypes = [POINTER(nv_data)]
    Nviz_num_cplanes.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 27
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_current_cplane'):
    Nviz_get_current_cplane = _libs['grass_nviz.7.8'].Nviz_get_current_cplane
    Nviz_get_current_cplane.argtypes = [POINTER(nv_data)]
    Nviz_get_current_cplane.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 28
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_cplane_rotation'):
    Nviz_set_cplane_rotation = _libs['grass_nviz.7.8'].Nviz_set_cplane_rotation
    Nviz_set_cplane_rotation.argtypes = [POINTER(nv_data), c_int, c_float, c_float, c_float]
    Nviz_set_cplane_rotation.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 29
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_cplane_rotation'):
    Nviz_get_cplane_rotation = _libs['grass_nviz.7.8'].Nviz_get_cplane_rotation
    Nviz_get_cplane_rotation.argtypes = [POINTER(nv_data), c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    Nviz_get_cplane_rotation.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 30
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_cplane_translation'):
    Nviz_set_cplane_translation = _libs['grass_nviz.7.8'].Nviz_set_cplane_translation
    Nviz_set_cplane_translation.argtypes = [POINTER(nv_data), c_int, c_float, c_float, c_float]
    Nviz_set_cplane_translation.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 31
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_cplane_translation'):
    Nviz_get_cplane_translation = _libs['grass_nviz.7.8'].Nviz_get_cplane_translation
    Nviz_get_cplane_translation.argtypes = [POINTER(nv_data), c_int, POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    Nviz_get_cplane_translation.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 32
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_fence_color'):
    Nviz_set_fence_color = _libs['grass_nviz.7.8'].Nviz_set_fence_color
    Nviz_set_fence_color.argtypes = [POINTER(nv_data), c_int]
    Nviz_set_fence_color.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 33
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_cplane_here'):
    Nviz_set_cplane_here = _libs['grass_nviz.7.8'].Nviz_set_cplane_here
    Nviz_set_cplane_here.argtypes = [POINTER(nv_data), c_int, c_float, c_float]
    Nviz_set_cplane_here.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 37
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_all_surf'):
    Nviz_draw_all_surf = _libs['grass_nviz.7.8'].Nviz_draw_all_surf
    Nviz_draw_all_surf.argtypes = [POINTER(nv_data)]
    Nviz_draw_all_surf.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 38
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_all_vect'):
    Nviz_draw_all_vect = _libs['grass_nviz.7.8'].Nviz_draw_all_vect
    Nviz_draw_all_vect.argtypes = []
    Nviz_draw_all_vect.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 39
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_all_site'):
    Nviz_draw_all_site = _libs['grass_nviz.7.8'].Nviz_draw_all_site
    Nviz_draw_all_site.argtypes = []
    Nviz_draw_all_site.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 40
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_all_vol'):
    Nviz_draw_all_vol = _libs['grass_nviz.7.8'].Nviz_draw_all_vol
    Nviz_draw_all_vol.argtypes = []
    Nviz_draw_all_vol.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 41
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_all'):
    Nviz_draw_all = _libs['grass_nviz.7.8'].Nviz_draw_all
    Nviz_draw_all.argtypes = [POINTER(nv_data)]
    Nviz_draw_all.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 42
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_quick'):
    Nviz_draw_quick = _libs['grass_nviz.7.8'].Nviz_draw_quick
    Nviz_draw_quick.argtypes = [POINTER(nv_data), c_int]
    Nviz_draw_quick.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 43
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_load_image'):
    Nviz_load_image = _libs['grass_nviz.7.8'].Nviz_load_image
    Nviz_load_image.argtypes = [POINTER(GLubyte), c_int, c_int, c_int]
    Nviz_load_image.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 44
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_image'):
    Nviz_draw_image = _libs['grass_nviz.7.8'].Nviz_draw_image
    Nviz_draw_image.argtypes = [c_int, c_int, c_int, c_int, c_int]
    Nviz_draw_image.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 45
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_2D'):
    Nviz_set_2D = _libs['grass_nviz.7.8'].Nviz_set_2D
    Nviz_set_2D.argtypes = [c_int, c_int]
    Nviz_set_2D.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 46
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_del_texture'):
    Nviz_del_texture = _libs['grass_nviz.7.8'].Nviz_del_texture
    Nviz_del_texture.argtypes = [c_int]
    Nviz_del_texture.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 47
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_max_texture'):
    Nviz_get_max_texture = _libs['grass_nviz.7.8'].Nviz_get_max_texture
    Nviz_get_max_texture.argtypes = [POINTER(c_int)]
    Nviz_get_max_texture.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 50
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_exag_height'):
    Nviz_get_exag_height = _libs['grass_nviz.7.8'].Nviz_get_exag_height
    Nviz_get_exag_height.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Nviz_get_exag_height.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 51
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_exag'):
    Nviz_get_exag = _libs['grass_nviz.7.8'].Nviz_get_exag
    Nviz_get_exag.argtypes = []
    Nviz_get_exag.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 54
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_light_position'):
    Nviz_set_light_position = _libs['grass_nviz.7.8'].Nviz_set_light_position
    Nviz_set_light_position.argtypes = [POINTER(nv_data), c_int, c_double, c_double, c_double, c_double]
    Nviz_set_light_position.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 55
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_light_bright'):
    Nviz_set_light_bright = _libs['grass_nviz.7.8'].Nviz_set_light_bright
    Nviz_set_light_bright.argtypes = [POINTER(nv_data), c_int, c_double]
    Nviz_set_light_bright.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 56
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_light_color'):
    Nviz_set_light_color = _libs['grass_nviz.7.8'].Nviz_set_light_color
    Nviz_set_light_color.argtypes = [POINTER(nv_data), c_int, c_int, c_int, c_int]
    Nviz_set_light_color.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 57
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_light_ambient'):
    Nviz_set_light_ambient = _libs['grass_nviz.7.8'].Nviz_set_light_ambient
    Nviz_set_light_ambient.argtypes = [POINTER(nv_data), c_int, c_double]
    Nviz_set_light_ambient.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 58
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_init_light'):
    Nviz_init_light = _libs['grass_nviz.7.8'].Nviz_init_light
    Nviz_init_light.argtypes = [POINTER(nv_data), c_int]
    Nviz_init_light.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 59
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_new_light'):
    Nviz_new_light = _libs['grass_nviz.7.8'].Nviz_new_light
    Nviz_new_light.argtypes = [POINTER(nv_data)]
    Nviz_new_light.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 60
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_model'):
    Nviz_draw_model = _libs['grass_nviz.7.8'].Nviz_draw_model
    Nviz_draw_model.argtypes = [POINTER(nv_data)]
    Nviz_draw_model.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 63
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_new_map_obj'):
    Nviz_new_map_obj = _libs['grass_nviz.7.8'].Nviz_new_map_obj
    Nviz_new_map_obj.argtypes = [c_int, String, c_double, POINTER(nv_data)]
    Nviz_new_map_obj.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 64
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_attr'):
    Nviz_set_attr = _libs['grass_nviz.7.8'].Nviz_set_attr
    Nviz_set_attr.argtypes = [c_int, c_int, c_int, c_int, String, c_double, POINTER(nv_data)]
    Nviz_set_attr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 65
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_surface_attr_default'):
    Nviz_set_surface_attr_default = _libs['grass_nviz.7.8'].Nviz_set_surface_attr_default
    Nviz_set_surface_attr_default.argtypes = []
    Nviz_set_surface_attr_default.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 66
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_vpoint_attr_default'):
    Nviz_set_vpoint_attr_default = _libs['grass_nviz.7.8'].Nviz_set_vpoint_attr_default
    Nviz_set_vpoint_attr_default.argtypes = []
    Nviz_set_vpoint_attr_default.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 67
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_volume_attr_default'):
    Nviz_set_volume_attr_default = _libs['grass_nviz.7.8'].Nviz_set_volume_attr_default
    Nviz_set_volume_attr_default.argtypes = []
    Nviz_set_volume_attr_default.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 68
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_unset_attr'):
    Nviz_unset_attr = _libs['grass_nviz.7.8'].Nviz_unset_attr
    Nviz_unset_attr.argtypes = [c_int, c_int, c_int]
    Nviz_unset_attr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 71
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_init_data'):
    Nviz_init_data = _libs['grass_nviz.7.8'].Nviz_init_data
    Nviz_init_data.argtypes = [POINTER(nv_data)]
    Nviz_init_data.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 72
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_destroy_data'):
    Nviz_destroy_data = _libs['grass_nviz.7.8'].Nviz_destroy_data
    Nviz_destroy_data.argtypes = [POINTER(nv_data)]
    Nviz_destroy_data.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 73
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_bgcolor'):
    Nviz_set_bgcolor = _libs['grass_nviz.7.8'].Nviz_set_bgcolor
    Nviz_set_bgcolor.argtypes = [POINTER(nv_data), c_int]
    Nviz_set_bgcolor.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 74
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_bgcolor'):
    Nviz_get_bgcolor = _libs['grass_nviz.7.8'].Nviz_get_bgcolor
    Nviz_get_bgcolor.argtypes = [POINTER(nv_data)]
    Nviz_get_bgcolor.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 75
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_color_from_str'):
    Nviz_color_from_str = _libs['grass_nviz.7.8'].Nviz_color_from_str
    Nviz_color_from_str.argtypes = [String]
    Nviz_color_from_str.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 76
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_new_fringe'):
    Nviz_new_fringe = _libs['grass_nviz.7.8'].Nviz_new_fringe
    Nviz_new_fringe.argtypes = [POINTER(nv_data), c_int, c_ulong, c_double, c_int, c_int, c_int, c_int]
    Nviz_new_fringe.restype = POINTER(struct_fringe_data)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 78
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_fringe'):
    Nviz_set_fringe = _libs['grass_nviz.7.8'].Nviz_set_fringe
    Nviz_set_fringe.argtypes = [POINTER(nv_data), c_int, c_ulong, c_double, c_int, c_int, c_int, c_int]
    Nviz_set_fringe.restype = POINTER(struct_fringe_data)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 80
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_fringe'):
    Nviz_draw_fringe = _libs['grass_nviz.7.8'].Nviz_draw_fringe
    Nviz_draw_fringe.argtypes = [POINTER(nv_data)]
    Nviz_draw_fringe.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 81
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_arrow'):
    Nviz_draw_arrow = _libs['grass_nviz.7.8'].Nviz_draw_arrow
    Nviz_draw_arrow.argtypes = [POINTER(nv_data)]
    Nviz_draw_arrow.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 82
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_arrow'):
    Nviz_set_arrow = _libs['grass_nviz.7.8'].Nviz_set_arrow
    Nviz_set_arrow.argtypes = [POINTER(nv_data), c_int, c_int, c_float, c_uint]
    Nviz_set_arrow.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 83
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_delete_arrow'):
    Nviz_delete_arrow = _libs['grass_nviz.7.8'].Nviz_delete_arrow
    Nviz_delete_arrow.argtypes = [POINTER(nv_data)]
    Nviz_delete_arrow.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 84
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_new_scalebar'):
    Nviz_new_scalebar = _libs['grass_nviz.7.8'].Nviz_new_scalebar
    Nviz_new_scalebar.argtypes = [POINTER(nv_data), c_int, POINTER(c_float), c_float, c_uint]
    Nviz_new_scalebar.restype = POINTER(struct_scalebar_data)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 85
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_scalebar'):
    Nviz_set_scalebar = _libs['grass_nviz.7.8'].Nviz_set_scalebar
    Nviz_set_scalebar.argtypes = [POINTER(nv_data), c_int, c_int, c_int, c_float, c_uint]
    Nviz_set_scalebar.restype = POINTER(struct_scalebar_data)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 86
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_draw_scalebar'):
    Nviz_draw_scalebar = _libs['grass_nviz.7.8'].Nviz_draw_scalebar
    Nviz_draw_scalebar.argtypes = [POINTER(nv_data)]
    Nviz_draw_scalebar.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 87
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_delete_scalebar'):
    Nviz_delete_scalebar = _libs['grass_nviz.7.8'].Nviz_delete_scalebar
    Nviz_delete_scalebar.argtypes = [POINTER(nv_data), c_int]
    Nviz_delete_scalebar.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 90
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_init_view'):
    Nviz_init_view = _libs['grass_nviz.7.8'].Nviz_init_view
    Nviz_init_view.argtypes = [POINTER(nv_data)]
    Nviz_init_view.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 91
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_focus_state'):
    Nviz_set_focus_state = _libs['grass_nviz.7.8'].Nviz_set_focus_state
    Nviz_set_focus_state.argtypes = [c_int]
    Nviz_set_focus_state.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 92
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_focus_map'):
    Nviz_set_focus_map = _libs['grass_nviz.7.8'].Nviz_set_focus_map
    Nviz_set_focus_map.argtypes = [c_int, c_int]
    Nviz_set_focus_map.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 93
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_has_focus'):
    Nviz_has_focus = _libs['grass_nviz.7.8'].Nviz_has_focus
    Nviz_has_focus.argtypes = [POINTER(nv_data)]
    Nviz_has_focus.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 94
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_set_focus'):
    Nviz_set_focus = _libs['grass_nviz.7.8'].Nviz_set_focus
    Nviz_set_focus.argtypes = [POINTER(nv_data), c_float, c_float, c_float]
    Nviz_set_focus.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 95
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_focus'):
    Nviz_get_focus = _libs['grass_nviz.7.8'].Nviz_get_focus
    Nviz_get_focus.argtypes = [POINTER(nv_data), POINTER(c_float), POINTER(c_float), POINTER(c_float)]
    Nviz_get_focus.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 96
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_xyrange'):
    Nviz_get_xyrange = _libs['grass_nviz.7.8'].Nviz_get_xyrange
    Nviz_get_xyrange.argtypes = [POINTER(nv_data)]
    Nviz_get_xyrange.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 97
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_zrange'):
    Nviz_get_zrange = _libs['grass_nviz.7.8'].Nviz_get_zrange
    Nviz_get_zrange.argtypes = [POINTER(nv_data), POINTER(c_float), POINTER(c_float)]
    Nviz_get_zrange.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 98
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_get_longdim'):
    Nviz_get_longdim = _libs['grass_nviz.7.8'].Nviz_get_longdim
    Nviz_get_longdim.argtypes = [POINTER(nv_data)]
    Nviz_get_longdim.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 101
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_new_render_window'):
    Nviz_new_render_window = _libs['grass_nviz.7.8'].Nviz_new_render_window
    Nviz_new_render_window.argtypes = []
    Nviz_new_render_window.restype = POINTER(struct_render_window)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 102
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_init_render_window'):
    Nviz_init_render_window = _libs['grass_nviz.7.8'].Nviz_init_render_window
    Nviz_init_render_window.argtypes = [POINTER(struct_render_window)]
    Nviz_init_render_window.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 103
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_destroy_render_window'):
    Nviz_destroy_render_window = _libs['grass_nviz.7.8'].Nviz_destroy_render_window
    Nviz_destroy_render_window.argtypes = [POINTER(struct_render_window)]
    Nviz_destroy_render_window.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 104
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_create_render_window'):
    Nviz_create_render_window = _libs['grass_nviz.7.8'].Nviz_create_render_window
    Nviz_create_render_window.argtypes = [POINTER(struct_render_window), POINTER(None), c_int, c_int]
    Nviz_create_render_window.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/nviz.h: 105
if hasattr(_libs['grass_nviz.7.8'], 'Nviz_make_current_render_window'):
    Nviz_make_current_render_window = _libs['grass_nviz.7.8'].Nviz_make_current_render_window
    Nviz_make_current_render_window.argtypes = [POINTER(struct_render_window)]
    Nviz_make_current_render_window.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/ogsf.h: 30
try:
    GS_UNIT_SIZE = 1000.0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 42
try:
    MAP_OBJ_UNDEFINED = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 43
try:
    MAP_OBJ_SURF = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 44
try:
    MAP_OBJ_VOL = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 45
try:
    MAP_OBJ_VECT = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 46
try:
    MAP_OBJ_SITE = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 48
try:
    DRAW_COARSE = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 49
try:
    DRAW_FINE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 50
try:
    DRAW_BOTH = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 53
try:
    DRAW_QUICK_SURFACE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 54
try:
    DRAW_QUICK_VLINES = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 55
try:
    DRAW_QUICK_VPOINTS = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 56
try:
    DRAW_QUICK_VOLUME = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 58
try:
    RANGE = (5 * GS_UNIT_SIZE)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 59
try:
    RANGE_OFFSET = (2 * GS_UNIT_SIZE)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 60
try:
    ZRANGE = (3 * GS_UNIT_SIZE)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 61
try:
    ZRANGE_OFFSET = (1 * GS_UNIT_SIZE)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 63
try:
    DEFAULT_SURF_COLOR = 3390463
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 65
try:
    FORMAT_PPM = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 66
try:
    FORMAT_TIF = 2
except:
    pass

fringe_data = struct_fringe_data # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 78

arrow_data = struct_arrow_data # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 86

scalebar_data = struct_scalebar_data # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 93

render_window = struct_render_window # C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\nviz.h: 132

# No inserted files

