'''Wrapper for vector.h

Generated with:
./ctypesgen.py --cpp gcc -E -I/c/OSGeo4W64/include -D_FILE_OFFSET_BITS=64      -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -I/usr/src/grass785/dist.x86_64-w64-mingw32/include -D__GLIBC_HAVE_LONG_LONG -lgrass_vector.7.8 -IC:/OSGeo4W64/include -IC:/OSGeo4W64/include -IC:/OSGeo4W64/include C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vector.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h -o OBJ.x86_64-w64-mingw32/vector.py

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

_libs["grass_vector.7.8"] = load_library("grass_vector.7.8")

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

off_t = c_int64 # C:/msys64/mingw64/x86_64-w64-mingw32/include/_mingw_off_t.h: 24

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

DCELL = c_double # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 598

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

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/gis.h: 684
class struct_ilist(Structure):
    pass

struct_ilist.__slots__ = [
    'value',
    'n_values',
    'alloc_values',
]
struct_ilist._fields_ = [
    ('value', POINTER(c_int)),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

enum_overlay_operator = c_int # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 208

GV_O_AND = 0 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 208

GV_O_OVERLAP = (GV_O_AND + 1) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 208

OVERLAY_OPERATOR = enum_overlay_operator # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 214

enum_anon_7 = c_int # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_GEOMETRY = 0 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_POINT = 1 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_LINESTRING = 2 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_POLYGON = 3 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_MULTIPOINT = 4 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_MULTILINESTRING = 5 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_MULTIPOLYGON = 6 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_GEOMETRYCOLLECTION = 7 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_NONE = 100 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_LINEARRING = 101 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_POINT25D = 2147483649 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_LINESTRING25D = 2147483650 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_POLYGON25D = 2147483651 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_MULTIPOINT25D = 2147483652 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_MULTILINESTRING25D = 2147483653 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_MULTIPOLYGON25D = 2147483654 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_GEOMETRYCOLLECTION25D = 2147483655 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

SF_FeatureType = enum_anon_7 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 257

dglByte_t = c_ubyte # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/type.h: 36

dglInt32_t = c_long # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/type.h: 37

dglInt64_t = c_longlong # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/type.h: 38

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/heap.h: 33
class union__dglHeapData(Union):
    pass

union__dglHeapData.__slots__ = [
    'pv',
    'n',
    'un',
    'l',
    'ul',
]
union__dglHeapData._fields_ = [
    ('pv', POINTER(None)),
    ('n', c_int),
    ('un', c_uint),
    ('l', c_long),
    ('ul', c_ulong),
]

dglHeapData_u = union__dglHeapData # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/heap.h: 33

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/heap.h: 42
class struct__dglHeapNode(Structure):
    pass

struct__dglHeapNode.__slots__ = [
    'key',
    'value',
    'flags',
]
struct__dglHeapNode._fields_ = [
    ('key', c_long),
    ('value', dglHeapData_u),
    ('flags', c_ubyte),
]

dglHeapNode_s = struct__dglHeapNode # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/heap.h: 42

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/heap.h: 52
class struct__dglHeap(Structure):
    pass

struct__dglHeap.__slots__ = [
    'index',
    'count',
    'block',
    'pnode',
]
struct__dglHeap._fields_ = [
    ('index', c_long),
    ('count', c_long),
    ('block', c_long),
    ('pnode', POINTER(dglHeapNode_s)),
]

dglHeap_s = struct__dglHeap # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/heap.h: 52

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/tree.h: 164
class struct__dglTreeEdgePri32(Structure):
    pass

struct__dglTreeEdgePri32.__slots__ = [
    'nKey',
    'cnData',
    'pnData',
]
struct__dglTreeEdgePri32._fields_ = [
    ('nKey', dglInt32_t),
    ('cnData', dglInt32_t),
    ('pnData', POINTER(dglInt32_t)),
]

dglTreeEdgePri32_s = struct__dglTreeEdgePri32 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/tree.h: 164

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/graph.h: 135
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'pvAVL',
]
struct_anon_9._fields_ = [
    ('pvAVL', POINTER(None)),
]

dglNodePrioritizer_s = struct_anon_9 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/graph.h: 135

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/graph.h: 146
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'cEdge',
    'iEdge',
    'pEdgePri32Item',
    'pvAVL',
]
struct_anon_10._fields_ = [
    ('cEdge', c_int),
    ('iEdge', c_int),
    ('pEdgePri32Item', POINTER(dglTreeEdgePri32_s)),
    ('pvAVL', POINTER(None)),
]

dglEdgePrioritizer_s = struct_anon_10 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/graph.h: 146

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/graph.h: 193
class struct__dglGraph(Structure):
    pass

struct__dglGraph.__slots__ = [
    'iErrno',
    'Version',
    'Endian',
    'NodeAttrSize',
    'EdgeAttrSize',
    'aOpaqueSet',
    'cNode',
    'cHead',
    'cTail',
    'cAlone',
    'cEdge',
    'nnCost',
    'Flags',
    'nFamily',
    'nOptions',
    'pNodeTree',
    'pEdgeTree',
    'pNodeBuffer',
    'iNodeBuffer',
    'pEdgeBuffer',
    'iEdgeBuffer',
    'edgePrioritizer',
    'nodePrioritizer',
]
struct__dglGraph._fields_ = [
    ('iErrno', c_int),
    ('Version', dglByte_t),
    ('Endian', dglByte_t),
    ('NodeAttrSize', dglInt32_t),
    ('EdgeAttrSize', dglInt32_t),
    ('aOpaqueSet', dglInt32_t * 16),
    ('cNode', dglInt32_t),
    ('cHead', dglInt32_t),
    ('cTail', dglInt32_t),
    ('cAlone', dglInt32_t),
    ('cEdge', dglInt32_t),
    ('nnCost', dglInt64_t),
    ('Flags', dglInt32_t),
    ('nFamily', dglInt32_t),
    ('nOptions', dglInt32_t),
    ('pNodeTree', POINTER(None)),
    ('pEdgeTree', POINTER(None)),
    ('pNodeBuffer', POINTER(dglByte_t)),
    ('iNodeBuffer', dglInt32_t),
    ('pEdgeBuffer', POINTER(dglByte_t)),
    ('iEdgeBuffer', dglInt32_t),
    ('edgePrioritizer', dglEdgePrioritizer_s),
    ('nodePrioritizer', dglNodePrioritizer_s),
]

dglGraph_s = struct__dglGraph # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/graph.h: 193

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/graph.h: 243
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'nStartNode',
    'NodeHeap',
    'pvVisited',
    'pvPredist',
]
struct_anon_11._fields_ = [
    ('nStartNode', dglInt32_t),
    ('NodeHeap', dglHeap_s),
    ('pvVisited', POINTER(None)),
    ('pvPredist', POINTER(None)),
]

dglSPCache_s = struct_anon_11 # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dgl/graph.h: 243

RectReal = c_double # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 28

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 57
class struct_RTree_Rect(Structure):
    pass

struct_RTree_Rect.__slots__ = [
    'boundary',
]
struct_RTree_Rect._fields_ = [
    ('boundary', POINTER(RectReal)),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 77
class struct_RTree_Node(Structure):
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 64
class union_RTree_Child(Union):
    pass

union_RTree_Child.__slots__ = [
    'id',
    'ptr',
    'pos',
]
union_RTree_Child._fields_ = [
    ('id', c_int),
    ('ptr', POINTER(struct_RTree_Node)),
    ('pos', off_t),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 71
class struct_RTree_Branch(Structure):
    pass

struct_RTree_Branch.__slots__ = [
    'rect',
    'child',
]
struct_RTree_Branch._fields_ = [
    ('rect', struct_RTree_Rect),
    ('child', union_RTree_Child),
]

struct_RTree_Node.__slots__ = [
    'count',
    'level',
    'branch',
]
struct_RTree_Node._fields_ = [
    ('count', c_int),
    ('level', c_int),
    ('branch', POINTER(struct_RTree_Branch)),
]

SearchHitCallback = CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(struct_RTree_Rect), POINTER(None)) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 91

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 128
class struct_RTree(Structure):
    pass

rt_search_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree), POINTER(struct_RTree_Rect), POINTER(SearchHitCallback), POINTER(None)) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 95

rt_insert_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, c_int, POINTER(struct_RTree)) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 97

rt_delete_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(struct_RTree_Rect), union_RTree_Child, POINTER(struct_RTree)) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 98

rt_valid_child_fn = CFUNCTYPE(UNCHECKED(c_int), POINTER(union_RTree_Child)) # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 99

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 103
class struct_nstack(Structure):
    pass

struct_nstack.__slots__ = [
    'sn',
    'branch_id',
    'pos',
]
struct_nstack._fields_ = [
    ('sn', POINTER(struct_RTree_Node)),
    ('branch_id', c_int),
    ('pos', off_t),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 111
class struct_NodeBuffer(Structure):
    pass

struct_NodeBuffer.__slots__ = [
    'n',
    'pos',
    'dirty',
]
struct_NodeBuffer._fields_ = [
    ('n', struct_RTree_Node),
    ('pos', off_t),
    ('dirty', c_char),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 119
class struct_RTree_PartitionVars(Structure):
    pass

struct_RTree_PartitionVars.__slots__ = [
    'partition',
    'total',
    'minfill',
    'taken',
    'count',
    'cover',
    'area',
]
struct_RTree_PartitionVars._fields_ = [
    ('partition', c_int * (9 + 1)),
    ('total', c_int),
    ('minfill', c_int),
    ('taken', c_int * (9 + 1)),
    ('count', c_int * 2),
    ('cover', struct_RTree_Rect * 2),
    ('area', RectReal * 2),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/rtree.h: 155
class struct__recycle(Structure):
    pass

struct__recycle.__slots__ = [
    'avail',
    'alloc',
    'pos',
]
struct__recycle._fields_ = [
    ('avail', c_int),
    ('alloc', c_int),
    ('pos', POINTER(off_t)),
]

struct_RTree.__slots__ = [
    'fd',
    'ndims',
    'nsides',
    'ndims_alloc',
    'nsides_alloc',
    'nodesize',
    'branchsize',
    'rectsize',
    'n_nodes',
    'n_leafs',
    'rootlevel',
    'nodecard',
    'leafcard',
    'min_node_fill',
    'min_leaf_fill',
    'minfill_node_split',
    'minfill_leaf_split',
    'overflow',
    'free_nodes',
    'nb',
    'used',
    'insert_rect',
    'delete_rect',
    'search_rect',
    'valid_child',
    'root',
    'ns',
    'p',
    'BranchBuf',
    'tmpb1',
    'tmpb2',
    'c',
    'BranchCount',
    'rect_0',
    'rect_1',
    'upperrect',
    'orect',
    'center_n',
    'rootpos',
]
struct_RTree._fields_ = [
    ('fd', c_int),
    ('ndims', c_ubyte),
    ('nsides', c_ubyte),
    ('ndims_alloc', c_ubyte),
    ('nsides_alloc', c_ubyte),
    ('nodesize', c_int),
    ('branchsize', c_int),
    ('rectsize', c_int),
    ('n_nodes', c_int),
    ('n_leafs', c_int),
    ('rootlevel', c_int),
    ('nodecard', c_int),
    ('leafcard', c_int),
    ('min_node_fill', c_int),
    ('min_leaf_fill', c_int),
    ('minfill_node_split', c_int),
    ('minfill_leaf_split', c_int),
    ('overflow', c_char),
    ('free_nodes', struct__recycle),
    ('nb', POINTER(POINTER(struct_NodeBuffer))),
    ('used', POINTER(POINTER(c_int))),
    ('insert_rect', POINTER(rt_insert_fn)),
    ('delete_rect', POINTER(rt_delete_fn)),
    ('search_rect', POINTER(rt_search_fn)),
    ('valid_child', POINTER(rt_valid_child_fn)),
    ('root', POINTER(struct_RTree_Node)),
    ('ns', POINTER(struct_nstack)),
    ('p', struct_RTree_PartitionVars),
    ('BranchBuf', POINTER(struct_RTree_Branch)),
    ('tmpb1', struct_RTree_Branch),
    ('tmpb2', struct_RTree_Branch),
    ('c', struct_RTree_Branch),
    ('BranchCount', c_int),
    ('rect_0', struct_RTree_Rect),
    ('rect_1', struct_RTree_Rect),
    ('upperrect', struct_RTree_Rect),
    ('orect', struct_RTree_Rect),
    ('center_n', POINTER(RectReal)),
    ('rootpos', off_t),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dbmi.h: 153
class struct__dbmscap(Structure):
    pass

struct__dbmscap.__slots__ = [
    'driverName',
    'startup',
    'comment',
    'next',
]
struct__dbmscap._fields_ = [
    ('driverName', c_char * 256),
    ('startup', c_char * 256),
    ('comment', c_char * 256),
    ('next', POINTER(struct__dbmscap)),
]

dbDbmscap = struct__dbmscap # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dbmi.h: 159

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dbmi.h: 173
class struct__db_driver(Structure):
    pass

struct__db_driver.__slots__ = [
    'dbmscap',
    'send',
    'recv',
    'pid',
]
struct__db_driver._fields_ = [
    ('dbmscap', dbDbmscap),
    ('send', POINTER(FILE)),
    ('recv', POINTER(FILE)),
    ('pid', c_int),
]

dbDriver = struct__db_driver # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/dbmi.h: 173

OGRFeatureH = POINTER(None) # C:/OSGeo4W64/include/ogr_api.h: 314

OGRLayerH = POINTER(None) # C:/OSGeo4W64/include/ogr_api.h: 521

OGRDataSourceH = POINTER(None) # C:/OSGeo4W64/include/ogr_api.h: 523

OGRSFDriverH = POINTER(None) # C:/OSGeo4W64/include/ogr_api.h: 525

# C:/OSGeo4W64/include/libpq-fe.h: 140
class struct_pg_conn(Structure):
    pass

PGconn = struct_pg_conn # C:/OSGeo4W64/include/libpq-fe.h: 140

# C:/OSGeo4W64/include/libpq-fe.h: 147
class struct_pg_result(Structure):
    pass

PGresult = struct_pg_result # C:/OSGeo4W64/include/libpq-fe.h: 147

plus_t = c_int # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 41

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 46
class struct_site_att(Structure):
    pass

struct_site_att.__slots__ = [
    'cat',
    'dbl',
    'str',
]
struct_site_att._fields_ = [
    ('cat', c_int),
    ('dbl', POINTER(c_double)),
    ('str', POINTER(POINTER(c_char))),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 65
class struct_bound_box(Structure):
    pass

struct_bound_box.__slots__ = [
    'N',
    'S',
    'E',
    'W',
    'T',
    'B',
]
struct_bound_box._fields_ = [
    ('N', c_double),
    ('S', c_double),
    ('E', c_double),
    ('W', c_double),
    ('T', c_double),
    ('B', c_double),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 96
class struct_gvfile(Structure):
    pass

struct_gvfile.__slots__ = [
    'file',
    'start',
    'current',
    'end',
    'size',
    'alloc',
    'loaded',
]
struct_gvfile._fields_ = [
    ('file', POINTER(FILE)),
    ('start', String),
    ('current', String),
    ('end', String),
    ('size', off_t),
    ('alloc', off_t),
    ('loaded', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 134
class struct_field_info(Structure):
    pass

struct_field_info.__slots__ = [
    'number',
    'name',
    'driver',
    'database',
    'table',
    'key',
]
struct_field_info._fields_ = [
    ('number', c_int),
    ('name', String),
    ('driver', String),
    ('database', String),
    ('table', String),
    ('key', String),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 165
class struct_dblinks(Structure):
    pass

struct_dblinks.__slots__ = [
    'field',
    'alloc_fields',
    'n_fields',
]
struct_dblinks._fields_ = [
    ('field', POINTER(struct_field_info)),
    ('alloc_fields', c_int),
    ('n_fields', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 186
class struct_Port_info(Structure):
    pass

struct_Port_info.__slots__ = [
    'byte_order',
    'off_t_size',
    'dbl_cnvrt',
    'flt_cnvrt',
    'lng_cnvrt',
    'int_cnvrt',
    'shrt_cnvrt',
    'off_t_cnvrt',
    'dbl_quick',
    'flt_quick',
    'lng_quick',
    'int_quick',
    'shrt_quick',
    'off_t_quick',
]
struct_Port_info._fields_ = [
    ('byte_order', c_int),
    ('off_t_size', c_int),
    ('dbl_cnvrt', c_ubyte * 8),
    ('flt_cnvrt', c_ubyte * 4),
    ('lng_cnvrt', c_ubyte * 4),
    ('int_cnvrt', c_ubyte * 4),
    ('shrt_cnvrt', c_ubyte * 2),
    ('off_t_cnvrt', c_ubyte * 8),
    ('dbl_quick', c_int),
    ('flt_quick', c_int),
    ('lng_quick', c_int),
    ('int_quick', c_int),
    ('shrt_quick', c_int),
    ('off_t_quick', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 272
class struct_recycle(Structure):
    pass

struct_recycle.__slots__ = [
    'dummy',
]
struct_recycle._fields_ = [
    ('dummy', c_char),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 278
class struct_Version_info(Structure):
    pass

struct_Version_info.__slots__ = [
    'major',
    'minor',
    'back_major',
    'back_minor',
]
struct_Version_info._fields_ = [
    ('major', c_int),
    ('minor', c_int),
    ('back_major', c_int),
    ('back_minor', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 294
class struct_dig_head(Structure):
    pass

struct_dig_head.__slots__ = [
    'organization',
    'date',
    'user_name',
    'map_name',
    'source_date',
    'orig_scale',
    'comment',
    'proj',
    'plani_zone',
    'digit_thresh',
    'coor_version',
    'with_z',
    'size',
    'head_size',
    'port',
    'last_offset',
    'recycle',
]
struct_dig_head._fields_ = [
    ('organization', String),
    ('date', String),
    ('user_name', String),
    ('map_name', String),
    ('source_date', String),
    ('orig_scale', c_long),
    ('comment', String),
    ('proj', c_int),
    ('plani_zone', c_int),
    ('digit_thresh', c_double),
    ('coor_version', struct_Version_info),
    ('with_z', c_int),
    ('size', off_t),
    ('head_size', c_long),
    ('port', struct_Port_info),
    ('last_offset', off_t),
    ('recycle', POINTER(struct_recycle)),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 379
class struct_Coor_info(Structure):
    pass

struct_Coor_info.__slots__ = [
    'size',
    'mtime',
]
struct_Coor_info._fields_ = [
    ('size', off_t),
    ('mtime', c_long),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 397
class struct_Format_info_offset(Structure):
    pass

struct_Format_info_offset.__slots__ = [
    'array',
    'array_num',
    'array_alloc',
]
struct_Format_info_offset._fields_ = [
    ('array', POINTER(c_int)),
    ('array_num', c_int),
    ('array_alloc', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1675
class struct_line_pnts(Structure):
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 461
class struct_Format_info_cache(Structure):
    pass

struct_Format_info_cache.__slots__ = [
    'lines',
    'lines_types',
    'lines_cats',
    'lines_alloc',
    'lines_num',
    'lines_next',
    'fid',
    'sf_type',
    'ctype',
]
struct_Format_info_cache._fields_ = [
    ('lines', POINTER(POINTER(struct_line_pnts))),
    ('lines_types', POINTER(c_int)),
    ('lines_cats', POINTER(c_int)),
    ('lines_alloc', c_int),
    ('lines_num', c_int),
    ('lines_next', c_int),
    ('fid', c_long),
    ('sf_type', SF_FeatureType),
    ('ctype', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 516
class struct_Format_info_ogr(Structure):
    pass

struct_Format_info_ogr.__slots__ = [
    'driver_name',
    'dsn',
    'layer_name',
    'where',
    'driver',
    'ds',
    'layer',
    'dbdriver',
    'dsn_options',
    'layer_options',
    'cache',
    'feature_cache',
    'offset',
    'next_line',
]
struct_Format_info_ogr._fields_ = [
    ('driver_name', String),
    ('dsn', String),
    ('layer_name', String),
    ('where', String),
    ('driver', OGRSFDriverH),
    ('ds', OGRDataSourceH),
    ('layer', OGRLayerH),
    ('dbdriver', POINTER(dbDriver)),
    ('dsn_options', POINTER(POINTER(c_char))),
    ('layer_options', POINTER(POINTER(c_char))),
    ('cache', struct_Format_info_cache),
    ('feature_cache', OGRFeatureH),
    ('offset', struct_Format_info_offset),
    ('next_line', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 602
class struct_Format_info_pg(Structure):
    pass

struct_Format_info_pg.__slots__ = [
    'conninfo',
    'db_name',
    'schema_name',
    'table_name',
    'where',
    'fid_column',
    'geom_column',
    'feature_type',
    'coor_dim',
    'srid',
    'dbdriver',
    'fi',
    'inTransaction',
    'conn',
    'res',
    'cursor_name',
    'cursor_fid',
    'next_line',
    'cache',
    'offset',
    'topogeom_column',
    'toposchema_name',
    'toposchema_id',
    'topo_geo_only',
]
struct_Format_info_pg._fields_ = [
    ('conninfo', String),
    ('db_name', String),
    ('schema_name', String),
    ('table_name', String),
    ('where', String),
    ('fid_column', String),
    ('geom_column', String),
    ('feature_type', SF_FeatureType),
    ('coor_dim', c_int),
    ('srid', c_int),
    ('dbdriver', POINTER(dbDriver)),
    ('fi', POINTER(struct_field_info)),
    ('inTransaction', c_int),
    ('conn', POINTER(PGconn)),
    ('res', POINTER(PGresult)),
    ('cursor_name', String),
    ('cursor_fid', c_int),
    ('next_line', c_int),
    ('cache', struct_Format_info_cache),
    ('offset', struct_Format_info_offset),
    ('topogeom_column', String),
    ('toposchema_name', String),
    ('toposchema_id', c_int),
    ('topo_geo_only', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 713
class struct_Format_info(Structure):
    pass

struct_Format_info.__slots__ = [
    'i',
    'ogr',
    'pg',
]
struct_Format_info._fields_ = [
    ('i', c_int),
    ('ogr', struct_Format_info_ogr),
    ('pg', struct_Format_info_pg),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 732
class struct_Cat_index(Structure):
    pass

struct_Cat_index.__slots__ = [
    'field',
    'n_cats',
    'a_cats',
    'cat',
    'n_ucats',
    'n_types',
    'type',
    'offset',
]
struct_Cat_index._fields_ = [
    ('field', c_int),
    ('n_cats', c_int),
    ('a_cats', c_int),
    ('cat', POINTER(c_int * 3)),
    ('n_ucats', c_int),
    ('n_types', c_int),
    ('type', (c_int * 2) * 7),
    ('offset', off_t),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 787
class struct_anon_61(Structure):
    pass

struct_anon_61.__slots__ = [
    'topo',
    'spidx',
    'cidx',
]
struct_anon_61._fields_ = [
    ('topo', struct_Version_info),
    ('spidx', struct_Version_info),
    ('cidx', struct_Version_info),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1448
class struct_P_node(Structure):
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1574
class struct_P_line(Structure):
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1605
class struct_P_area(Structure):
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1646
class struct_P_isle(Structure):
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1173
class struct_anon_62(Structure):
    pass

struct_anon_62.__slots__ = [
    'do_uplist',
    'uplines',
    'uplines_offset',
    'alloc_uplines',
    'n_uplines',
    'upnodes',
    'alloc_upnodes',
    'n_upnodes',
]
struct_anon_62._fields_ = [
    ('do_uplist', c_int),
    ('uplines', POINTER(c_int)),
    ('uplines_offset', POINTER(off_t)),
    ('alloc_uplines', c_int),
    ('n_uplines', c_int),
    ('upnodes', POINTER(c_int)),
    ('alloc_upnodes', c_int),
    ('n_upnodes', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 784
class struct_Plus_head(Structure):
    pass

struct_Plus_head.__slots__ = [
    'version',
    'with_z',
    'spidx_with_z',
    'off_t_size',
    'head_size',
    'spidx_head_size',
    'cidx_head_size',
    'release_support',
    'port',
    'spidx_port',
    'cidx_port',
    'mode',
    'built',
    'box',
    'Node',
    'Line',
    'Area',
    'Isle',
    'n_plines',
    'n_llines',
    'n_blines',
    'n_clines',
    'n_flines',
    'n_klines',
    'n_vfaces',
    'n_hfaces',
    'n_nodes',
    'n_edges',
    'n_lines',
    'n_areas',
    'n_isles',
    'n_faces',
    'n_volumes',
    'n_holes',
    'alloc_nodes',
    'alloc_edges',
    'alloc_lines',
    'alloc_areas',
    'alloc_isles',
    'alloc_faces',
    'alloc_volumes',
    'alloc_holes',
    'Node_offset',
    'Edge_offset',
    'Line_offset',
    'Area_offset',
    'Isle_offset',
    'Volume_offset',
    'Hole_offset',
    'Spidx_built',
    'Spidx_new',
    'Spidx_file',
    'spidx_fp',
    'Node_spidx_offset',
    'Line_spidx_offset',
    'Area_spidx_offset',
    'Isle_spidx_offset',
    'Face_spidx_offset',
    'Volume_spidx_offset',
    'Hole_spidx_offset',
    'Node_spidx',
    'Line_spidx',
    'Area_spidx',
    'Isle_spidx',
    'Face_spidx',
    'Volume_spidx',
    'Hole_spidx',
    'update_cidx',
    'n_cidx',
    'a_cidx',
    'cidx',
    'cidx_up_to_date',
    'coor_size',
    'coor_mtime',
    'uplist',
]
struct_Plus_head._fields_ = [
    ('version', struct_anon_61),
    ('with_z', c_int),
    ('spidx_with_z', c_int),
    ('off_t_size', c_int),
    ('head_size', c_long),
    ('spidx_head_size', c_long),
    ('cidx_head_size', c_long),
    ('release_support', c_int),
    ('port', struct_Port_info),
    ('spidx_port', struct_Port_info),
    ('cidx_port', struct_Port_info),
    ('mode', c_int),
    ('built', c_int),
    ('box', struct_bound_box),
    ('Node', POINTER(POINTER(struct_P_node))),
    ('Line', POINTER(POINTER(struct_P_line))),
    ('Area', POINTER(POINTER(struct_P_area))),
    ('Isle', POINTER(POINTER(struct_P_isle))),
    ('n_plines', plus_t),
    ('n_llines', plus_t),
    ('n_blines', plus_t),
    ('n_clines', plus_t),
    ('n_flines', plus_t),
    ('n_klines', plus_t),
    ('n_vfaces', plus_t),
    ('n_hfaces', plus_t),
    ('n_nodes', plus_t),
    ('n_edges', plus_t),
    ('n_lines', plus_t),
    ('n_areas', plus_t),
    ('n_isles', plus_t),
    ('n_faces', plus_t),
    ('n_volumes', plus_t),
    ('n_holes', plus_t),
    ('alloc_nodes', plus_t),
    ('alloc_edges', plus_t),
    ('alloc_lines', plus_t),
    ('alloc_areas', plus_t),
    ('alloc_isles', plus_t),
    ('alloc_faces', plus_t),
    ('alloc_volumes', plus_t),
    ('alloc_holes', plus_t),
    ('Node_offset', off_t),
    ('Edge_offset', off_t),
    ('Line_offset', off_t),
    ('Area_offset', off_t),
    ('Isle_offset', off_t),
    ('Volume_offset', off_t),
    ('Hole_offset', off_t),
    ('Spidx_built', c_int),
    ('Spidx_new', c_int),
    ('Spidx_file', c_int),
    ('spidx_fp', struct_gvfile),
    ('Node_spidx_offset', off_t),
    ('Line_spidx_offset', off_t),
    ('Area_spidx_offset', off_t),
    ('Isle_spidx_offset', off_t),
    ('Face_spidx_offset', off_t),
    ('Volume_spidx_offset', off_t),
    ('Hole_spidx_offset', off_t),
    ('Node_spidx', POINTER(struct_RTree)),
    ('Line_spidx', POINTER(struct_RTree)),
    ('Area_spidx', POINTER(struct_RTree)),
    ('Isle_spidx', POINTER(struct_RTree)),
    ('Face_spidx', POINTER(struct_RTree)),
    ('Volume_spidx', POINTER(struct_RTree)),
    ('Hole_spidx', POINTER(struct_RTree)),
    ('update_cidx', c_int),
    ('n_cidx', c_int),
    ('a_cidx', c_int),
    ('cidx', POINTER(struct_Cat_index)),
    ('cidx_up_to_date', c_int),
    ('coor_size', off_t),
    ('coor_mtime', c_long),
    ('uplist', struct_anon_62),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1220
class struct_Graph_info(Structure):
    pass

struct_Graph_info.__slots__ = [
    'line_type',
    'graph_s',
    'spCache',
    'edge_fcosts',
    'edge_bcosts',
    'node_costs',
    'cost_multip',
]
struct_Graph_info._fields_ = [
    ('line_type', c_int),
    ('graph_s', dglGraph_s),
    ('spCache', dglSPCache_s),
    ('edge_fcosts', POINTER(c_double)),
    ('edge_bcosts', POINTER(c_double)),
    ('node_costs', POINTER(c_double)),
    ('cost_multip', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1358
class struct_anon_63(Structure):
    pass

struct_anon_63.__slots__ = [
    'region_flag',
    'box',
    'type_flag',
    'type',
    'field_flag',
    'field',
]
struct_anon_63._fields_ = [
    ('region_flag', c_int),
    ('box', struct_bound_box),
    ('type_flag', c_int),
    ('type', c_int),
    ('field_flag', c_int),
    ('field', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1259
class struct_Map_info(Structure):
    pass

struct_Map_info.__slots__ = [
    'format',
    'temporary',
    'dblnk',
    'plus',
    'open',
    'mode',
    'level',
    'head_only',
    'support_updated',
    'name',
    'mapset',
    'location',
    'gisdbase',
    'next_line',
    'constraint',
    'proj',
    'hist_fp',
    'dgraph',
    'head',
    'dig_fp',
    'fInfo',
    'site_att',
    'n_site_att',
    'n_site_dbl',
    'n_site_str',
]
struct_Map_info._fields_ = [
    ('format', c_int),
    ('temporary', c_int),
    ('dblnk', POINTER(struct_dblinks)),
    ('plus', struct_Plus_head),
    ('open', c_int),
    ('mode', c_int),
    ('level', c_int),
    ('head_only', c_int),
    ('support_updated', c_int),
    ('name', String),
    ('mapset', String),
    ('location', String),
    ('gisdbase', String),
    ('next_line', plus_t),
    ('constraint', struct_anon_63),
    ('proj', c_int),
    ('hist_fp', POINTER(FILE)),
    ('dgraph', struct_Graph_info),
    ('head', struct_dig_head),
    ('dig_fp', struct_gvfile),
    ('fInfo', struct_Format_info),
    ('site_att', POINTER(struct_site_att)),
    ('n_site_att', c_int),
    ('n_site_dbl', c_int),
    ('n_site_str', c_int),
]

struct_P_node.__slots__ = [
    'x',
    'y',
    'z',
    'alloc_lines',
    'n_lines',
    'lines',
    'angles',
]
struct_P_node._fields_ = [
    ('x', c_double),
    ('y', c_double),
    ('z', c_double),
    ('alloc_lines', plus_t),
    ('n_lines', plus_t),
    ('lines', POINTER(plus_t)),
    ('angles', POINTER(c_float)),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1494
class struct_P_topo_l(Structure):
    pass

struct_P_topo_l.__slots__ = [
    'N1',
    'N2',
]
struct_P_topo_l._fields_ = [
    ('N1', plus_t),
    ('N2', plus_t),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1509
class struct_P_topo_b(Structure):
    pass

struct_P_topo_b.__slots__ = [
    'N1',
    'N2',
    'left',
    'right',
]
struct_P_topo_b._fields_ = [
    ('N1', plus_t),
    ('N2', plus_t),
    ('left', plus_t),
    ('right', plus_t),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1532
class struct_P_topo_c(Structure):
    pass

struct_P_topo_c.__slots__ = [
    'area',
]
struct_P_topo_c._fields_ = [
    ('area', plus_t),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1543
class struct_P_topo_f(Structure):
    pass

struct_P_topo_f.__slots__ = [
    'E',
    'left',
    'right',
]
struct_P_topo_f._fields_ = [
    ('E', plus_t * 3),
    ('left', plus_t),
    ('right', plus_t),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1563
class struct_P_topo_k(Structure):
    pass

struct_P_topo_k.__slots__ = [
    'volume',
]
struct_P_topo_k._fields_ = [
    ('volume', plus_t),
]

struct_P_line.__slots__ = [
    'type',
    'offset',
    'topo',
]
struct_P_line._fields_ = [
    ('type', c_char),
    ('offset', off_t),
    ('topo', POINTER(None)),
]

struct_P_area.__slots__ = [
    'n_lines',
    'alloc_lines',
    'lines',
    'centroid',
    'n_isles',
    'alloc_isles',
    'isles',
]
struct_P_area._fields_ = [
    ('n_lines', plus_t),
    ('alloc_lines', plus_t),
    ('lines', POINTER(plus_t)),
    ('centroid', plus_t),
    ('n_isles', plus_t),
    ('alloc_isles', plus_t),
    ('isles', POINTER(plus_t)),
]

struct_P_isle.__slots__ = [
    'n_lines',
    'alloc_lines',
    'lines',
    'area',
]
struct_P_isle._fields_ = [
    ('n_lines', plus_t),
    ('alloc_lines', plus_t),
    ('lines', POINTER(plus_t)),
    ('area', plus_t),
]

struct_line_pnts.__slots__ = [
    'x',
    'y',
    'z',
    'n_points',
    'alloc_points',
]
struct_line_pnts._fields_ = [
    ('x', POINTER(c_double)),
    ('y', POINTER(c_double)),
    ('z', POINTER(c_double)),
    ('n_points', c_int),
    ('alloc_points', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1702
class struct_line_cats(Structure):
    pass

struct_line_cats.__slots__ = [
    'field',
    'cat',
    'n_cats',
    'alloc_cats',
]
struct_line_cats._fields_ = [
    ('field', POINTER(c_int)),
    ('cat', POINTER(c_int)),
    ('n_cats', c_int),
    ('alloc_cats', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1723
class struct_cat_list(Structure):
    pass

struct_cat_list.__slots__ = [
    'field',
    'min',
    'max',
    'n_ranges',
    'alloc_ranges',
]
struct_cat_list._fields_ = [
    ('field', c_int),
    ('min', POINTER(c_int)),
    ('max', POINTER(c_int)),
    ('n_ranges', c_int),
    ('alloc_ranges', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1750
class struct_boxlist(Structure):
    pass

struct_boxlist.__slots__ = [
    'id',
    'box',
    'have_boxes',
    'n_values',
    'alloc_values',
]
struct_boxlist._fields_ = [
    ('id', POINTER(c_int)),
    ('box', POINTER(struct_bound_box)),
    ('have_boxes', c_int),
    ('n_values', c_int),
    ('alloc_values', c_int),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1779
class struct_varray(Structure):
    pass

struct_varray.__slots__ = [
    'size',
    'c',
]
struct_varray._fields_ = [
    ('size', c_int),
    ('c', POINTER(c_int)),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1799
class struct_spatial_index(Structure):
    pass

struct_spatial_index.__slots__ = [
    'si_tree',
    'name',
]
struct_spatial_index._fields_ = [
    ('si_tree', POINTER(struct_RTree)),
    ('name', String),
]

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 14
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_space'):
        continue
    dig_alloc_space = _lib.dig_alloc_space
    dig_alloc_space.argtypes = [c_int, POINTER(c_int), c_int, POINTER(None), c_int]
    dig_alloc_space.restype = POINTER(c_ubyte)
    dig_alloc_space.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 15
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__alloc_space'):
        continue
    dig__alloc_space = _lib.dig__alloc_space
    dig__alloc_space.argtypes = [c_int, POINTER(c_int), c_int, POINTER(None), c_int]
    dig__alloc_space.restype = POINTER(c_ubyte)
    dig__alloc_space.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 16
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_falloc'):
        continue
    dig_falloc = _lib.dig_falloc
    dig_falloc.argtypes = [c_int, c_int]
    dig_falloc.restype = POINTER(c_ubyte)
    dig_falloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 17
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_frealloc'):
        continue
    dig_frealloc = _lib.dig_frealloc
    dig_frealloc.argtypes = [POINTER(None), c_int, c_int, c_int]
    dig_frealloc.restype = POINTER(c_ubyte)
    dig_frealloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 18
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__falloc'):
        continue
    dig__falloc = _lib.dig__falloc
    dig__falloc.argtypes = [c_int, c_int]
    dig__falloc.restype = POINTER(c_ubyte)
    dig__falloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 19
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__frealloc'):
        continue
    dig__frealloc = _lib.dig__frealloc
    dig__frealloc.argtypes = [POINTER(None), c_int, c_int, c_int]
    dig__frealloc.restype = POINTER(c_ubyte)
    dig__frealloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 22
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_calc_begin_angle'):
        continue
    dig_calc_begin_angle = _lib.dig_calc_begin_angle
    dig_calc_begin_angle.argtypes = [POINTER(struct_line_pnts), c_double]
    dig_calc_begin_angle.restype = c_float
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 23
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_calc_end_angle'):
        continue
    dig_calc_end_angle = _lib.dig_calc_end_angle
    dig_calc_end_angle.argtypes = [POINTER(struct_line_pnts), c_double]
    dig_calc_end_angle.restype = c_float
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 24
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_line_degenerate'):
        continue
    dig_line_degenerate = _lib.dig_line_degenerate
    dig_line_degenerate.argtypes = [POINTER(struct_line_pnts)]
    dig_line_degenerate.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 25
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_is_line_degenerate'):
        continue
    dig_is_line_degenerate = _lib.dig_is_line_degenerate
    dig_is_line_degenerate.argtypes = [POINTER(struct_line_pnts), c_double]
    dig_is_line_degenerate.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 28
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_box_copy'):
        continue
    dig_box_copy = _lib.dig_box_copy
    dig_box_copy.argtypes = [POINTER(struct_bound_box), POINTER(struct_bound_box)]
    dig_box_copy.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 29
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_box_extend'):
        continue
    dig_box_extend = _lib.dig_box_extend
    dig_box_extend.argtypes = [POINTER(struct_bound_box), POINTER(struct_bound_box)]
    dig_box_extend.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 30
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_line_box'):
        continue
    dig_line_box = _lib.dig_line_box
    dig_line_box.argtypes = [POINTER(struct_line_pnts), POINTER(struct_bound_box)]
    dig_line_box.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 42
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_cidx_init'):
        continue
    dig_cidx_init = _lib.dig_cidx_init
    dig_cidx_init.argtypes = [POINTER(struct_Plus_head)]
    dig_cidx_init.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 43
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_cidx_free'):
        continue
    dig_cidx_free = _lib.dig_cidx_free
    dig_cidx_free.argtypes = [POINTER(struct_Plus_head)]
    dig_cidx_free.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 44
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_cidx_add_cat'):
        continue
    dig_cidx_add_cat = _lib.dig_cidx_add_cat
    dig_cidx_add_cat.argtypes = [POINTER(struct_Plus_head), c_int, c_int, c_int, c_int]
    dig_cidx_add_cat.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 45
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_cidx_add_cat_sorted'):
        continue
    dig_cidx_add_cat_sorted = _lib.dig_cidx_add_cat_sorted
    dig_cidx_add_cat_sorted.argtypes = [POINTER(struct_Plus_head), c_int, c_int, c_int, c_int]
    dig_cidx_add_cat_sorted.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 46
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_cidx_del_cat'):
        continue
    dig_cidx_del_cat = _lib.dig_cidx_del_cat
    dig_cidx_del_cat.argtypes = [POINTER(struct_Plus_head), c_int, c_int, c_int, c_int]
    dig_cidx_del_cat.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 47
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_cidx_sort'):
        continue
    dig_cidx_sort = _lib.dig_cidx_sort
    dig_cidx_sort.argtypes = [POINTER(struct_Plus_head)]
    dig_cidx_sort.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 50
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_cidx_head'):
        continue
    dig_write_cidx_head = _lib.dig_write_cidx_head
    dig_write_cidx_head.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_write_cidx_head.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 51
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_read_cidx_head'):
        continue
    dig_read_cidx_head = _lib.dig_read_cidx_head
    dig_read_cidx_head.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_read_cidx_head.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 52
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_cidx'):
        continue
    dig_write_cidx = _lib.dig_write_cidx
    dig_write_cidx.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_write_cidx.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 53
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_read_cidx'):
        continue
    dig_read_cidx = _lib.dig_read_cidx
    dig_read_cidx.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head), c_int]
    dig_read_cidx.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 57
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_ftell'):
        continue
    dig_ftell = _lib.dig_ftell
    dig_ftell.argtypes = [POINTER(struct_gvfile)]
    dig_ftell.restype = off_t
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 58
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_fseek'):
        continue
    dig_fseek = _lib.dig_fseek
    dig_fseek.argtypes = [POINTER(struct_gvfile), off_t, c_int]
    dig_fseek.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 59
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_rewind'):
        continue
    dig_rewind = _lib.dig_rewind
    dig_rewind.argtypes = [POINTER(struct_gvfile)]
    dig_rewind.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 60
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_fflush'):
        continue
    dig_fflush = _lib.dig_fflush
    dig_fflush.argtypes = [POINTER(struct_gvfile)]
    dig_fflush.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 61
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_fread'):
        continue
    dig_fread = _lib.dig_fread
    dig_fread.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(struct_gvfile)]
    dig_fread.restype = c_size_t
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 62
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_fwrite'):
        continue
    dig_fwrite = _lib.dig_fwrite
    dig_fwrite.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(struct_gvfile)]
    dig_fwrite.restype = c_size_t
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 63
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_file_init'):
        continue
    dig_file_init = _lib.dig_file_init
    dig_file_init.argtypes = [POINTER(struct_gvfile)]
    dig_file_init.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 64
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_file_load'):
        continue
    dig_file_load = _lib.dig_file_load
    dig_file_load.argtypes = [POINTER(struct_gvfile)]
    dig_file_load.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 65
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_file_free'):
        continue
    dig_file_free = _lib.dig_file_free
    dig_file_free.argtypes = [POINTER(struct_gvfile)]
    dig_file_free.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 68
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_frmt_ascii'):
        continue
    dig_write_frmt_ascii = _lib.dig_write_frmt_ascii
    dig_write_frmt_ascii.argtypes = [POINTER(FILE), POINTER(struct_Format_info), c_int]
    dig_write_frmt_ascii.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 69
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_read_frmt_ascii'):
        continue
    dig_read_frmt_ascii = _lib.dig_read_frmt_ascii
    dig_read_frmt_ascii.argtypes = [POINTER(FILE), POINTER(struct_Format_info)]
    dig_read_frmt_ascii.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 72
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__write_head'):
        continue
    dig__write_head = _lib.dig__write_head
    dig__write_head.argtypes = [POINTER(struct_Map_info)]
    dig__write_head.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 73
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__read_head'):
        continue
    dig__read_head = _lib.dig__read_head
    dig__read_head.argtypes = [POINTER(struct_Map_info)]
    dig__read_head.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 76
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_x_intersect'):
        continue
    dig_x_intersect = _lib.dig_x_intersect
    dig_x_intersect.argtypes = [c_double, c_double, c_double, c_double, c_double]
    dig_x_intersect.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 79
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_test_for_intersection'):
        continue
    dig_test_for_intersection = _lib.dig_test_for_intersection
    dig_test_for_intersection.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double]
    dig_test_for_intersection.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 81
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_find_intersection'):
        continue
    dig_find_intersection = _lib.dig_find_intersection
    dig_find_intersection.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
    dig_find_intersection.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 85
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_distance2_point_to_line'):
        continue
    dig_distance2_point_to_line = _lib.dig_distance2_point_to_line
    dig_distance2_point_to_line.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int)]
    dig_distance2_point_to_line.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 89
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_set_distance_to_line_tolerance'):
        continue
    dig_set_distance_to_line_tolerance = _lib.dig_set_distance_to_line_tolerance
    dig_set_distance_to_line_tolerance.argtypes = [c_double]
    dig_set_distance_to_line_tolerance.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 92
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_init_boxlist'):
        continue
    dig_init_boxlist = _lib.dig_init_boxlist
    dig_init_boxlist.argtypes = [POINTER(struct_boxlist), c_int]
    dig_init_boxlist.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 93
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_boxlist_add'):
        continue
    dig_boxlist_add = _lib.dig_boxlist_add
    dig_boxlist_add.argtypes = [POINTER(struct_boxlist), c_int, POINTER(struct_bound_box)]
    dig_boxlist_add.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 96
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_init_plus'):
        continue
    dig_init_plus = _lib.dig_init_plus
    dig_init_plus.argtypes = [POINTER(struct_Plus_head)]
    dig_init_plus.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 97
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_free_plus_nodes'):
        continue
    dig_free_plus_nodes = _lib.dig_free_plus_nodes
    dig_free_plus_nodes.argtypes = [POINTER(struct_Plus_head)]
    dig_free_plus_nodes.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 98
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_free_plus_lines'):
        continue
    dig_free_plus_lines = _lib.dig_free_plus_lines
    dig_free_plus_lines.argtypes = [POINTER(struct_Plus_head)]
    dig_free_plus_lines.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 99
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_free_plus_areas'):
        continue
    dig_free_plus_areas = _lib.dig_free_plus_areas
    dig_free_plus_areas.argtypes = [POINTER(struct_Plus_head)]
    dig_free_plus_areas.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 100
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_free_plus_isles'):
        continue
    dig_free_plus_isles = _lib.dig_free_plus_isles
    dig_free_plus_isles.argtypes = [POINTER(struct_Plus_head)]
    dig_free_plus_isles.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 101
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_free_plus'):
        continue
    dig_free_plus = _lib.dig_free_plus
    dig_free_plus.argtypes = [POINTER(struct_Plus_head)]
    dig_free_plus.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 102
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_load_plus'):
        continue
    dig_load_plus = _lib.dig_load_plus
    dig_load_plus.argtypes = [POINTER(struct_Plus_head), POINTER(struct_gvfile), c_int]
    dig_load_plus.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 103
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_plus_file'):
        continue
    dig_write_plus_file = _lib.dig_write_plus_file
    dig_write_plus_file.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_write_plus_file.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 104
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_nodes'):
        continue
    dig_write_nodes = _lib.dig_write_nodes
    dig_write_nodes.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_write_nodes.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 105
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_lines'):
        continue
    dig_write_lines = _lib.dig_write_lines
    dig_write_lines.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_write_lines.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 106
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_areas'):
        continue
    dig_write_areas = _lib.dig_write_areas
    dig_write_areas.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_write_areas.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 107
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_isles'):
        continue
    dig_write_isles = _lib.dig_write_isles
    dig_write_isles.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_write_isles.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 110
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_add_area'):
        continue
    dig_add_area = _lib.dig_add_area
    dig_add_area.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(plus_t), POINTER(struct_bound_box)]
    dig_add_area.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 111
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_area_add_isle'):
        continue
    dig_area_add_isle = _lib.dig_area_add_isle
    dig_area_add_isle.argtypes = [POINTER(struct_Plus_head), c_int, c_int]
    dig_area_add_isle.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 112
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_area_del_isle'):
        continue
    dig_area_del_isle = _lib.dig_area_del_isle
    dig_area_del_isle.argtypes = [POINTER(struct_Plus_head), c_int, c_int]
    dig_area_del_isle.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 113
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_del_area'):
        continue
    dig_del_area = _lib.dig_del_area
    dig_del_area.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_del_area.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 114
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_add_isle'):
        continue
    dig_add_isle = _lib.dig_add_isle
    dig_add_isle.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(plus_t), POINTER(struct_bound_box)]
    dig_add_isle.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 115
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_del_isle'):
        continue
    dig_del_isle = _lib.dig_del_isle
    dig_del_isle.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_del_isle.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 116
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_build_area_with_line'):
        continue
    dig_build_area_with_line = _lib.dig_build_area_with_line
    dig_build_area_with_line.argtypes = [POINTER(struct_Plus_head), plus_t, c_int, POINTER(POINTER(plus_t))]
    dig_build_area_with_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 117
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_angle_next_line'):
        continue
    dig_angle_next_line = _lib.dig_angle_next_line
    dig_angle_next_line.argtypes = [POINTER(struct_Plus_head), plus_t, c_int, c_int, POINTER(c_float)]
    dig_angle_next_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 118
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_node_angle_check'):
        continue
    dig_node_angle_check = _lib.dig_node_angle_check
    dig_node_angle_check.argtypes = [POINTER(struct_Plus_head), c_int, c_int]
    dig_node_angle_check.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 119
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_area_get_box'):
        continue
    dig_area_get_box = _lib.dig_area_get_box
    dig_area_get_box.argtypes = [POINTER(struct_Plus_head), plus_t, POINTER(struct_bound_box)]
    dig_area_get_box.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 120
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_isle_get_box'):
        continue
    dig_isle_get_box = _lib.dig_isle_get_box
    dig_isle_get_box.argtypes = [POINTER(struct_Plus_head), plus_t, POINTER(struct_bound_box)]
    dig_isle_get_box.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 123
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_add_line'):
        continue
    dig_add_line = _lib.dig_add_line
    dig_add_line.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_line_pnts), POINTER(struct_bound_box), off_t]
    dig_add_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 125
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_restore_line'):
        continue
    dig_restore_line = _lib.dig_restore_line
    dig_restore_line.argtypes = [POINTER(struct_Plus_head), c_int, c_int, POINTER(struct_line_pnts), POINTER(struct_bound_box), off_t]
    dig_restore_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 127
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_del_line'):
        continue
    dig_del_line = _lib.dig_del_line
    dig_del_line.argtypes = [POINTER(struct_Plus_head), c_int, c_double, c_double, c_double]
    dig_del_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 128
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_line_get_area'):
        continue
    dig_line_get_area = _lib.dig_line_get_area
    dig_line_get_area.argtypes = [POINTER(struct_Plus_head), plus_t, c_int]
    dig_line_get_area.restype = plus_t
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 129
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_line_set_area'):
        continue
    dig_line_set_area = _lib.dig_line_set_area
    dig_line_set_area.argtypes = [POINTER(struct_Plus_head), plus_t, c_int, plus_t]
    dig_line_set_area.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 132
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_add_node'):
        continue
    dig_add_node = _lib.dig_add_node
    dig_add_node.argtypes = [POINTER(struct_Plus_head), c_double, c_double, c_double]
    dig_add_node.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 133
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_which_node'):
        continue
    dig_which_node = _lib.dig_which_node
    dig_which_node.argtypes = [POINTER(struct_Plus_head), c_double, c_double, c_double]
    dig_which_node.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 135
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_node_add_line'):
        continue
    dig_node_add_line = _lib.dig_node_add_line
    dig_node_add_line.argtypes = [POINTER(struct_Plus_head), c_int, c_int, POINTER(struct_line_pnts), c_int]
    dig_node_add_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 136
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_node_line_angle'):
        continue
    dig_node_line_angle = _lib.dig_node_line_angle
    dig_node_line_angle.argtypes = [POINTER(struct_Plus_head), c_int, c_int]
    dig_node_line_angle.restype = c_float
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 139
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Rd_P_node'):
        continue
    dig_Rd_P_node = _lib.dig_Rd_P_node
    dig_Rd_P_node.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_gvfile)]
    dig_Rd_P_node.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 140
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Wr_P_node'):
        continue
    dig_Wr_P_node = _lib.dig_Wr_P_node
    dig_Wr_P_node.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_gvfile)]
    dig_Wr_P_node.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 141
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Rd_P_line'):
        continue
    dig_Rd_P_line = _lib.dig_Rd_P_line
    dig_Rd_P_line.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_gvfile)]
    dig_Rd_P_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 142
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Wr_P_line'):
        continue
    dig_Wr_P_line = _lib.dig_Wr_P_line
    dig_Wr_P_line.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_gvfile)]
    dig_Wr_P_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 143
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Rd_P_area'):
        continue
    dig_Rd_P_area = _lib.dig_Rd_P_area
    dig_Rd_P_area.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_gvfile)]
    dig_Rd_P_area.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 144
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Wr_P_area'):
        continue
    dig_Wr_P_area = _lib.dig_Wr_P_area
    dig_Wr_P_area.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_gvfile)]
    dig_Wr_P_area.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 145
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Rd_P_isle'):
        continue
    dig_Rd_P_isle = _lib.dig_Rd_P_isle
    dig_Rd_P_isle.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_gvfile)]
    dig_Rd_P_isle.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 146
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Wr_P_isle'):
        continue
    dig_Wr_P_isle = _lib.dig_Wr_P_isle
    dig_Wr_P_isle.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_gvfile)]
    dig_Wr_P_isle.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 147
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Rd_Plus_head'):
        continue
    dig_Rd_Plus_head = _lib.dig_Rd_Plus_head
    dig_Rd_Plus_head.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_Rd_Plus_head.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 148
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Wr_Plus_head'):
        continue
    dig_Wr_Plus_head = _lib.dig_Wr_Plus_head
    dig_Wr_Plus_head.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_Wr_Plus_head.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 151
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_find_area_poly'):
        continue
    dig_find_area_poly = _lib.dig_find_area_poly
    dig_find_area_poly.argtypes = [POINTER(struct_line_pnts), POINTER(c_double)]
    dig_find_area_poly.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 152
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_find_poly_orientation'):
        continue
    dig_find_poly_orientation = _lib.dig_find_poly_orientation
    dig_find_poly_orientation.argtypes = [POINTER(struct_line_pnts)]
    dig_find_poly_orientation.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 153
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_get_poly_points'):
        continue
    dig_get_poly_points = _lib.dig_get_poly_points
    dig_get_poly_points.argtypes = [c_int, POINTER(POINTER(struct_line_pnts)), POINTER(c_int), POINTER(struct_line_pnts)]
    dig_get_poly_points.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 156
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_init_portable'):
        continue
    dig_init_portable = _lib.dig_init_portable
    dig_init_portable.argtypes = [POINTER(struct_Port_info), c_int]
    dig_init_portable.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 157
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__byte_order_out'):
        continue
    dig__byte_order_out = _lib.dig__byte_order_out
    dig__byte_order_out.argtypes = []
    dig__byte_order_out.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 160
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_set_cur_port'):
        continue
    dig_set_cur_port = _lib.dig_set_cur_port
    dig_set_cur_port.argtypes = [POINTER(struct_Port_info)]
    dig_set_cur_port.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 162
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fread_port_D'):
        continue
    dig__fread_port_D = _lib.dig__fread_port_D
    dig__fread_port_D.argtypes = [POINTER(c_double), c_size_t, POINTER(struct_gvfile)]
    dig__fread_port_D.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 163
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fread_port_F'):
        continue
    dig__fread_port_F = _lib.dig__fread_port_F
    dig__fread_port_F.argtypes = [POINTER(c_float), c_size_t, POINTER(struct_gvfile)]
    dig__fread_port_F.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 164
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fread_port_O'):
        continue
    dig__fread_port_O = _lib.dig__fread_port_O
    dig__fread_port_O.argtypes = [POINTER(off_t), c_size_t, POINTER(struct_gvfile), c_size_t]
    dig__fread_port_O.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 165
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fread_port_L'):
        continue
    dig__fread_port_L = _lib.dig__fread_port_L
    dig__fread_port_L.argtypes = [POINTER(c_long), c_size_t, POINTER(struct_gvfile)]
    dig__fread_port_L.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 166
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fread_port_S'):
        continue
    dig__fread_port_S = _lib.dig__fread_port_S
    dig__fread_port_S.argtypes = [POINTER(c_short), c_size_t, POINTER(struct_gvfile)]
    dig__fread_port_S.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 167
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fread_port_I'):
        continue
    dig__fread_port_I = _lib.dig__fread_port_I
    dig__fread_port_I.argtypes = [POINTER(c_int), c_size_t, POINTER(struct_gvfile)]
    dig__fread_port_I.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 168
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fread_port_P'):
        continue
    dig__fread_port_P = _lib.dig__fread_port_P
    dig__fread_port_P.argtypes = [POINTER(plus_t), c_size_t, POINTER(struct_gvfile)]
    dig__fread_port_P.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 169
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fread_port_C'):
        continue
    dig__fread_port_C = _lib.dig__fread_port_C
    dig__fread_port_C.argtypes = [String, c_size_t, POINTER(struct_gvfile)]
    dig__fread_port_C.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 170
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fwrite_port_D'):
        continue
    dig__fwrite_port_D = _lib.dig__fwrite_port_D
    dig__fwrite_port_D.argtypes = [POINTER(c_double), c_size_t, POINTER(struct_gvfile)]
    dig__fwrite_port_D.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 171
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fwrite_port_F'):
        continue
    dig__fwrite_port_F = _lib.dig__fwrite_port_F
    dig__fwrite_port_F.argtypes = [POINTER(c_float), c_size_t, POINTER(struct_gvfile)]
    dig__fwrite_port_F.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 172
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fwrite_port_O'):
        continue
    dig__fwrite_port_O = _lib.dig__fwrite_port_O
    dig__fwrite_port_O.argtypes = [POINTER(off_t), c_size_t, POINTER(struct_gvfile), c_size_t]
    dig__fwrite_port_O.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 173
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fwrite_port_L'):
        continue
    dig__fwrite_port_L = _lib.dig__fwrite_port_L
    dig__fwrite_port_L.argtypes = [POINTER(c_long), c_size_t, POINTER(struct_gvfile)]
    dig__fwrite_port_L.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 174
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fwrite_port_S'):
        continue
    dig__fwrite_port_S = _lib.dig__fwrite_port_S
    dig__fwrite_port_S.argtypes = [POINTER(c_short), c_size_t, POINTER(struct_gvfile)]
    dig__fwrite_port_S.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 175
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fwrite_port_I'):
        continue
    dig__fwrite_port_I = _lib.dig__fwrite_port_I
    dig__fwrite_port_I.argtypes = [POINTER(c_int), c_size_t, POINTER(struct_gvfile)]
    dig__fwrite_port_I.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 176
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fwrite_port_P'):
        continue
    dig__fwrite_port_P = _lib.dig__fwrite_port_P
    dig__fwrite_port_P.argtypes = [POINTER(plus_t), c_size_t, POINTER(struct_gvfile)]
    dig__fwrite_port_P.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 177
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__fwrite_port_C'):
        continue
    dig__fwrite_port_C = _lib.dig__fwrite_port_C
    dig__fwrite_port_C.argtypes = [String, c_size_t, POINTER(struct_gvfile)]
    dig__fwrite_port_C.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 184
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_prune'):
        continue
    dig_prune = _lib.dig_prune
    dig_prune.argtypes = [POINTER(struct_line_pnts), c_double]
    dig_prune.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 188
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_init'):
        continue
    dig_spidx_init = _lib.dig_spidx_init
    dig_spidx_init.argtypes = [POINTER(struct_Plus_head)]
    dig_spidx_init.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 189
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_free_nodes'):
        continue
    dig_spidx_free_nodes = _lib.dig_spidx_free_nodes
    dig_spidx_free_nodes.argtypes = [POINTER(struct_Plus_head)]
    dig_spidx_free_nodes.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 190
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_free_lines'):
        continue
    dig_spidx_free_lines = _lib.dig_spidx_free_lines
    dig_spidx_free_lines.argtypes = [POINTER(struct_Plus_head)]
    dig_spidx_free_lines.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 191
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_free_areas'):
        continue
    dig_spidx_free_areas = _lib.dig_spidx_free_areas
    dig_spidx_free_areas.argtypes = [POINTER(struct_Plus_head)]
    dig_spidx_free_areas.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 192
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_free_isles'):
        continue
    dig_spidx_free_isles = _lib.dig_spidx_free_isles
    dig_spidx_free_isles.argtypes = [POINTER(struct_Plus_head)]
    dig_spidx_free_isles.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 193
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_free'):
        continue
    dig_spidx_free = _lib.dig_spidx_free
    dig_spidx_free.argtypes = [POINTER(struct_Plus_head)]
    dig_spidx_free.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 195
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_add_node'):
        continue
    dig_spidx_add_node = _lib.dig_spidx_add_node
    dig_spidx_add_node.argtypes = [POINTER(struct_Plus_head), c_int, c_double, c_double, c_double]
    dig_spidx_add_node.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 196
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_add_line'):
        continue
    dig_spidx_add_line = _lib.dig_spidx_add_line
    dig_spidx_add_line.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_bound_box)]
    dig_spidx_add_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 197
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_add_area'):
        continue
    dig_spidx_add_area = _lib.dig_spidx_add_area
    dig_spidx_add_area.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_bound_box)]
    dig_spidx_add_area.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 198
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_add_isle'):
        continue
    dig_spidx_add_isle = _lib.dig_spidx_add_isle
    dig_spidx_add_isle.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_bound_box)]
    dig_spidx_add_isle.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 200
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_del_node'):
        continue
    dig_spidx_del_node = _lib.dig_spidx_del_node
    dig_spidx_del_node.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_spidx_del_node.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 201
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_del_line'):
        continue
    dig_spidx_del_line = _lib.dig_spidx_del_line
    dig_spidx_del_line.argtypes = [POINTER(struct_Plus_head), c_int, c_double, c_double, c_double]
    dig_spidx_del_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 202
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_del_area'):
        continue
    dig_spidx_del_area = _lib.dig_spidx_del_area
    dig_spidx_del_area.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_spidx_del_area.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 203
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spidx_del_isle'):
        continue
    dig_spidx_del_isle = _lib.dig_spidx_del_isle
    dig_spidx_del_isle.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_spidx_del_isle.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 205
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_select_nodes'):
        continue
    dig_select_nodes = _lib.dig_select_nodes
    dig_select_nodes.argtypes = [POINTER(struct_Plus_head), POINTER(struct_bound_box), POINTER(struct_ilist)]
    dig_select_nodes.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 206
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_select_lines'):
        continue
    dig_select_lines = _lib.dig_select_lines
    dig_select_lines.argtypes = [POINTER(struct_Plus_head), POINTER(struct_bound_box), POINTER(struct_boxlist)]
    dig_select_lines.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 207
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_select_areas'):
        continue
    dig_select_areas = _lib.dig_select_areas
    dig_select_areas.argtypes = [POINTER(struct_Plus_head), POINTER(struct_bound_box), POINTER(struct_boxlist)]
    dig_select_areas.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 208
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_select_isles'):
        continue
    dig_select_isles = _lib.dig_select_isles
    dig_select_isles.argtypes = [POINTER(struct_Plus_head), POINTER(struct_bound_box), POINTER(struct_boxlist)]
    dig_select_isles.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 209
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_find_node'):
        continue
    dig_find_node = _lib.dig_find_node
    dig_find_node.argtypes = [POINTER(struct_Plus_head), c_double, c_double, c_double]
    dig_find_node.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 210
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_find_line_box'):
        continue
    dig_find_line_box = _lib.dig_find_line_box
    dig_find_line_box.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_bound_box)]
    dig_find_line_box.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 211
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_find_area_box'):
        continue
    dig_find_area_box = _lib.dig_find_area_box
    dig_find_area_box.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_bound_box)]
    dig_find_area_box.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 212
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_find_isle_box'):
        continue
    dig_find_isle_box = _lib.dig_find_isle_box
    dig_find_isle_box.argtypes = [POINTER(struct_Plus_head), c_int, POINTER(struct_bound_box)]
    dig_find_isle_box.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 215
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Rd_spidx_head'):
        continue
    dig_Rd_spidx_head = _lib.dig_Rd_spidx_head
    dig_Rd_spidx_head.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_Rd_spidx_head.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 216
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Wr_spidx_head'):
        continue
    dig_Wr_spidx_head = _lib.dig_Wr_spidx_head
    dig_Wr_spidx_head.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_Wr_spidx_head.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 217
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Wr_spidx'):
        continue
    dig_Wr_spidx = _lib.dig_Wr_spidx
    dig_Wr_spidx.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_Wr_spidx.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 218
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_Rd_spidx'):
        continue
    dig_Rd_spidx = _lib.dig_Rd_spidx
    dig_Rd_spidx.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_Rd_spidx.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 220
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_dump_spidx'):
        continue
    dig_dump_spidx = _lib.dig_dump_spidx
    dig_dump_spidx.argtypes = [POINTER(FILE), POINTER(struct_Plus_head)]
    dig_dump_spidx.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 222
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'rtree_search'):
        continue
    rtree_search = _lib.rtree_search
    rtree_search.argtypes = [POINTER(struct_RTree), POINTER(struct_RTree_Rect), SearchHitCallback, POINTER(None), POINTER(struct_Plus_head)]
    rtree_search.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 226
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_node_alloc_line'):
        continue
    dig_node_alloc_line = _lib.dig_node_alloc_line
    dig_node_alloc_line.argtypes = [POINTER(struct_P_node), c_int]
    dig_node_alloc_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 227
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_nodes'):
        continue
    dig_alloc_nodes = _lib.dig_alloc_nodes
    dig_alloc_nodes.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_alloc_nodes.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 228
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_lines'):
        continue
    dig_alloc_lines = _lib.dig_alloc_lines
    dig_alloc_lines.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_alloc_lines.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 229
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_areas'):
        continue
    dig_alloc_areas = _lib.dig_alloc_areas
    dig_alloc_areas.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_alloc_areas.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 230
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_isles'):
        continue
    dig_alloc_isles = _lib.dig_alloc_isles
    dig_alloc_isles.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_alloc_isles.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 231
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_node'):
        continue
    dig_alloc_node = _lib.dig_alloc_node
    dig_alloc_node.argtypes = []
    dig_alloc_node.restype = POINTER(struct_P_node)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 232
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_line'):
        continue
    dig_alloc_line = _lib.dig_alloc_line
    dig_alloc_line.argtypes = []
    dig_alloc_line.restype = POINTER(struct_P_line)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 233
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_topo'):
        continue
    dig_alloc_topo = _lib.dig_alloc_topo
    dig_alloc_topo.argtypes = [c_char]
    dig_alloc_topo.restype = POINTER(c_ubyte)
    dig_alloc_topo.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 234
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_area'):
        continue
    dig_alloc_area = _lib.dig_alloc_area
    dig_alloc_area.argtypes = []
    dig_alloc_area.restype = POINTER(struct_P_area)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 235
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_isle'):
        continue
    dig_alloc_isle = _lib.dig_alloc_isle
    dig_alloc_isle.argtypes = []
    dig_alloc_isle.restype = POINTER(struct_P_isle)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 236
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_free_node'):
        continue
    dig_free_node = _lib.dig_free_node
    dig_free_node.argtypes = [POINTER(struct_P_node)]
    dig_free_node.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 237
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_free_line'):
        continue
    dig_free_line = _lib.dig_free_line
    dig_free_line.argtypes = [POINTER(struct_P_line)]
    dig_free_line.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 238
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_free_area'):
        continue
    dig_free_area = _lib.dig_free_area
    dig_free_area.argtypes = [POINTER(struct_P_area)]
    dig_free_area.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 239
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_free_isle'):
        continue
    dig_free_isle = _lib.dig_free_isle
    dig_free_isle.argtypes = [POINTER(struct_P_isle)]
    dig_free_isle.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 240
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_points'):
        continue
    dig_alloc_points = _lib.dig_alloc_points
    dig_alloc_points.argtypes = [POINTER(struct_line_pnts), c_int]
    dig_alloc_points.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 241
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_alloc_cats'):
        continue
    dig_alloc_cats = _lib.dig_alloc_cats
    dig_alloc_cats.argtypes = [POINTER(struct_line_cats), c_int]
    dig_alloc_cats.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 242
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_area_alloc_line'):
        continue
    dig_area_alloc_line = _lib.dig_area_alloc_line
    dig_area_alloc_line.argtypes = [POINTER(struct_P_area), c_int]
    dig_area_alloc_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 243
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_area_alloc_isle'):
        continue
    dig_area_alloc_isle = _lib.dig_area_alloc_isle
    dig_area_alloc_isle.argtypes = [POINTER(struct_P_area), c_int]
    dig_area_alloc_isle.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 244
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_isle_alloc_line'):
        continue
    dig_isle_alloc_line = _lib.dig_isle_alloc_line
    dig_isle_alloc_line.argtypes = [POINTER(struct_P_isle), c_int]
    dig_isle_alloc_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 245
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_out_of_memory'):
        continue
    dig_out_of_memory = _lib.dig_out_of_memory
    dig_out_of_memory.argtypes = []
    dig_out_of_memory.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 249
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_type_to_store'):
        continue
    dig_type_to_store = _lib.dig_type_to_store
    dig_type_to_store.argtypes = [c_int]
    dig_type_to_store.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 250
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_type_from_store'):
        continue
    dig_type_from_store = _lib.dig_type_from_store
    dig_type_from_store.argtypes = [c_int]
    dig_type_from_store.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 254
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_line_reset_updated'):
        continue
    dig_line_reset_updated = _lib.dig_line_reset_updated
    dig_line_reset_updated.argtypes = [POINTER(struct_Plus_head)]
    dig_line_reset_updated.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 255
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_line_add_updated'):
        continue
    dig_line_add_updated = _lib.dig_line_add_updated
    dig_line_add_updated.argtypes = [POINTER(struct_Plus_head), c_int, off_t]
    dig_line_add_updated.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 256
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_node_reset_updated'):
        continue
    dig_node_reset_updated = _lib.dig_node_reset_updated
    dig_node_reset_updated.argtypes = [POINTER(struct_Plus_head)]
    dig_node_reset_updated.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 257
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_node_add_updated'):
        continue
    dig_node_add_updated = _lib.dig_node_add_updated
    dig_node_add_updated.argtypes = [POINTER(struct_Plus_head), c_int]
    dig_node_add_updated.restype = None
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 264
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'color_name'):
        continue
    color_name = _lib.color_name
    color_name.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        color_name.restype = ReturnString
    else:
        color_name.restype = String
        color_name.errcheck = ReturnString
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 266
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_float_point'):
        continue
    dig_float_point = _lib.dig_float_point
    dig_float_point.argtypes = [String, c_int, c_double]
    if sizeof(c_int) == sizeof(c_void_p):
        dig_float_point.restype = ReturnString
    else:
        dig_float_point.restype = String
        dig_float_point.errcheck = ReturnString
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 270
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_unit_conversion'):
        continue
    dig_unit_conversion = _lib.dig_unit_conversion
    dig_unit_conversion.argtypes = []
    dig_unit_conversion.restype = c_double
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 273
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__double_convert'):
        continue
    dig__double_convert = _lib.dig__double_convert
    dig__double_convert.argtypes = [POINTER(c_double), POINTER(c_double), c_int, POINTER(struct_dig_head)]
    dig__double_convert.restype = POINTER(c_double)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 274
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__float_convert'):
        continue
    dig__float_convert = _lib.dig__float_convert
    dig__float_convert.argtypes = [POINTER(c_float), POINTER(c_float), c_int, POINTER(struct_dig_head)]
    dig__float_convert.restype = POINTER(c_float)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 275
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__short_convert'):
        continue
    dig__short_convert = _lib.dig__short_convert
    dig__short_convert.argtypes = [POINTER(c_short), POINTER(c_short), c_int, POINTER(struct_dig_head)]
    dig__short_convert.restype = POINTER(c_short)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 276
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__long_convert'):
        continue
    dig__long_convert = _lib.dig__long_convert
    dig__long_convert.argtypes = [POINTER(c_long), POINTER(c_long), c_int, POINTER(struct_dig_head)]
    dig__long_convert.restype = POINTER(c_long)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 277
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__int_convert'):
        continue
    dig__int_convert = _lib.dig__int_convert
    dig__int_convert.argtypes = [POINTER(c_int), POINTER(c_long), c_int, POINTER(struct_dig_head)]
    dig__int_convert.restype = POINTER(c_long)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 278
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__plus_t_convert'):
        continue
    dig__plus_t_convert = _lib.dig__plus_t_convert
    dig__plus_t_convert.argtypes = [POINTER(plus_t), POINTER(c_long), c_int, POINTER(struct_dig_head)]
    dig__plus_t_convert.restype = POINTER(c_long)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 279
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__long_convert_to_int'):
        continue
    dig__long_convert_to_int = _lib.dig__long_convert_to_int
    dig__long_convert_to_int.argtypes = [POINTER(c_long), POINTER(c_int), c_int, POINTER(struct_dig_head)]
    dig__long_convert_to_int.restype = POINTER(c_int)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 280
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__long_convert_to_plus_t'):
        continue
    dig__long_convert_to_plus_t = _lib.dig__long_convert_to_plus_t
    dig__long_convert_to_plus_t.argtypes = [POINTER(c_long), POINTER(plus_t), c_int, POINTER(struct_dig_head)]
    dig__long_convert_to_plus_t.restype = POINTER(plus_t)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 281
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__convert_buffer'):
        continue
    dig__convert_buffer = _lib.dig__convert_buffer
    dig__convert_buffer.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        dig__convert_buffer.restype = ReturnString
    else:
        dig__convert_buffer.restype = String
        dig__convert_buffer.errcheck = ReturnString
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 283
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_get_cont_lines'):
        continue
    dig_get_cont_lines = _lib.dig_get_cont_lines
    dig_get_cont_lines.argtypes = [POINTER(struct_Map_info), plus_t, c_double, c_int]
    dig_get_cont_lines.restype = POINTER(POINTER(plus_t))
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 284
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_get_next_cont_line'):
        continue
    dig_get_next_cont_line = _lib.dig_get_next_cont_line
    dig_get_next_cont_line.argtypes = [POINTER(struct_Map_info), plus_t, c_double, c_int]
    dig_get_next_cont_line.restype = plus_t
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 286
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_get_head'):
        continue
    dig_get_head = _lib.dig_get_head
    dig_get_head.argtypes = []
    dig_get_head.restype = POINTER(struct_dig_head)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 287
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__get_head'):
        continue
    dig__get_head = _lib.dig__get_head
    dig__get_head.argtypes = []
    dig__get_head.restype = POINTER(struct_dig_head)
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 292
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_start_clock'):
        continue
    dig_start_clock = _lib.dig_start_clock
    dig_start_clock.argtypes = [POINTER(c_long)]
    dig_start_clock.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 293
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_stop_clock'):
        continue
    dig_stop_clock = _lib.dig_stop_clock
    dig_stop_clock.argtypes = [POINTER(c_long)]
    dig_stop_clock.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 294
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_stop_clock_str'):
        continue
    dig_stop_clock_str = _lib.dig_stop_clock_str
    dig_stop_clock_str.argtypes = [POINTER(c_long)]
    if sizeof(c_int) == sizeof(c_void_p):
        dig_stop_clock_str.restype = ReturnString
    else:
        dig_stop_clock_str.restype = String
        dig_stop_clock_str.errcheck = ReturnString
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 295
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_file_checks'):
        continue
    dig_write_file_checks = _lib.dig_write_file_checks
    dig_write_file_checks.argtypes = [POINTER(struct_gvfile), POINTER(struct_Plus_head)]
    dig_write_file_checks.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 296
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_do_file_checks'):
        continue
    dig_do_file_checks = _lib.dig_do_file_checks
    dig_do_file_checks.argtypes = [POINTER(struct_Map_info), String, String]
    dig_do_file_checks.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 301
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_map_to_head'):
        continue
    dig_map_to_head = _lib.dig_map_to_head
    dig_map_to_head.argtypes = [POINTER(struct_Map_info), POINTER(struct_Plus_head)]
    dig_map_to_head.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 302
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_head_to_map'):
        continue
    dig_head_to_map = _lib.dig_head_to_map
    dig_head_to_map.argtypes = [POINTER(struct_Plus_head), POINTER(struct_Map_info)]
    dig_head_to_map.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 303
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_spindex_init'):
        continue
    dig_spindex_init = _lib.dig_spindex_init
    dig_spindex_init.argtypes = [POINTER(struct_Plus_head)]
    dig_spindex_init.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 309
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_point_to_area'):
        continue
    dig_point_to_area = _lib.dig_point_to_area
    dig_point_to_area.argtypes = [POINTER(struct_Map_info), c_double, c_double]
    dig_point_to_area.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 310
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_point_to_next_area'):
        continue
    dig_point_to_next_area = _lib.dig_point_to_next_area
    dig_point_to_next_area.argtypes = [POINTER(struct_Map_info), c_double, c_double, POINTER(c_double)]
    dig_point_to_next_area.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 311
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_point_to_line'):
        continue
    dig_point_to_line = _lib.dig_point_to_line
    dig_point_to_line.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_char]
    dig_point_to_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 314
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_check_dist'):
        continue
    dig_check_dist = _lib.dig_check_dist
    dig_check_dist.argtypes = [POINTER(struct_Map_info), c_int, c_double, c_double, POINTER(c_double)]
    dig_check_dist.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 315
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig__check_dist'):
        continue
    dig__check_dist = _lib.dig__check_dist
    dig__check_dist.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), c_double, c_double, POINTER(c_double)]
    dig__check_dist.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 318
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_point_by_line'):
        continue
    dig_point_by_line = _lib.dig_point_by_line
    dig_point_by_line.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double, c_char]
    dig_point_by_line.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 321
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_write_head_ascii'):
        continue
    dig_write_head_ascii = _lib.dig_write_head_ascii
    dig_write_head_ascii.argtypes = [POINTER(FILE), POINTER(struct_dig_head)]
    dig_write_head_ascii.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 322
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_read_head_ascii'):
        continue
    dig_read_head_ascii = _lib.dig_read_head_ascii
    dig_read_head_ascii.argtypes = [POINTER(FILE), POINTER(struct_dig_head)]
    dig_read_head_ascii.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 324
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_struct_copy'):
        continue
    dig_struct_copy = _lib.dig_struct_copy
    dig_struct_copy.argtypes = [POINTER(None), POINTER(None), c_int]
    dig_struct_copy.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_externs.h: 325
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'dig_rmcr'):
        continue
    dig_rmcr = _lib.dig_rmcr
    dig_rmcr.argtypes = [String]
    dig_rmcr.restype = c_int
    break

# C:/OSGeo4W64/include/geos_c.h: 108
class struct_GEOSGeom_t(Structure):
    pass

GEOSGeometry = struct_GEOSGeom_t # C:/OSGeo4W64/include/geos_c.h: 108

# C:/OSGeo4W64/include/geos_c.h: 110
class struct_GEOSCoordSeq_t(Structure):
    pass

GEOSCoordSequence = struct_GEOSCoordSeq_t # C:/OSGeo4W64/include/geos_c.h: 110

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 8
if hasattr(_libs['grass_vector.7.8'], 'Vect_new_line_struct'):
    Vect_new_line_struct = _libs['grass_vector.7.8'].Vect_new_line_struct
    Vect_new_line_struct.argtypes = []
    Vect_new_line_struct.restype = POINTER(struct_line_pnts)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 9
if hasattr(_libs['grass_vector.7.8'], 'Vect_append_point'):
    Vect_append_point = _libs['grass_vector.7.8'].Vect_append_point
    Vect_append_point.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_double]
    Vect_append_point.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 10
if hasattr(_libs['grass_vector.7.8'], 'Vect_append_points'):
    Vect_append_points = _libs['grass_vector.7.8'].Vect_append_points
    Vect_append_points.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]
    Vect_append_points.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 11
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_insert_point'):
    Vect_line_insert_point = _libs['grass_vector.7.8'].Vect_line_insert_point
    Vect_line_insert_point.argtypes = [POINTER(struct_line_pnts), c_int, c_double, c_double, c_double]
    Vect_line_insert_point.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 12
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_delete_point'):
    Vect_line_delete_point = _libs['grass_vector.7.8'].Vect_line_delete_point
    Vect_line_delete_point.argtypes = [POINTER(struct_line_pnts), c_int]
    Vect_line_delete_point.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 13
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_get_point'):
    Vect_line_get_point = _libs['grass_vector.7.8'].Vect_line_get_point
    Vect_line_get_point.argtypes = [POINTER(struct_line_pnts), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Vect_line_get_point.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 15
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_line_points'):
    Vect_get_num_line_points = _libs['grass_vector.7.8'].Vect_get_num_line_points
    Vect_get_num_line_points.argtypes = [POINTER(struct_line_pnts)]
    Vect_get_num_line_points.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 16
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_prune'):
    Vect_line_prune = _libs['grass_vector.7.8'].Vect_line_prune
    Vect_line_prune.argtypes = [POINTER(struct_line_pnts)]
    Vect_line_prune.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 17
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_prune_thresh'):
    Vect_line_prune_thresh = _libs['grass_vector.7.8'].Vect_line_prune_thresh
    Vect_line_prune_thresh.argtypes = [POINTER(struct_line_pnts), c_double]
    Vect_line_prune_thresh.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 18
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_reverse'):
    Vect_line_reverse = _libs['grass_vector.7.8'].Vect_line_reverse
    Vect_line_reverse.argtypes = [POINTER(struct_line_pnts)]
    Vect_line_reverse.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 19
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_xyz_to_pnts'):
    Vect_copy_xyz_to_pnts = _libs['grass_vector.7.8'].Vect_copy_xyz_to_pnts
    Vect_copy_xyz_to_pnts.argtypes = [POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    Vect_copy_xyz_to_pnts.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 21
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_pnts_to_xyz'):
    Vect_copy_pnts_to_xyz = _libs['grass_vector.7.8'].Vect_copy_pnts_to_xyz
    Vect_copy_pnts_to_xyz.argtypes = [POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int)]
    Vect_copy_pnts_to_xyz.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 23
if hasattr(_libs['grass_vector.7.8'], 'Vect_reset_line'):
    Vect_reset_line = _libs['grass_vector.7.8'].Vect_reset_line
    Vect_reset_line.argtypes = [POINTER(struct_line_pnts)]
    Vect_reset_line.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 24
if hasattr(_libs['grass_vector.7.8'], 'Vect_destroy_line_struct'):
    Vect_destroy_line_struct = _libs['grass_vector.7.8'].Vect_destroy_line_struct
    Vect_destroy_line_struct.argtypes = [POINTER(struct_line_pnts)]
    Vect_destroy_line_struct.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 25
if hasattr(_libs['grass_vector.7.8'], 'Vect_point_on_line'):
    Vect_point_on_line = _libs['grass_vector.7.8'].Vect_point_on_line
    Vect_point_on_line.argtypes = [POINTER(struct_line_pnts), c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Vect_point_on_line.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 27
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_segment'):
    Vect_line_segment = _libs['grass_vector.7.8'].Vect_line_segment
    Vect_line_segment.argtypes = [POINTER(struct_line_pnts), c_double, c_double, POINTER(struct_line_pnts)]
    Vect_line_segment.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 28
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_length'):
    Vect_line_length = _libs['grass_vector.7.8'].Vect_line_length
    Vect_line_length.argtypes = [POINTER(struct_line_pnts)]
    Vect_line_length.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 29
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_geodesic_length'):
    Vect_line_geodesic_length = _libs['grass_vector.7.8'].Vect_line_geodesic_length
    Vect_line_geodesic_length.argtypes = [POINTER(struct_line_pnts)]
    Vect_line_geodesic_length.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 30
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_distance'):
    Vect_line_distance = _libs['grass_vector.7.8'].Vect_line_distance
    Vect_line_distance.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_double, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Vect_line_distance.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 33
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_geodesic_distance'):
    Vect_line_geodesic_distance = _libs['grass_vector.7.8'].Vect_line_geodesic_distance
    Vect_line_geodesic_distance.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_double, c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Vect_line_geodesic_distance.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 36
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_box'):
    Vect_line_box = _libs['grass_vector.7.8'].Vect_line_box
    Vect_line_box.argtypes = [POINTER(struct_line_pnts), POINTER(struct_bound_box)]
    Vect_line_box.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 37
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_parallel'):
    Vect_line_parallel = _libs['grass_vector.7.8'].Vect_line_parallel
    Vect_line_parallel.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_int, POINTER(struct_line_pnts)]
    Vect_line_parallel.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 39
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_parallel2'):
    Vect_line_parallel2 = _libs['grass_vector.7.8'].Vect_line_parallel2
    Vect_line_parallel2.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_double, c_int, c_int, c_double, POINTER(struct_line_pnts)]
    Vect_line_parallel2.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 42
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_buffer'):
    Vect_line_buffer = _libs['grass_vector.7.8'].Vect_line_buffer
    Vect_line_buffer.argtypes = [POINTER(struct_line_pnts), c_double, c_double, POINTER(struct_line_pnts)]
    Vect_line_buffer.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 43
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_buffer2'):
    Vect_line_buffer2 = _libs['grass_vector.7.8'].Vect_line_buffer2
    Vect_line_buffer2.argtypes = [POINTER(struct_line_pnts), c_double, c_double, c_double, c_int, c_int, c_double, POINTER(POINTER(struct_line_pnts)), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(c_int)]
    Vect_line_buffer2.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 47
if hasattr(_libs['grass_vector.7.8'], 'Vect_area_buffer2'):
    Vect_area_buffer2 = _libs['grass_vector.7.8'].Vect_area_buffer2
    Vect_area_buffer2.argtypes = [POINTER(struct_Map_info), c_int, c_double, c_double, c_double, c_int, c_int, c_double, POINTER(POINTER(struct_line_pnts)), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(c_int)]
    Vect_area_buffer2.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 51
if hasattr(_libs['grass_vector.7.8'], 'Vect_point_buffer2'):
    Vect_point_buffer2 = _libs['grass_vector.7.8'].Vect_point_buffer2
    Vect_point_buffer2.argtypes = [c_double, c_double, c_double, c_double, c_double, c_int, c_double, POINTER(POINTER(struct_line_pnts))]
    Vect_point_buffer2.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 57
if hasattr(_libs['grass_vector.7.8'], 'Vect_new_cats_struct'):
    Vect_new_cats_struct = _libs['grass_vector.7.8'].Vect_new_cats_struct
    Vect_new_cats_struct.argtypes = []
    Vect_new_cats_struct.restype = POINTER(struct_line_cats)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 58
if hasattr(_libs['grass_vector.7.8'], 'Vect_cat_set'):
    Vect_cat_set = _libs['grass_vector.7.8'].Vect_cat_set
    Vect_cat_set.argtypes = [POINTER(struct_line_cats), c_int, c_int]
    Vect_cat_set.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 59
if hasattr(_libs['grass_vector.7.8'], 'Vect_cat_get'):
    Vect_cat_get = _libs['grass_vector.7.8'].Vect_cat_get
    Vect_cat_get.argtypes = [POINTER(struct_line_cats), c_int, POINTER(c_int)]
    Vect_cat_get.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 60
if hasattr(_libs['grass_vector.7.8'], 'Vect_cat_del'):
    Vect_cat_del = _libs['grass_vector.7.8'].Vect_cat_del
    Vect_cat_del.argtypes = [POINTER(struct_line_cats), c_int]
    Vect_cat_del.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 61
if hasattr(_libs['grass_vector.7.8'], 'Vect_field_cat_del'):
    Vect_field_cat_del = _libs['grass_vector.7.8'].Vect_field_cat_del
    Vect_field_cat_del.argtypes = [POINTER(struct_line_cats), c_int, c_int]
    Vect_field_cat_del.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 62
if hasattr(_libs['grass_vector.7.8'], 'Vect_field_cat_get'):
    Vect_field_cat_get = _libs['grass_vector.7.8'].Vect_field_cat_get
    Vect_field_cat_get.argtypes = [POINTER(struct_line_cats), c_int, POINTER(struct_ilist)]
    Vect_field_cat_get.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 63
if hasattr(_libs['grass_vector.7.8'], 'Vect_cat_in_array'):
    Vect_cat_in_array = _libs['grass_vector.7.8'].Vect_cat_in_array
    Vect_cat_in_array.argtypes = [c_int, POINTER(c_int), c_int]
    Vect_cat_in_array.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 64
if hasattr(_libs['grass_vector.7.8'], 'Vect_reset_cats'):
    Vect_reset_cats = _libs['grass_vector.7.8'].Vect_reset_cats
    Vect_reset_cats.argtypes = [POINTER(struct_line_cats)]
    Vect_reset_cats.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 65
if hasattr(_libs['grass_vector.7.8'], 'Vect_destroy_cats_struct'):
    Vect_destroy_cats_struct = _libs['grass_vector.7.8'].Vect_destroy_cats_struct
    Vect_destroy_cats_struct.argtypes = [POINTER(struct_line_cats)]
    Vect_destroy_cats_struct.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 66
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_cats'):
    Vect_get_area_cats = _libs['grass_vector.7.8'].Vect_get_area_cats
    Vect_get_area_cats.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_cats)]
    Vect_get_area_cats.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 67
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_cat'):
    Vect_get_area_cat = _libs['grass_vector.7.8'].Vect_get_area_cat
    Vect_get_area_cat.argtypes = [POINTER(struct_Map_info), c_int, c_int]
    Vect_get_area_cat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 68
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_line_cat'):
    Vect_get_line_cat = _libs['grass_vector.7.8'].Vect_get_line_cat
    Vect_get_line_cat.argtypes = [POINTER(struct_Map_info), c_int, c_int]
    Vect_get_line_cat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 69
if hasattr(_libs['grass_vector.7.8'], 'Vect_cats_set_constraint'):
    Vect_cats_set_constraint = _libs['grass_vector.7.8'].Vect_cats_set_constraint
    Vect_cats_set_constraint.argtypes = [POINTER(struct_Map_info), c_int, String, String]
    Vect_cats_set_constraint.restype = POINTER(struct_cat_list)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 70
if hasattr(_libs['grass_vector.7.8'], 'Vect_cats_in_constraint'):
    Vect_cats_in_constraint = _libs['grass_vector.7.8'].Vect_cats_in_constraint
    Vect_cats_in_constraint.argtypes = [POINTER(struct_line_cats), c_int, POINTER(struct_cat_list)]
    Vect_cats_in_constraint.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 73
if hasattr(_libs['grass_vector.7.8'], 'Vect_new_cat_list'):
    Vect_new_cat_list = _libs['grass_vector.7.8'].Vect_new_cat_list
    Vect_new_cat_list.argtypes = []
    Vect_new_cat_list.restype = POINTER(struct_cat_list)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 74
if hasattr(_libs['grass_vector.7.8'], 'Vect_str_to_cat_list'):
    Vect_str_to_cat_list = _libs['grass_vector.7.8'].Vect_str_to_cat_list
    Vect_str_to_cat_list.argtypes = [String, POINTER(struct_cat_list)]
    Vect_str_to_cat_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 75
if hasattr(_libs['grass_vector.7.8'], 'Vect_array_to_cat_list'):
    Vect_array_to_cat_list = _libs['grass_vector.7.8'].Vect_array_to_cat_list
    Vect_array_to_cat_list.argtypes = [POINTER(c_int), c_int, POINTER(struct_cat_list)]
    Vect_array_to_cat_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 76
if hasattr(_libs['grass_vector.7.8'], 'Vect_cat_list_to_array'):
    Vect_cat_list_to_array = _libs['grass_vector.7.8'].Vect_cat_list_to_array
    Vect_cat_list_to_array.argtypes = [POINTER(struct_cat_list), POINTER(POINTER(c_int)), POINTER(c_int)]
    Vect_cat_list_to_array.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 77
if hasattr(_libs['grass_vector.7.8'], 'Vect_cat_in_cat_list'):
    Vect_cat_in_cat_list = _libs['grass_vector.7.8'].Vect_cat_in_cat_list
    Vect_cat_in_cat_list.argtypes = [c_int, POINTER(struct_cat_list)]
    Vect_cat_in_cat_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 78
if hasattr(_libs['grass_vector.7.8'], 'Vect_destroy_cat_list'):
    Vect_destroy_cat_list = _libs['grass_vector.7.8'].Vect_destroy_cat_list
    Vect_destroy_cat_list.argtypes = [POINTER(struct_cat_list)]
    Vect_destroy_cat_list.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 81
if hasattr(_libs['grass_vector.7.8'], 'Vect_new_varray'):
    Vect_new_varray = _libs['grass_vector.7.8'].Vect_new_varray
    Vect_new_varray.argtypes = [c_int]
    Vect_new_varray.restype = POINTER(struct_varray)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 82
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_varray_from_cat_string'):
    Vect_set_varray_from_cat_string = _libs['grass_vector.7.8'].Vect_set_varray_from_cat_string
    Vect_set_varray_from_cat_string.argtypes = [POINTER(struct_Map_info), c_int, String, c_int, c_int, POINTER(struct_varray)]
    Vect_set_varray_from_cat_string.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 84
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_varray_from_cat_list'):
    Vect_set_varray_from_cat_list = _libs['grass_vector.7.8'].Vect_set_varray_from_cat_list
    Vect_set_varray_from_cat_list.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_cat_list), c_int, c_int, POINTER(struct_varray)]
    Vect_set_varray_from_cat_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 86
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_varray_from_db'):
    Vect_set_varray_from_db = _libs['grass_vector.7.8'].Vect_set_varray_from_db
    Vect_set_varray_from_db.argtypes = [POINTER(struct_Map_info), c_int, String, c_int, c_int, POINTER(struct_varray)]
    Vect_set_varray_from_db.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 90
if hasattr(_libs['grass_vector.7.8'], 'Vect_new_dblinks_struct'):
    Vect_new_dblinks_struct = _libs['grass_vector.7.8'].Vect_new_dblinks_struct
    Vect_new_dblinks_struct.argtypes = []
    Vect_new_dblinks_struct.restype = POINTER(struct_dblinks)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 91
if hasattr(_libs['grass_vector.7.8'], 'Vect_reset_dblinks'):
    Vect_reset_dblinks = _libs['grass_vector.7.8'].Vect_reset_dblinks
    Vect_reset_dblinks.argtypes = [POINTER(struct_dblinks)]
    Vect_reset_dblinks.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 92
if hasattr(_libs['grass_vector.7.8'], 'Vect_add_dblink'):
    Vect_add_dblink = _libs['grass_vector.7.8'].Vect_add_dblink
    Vect_add_dblink.argtypes = [POINTER(struct_dblinks), c_int, String, String, String, String, String]
    Vect_add_dblink.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 94
if hasattr(_libs['grass_vector.7.8'], 'Vect_check_dblink'):
    Vect_check_dblink = _libs['grass_vector.7.8'].Vect_check_dblink
    Vect_check_dblink.argtypes = [POINTER(struct_dblinks), c_int, String]
    Vect_check_dblink.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 95
if hasattr(_libs['grass_vector.7.8'], 'Vect_map_add_dblink'):
    Vect_map_add_dblink = _libs['grass_vector.7.8'].Vect_map_add_dblink
    Vect_map_add_dblink.argtypes = [POINTER(struct_Map_info), c_int, String, String, String, String, String]
    Vect_map_add_dblink.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 98
if hasattr(_libs['grass_vector.7.8'], 'Vect_map_del_dblink'):
    Vect_map_del_dblink = _libs['grass_vector.7.8'].Vect_map_del_dblink
    Vect_map_del_dblink.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_map_del_dblink.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 99
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_map_dblinks'):
    Vect_copy_map_dblinks = _libs['grass_vector.7.8'].Vect_copy_map_dblinks
    Vect_copy_map_dblinks.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), c_int]
    Vect_copy_map_dblinks.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 100
if hasattr(_libs['grass_vector.7.8'], 'Vect_map_check_dblink'):
    Vect_map_check_dblink = _libs['grass_vector.7.8'].Vect_map_check_dblink
    Vect_map_check_dblink.argtypes = [POINTER(struct_Map_info), c_int, String]
    Vect_map_check_dblink.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 101
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_dblinks'):
    Vect_read_dblinks = _libs['grass_vector.7.8'].Vect_read_dblinks
    Vect_read_dblinks.argtypes = [POINTER(struct_Map_info)]
    Vect_read_dblinks.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 102
if hasattr(_libs['grass_vector.7.8'], 'Vect_write_dblinks'):
    Vect_write_dblinks = _libs['grass_vector.7.8'].Vect_write_dblinks
    Vect_write_dblinks.argtypes = [POINTER(struct_Map_info)]
    Vect_write_dblinks.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 103
if hasattr(_libs['grass_vector.7.8'], 'Vect_default_field_info'):
    Vect_default_field_info = _libs['grass_vector.7.8'].Vect_default_field_info
    Vect_default_field_info.argtypes = [POINTER(struct_Map_info), c_int, String, c_int]
    Vect_default_field_info.restype = POINTER(struct_field_info)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 105
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_dblink'):
    Vect_get_dblink = _libs['grass_vector.7.8'].Vect_get_dblink
    Vect_get_dblink.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_dblink.restype = POINTER(struct_field_info)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 106
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_field'):
    Vect_get_field = _libs['grass_vector.7.8'].Vect_get_field
    Vect_get_field.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_field.restype = POINTER(struct_field_info)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 107
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_field_by_name'):
    Vect_get_field_by_name = _libs['grass_vector.7.8'].Vect_get_field_by_name
    Vect_get_field_by_name.argtypes = [POINTER(struct_Map_info), String]
    Vect_get_field_by_name.restype = POINTER(struct_field_info)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 108
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_field2'):
    Vect_get_field2 = _libs['grass_vector.7.8'].Vect_get_field2
    Vect_get_field2.argtypes = [POINTER(struct_Map_info), String]
    Vect_get_field2.restype = POINTER(struct_field_info)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 109
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_field_number'):
    Vect_get_field_number = _libs['grass_vector.7.8'].Vect_get_field_number
    Vect_get_field_number.argtypes = [POINTER(struct_Map_info), String]
    Vect_get_field_number.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 110
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_db_updated'):
    Vect_set_db_updated = _libs['grass_vector.7.8'].Vect_set_db_updated
    Vect_set_db_updated.argtypes = [POINTER(struct_Map_info)]
    Vect_set_db_updated.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 111
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_column_names'):
    Vect_get_column_names = _libs['grass_vector.7.8'].Vect_get_column_names
    Vect_get_column_names.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_column_names.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 112
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_column_types'):
    Vect_get_column_types = _libs['grass_vector.7.8'].Vect_get_column_types
    Vect_get_column_types.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_column_types.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 113
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_column_names_types'):
    Vect_get_column_names_types = _libs['grass_vector.7.8'].Vect_get_column_names_types
    Vect_get_column_names_types.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_column_names_types.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 116
if hasattr(_libs['grass_vector.7.8'], 'Vect_new_list'):
    Vect_new_list = _libs['grass_vector.7.8'].Vect_new_list
    Vect_new_list.argtypes = []
    Vect_new_list.restype = POINTER(struct_ilist)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 117
if hasattr(_libs['grass_vector.7.8'], 'Vect_list_append'):
    Vect_list_append = _libs['grass_vector.7.8'].Vect_list_append
    Vect_list_append.argtypes = [POINTER(struct_ilist), c_int]
    Vect_list_append.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 118
if hasattr(_libs['grass_vector.7.8'], 'Vect_list_append_list'):
    Vect_list_append_list = _libs['grass_vector.7.8'].Vect_list_append_list
    Vect_list_append_list.argtypes = [POINTER(struct_ilist), POINTER(struct_ilist)]
    Vect_list_append_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 119
if hasattr(_libs['grass_vector.7.8'], 'Vect_list_delete'):
    Vect_list_delete = _libs['grass_vector.7.8'].Vect_list_delete
    Vect_list_delete.argtypes = [POINTER(struct_ilist), c_int]
    Vect_list_delete.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 120
if hasattr(_libs['grass_vector.7.8'], 'Vect_list_delete_list'):
    Vect_list_delete_list = _libs['grass_vector.7.8'].Vect_list_delete_list
    Vect_list_delete_list.argtypes = [POINTER(struct_ilist), POINTER(struct_ilist)]
    Vect_list_delete_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 121
if hasattr(_libs['grass_vector.7.8'], 'Vect_val_in_list'):
    Vect_val_in_list = _libs['grass_vector.7.8'].Vect_val_in_list
    Vect_val_in_list.argtypes = [POINTER(struct_ilist), c_int]
    Vect_val_in_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 122
if hasattr(_libs['grass_vector.7.8'], 'Vect_reset_list'):
    Vect_reset_list = _libs['grass_vector.7.8'].Vect_reset_list
    Vect_reset_list.argtypes = [POINTER(struct_ilist)]
    Vect_reset_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 123
if hasattr(_libs['grass_vector.7.8'], 'Vect_destroy_list'):
    Vect_destroy_list = _libs['grass_vector.7.8'].Vect_destroy_list
    Vect_destroy_list.argtypes = [POINTER(struct_ilist)]
    Vect_destroy_list.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 126
if hasattr(_libs['grass_vector.7.8'], 'Vect_new_boxlist'):
    Vect_new_boxlist = _libs['grass_vector.7.8'].Vect_new_boxlist
    Vect_new_boxlist.argtypes = [c_int]
    Vect_new_boxlist.restype = POINTER(struct_boxlist)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 127
if hasattr(_libs['grass_vector.7.8'], 'Vect_boxlist_append'):
    Vect_boxlist_append = _libs['grass_vector.7.8'].Vect_boxlist_append
    Vect_boxlist_append.argtypes = [POINTER(struct_boxlist), c_int, POINTER(struct_bound_box)]
    Vect_boxlist_append.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 128
if hasattr(_libs['grass_vector.7.8'], 'Vect_boxlist_append_boxlist'):
    Vect_boxlist_append_boxlist = _libs['grass_vector.7.8'].Vect_boxlist_append_boxlist
    Vect_boxlist_append_boxlist.argtypes = [POINTER(struct_boxlist), POINTER(struct_boxlist)]
    Vect_boxlist_append_boxlist.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 129
if hasattr(_libs['grass_vector.7.8'], 'Vect_boxlist_delete'):
    Vect_boxlist_delete = _libs['grass_vector.7.8'].Vect_boxlist_delete
    Vect_boxlist_delete.argtypes = [POINTER(struct_boxlist), c_int]
    Vect_boxlist_delete.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 130
if hasattr(_libs['grass_vector.7.8'], 'Vect_boxlist_delete_boxlist'):
    Vect_boxlist_delete_boxlist = _libs['grass_vector.7.8'].Vect_boxlist_delete_boxlist
    Vect_boxlist_delete_boxlist.argtypes = [POINTER(struct_boxlist), POINTER(struct_boxlist)]
    Vect_boxlist_delete_boxlist.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 131
if hasattr(_libs['grass_vector.7.8'], 'Vect_val_in_boxlist'):
    Vect_val_in_boxlist = _libs['grass_vector.7.8'].Vect_val_in_boxlist
    Vect_val_in_boxlist.argtypes = [POINTER(struct_boxlist), c_int]
    Vect_val_in_boxlist.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 132
if hasattr(_libs['grass_vector.7.8'], 'Vect_reset_boxlist'):
    Vect_reset_boxlist = _libs['grass_vector.7.8'].Vect_reset_boxlist
    Vect_reset_boxlist.argtypes = [POINTER(struct_boxlist)]
    Vect_reset_boxlist.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 133
if hasattr(_libs['grass_vector.7.8'], 'Vect_destroy_boxlist'):
    Vect_destroy_boxlist = _libs['grass_vector.7.8'].Vect_destroy_boxlist
    Vect_destroy_boxlist.argtypes = [POINTER(struct_boxlist)]
    Vect_destroy_boxlist.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 136
if hasattr(_libs['grass_vector.7.8'], 'Vect_point_in_box'):
    Vect_point_in_box = _libs['grass_vector.7.8'].Vect_point_in_box
    Vect_point_in_box.argtypes = [c_double, c_double, c_double, POINTER(struct_bound_box)]
    Vect_point_in_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 137
if hasattr(_libs['grass_vector.7.8'], 'Vect_point_in_box_2d'):
    Vect_point_in_box_2d = _libs['grass_vector.7.8'].Vect_point_in_box_2d
    Vect_point_in_box_2d.argtypes = [c_double, c_double, POINTER(struct_bound_box)]
    Vect_point_in_box_2d.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 138
if hasattr(_libs['grass_vector.7.8'], 'Vect_box_overlap'):
    Vect_box_overlap = _libs['grass_vector.7.8'].Vect_box_overlap
    Vect_box_overlap.argtypes = [POINTER(struct_bound_box), POINTER(struct_bound_box)]
    Vect_box_overlap.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 139
if hasattr(_libs['grass_vector.7.8'], 'Vect_box_copy'):
    Vect_box_copy = _libs['grass_vector.7.8'].Vect_box_copy
    Vect_box_copy.argtypes = [POINTER(struct_bound_box), POINTER(struct_bound_box)]
    Vect_box_copy.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 140
if hasattr(_libs['grass_vector.7.8'], 'Vect_box_extend'):
    Vect_box_extend = _libs['grass_vector.7.8'].Vect_box_extend
    Vect_box_extend.argtypes = [POINTER(struct_bound_box), POINTER(struct_bound_box)]
    Vect_box_extend.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 141
if hasattr(_libs['grass_vector.7.8'], 'Vect_box_clip'):
    Vect_box_clip = _libs['grass_vector.7.8'].Vect_box_clip
    Vect_box_clip.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(struct_bound_box)]
    Vect_box_clip.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 142
if hasattr(_libs['grass_vector.7.8'], 'Vect_region_box'):
    Vect_region_box = _libs['grass_vector.7.8'].Vect_region_box
    Vect_region_box.argtypes = [POINTER(struct_Cell_head), POINTER(struct_bound_box)]
    Vect_region_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 145
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_num_fields'):
    Vect_cidx_get_num_fields = _libs['grass_vector.7.8'].Vect_cidx_get_num_fields
    Vect_cidx_get_num_fields.argtypes = [POINTER(struct_Map_info)]
    Vect_cidx_get_num_fields.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 146
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_field_number'):
    Vect_cidx_get_field_number = _libs['grass_vector.7.8'].Vect_cidx_get_field_number
    Vect_cidx_get_field_number.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_cidx_get_field_number.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 147
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_field_index'):
    Vect_cidx_get_field_index = _libs['grass_vector.7.8'].Vect_cidx_get_field_index
    Vect_cidx_get_field_index.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_cidx_get_field_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 148
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_num_unique_cats_by_index'):
    Vect_cidx_get_num_unique_cats_by_index = _libs['grass_vector.7.8'].Vect_cidx_get_num_unique_cats_by_index
    Vect_cidx_get_num_unique_cats_by_index.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_cidx_get_num_unique_cats_by_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 149
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_num_cats_by_index'):
    Vect_cidx_get_num_cats_by_index = _libs['grass_vector.7.8'].Vect_cidx_get_num_cats_by_index
    Vect_cidx_get_num_cats_by_index.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_cidx_get_num_cats_by_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 150
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_num_types_by_index'):
    Vect_cidx_get_num_types_by_index = _libs['grass_vector.7.8'].Vect_cidx_get_num_types_by_index
    Vect_cidx_get_num_types_by_index.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_cidx_get_num_types_by_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 151
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_type_count_by_index'):
    Vect_cidx_get_type_count_by_index = _libs['grass_vector.7.8'].Vect_cidx_get_type_count_by_index
    Vect_cidx_get_type_count_by_index.argtypes = [POINTER(struct_Map_info), c_int, c_int, POINTER(c_int), POINTER(c_int)]
    Vect_cidx_get_type_count_by_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 153
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_type_count'):
    Vect_cidx_get_type_count = _libs['grass_vector.7.8'].Vect_cidx_get_type_count
    Vect_cidx_get_type_count.argtypes = [POINTER(struct_Map_info), c_int, c_int]
    Vect_cidx_get_type_count.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 154
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_cat_by_index'):
    Vect_cidx_get_cat_by_index = _libs['grass_vector.7.8'].Vect_cidx_get_cat_by_index
    Vect_cidx_get_cat_by_index.argtypes = [POINTER(struct_Map_info), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Vect_cidx_get_cat_by_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 156
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_get_unique_cats_by_index'):
    Vect_cidx_get_unique_cats_by_index = _libs['grass_vector.7.8'].Vect_cidx_get_unique_cats_by_index
    Vect_cidx_get_unique_cats_by_index.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_ilist)]
    Vect_cidx_get_unique_cats_by_index.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 157
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_find_next'):
    Vect_cidx_find_next = _libs['grass_vector.7.8'].Vect_cidx_find_next
    Vect_cidx_find_next.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_int, c_int, POINTER(c_int), POINTER(c_int)]
    Vect_cidx_find_next.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 158
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_find_all'):
    Vect_cidx_find_all = _libs['grass_vector.7.8'].Vect_cidx_find_all
    Vect_cidx_find_all.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_int, POINTER(struct_ilist)]
    Vect_cidx_find_all.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 159
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_dump'):
    Vect_cidx_dump = _libs['grass_vector.7.8'].Vect_cidx_dump
    Vect_cidx_dump.argtypes = [POINTER(struct_Map_info), POINTER(FILE)]
    Vect_cidx_dump.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 160
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_save'):
    Vect_cidx_save = _libs['grass_vector.7.8'].Vect_cidx_save
    Vect_cidx_save.argtypes = [POINTER(struct_Map_info)]
    Vect_cidx_save.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 161
if hasattr(_libs['grass_vector.7.8'], 'Vect_cidx_open'):
    Vect_cidx_open = _libs['grass_vector.7.8'].Vect_cidx_open
    Vect_cidx_open.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_cidx_open.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 164
if hasattr(_libs['grass_vector.7.8'], 'Vect_new_map_struct'):
    Vect_new_map_struct = _libs['grass_vector.7.8'].Vect_new_map_struct
    Vect_new_map_struct.argtypes = []
    Vect_new_map_struct.restype = POINTER(struct_Map_info)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 165
if hasattr(_libs['grass_vector.7.8'], 'Vect_destroy_map_struct'):
    Vect_destroy_map_struct = _libs['grass_vector.7.8'].Vect_destroy_map_struct
    Vect_destroy_map_struct.argtypes = [POINTER(struct_Map_info)]
    Vect_destroy_map_struct.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 168
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_header'):
    Vect_read_header = _libs['grass_vector.7.8'].Vect_read_header
    Vect_read_header.argtypes = [POINTER(struct_Map_info)]
    Vect_read_header.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 169
if hasattr(_libs['grass_vector.7.8'], 'Vect_write_header'):
    Vect_write_header = _libs['grass_vector.7.8'].Vect_write_header
    Vect_write_header.argtypes = [POINTER(struct_Map_info)]
    Vect_write_header.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 170
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_name'):
    Vect_get_name = _libs['grass_vector.7.8'].Vect_get_name
    Vect_get_name.argtypes = [POINTER(struct_Map_info)]
    Vect_get_name.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 171
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_mapset'):
    Vect_get_mapset = _libs['grass_vector.7.8'].Vect_get_mapset
    Vect_get_mapset.argtypes = [POINTER(struct_Map_info)]
    Vect_get_mapset.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 172
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_full_name'):
    Vect_get_full_name = _libs['grass_vector.7.8'].Vect_get_full_name
    Vect_get_full_name.argtypes = [POINTER(struct_Map_info)]
    Vect_get_full_name.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 173
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_finfo_dsn_name'):
    Vect_get_finfo_dsn_name = _libs['grass_vector.7.8'].Vect_get_finfo_dsn_name
    Vect_get_finfo_dsn_name.argtypes = [POINTER(struct_Map_info)]
    Vect_get_finfo_dsn_name.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 174
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_finfo_layer_name'):
    Vect_get_finfo_layer_name = _libs['grass_vector.7.8'].Vect_get_finfo_layer_name
    Vect_get_finfo_layer_name.argtypes = [POINTER(struct_Map_info)]
    if sizeof(c_int) == sizeof(c_void_p):
        Vect_get_finfo_layer_name.restype = ReturnString
    else:
        Vect_get_finfo_layer_name.restype = String
        Vect_get_finfo_layer_name.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 175
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_finfo_format_info'):
    Vect_get_finfo_format_info = _libs['grass_vector.7.8'].Vect_get_finfo_format_info
    Vect_get_finfo_format_info.argtypes = [POINTER(struct_Map_info)]
    Vect_get_finfo_format_info.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 176
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_finfo_geometry_type'):
    Vect_get_finfo_geometry_type = _libs['grass_vector.7.8'].Vect_get_finfo_geometry_type
    Vect_get_finfo_geometry_type.argtypes = [POINTER(struct_Map_info)]
    Vect_get_finfo_geometry_type.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 177
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_finfo'):
    Vect_get_finfo = _libs['grass_vector.7.8'].Vect_get_finfo
    Vect_get_finfo.argtypes = [POINTER(struct_Map_info)]
    Vect_get_finfo.restype = POINTER(struct_Format_info)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 178
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_finfo_topology_info'):
    Vect_get_finfo_topology_info = _libs['grass_vector.7.8'].Vect_get_finfo_topology_info
    Vect_get_finfo_topology_info.argtypes = [POINTER(struct_Map_info), POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(c_int)]
    Vect_get_finfo_topology_info.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 179
if hasattr(_libs['grass_vector.7.8'], 'Vect_is_3d'):
    Vect_is_3d = _libs['grass_vector.7.8'].Vect_is_3d
    Vect_is_3d.argtypes = [POINTER(struct_Map_info)]
    Vect_is_3d.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 180
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_organization'):
    Vect_set_organization = _libs['grass_vector.7.8'].Vect_set_organization
    Vect_set_organization.argtypes = [POINTER(struct_Map_info), String]
    Vect_set_organization.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 181
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_organization'):
    Vect_get_organization = _libs['grass_vector.7.8'].Vect_get_organization
    Vect_get_organization.argtypes = [POINTER(struct_Map_info)]
    Vect_get_organization.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 182
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_date'):
    Vect_set_date = _libs['grass_vector.7.8'].Vect_set_date
    Vect_set_date.argtypes = [POINTER(struct_Map_info), String]
    Vect_set_date.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 183
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_date'):
    Vect_get_date = _libs['grass_vector.7.8'].Vect_get_date
    Vect_get_date.argtypes = [POINTER(struct_Map_info)]
    Vect_get_date.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 184
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_person'):
    Vect_set_person = _libs['grass_vector.7.8'].Vect_set_person
    Vect_set_person.argtypes = [POINTER(struct_Map_info), String]
    Vect_set_person.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 185
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_person'):
    Vect_get_person = _libs['grass_vector.7.8'].Vect_get_person
    Vect_get_person.argtypes = [POINTER(struct_Map_info)]
    Vect_get_person.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 186
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_map_name'):
    Vect_set_map_name = _libs['grass_vector.7.8'].Vect_set_map_name
    Vect_set_map_name.argtypes = [POINTER(struct_Map_info), String]
    Vect_set_map_name.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 187
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_map_name'):
    Vect_get_map_name = _libs['grass_vector.7.8'].Vect_get_map_name
    Vect_get_map_name.argtypes = [POINTER(struct_Map_info)]
    Vect_get_map_name.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 188
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_map_date'):
    Vect_set_map_date = _libs['grass_vector.7.8'].Vect_set_map_date
    Vect_set_map_date.argtypes = [POINTER(struct_Map_info), String]
    Vect_set_map_date.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 189
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_map_date'):
    Vect_get_map_date = _libs['grass_vector.7.8'].Vect_get_map_date
    Vect_get_map_date.argtypes = [POINTER(struct_Map_info)]
    Vect_get_map_date.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 190
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_comment'):
    Vect_set_comment = _libs['grass_vector.7.8'].Vect_set_comment
    Vect_set_comment.argtypes = [POINTER(struct_Map_info), String]
    Vect_set_comment.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 191
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_comment'):
    Vect_get_comment = _libs['grass_vector.7.8'].Vect_get_comment
    Vect_get_comment.argtypes = [POINTER(struct_Map_info)]
    Vect_get_comment.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 192
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_scale'):
    Vect_set_scale = _libs['grass_vector.7.8'].Vect_set_scale
    Vect_set_scale.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_set_scale.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 193
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_scale'):
    Vect_get_scale = _libs['grass_vector.7.8'].Vect_get_scale
    Vect_get_scale.argtypes = [POINTER(struct_Map_info)]
    Vect_get_scale.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 194
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_zone'):
    Vect_set_zone = _libs['grass_vector.7.8'].Vect_set_zone
    Vect_set_zone.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_set_zone.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 195
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_zone'):
    Vect_get_zone = _libs['grass_vector.7.8'].Vect_get_zone
    Vect_get_zone.argtypes = [POINTER(struct_Map_info)]
    Vect_get_zone.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 196
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_proj'):
    Vect_get_proj = _libs['grass_vector.7.8'].Vect_get_proj
    Vect_get_proj.argtypes = [POINTER(struct_Map_info)]
    Vect_get_proj.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 197
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_proj'):
    Vect_set_proj = _libs['grass_vector.7.8'].Vect_set_proj
    Vect_set_proj.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_set_proj.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 198
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_proj_name'):
    Vect_get_proj_name = _libs['grass_vector.7.8'].Vect_get_proj_name
    Vect_get_proj_name.argtypes = [POINTER(struct_Map_info)]
    Vect_get_proj_name.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 199
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_thresh'):
    Vect_set_thresh = _libs['grass_vector.7.8'].Vect_set_thresh
    Vect_set_thresh.argtypes = [POINTER(struct_Map_info), c_double]
    Vect_set_thresh.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 200
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_thresh'):
    Vect_get_thresh = _libs['grass_vector.7.8'].Vect_get_thresh
    Vect_get_thresh.argtypes = [POINTER(struct_Map_info)]
    Vect_get_thresh.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 201
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_constraint_box'):
    Vect_get_constraint_box = _libs['grass_vector.7.8'].Vect_get_constraint_box
    Vect_get_constraint_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box)]
    Vect_get_constraint_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 204
if hasattr(_libs['grass_vector.7.8'], 'Vect_level'):
    Vect_level = _libs['grass_vector.7.8'].Vect_level
    Vect_level.argtypes = [POINTER(struct_Map_info)]
    Vect_level.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 207
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_map_box1'):
    Vect_get_map_box1 = _libs['grass_vector.7.8'].Vect_get_map_box1
    Vect_get_map_box1.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box)]
    Vect_get_map_box1.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 210
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_line_type'):
    Vect_get_line_type = _libs['grass_vector.7.8'].Vect_get_line_type
    Vect_get_line_type.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_line_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 211
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_nodes'):
    Vect_get_num_nodes = _libs['grass_vector.7.8'].Vect_get_num_nodes
    Vect_get_num_nodes.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_nodes.restype = plus_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 212
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_primitives'):
    Vect_get_num_primitives = _libs['grass_vector.7.8'].Vect_get_num_primitives
    Vect_get_num_primitives.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_num_primitives.restype = plus_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 213
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_lines'):
    Vect_get_num_lines = _libs['grass_vector.7.8'].Vect_get_num_lines
    Vect_get_num_lines.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_lines.restype = plus_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 214
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_areas'):
    Vect_get_num_areas = _libs['grass_vector.7.8'].Vect_get_num_areas
    Vect_get_num_areas.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_areas.restype = plus_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 215
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_faces'):
    Vect_get_num_faces = _libs['grass_vector.7.8'].Vect_get_num_faces
    Vect_get_num_faces.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_faces.restype = plus_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 216
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_kernels'):
    Vect_get_num_kernels = _libs['grass_vector.7.8'].Vect_get_num_kernels
    Vect_get_num_kernels.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_kernels.restype = plus_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 217
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_volumes'):
    Vect_get_num_volumes = _libs['grass_vector.7.8'].Vect_get_num_volumes
    Vect_get_num_volumes.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_volumes.restype = plus_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 218
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_islands'):
    Vect_get_num_islands = _libs['grass_vector.7.8'].Vect_get_num_islands
    Vect_get_num_islands.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_islands.restype = plus_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 219
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_holes'):
    Vect_get_num_holes = _libs['grass_vector.7.8'].Vect_get_num_holes
    Vect_get_num_holes.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_holes.restype = plus_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 220
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_line_box'):
    Vect_get_line_box = _libs['grass_vector.7.8'].Vect_get_line_box
    Vect_get_line_box.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]
    Vect_get_line_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 221
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_box'):
    Vect_get_area_box = _libs['grass_vector.7.8'].Vect_get_area_box
    Vect_get_area_box.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]
    Vect_get_area_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 222
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_isle_box'):
    Vect_get_isle_box = _libs['grass_vector.7.8'].Vect_get_isle_box
    Vect_get_isle_box.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]
    Vect_get_isle_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 223
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_map_box'):
    Vect_get_map_box = _libs['grass_vector.7.8'].Vect_get_map_box
    Vect_get_map_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box)]
    Vect_get_map_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 224
if hasattr(_libs['grass_vector.7.8'], 'V__map_overlap'):
    V__map_overlap = _libs['grass_vector.7.8'].V__map_overlap
    V__map_overlap.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double]
    V__map_overlap.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 225
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_release_support'):
    Vect_set_release_support = _libs['grass_vector.7.8'].Vect_set_release_support
    Vect_set_release_support.argtypes = [POINTER(struct_Map_info)]
    Vect_set_release_support.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 226
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_category_index_update'):
    Vect_set_category_index_update = _libs['grass_vector.7.8'].Vect_set_category_index_update
    Vect_set_category_index_update.argtypes = [POINTER(struct_Map_info)]
    Vect_set_category_index_update.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 229
if hasattr(_libs['grass_vector.7.8'], 'Vect_check_input_output_name'):
    Vect_check_input_output_name = _libs['grass_vector.7.8'].Vect_check_input_output_name
    Vect_check_input_output_name.argtypes = [String, String, c_int]
    Vect_check_input_output_name.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 230
if hasattr(_libs['grass_vector.7.8'], 'Vect_legal_filename'):
    Vect_legal_filename = _libs['grass_vector.7.8'].Vect_legal_filename
    Vect_legal_filename.argtypes = [String]
    Vect_legal_filename.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 231
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_open_level'):
    Vect_set_open_level = _libs['grass_vector.7.8'].Vect_set_open_level
    Vect_set_open_level.argtypes = [c_int]
    Vect_set_open_level.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 232
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_old'):
    Vect_open_old = _libs['grass_vector.7.8'].Vect_open_old
    Vect_open_old.argtypes = [POINTER(struct_Map_info), String, String]
    Vect_open_old.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 233
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_tmp_old'):
    Vect_open_tmp_old = _libs['grass_vector.7.8'].Vect_open_tmp_old
    Vect_open_tmp_old.argtypes = [POINTER(struct_Map_info), String, String]
    Vect_open_tmp_old.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 234
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_old2'):
    Vect_open_old2 = _libs['grass_vector.7.8'].Vect_open_old2
    Vect_open_old2.argtypes = [POINTER(struct_Map_info), String, String, String]
    Vect_open_old2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 235
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_old_head'):
    Vect_open_old_head = _libs['grass_vector.7.8'].Vect_open_old_head
    Vect_open_old_head.argtypes = [POINTER(struct_Map_info), String, String]
    Vect_open_old_head.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 236
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_old_head2'):
    Vect_open_old_head2 = _libs['grass_vector.7.8'].Vect_open_old_head2
    Vect_open_old_head2.argtypes = [POINTER(struct_Map_info), String, String, String]
    Vect_open_old_head2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 237
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_new'):
    Vect_open_new = _libs['grass_vector.7.8'].Vect_open_new
    Vect_open_new.argtypes = [POINTER(struct_Map_info), String, c_int]
    Vect_open_new.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 238
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_tmp_new'):
    Vect_open_tmp_new = _libs['grass_vector.7.8'].Vect_open_tmp_new
    Vect_open_tmp_new.argtypes = [POINTER(struct_Map_info), String, c_int]
    Vect_open_tmp_new.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 239
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_update'):
    Vect_open_update = _libs['grass_vector.7.8'].Vect_open_update
    Vect_open_update.argtypes = [POINTER(struct_Map_info), String, String]
    Vect_open_update.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 240
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_tmp_update'):
    Vect_open_tmp_update = _libs['grass_vector.7.8'].Vect_open_tmp_update
    Vect_open_tmp_update.argtypes = [POINTER(struct_Map_info), String, String]
    Vect_open_tmp_update.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 241
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_update2'):
    Vect_open_update2 = _libs['grass_vector.7.8'].Vect_open_update2
    Vect_open_update2.argtypes = [POINTER(struct_Map_info), String, String, String]
    Vect_open_update2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 242
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_update_head'):
    Vect_open_update_head = _libs['grass_vector.7.8'].Vect_open_update_head
    Vect_open_update_head.argtypes = [POINTER(struct_Map_info), String, String]
    Vect_open_update_head.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 243
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_head_data'):
    Vect_copy_head_data = _libs['grass_vector.7.8'].Vect_copy_head_data
    Vect_copy_head_data.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]
    Vect_copy_head_data.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 244
if hasattr(_libs['grass_vector.7.8'], 'Vect_build'):
    Vect_build = _libs['grass_vector.7.8'].Vect_build
    Vect_build.argtypes = [POINTER(struct_Map_info)]
    Vect_build.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 245
if hasattr(_libs['grass_vector.7.8'], 'Vect_topo_check'):
    Vect_topo_check = _libs['grass_vector.7.8'].Vect_topo_check
    Vect_topo_check.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]
    Vect_topo_check.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 246
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_built'):
    Vect_get_built = _libs['grass_vector.7.8'].Vect_get_built
    Vect_get_built.argtypes = [POINTER(struct_Map_info)]
    Vect_get_built.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 247
if hasattr(_libs['grass_vector.7.8'], 'Vect_build_partial'):
    Vect_build_partial = _libs['grass_vector.7.8'].Vect_build_partial
    Vect_build_partial.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_build_partial.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 248
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_constraint_region'):
    Vect_set_constraint_region = _libs['grass_vector.7.8'].Vect_set_constraint_region
    Vect_set_constraint_region.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double, c_double, c_double]
    Vect_set_constraint_region.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 250
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_constraint_type'):
    Vect_set_constraint_type = _libs['grass_vector.7.8'].Vect_set_constraint_type
    Vect_set_constraint_type.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_set_constraint_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 251
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_constraint_field'):
    Vect_set_constraint_field = _libs['grass_vector.7.8'].Vect_set_constraint_field
    Vect_set_constraint_field.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_set_constraint_field.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 252
if hasattr(_libs['grass_vector.7.8'], 'Vect_remove_constraints'):
    Vect_remove_constraints = _libs['grass_vector.7.8'].Vect_remove_constraints
    Vect_remove_constraints.argtypes = [POINTER(struct_Map_info)]
    Vect_remove_constraints.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 253
if hasattr(_libs['grass_vector.7.8'], 'Vect_rewind'):
    Vect_rewind = _libs['grass_vector.7.8'].Vect_rewind
    Vect_rewind.argtypes = [POINTER(struct_Map_info)]
    Vect_rewind.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 254
if hasattr(_libs['grass_vector.7.8'], 'Vect_close'):
    Vect_close = _libs['grass_vector.7.8'].Vect_close
    Vect_close.argtypes = [POINTER(struct_Map_info)]
    Vect_close.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 255
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_error_handler_io'):
    Vect_set_error_handler_io = _libs['grass_vector.7.8'].Vect_set_error_handler_io
    Vect_set_error_handler_io.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]
    Vect_set_error_handler_io.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 259
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_next_line_id'):
    Vect_get_next_line_id = _libs['grass_vector.7.8'].Vect_get_next_line_id
    Vect_get_next_line_id.argtypes = [POINTER(struct_Map_info)]
    Vect_get_next_line_id.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 260
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_next_line'):
    Vect_read_next_line = _libs['grass_vector.7.8'].Vect_read_next_line
    Vect_read_next_line.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    Vect_read_next_line.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 262
if hasattr(_libs['grass_vector.7.8'], 'Vect_write_line'):
    Vect_write_line = _libs['grass_vector.7.8'].Vect_write_line
    Vect_write_line.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    Vect_write_line.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 264
if hasattr(_libs['grass_vector.7.8'], 'Vect_rewrite_line'):
    Vect_rewrite_line = _libs['grass_vector.7.8'].Vect_rewrite_line
    Vect_rewrite_line.argtypes = [POINTER(struct_Map_info), off_t, c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    Vect_rewrite_line.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 266
if hasattr(_libs['grass_vector.7.8'], 'Vect_delete_line'):
    Vect_delete_line = _libs['grass_vector.7.8'].Vect_delete_line
    Vect_delete_line.argtypes = [POINTER(struct_Map_info), off_t]
    Vect_delete_line.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 267
if hasattr(_libs['grass_vector.7.8'], 'Vect_restore_line'):
    Vect_restore_line = _libs['grass_vector.7.8'].Vect_restore_line
    Vect_restore_line.argtypes = [POINTER(struct_Map_info), off_t, off_t]
    Vect_restore_line.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 269
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_dblinks'):
    Vect_get_num_dblinks = _libs['grass_vector.7.8'].Vect_get_num_dblinks
    Vect_get_num_dblinks.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_dblinks.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 272
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_line'):
    Vect_read_line = _libs['grass_vector.7.8'].Vect_read_line
    Vect_read_line.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), c_int]
    Vect_read_line.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 275
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_alive'):
    Vect_line_alive = _libs['grass_vector.7.8'].Vect_line_alive
    Vect_line_alive.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_line_alive.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 276
if hasattr(_libs['grass_vector.7.8'], 'Vect_node_alive'):
    Vect_node_alive = _libs['grass_vector.7.8'].Vect_node_alive
    Vect_node_alive.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_node_alive.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 277
if hasattr(_libs['grass_vector.7.8'], 'Vect_area_alive'):
    Vect_area_alive = _libs['grass_vector.7.8'].Vect_area_alive
    Vect_area_alive.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_area_alive.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 278
if hasattr(_libs['grass_vector.7.8'], 'Vect_isle_alive'):
    Vect_isle_alive = _libs['grass_vector.7.8'].Vect_isle_alive
    Vect_isle_alive.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_isle_alive.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 279
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_line_nodes'):
    Vect_get_line_nodes = _libs['grass_vector.7.8'].Vect_get_line_nodes
    Vect_get_line_nodes.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_int), POINTER(c_int)]
    Vect_get_line_nodes.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 280
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_line_areas'):
    Vect_get_line_areas = _libs['grass_vector.7.8'].Vect_get_line_areas
    Vect_get_line_areas.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_int), POINTER(c_int)]
    Vect_get_line_areas.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 281
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_line_offset'):
    Vect_get_line_offset = _libs['grass_vector.7.8'].Vect_get_line_offset
    Vect_get_line_offset.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_line_offset.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 283
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_node_coor'):
    Vect_get_node_coor = _libs['grass_vector.7.8'].Vect_get_node_coor
    Vect_get_node_coor.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Vect_get_node_coor.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 284
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_node_n_lines'):
    Vect_get_node_n_lines = _libs['grass_vector.7.8'].Vect_get_node_n_lines
    Vect_get_node_n_lines.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_node_n_lines.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 285
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_node_line'):
    Vect_get_node_line = _libs['grass_vector.7.8'].Vect_get_node_line
    Vect_get_node_line.argtypes = [POINTER(struct_Map_info), c_int, c_int]
    Vect_get_node_line.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 286
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_node_line_angle'):
    Vect_get_node_line_angle = _libs['grass_vector.7.8'].Vect_get_node_line_angle
    Vect_get_node_line_angle.argtypes = [POINTER(struct_Map_info), c_int, c_int]
    Vect_get_node_line_angle.restype = c_float

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 288
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_points'):
    Vect_get_area_points = _libs['grass_vector.7.8'].Vect_get_area_points
    Vect_get_area_points.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts)]
    Vect_get_area_points.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 289
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_centroid'):
    Vect_get_area_centroid = _libs['grass_vector.7.8'].Vect_get_area_centroid
    Vect_get_area_centroid.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_area_centroid.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 290
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_num_isles'):
    Vect_get_area_num_isles = _libs['grass_vector.7.8'].Vect_get_area_num_isles
    Vect_get_area_num_isles.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_area_num_isles.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 291
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_isle'):
    Vect_get_area_isle = _libs['grass_vector.7.8'].Vect_get_area_isle
    Vect_get_area_isle.argtypes = [POINTER(struct_Map_info), c_int, c_int]
    Vect_get_area_isle.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 292
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_perimeter'):
    Vect_get_area_perimeter = _libs['grass_vector.7.8'].Vect_get_area_perimeter
    Vect_get_area_perimeter.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_area_perimeter.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 293
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_area'):
    Vect_get_area_area = _libs['grass_vector.7.8'].Vect_get_area_area
    Vect_get_area_area.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_area_area.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 294
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_boundaries'):
    Vect_get_area_boundaries = _libs['grass_vector.7.8'].Vect_get_area_boundaries
    Vect_get_area_boundaries.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_ilist)]
    Vect_get_area_boundaries.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 296
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_isle_points'):
    Vect_get_isle_points = _libs['grass_vector.7.8'].Vect_get_isle_points
    Vect_get_isle_points.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts)]
    Vect_get_isle_points.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 297
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_isle_area'):
    Vect_get_isle_area = _libs['grass_vector.7.8'].Vect_get_isle_area
    Vect_get_isle_area.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_isle_area.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 298
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_isle_boundaries'):
    Vect_get_isle_boundaries = _libs['grass_vector.7.8'].Vect_get_isle_boundaries
    Vect_get_isle_boundaries.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_ilist)]
    Vect_get_isle_boundaries.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 300
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_centroid_area'):
    Vect_get_centroid_area = _libs['grass_vector.7.8'].Vect_get_centroid_area
    Vect_get_centroid_area.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_centroid_area.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 303
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_updated_lines'):
    Vect_get_num_updated_lines = _libs['grass_vector.7.8'].Vect_get_num_updated_lines
    Vect_get_num_updated_lines.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_updated_lines.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 304
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_updated_line'):
    Vect_get_updated_line = _libs['grass_vector.7.8'].Vect_get_updated_line
    Vect_get_updated_line.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_updated_line.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 305
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_updated_line_offset'):
    Vect_get_updated_line_offset = _libs['grass_vector.7.8'].Vect_get_updated_line_offset
    Vect_get_updated_line_offset.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_updated_line_offset.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 306
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_num_updated_nodes'):
    Vect_get_num_updated_nodes = _libs['grass_vector.7.8'].Vect_get_num_updated_nodes
    Vect_get_num_updated_nodes.argtypes = [POINTER(struct_Map_info)]
    Vect_get_num_updated_nodes.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 307
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_updated_node'):
    Vect_get_updated_node = _libs['grass_vector.7.8'].Vect_get_updated_node
    Vect_get_updated_node.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_updated_node.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 308
if hasattr(_libs['grass_vector.7.8'], 'Vect_set_updated'):
    Vect_set_updated = _libs['grass_vector.7.8'].Vect_set_updated
    Vect_set_updated.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_set_updated.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 309
if hasattr(_libs['grass_vector.7.8'], 'Vect_reset_updated'):
    Vect_reset_updated = _libs['grass_vector.7.8'].Vect_reset_updated
    Vect_reset_updated.argtypes = [POINTER(struct_Map_info)]
    Vect_reset_updated.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 312
if hasattr(_libs['grass_vector.7.8'], 'Vect_hist_command'):
    Vect_hist_command = _libs['grass_vector.7.8'].Vect_hist_command
    Vect_hist_command.argtypes = [POINTER(struct_Map_info)]
    Vect_hist_command.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 313
if hasattr(_libs['grass_vector.7.8'], 'Vect_hist_write'):
    Vect_hist_write = _libs['grass_vector.7.8'].Vect_hist_write
    Vect_hist_write.argtypes = [POINTER(struct_Map_info), String]
    Vect_hist_write.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 314
if hasattr(_libs['grass_vector.7.8'], 'Vect_hist_copy'):
    Vect_hist_copy = _libs['grass_vector.7.8'].Vect_hist_copy
    Vect_hist_copy.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]
    Vect_hist_copy.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 315
if hasattr(_libs['grass_vector.7.8'], 'Vect_hist_rewind'):
    Vect_hist_rewind = _libs['grass_vector.7.8'].Vect_hist_rewind
    Vect_hist_rewind.argtypes = [POINTER(struct_Map_info)]
    Vect_hist_rewind.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 316
if hasattr(_libs['grass_vector.7.8'], 'Vect_hist_read'):
    Vect_hist_read = _libs['grass_vector.7.8'].Vect_hist_read
    Vect_hist_read.argtypes = [String, c_int, POINTER(struct_Map_info)]
    if sizeof(c_int) == sizeof(c_void_p):
        Vect_hist_read.restype = ReturnString
    else:
        Vect_hist_read.restype = String
        Vect_hist_read.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 319
if hasattr(_libs['grass_vector.7.8'], 'Vect_select_lines_by_box'):
    Vect_select_lines_by_box = _libs['grass_vector.7.8'].Vect_select_lines_by_box
    Vect_select_lines_by_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), c_int, POINTER(struct_boxlist)]
    Vect_select_lines_by_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 321
if hasattr(_libs['grass_vector.7.8'], 'Vect_select_areas_by_box'):
    Vect_select_areas_by_box = _libs['grass_vector.7.8'].Vect_select_areas_by_box
    Vect_select_areas_by_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), POINTER(struct_boxlist)]
    Vect_select_areas_by_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 323
if hasattr(_libs['grass_vector.7.8'], 'Vect_select_isles_by_box'):
    Vect_select_isles_by_box = _libs['grass_vector.7.8'].Vect_select_isles_by_box
    Vect_select_isles_by_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), POINTER(struct_boxlist)]
    Vect_select_isles_by_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 325
if hasattr(_libs['grass_vector.7.8'], 'Vect_select_nodes_by_box'):
    Vect_select_nodes_by_box = _libs['grass_vector.7.8'].Vect_select_nodes_by_box
    Vect_select_nodes_by_box.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box), POINTER(struct_ilist)]
    Vect_select_nodes_by_box.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 327
if hasattr(_libs['grass_vector.7.8'], 'Vect_find_node'):
    Vect_find_node = _libs['grass_vector.7.8'].Vect_find_node
    Vect_find_node.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double, c_int]
    Vect_find_node.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 328
if hasattr(_libs['grass_vector.7.8'], 'Vect_find_line'):
    Vect_find_line = _libs['grass_vector.7.8'].Vect_find_line
    Vect_find_line.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_int, c_double, c_int, c_int]
    Vect_find_line.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 330
if hasattr(_libs['grass_vector.7.8'], 'Vect_find_line_list'):
    Vect_find_line_list = _libs['grass_vector.7.8'].Vect_find_line_list
    Vect_find_line_list.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_int, c_double, c_int, POINTER(struct_ilist), POINTER(struct_ilist)]
    Vect_find_line_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 332
if hasattr(_libs['grass_vector.7.8'], 'Vect_find_area'):
    Vect_find_area = _libs['grass_vector.7.8'].Vect_find_area
    Vect_find_area.argtypes = [POINTER(struct_Map_info), c_double, c_double]
    Vect_find_area.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 333
if hasattr(_libs['grass_vector.7.8'], 'Vect_find_island'):
    Vect_find_island = _libs['grass_vector.7.8'].Vect_find_island
    Vect_find_island.argtypes = [POINTER(struct_Map_info), c_double, c_double]
    Vect_find_island.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 334
if hasattr(_libs['grass_vector.7.8'], 'Vect_select_lines_by_polygon'):
    Vect_select_lines_by_polygon = _libs['grass_vector.7.8'].Vect_select_lines_by_polygon
    Vect_select_lines_by_polygon.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), c_int, POINTER(POINTER(struct_line_pnts)), c_int, POINTER(struct_ilist)]
    Vect_select_lines_by_polygon.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 336
if hasattr(_libs['grass_vector.7.8'], 'Vect_select_areas_by_polygon'):
    Vect_select_areas_by_polygon = _libs['grass_vector.7.8'].Vect_select_areas_by_polygon
    Vect_select_areas_by_polygon.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), c_int, POINTER(POINTER(struct_line_pnts)), POINTER(struct_ilist)]
    Vect_select_areas_by_polygon.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 340
if hasattr(_libs['grass_vector.7.8'], 'Vect_tin_get_z'):
    Vect_tin_get_z = _libs['grass_vector.7.8'].Vect_tin_get_z
    Vect_tin_get_z.argtypes = [POINTER(struct_Map_info), c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Vect_tin_get_z.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 344
if hasattr(_libs['grass_vector.7.8'], 'Vect_find_poly_centroid'):
    Vect_find_poly_centroid = _libs['grass_vector.7.8'].Vect_find_poly_centroid
    Vect_find_poly_centroid.argtypes = [POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double)]
    Vect_find_poly_centroid.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 345
for _lib in six.itervalues(_libs):
    if not hasattr(_lib, 'Vect__intersect_line_with_poly'):
        continue
    Vect__intersect_line_with_poly = _lib.Vect__intersect_line_with_poly
    Vect__intersect_line_with_poly.argtypes = [POINTER(struct_line_pnts), c_double, POINTER(struct_line_pnts)]
    Vect__intersect_line_with_poly.restype = c_int
    break

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 347
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_point_in_area'):
    Vect_get_point_in_area = _libs['grass_vector.7.8'].Vect_get_point_in_area
    Vect_get_point_in_area.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_double), POINTER(c_double)]
    Vect_get_point_in_area.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 348
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_point_in_poly'):
    Vect_get_point_in_poly = _libs['grass_vector.7.8'].Vect_get_point_in_poly
    Vect_get_point_in_poly.argtypes = [POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double)]
    Vect_get_point_in_poly.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 349
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_point_in_poly_isl'):
    Vect_get_point_in_poly_isl = _libs['grass_vector.7.8'].Vect_get_point_in_poly_isl
    Vect_get_point_in_poly_isl.argtypes = [POINTER(struct_line_pnts), POINTER(POINTER(struct_line_pnts)), c_int, POINTER(c_double), POINTER(c_double)]
    Vect_get_point_in_poly_isl.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 351
if hasattr(_libs['grass_vector.7.8'], 'Vect_point_in_area'):
    Vect_point_in_area = _libs['grass_vector.7.8'].Vect_point_in_area
    Vect_point_in_area.argtypes = [c_double, c_double, POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]
    Vect_point_in_area.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 352
if hasattr(_libs['grass_vector.7.8'], 'Vect_point_in_area_outer_ring'):
    Vect_point_in_area_outer_ring = _libs['grass_vector.7.8'].Vect_point_in_area_outer_ring
    Vect_point_in_area_outer_ring.argtypes = [c_double, c_double, POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]
    Vect_point_in_area_outer_ring.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 353
if hasattr(_libs['grass_vector.7.8'], 'Vect_point_in_island'):
    Vect_point_in_island = _libs['grass_vector.7.8'].Vect_point_in_island
    Vect_point_in_island.argtypes = [c_double, c_double, POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]
    Vect_point_in_island.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 354
if hasattr(_libs['grass_vector.7.8'], 'Vect_point_in_poly'):
    Vect_point_in_poly = _libs['grass_vector.7.8'].Vect_point_in_poly
    Vect_point_in_poly.argtypes = [c_double, c_double, POINTER(struct_line_pnts)]
    Vect_point_in_poly.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 357
if hasattr(_libs['grass_vector.7.8'], 'Vect_break_lines'):
    Vect_break_lines = _libs['grass_vector.7.8'].Vect_break_lines
    Vect_break_lines.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]
    Vect_break_lines.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 358
if hasattr(_libs['grass_vector.7.8'], 'Vect_break_lines_list'):
    Vect_break_lines_list = _libs['grass_vector.7.8'].Vect_break_lines_list
    Vect_break_lines_list.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_ilist), c_int, POINTER(struct_Map_info)]
    Vect_break_lines_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 360
if hasattr(_libs['grass_vector.7.8'], 'Vect_check_line_breaks'):
    Vect_check_line_breaks = _libs['grass_vector.7.8'].Vect_check_line_breaks
    Vect_check_line_breaks.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]
    Vect_check_line_breaks.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 361
if hasattr(_libs['grass_vector.7.8'], 'Vect_check_line_breaks_list'):
    Vect_check_line_breaks_list = _libs['grass_vector.7.8'].Vect_check_line_breaks_list
    Vect_check_line_breaks_list.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_ilist), c_int, POINTER(struct_Map_info)]
    Vect_check_line_breaks_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 363
if hasattr(_libs['grass_vector.7.8'], 'Vect_merge_lines'):
    Vect_merge_lines = _libs['grass_vector.7.8'].Vect_merge_lines
    Vect_merge_lines.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_int), POINTER(struct_Map_info)]
    Vect_merge_lines.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 364
if hasattr(_libs['grass_vector.7.8'], 'Vect_break_polygons'):
    Vect_break_polygons = _libs['grass_vector.7.8'].Vect_break_polygons
    Vect_break_polygons.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]
    Vect_break_polygons.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 365
if hasattr(_libs['grass_vector.7.8'], 'Vect_remove_duplicates'):
    Vect_remove_duplicates = _libs['grass_vector.7.8'].Vect_remove_duplicates
    Vect_remove_duplicates.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]
    Vect_remove_duplicates.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 366
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_check_duplicate'):
    Vect_line_check_duplicate = _libs['grass_vector.7.8'].Vect_line_check_duplicate
    Vect_line_check_duplicate.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]
    Vect_line_check_duplicate.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 368
if hasattr(_libs['grass_vector.7.8'], 'Vect_snap_lines'):
    Vect_snap_lines = _libs['grass_vector.7.8'].Vect_snap_lines
    Vect_snap_lines.argtypes = [POINTER(struct_Map_info), c_int, c_double, POINTER(struct_Map_info)]
    Vect_snap_lines.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 369
if hasattr(_libs['grass_vector.7.8'], 'Vect_snap_lines_list'):
    Vect_snap_lines_list = _libs['grass_vector.7.8'].Vect_snap_lines_list
    Vect_snap_lines_list.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), c_double, POINTER(struct_Map_info)]
    Vect_snap_lines_list.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 371
if hasattr(_libs['grass_vector.7.8'], 'Vect_snap_line'):
    Vect_snap_line = _libs['grass_vector.7.8'].Vect_snap_line
    Vect_snap_line.argtypes = [POINTER(struct_Map_info), POINTER(struct_ilist), POINTER(struct_line_pnts), c_double, c_int, POINTER(c_int), POINTER(c_int)]
    Vect_snap_line.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 373
if hasattr(_libs['grass_vector.7.8'], 'Vect_remove_dangles'):
    Vect_remove_dangles = _libs['grass_vector.7.8'].Vect_remove_dangles
    Vect_remove_dangles.argtypes = [POINTER(struct_Map_info), c_int, c_double, POINTER(struct_Map_info)]
    Vect_remove_dangles.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 374
if hasattr(_libs['grass_vector.7.8'], 'Vect_chtype_dangles'):
    Vect_chtype_dangles = _libs['grass_vector.7.8'].Vect_chtype_dangles
    Vect_chtype_dangles.argtypes = [POINTER(struct_Map_info), c_double, POINTER(struct_Map_info)]
    Vect_chtype_dangles.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 375
if hasattr(_libs['grass_vector.7.8'], 'Vect_select_dangles'):
    Vect_select_dangles = _libs['grass_vector.7.8'].Vect_select_dangles
    Vect_select_dangles.argtypes = [POINTER(struct_Map_info), c_int, c_double, POINTER(struct_ilist)]
    Vect_select_dangles.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 376
if hasattr(_libs['grass_vector.7.8'], 'Vect_remove_bridges'):
    Vect_remove_bridges = _libs['grass_vector.7.8'].Vect_remove_bridges
    Vect_remove_bridges.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), POINTER(c_int), POINTER(c_int)]
    Vect_remove_bridges.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 377
if hasattr(_libs['grass_vector.7.8'], 'Vect_chtype_bridges'):
    Vect_chtype_bridges = _libs['grass_vector.7.8'].Vect_chtype_bridges
    Vect_chtype_bridges.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), POINTER(c_int), POINTER(c_int)]
    Vect_chtype_bridges.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 378
if hasattr(_libs['grass_vector.7.8'], 'Vect_remove_small_areas'):
    Vect_remove_small_areas = _libs['grass_vector.7.8'].Vect_remove_small_areas
    Vect_remove_small_areas.argtypes = [POINTER(struct_Map_info), c_double, POINTER(struct_Map_info), POINTER(c_double)]
    Vect_remove_small_areas.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 380
if hasattr(_libs['grass_vector.7.8'], 'Vect_clean_small_angles_at_nodes'):
    Vect_clean_small_angles_at_nodes = _libs['grass_vector.7.8'].Vect_clean_small_angles_at_nodes
    Vect_clean_small_angles_at_nodes.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]
    Vect_clean_small_angles_at_nodes.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 384
if hasattr(_libs['grass_vector.7.8'], 'Vect_overlay_str_to_operator'):
    Vect_overlay_str_to_operator = _libs['grass_vector.7.8'].Vect_overlay_str_to_operator
    Vect_overlay_str_to_operator.argtypes = [String]
    Vect_overlay_str_to_operator.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 385
if hasattr(_libs['grass_vector.7.8'], 'Vect_overlay'):
    Vect_overlay = _libs['grass_vector.7.8'].Vect_overlay
    Vect_overlay.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_ilist), POINTER(struct_ilist), POINTER(struct_Map_info), c_int, POINTER(struct_ilist), POINTER(struct_ilist), c_int, POINTER(struct_Map_info)]
    Vect_overlay.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 388
if hasattr(_libs['grass_vector.7.8'], 'Vect_overlay_and'):
    Vect_overlay_and = _libs['grass_vector.7.8'].Vect_overlay_and
    Vect_overlay_and.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_ilist), POINTER(struct_ilist), POINTER(struct_Map_info), c_int, POINTER(struct_ilist), POINTER(struct_ilist), POINTER(struct_Map_info)]
    Vect_overlay_and.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 393
if hasattr(_libs['grass_vector.7.8'], 'Vect_graph_init'):
    Vect_graph_init = _libs['grass_vector.7.8'].Vect_graph_init
    Vect_graph_init.argtypes = [POINTER(dglGraph_s), c_int]
    Vect_graph_init.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 394
if hasattr(_libs['grass_vector.7.8'], 'Vect_graph_build'):
    Vect_graph_build = _libs['grass_vector.7.8'].Vect_graph_build
    Vect_graph_build.argtypes = [POINTER(dglGraph_s)]
    Vect_graph_build.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 395
if hasattr(_libs['grass_vector.7.8'], 'Vect_graph_add_edge'):
    Vect_graph_add_edge = _libs['grass_vector.7.8'].Vect_graph_add_edge
    Vect_graph_add_edge.argtypes = [POINTER(dglGraph_s), c_int, c_int, c_double, c_int]
    Vect_graph_add_edge.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 396
if hasattr(_libs['grass_vector.7.8'], 'Vect_graph_set_node_costs'):
    Vect_graph_set_node_costs = _libs['grass_vector.7.8'].Vect_graph_set_node_costs
    Vect_graph_set_node_costs.argtypes = [POINTER(dglGraph_s), c_int, c_double]
    Vect_graph_set_node_costs.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 397
if hasattr(_libs['grass_vector.7.8'], 'Vect_graph_shortest_path'):
    Vect_graph_shortest_path = _libs['grass_vector.7.8'].Vect_graph_shortest_path
    Vect_graph_shortest_path.argtypes = [POINTER(dglGraph_s), c_int, c_int, POINTER(struct_ilist), POINTER(c_double)]
    Vect_graph_shortest_path.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 400
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_build_graph'):
    Vect_net_build_graph = _libs['grass_vector.7.8'].Vect_net_build_graph
    Vect_net_build_graph.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_int, String, String, String, c_int, c_int]
    Vect_net_build_graph.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 402
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_ttb_build_graph'):
    Vect_net_ttb_build_graph = _libs['grass_vector.7.8'].Vect_net_ttb_build_graph
    Vect_net_ttb_build_graph.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_int, c_int, c_int, String, String, String, c_int, c_int]
    Vect_net_ttb_build_graph.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 404
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_shortest_path'):
    Vect_net_shortest_path = _libs['grass_vector.7.8'].Vect_net_shortest_path
    Vect_net_shortest_path.argtypes = [POINTER(struct_Map_info), c_int, c_int, POINTER(struct_ilist), POINTER(c_double)]
    Vect_net_shortest_path.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 406
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_ttb_shortest_path'):
    Vect_net_ttb_shortest_path = _libs['grass_vector.7.8'].Vect_net_ttb_shortest_path
    Vect_net_ttb_shortest_path.argtypes = [POINTER(struct_Map_info), c_int, c_int, c_int, c_int, c_int, POINTER(struct_ilist), POINTER(c_double)]
    Vect_net_ttb_shortest_path.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 408
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_get_graph'):
    Vect_net_get_graph = _libs['grass_vector.7.8'].Vect_net_get_graph
    Vect_net_get_graph.argtypes = [POINTER(struct_Map_info)]
    Vect_net_get_graph.restype = POINTER(dglGraph_s)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 409
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_get_line_cost'):
    Vect_net_get_line_cost = _libs['grass_vector.7.8'].Vect_net_get_line_cost
    Vect_net_get_line_cost.argtypes = [POINTER(struct_Map_info), c_int, c_int, POINTER(c_double)]
    Vect_net_get_line_cost.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 410
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_get_node_cost'):
    Vect_net_get_node_cost = _libs['grass_vector.7.8'].Vect_net_get_node_cost
    Vect_net_get_node_cost.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_double)]
    Vect_net_get_node_cost.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 411
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_nearest_nodes'):
    Vect_net_nearest_nodes = _libs['grass_vector.7.8'].Vect_net_nearest_nodes
    Vect_net_nearest_nodes.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_int, c_double, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(c_double)]
    Vect_net_nearest_nodes.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 414
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_shortest_path_coor'):
    Vect_net_shortest_path_coor = _libs['grass_vector.7.8'].Vect_net_shortest_path_coor
    Vect_net_shortest_path_coor.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(struct_line_pnts), POINTER(struct_ilist), POINTER(struct_ilist), POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double)]
    Vect_net_shortest_path_coor.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 419
if hasattr(_libs['grass_vector.7.8'], 'Vect_net_ttb_shortest_path_coor'):
    Vect_net_ttb_shortest_path_coor = _libs['grass_vector.7.8'].Vect_net_ttb_shortest_path_coor
    Vect_net_ttb_shortest_path_coor.argtypes = [POINTER(struct_Map_info), c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_int, POINTER(c_double), POINTER(struct_line_pnts), POINTER(struct_ilist), POINTER(struct_ilist), POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(c_double), POINTER(c_double)]
    Vect_net_ttb_shortest_path_coor.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 426
if hasattr(_libs['grass_vector.7.8'], 'Vect_topo_dump'):
    Vect_topo_dump = _libs['grass_vector.7.8'].Vect_topo_dump
    Vect_topo_dump.argtypes = [POINTER(struct_Map_info), POINTER(FILE)]
    Vect_topo_dump.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 427
if hasattr(_libs['grass_vector.7.8'], 'Vect_points_distance'):
    Vect_points_distance = _libs['grass_vector.7.8'].Vect_points_distance
    Vect_points_distance.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_int]
    Vect_points_distance.restype = c_double

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 429
if hasattr(_libs['grass_vector.7.8'], 'Vect_option_to_types'):
    Vect_option_to_types = _libs['grass_vector.7.8'].Vect_option_to_types
    Vect_option_to_types.argtypes = [POINTER(struct_Option)]
    Vect_option_to_types.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 430
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_map_lines'):
    Vect_copy_map_lines = _libs['grass_vector.7.8'].Vect_copy_map_lines
    Vect_copy_map_lines.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info)]
    Vect_copy_map_lines.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 431
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_map_lines_field'):
    Vect_copy_map_lines_field = _libs['grass_vector.7.8'].Vect_copy_map_lines_field
    Vect_copy_map_lines_field.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_Map_info)]
    Vect_copy_map_lines_field.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 432
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy'):
    Vect_copy = _libs['grass_vector.7.8'].Vect_copy
    Vect_copy.argtypes = [String, String, String]
    Vect_copy.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 433
if hasattr(_libs['grass_vector.7.8'], 'Vect_rename'):
    Vect_rename = _libs['grass_vector.7.8'].Vect_rename
    Vect_rename.argtypes = [String, String]
    Vect_rename.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 434
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_table'):
    Vect_copy_table = _libs['grass_vector.7.8'].Vect_copy_table
    Vect_copy_table.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), c_int, c_int, String, c_int]
    Vect_copy_table.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 436
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_table_by_cat_list'):
    Vect_copy_table_by_cat_list = _libs['grass_vector.7.8'].Vect_copy_table_by_cat_list
    Vect_copy_table_by_cat_list.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), c_int, c_int, String, c_int, POINTER(struct_cat_list)]
    Vect_copy_table_by_cat_list.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 438
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_table_by_cats'):
    Vect_copy_table_by_cats = _libs['grass_vector.7.8'].Vect_copy_table_by_cats
    Vect_copy_table_by_cats.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), c_int, c_int, String, c_int, POINTER(c_int), c_int]
    Vect_copy_table_by_cats.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 440
if hasattr(_libs['grass_vector.7.8'], 'Vect_copy_tables'):
    Vect_copy_tables = _libs['grass_vector.7.8'].Vect_copy_tables
    Vect_copy_tables.argtypes = [POINTER(struct_Map_info), POINTER(struct_Map_info), c_int]
    Vect_copy_tables.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 441
if hasattr(_libs['grass_vector.7.8'], 'Vect_delete'):
    Vect_delete = _libs['grass_vector.7.8'].Vect_delete
    Vect_delete.argtypes = [String]
    Vect_delete.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 442
if hasattr(_libs['grass_vector.7.8'], 'Vect_segment_intersection'):
    Vect_segment_intersection = _libs['grass_vector.7.8'].Vect_segment_intersection
    Vect_segment_intersection.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
    Vect_segment_intersection.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 446
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_intersection'):
    Vect_line_intersection = _libs['grass_vector.7.8'].Vect_line_intersection
    Vect_line_intersection.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(struct_bound_box), POINTER(struct_bound_box), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(c_int), POINTER(c_int), c_int]
    Vect_line_intersection.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 450
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_intersection2'):
    Vect_line_intersection2 = _libs['grass_vector.7.8'].Vect_line_intersection2
    Vect_line_intersection2.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(struct_bound_box), POINTER(struct_bound_box), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(POINTER(POINTER(struct_line_pnts))), POINTER(c_int), POINTER(c_int), c_int]
    Vect_line_intersection2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 454
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_check_intersection'):
    Vect_line_check_intersection = _libs['grass_vector.7.8'].Vect_line_check_intersection
    Vect_line_check_intersection.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]
    Vect_line_check_intersection.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 455
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_check_intersection2'):
    Vect_line_check_intersection2 = _libs['grass_vector.7.8'].Vect_line_check_intersection2
    Vect_line_check_intersection2.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]
    Vect_line_check_intersection2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 456
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_get_intersections'):
    Vect_line_get_intersections = _libs['grass_vector.7.8'].Vect_line_get_intersections
    Vect_line_get_intersections.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]
    Vect_line_get_intersections.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 458
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_get_intersections2'):
    Vect_line_get_intersections2 = _libs['grass_vector.7.8'].Vect_line_get_intersections2
    Vect_line_get_intersections2.argtypes = [POINTER(struct_line_pnts), POINTER(struct_line_pnts), POINTER(struct_line_pnts), c_int]
    Vect_line_get_intersections2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 460
if hasattr(_libs['grass_vector.7.8'], 'Vect_subst_var'):
    Vect_subst_var = _libs['grass_vector.7.8'].Vect_subst_var
    Vect_subst_var.argtypes = [String, POINTER(struct_Map_info)]
    if sizeof(c_int) == sizeof(c_void_p):
        Vect_subst_var.restype = ReturnString
    else:
        Vect_subst_var.restype = String
        Vect_subst_var.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 463
if hasattr(_libs['grass_vector.7.8'], 'Vect_spatial_index_init'):
    Vect_spatial_index_init = _libs['grass_vector.7.8'].Vect_spatial_index_init
    Vect_spatial_index_init.argtypes = [POINTER(struct_spatial_index), c_int]
    Vect_spatial_index_init.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 464
if hasattr(_libs['grass_vector.7.8'], 'Vect_spatial_index_destroy'):
    Vect_spatial_index_destroy = _libs['grass_vector.7.8'].Vect_spatial_index_destroy
    Vect_spatial_index_destroy.argtypes = [POINTER(struct_spatial_index)]
    Vect_spatial_index_destroy.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 465
if hasattr(_libs['grass_vector.7.8'], 'Vect_spatial_index_add_item'):
    Vect_spatial_index_add_item = _libs['grass_vector.7.8'].Vect_spatial_index_add_item
    Vect_spatial_index_add_item.argtypes = [POINTER(struct_spatial_index), c_int, POINTER(struct_bound_box)]
    Vect_spatial_index_add_item.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 466
if hasattr(_libs['grass_vector.7.8'], 'Vect_spatial_index_del_item'):
    Vect_spatial_index_del_item = _libs['grass_vector.7.8'].Vect_spatial_index_del_item
    Vect_spatial_index_del_item.argtypes = [POINTER(struct_spatial_index), c_int, POINTER(struct_bound_box)]
    Vect_spatial_index_del_item.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 467
if hasattr(_libs['grass_vector.7.8'], 'Vect_spatial_index_select'):
    Vect_spatial_index_select = _libs['grass_vector.7.8'].Vect_spatial_index_select
    Vect_spatial_index_select.argtypes = [POINTER(struct_spatial_index), POINTER(struct_bound_box), POINTER(struct_ilist)]
    Vect_spatial_index_select.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 470
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_ascii'):
    Vect_read_ascii = _libs['grass_vector.7.8'].Vect_read_ascii
    Vect_read_ascii.argtypes = [POINTER(FILE), POINTER(struct_Map_info)]
    Vect_read_ascii.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 471
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_ascii_head'):
    Vect_read_ascii_head = _libs['grass_vector.7.8'].Vect_read_ascii_head
    Vect_read_ascii_head.argtypes = [POINTER(FILE), POINTER(struct_Map_info)]
    Vect_read_ascii_head.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 472
if hasattr(_libs['grass_vector.7.8'], 'Vect_write_ascii'):
    Vect_write_ascii = _libs['grass_vector.7.8'].Vect_write_ascii
    Vect_write_ascii.argtypes = [POINTER(FILE), POINTER(FILE), POINTER(struct_Map_info), c_int, c_int, c_int, String, c_int, c_int, c_int, POINTER(struct_cat_list), String, POINTER(POINTER(c_char)), c_int]
    Vect_write_ascii.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 476
if hasattr(_libs['grass_vector.7.8'], 'Vect_write_ascii_head'):
    Vect_write_ascii_head = _libs['grass_vector.7.8'].Vect_write_ascii_head
    Vect_write_ascii_head.argtypes = [POINTER(FILE), POINTER(struct_Map_info)]
    Vect_write_ascii_head.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 479
if hasattr(_libs['grass_vector.7.8'], 'Vect_sfa_get_line_type'):
    Vect_sfa_get_line_type = _libs['grass_vector.7.8'].Vect_sfa_get_line_type
    Vect_sfa_get_line_type.argtypes = [POINTER(struct_line_pnts), c_int, c_int]
    Vect_sfa_get_line_type.restype = SF_FeatureType

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 480
if hasattr(_libs['grass_vector.7.8'], 'Vect_sfa_get_type'):
    Vect_sfa_get_type = _libs['grass_vector.7.8'].Vect_sfa_get_type
    Vect_sfa_get_type.argtypes = [SF_FeatureType]
    Vect_sfa_get_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 481
if hasattr(_libs['grass_vector.7.8'], 'Vect_sfa_check_line_type'):
    Vect_sfa_check_line_type = _libs['grass_vector.7.8'].Vect_sfa_check_line_type
    Vect_sfa_check_line_type.argtypes = [POINTER(struct_line_pnts), c_int, SF_FeatureType, c_int]
    Vect_sfa_check_line_type.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 482
if hasattr(_libs['grass_vector.7.8'], 'Vect_sfa_line_dimension'):
    Vect_sfa_line_dimension = _libs['grass_vector.7.8'].Vect_sfa_line_dimension
    Vect_sfa_line_dimension.argtypes = [c_int]
    Vect_sfa_line_dimension.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 483
if hasattr(_libs['grass_vector.7.8'], 'Vect_sfa_line_geometry_type'):
    Vect_sfa_line_geometry_type = _libs['grass_vector.7.8'].Vect_sfa_line_geometry_type
    Vect_sfa_line_geometry_type.argtypes = [POINTER(struct_line_pnts), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        Vect_sfa_line_geometry_type.restype = ReturnString
    else:
        Vect_sfa_line_geometry_type.restype = String
        Vect_sfa_line_geometry_type.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 484
if hasattr(_libs['grass_vector.7.8'], 'Vect_sfa_line_astext'):
    Vect_sfa_line_astext = _libs['grass_vector.7.8'].Vect_sfa_line_astext
    Vect_sfa_line_astext.argtypes = [POINTER(struct_line_pnts), c_int, c_int, c_int, POINTER(FILE)]
    Vect_sfa_line_astext.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 485
if hasattr(_libs['grass_vector.7.8'], 'Vect_sfa_is_line_simple'):
    Vect_sfa_is_line_simple = _libs['grass_vector.7.8'].Vect_sfa_is_line_simple
    Vect_sfa_is_line_simple.argtypes = [POINTER(struct_line_pnts), c_int, c_int]
    Vect_sfa_is_line_simple.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 486
if hasattr(_libs['grass_vector.7.8'], 'Vect_sfa_is_line_closed'):
    Vect_sfa_is_line_closed = _libs['grass_vector.7.8'].Vect_sfa_is_line_closed
    Vect_sfa_is_line_closed.argtypes = [POINTER(struct_line_pnts), c_int, c_int]
    Vect_sfa_is_line_closed.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 487
if hasattr(_libs['grass_vector.7.8'], 'Vect_sfa_get_num_features'):
    Vect_sfa_get_num_features = _libs['grass_vector.7.8'].Vect_sfa_get_num_features
    Vect_sfa_get_num_features.argtypes = [POINTER(struct_Map_info)]
    Vect_sfa_get_num_features.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 492
if hasattr(_libs['grass_vector.7.8'], 'Vect_print_header'):
    Vect_print_header = _libs['grass_vector.7.8'].Vect_print_header
    Vect_print_header.argtypes = [POINTER(struct_Map_info)]
    Vect_print_header.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 493
if hasattr(_libs['grass_vector.7.8'], 'Vect__init_head'):
    Vect__init_head = _libs['grass_vector.7.8'].Vect__init_head
    Vect__init_head.argtypes = [POINTER(struct_Map_info)]
    Vect__init_head.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 496
if hasattr(_libs['grass_vector.7.8'], 'Vect_coor_info'):
    Vect_coor_info = _libs['grass_vector.7.8'].Vect_coor_info
    Vect_coor_info.argtypes = [POINTER(struct_Map_info), POINTER(struct_Coor_info)]
    Vect_coor_info.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 497
if hasattr(_libs['grass_vector.7.8'], 'Vect_maptype_info'):
    Vect_maptype_info = _libs['grass_vector.7.8'].Vect_maptype_info
    Vect_maptype_info.argtypes = [POINTER(struct_Map_info)]
    Vect_maptype_info.restype = c_char_p

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 498
if hasattr(_libs['grass_vector.7.8'], 'Vect_maptype'):
    Vect_maptype = _libs['grass_vector.7.8'].Vect_maptype
    Vect_maptype.argtypes = [POINTER(struct_Map_info)]
    Vect_maptype.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 499
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_topo'):
    Vect_open_topo = _libs['grass_vector.7.8'].Vect_open_topo
    Vect_open_topo.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_open_topo.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 500
if hasattr(_libs['grass_vector.7.8'], 'Vect_save_topo'):
    Vect_save_topo = _libs['grass_vector.7.8'].Vect_save_topo
    Vect_save_topo.argtypes = [POINTER(struct_Map_info)]
    Vect_save_topo.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 501
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_sidx'):
    Vect_open_sidx = _libs['grass_vector.7.8'].Vect_open_sidx
    Vect_open_sidx.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_open_sidx.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 502
if hasattr(_libs['grass_vector.7.8'], 'Vect_save_sidx'):
    Vect_save_sidx = _libs['grass_vector.7.8'].Vect_save_sidx
    Vect_save_sidx.argtypes = [POINTER(struct_Map_info)]
    Vect_save_sidx.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 503
if hasattr(_libs['grass_vector.7.8'], 'Vect_sidx_dump'):
    Vect_sidx_dump = _libs['grass_vector.7.8'].Vect_sidx_dump
    Vect_sidx_dump.argtypes = [POINTER(struct_Map_info), POINTER(FILE)]
    Vect_sidx_dump.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 504
if hasattr(_libs['grass_vector.7.8'], 'Vect_build_sidx_from_topo'):
    Vect_build_sidx_from_topo = _libs['grass_vector.7.8'].Vect_build_sidx_from_topo
    Vect_build_sidx_from_topo.argtypes = [POINTER(struct_Map_info)]
    Vect_build_sidx_from_topo.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 505
if hasattr(_libs['grass_vector.7.8'], 'Vect_build_sidx'):
    Vect_build_sidx = _libs['grass_vector.7.8'].Vect_build_sidx
    Vect_build_sidx.argtypes = [POINTER(struct_Map_info)]
    Vect_build_sidx.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 506
if hasattr(_libs['grass_vector.7.8'], 'Vect_open_fidx'):
    Vect_open_fidx = _libs['grass_vector.7.8'].Vect_open_fidx
    Vect_open_fidx.argtypes = [POINTER(struct_Map_info), POINTER(struct_Format_info_offset)]
    Vect_open_fidx.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 507
if hasattr(_libs['grass_vector.7.8'], 'Vect_save_fidx'):
    Vect_save_fidx = _libs['grass_vector.7.8'].Vect_save_fidx
    Vect_save_fidx.argtypes = [POINTER(struct_Map_info), POINTER(struct_Format_info_offset)]
    Vect_save_fidx.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 508
if hasattr(_libs['grass_vector.7.8'], 'Vect_fidx_dump'):
    Vect_fidx_dump = _libs['grass_vector.7.8'].Vect_fidx_dump
    Vect_fidx_dump.argtypes = [POINTER(struct_Map_info), POINTER(FILE)]
    Vect_fidx_dump.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 509
if hasattr(_libs['grass_vector.7.8'], 'Vect_save_frmt'):
    Vect_save_frmt = _libs['grass_vector.7.8'].Vect_save_frmt
    Vect_save_frmt.argtypes = [POINTER(struct_Map_info)]
    Vect_save_frmt.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 511
if hasattr(_libs['grass_vector.7.8'], 'Vect__write_head'):
    Vect__write_head = _libs['grass_vector.7.8'].Vect__write_head
    Vect__write_head.argtypes = [POINTER(struct_Map_info)]
    Vect__write_head.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 512
if hasattr(_libs['grass_vector.7.8'], 'Vect__read_head'):
    Vect__read_head = _libs['grass_vector.7.8'].Vect__read_head
    Vect__read_head.argtypes = [POINTER(struct_Map_info)]
    Vect__read_head.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 513
if hasattr(_libs['grass_vector.7.8'], 'V1_open_old_nat'):
    V1_open_old_nat = _libs['grass_vector.7.8'].V1_open_old_nat
    V1_open_old_nat.argtypes = [POINTER(struct_Map_info), c_int]
    V1_open_old_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 514
if hasattr(_libs['grass_vector.7.8'], 'V1_open_old_ogr'):
    V1_open_old_ogr = _libs['grass_vector.7.8'].V1_open_old_ogr
    V1_open_old_ogr.argtypes = [POINTER(struct_Map_info), c_int]
    V1_open_old_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 515
if hasattr(_libs['grass_vector.7.8'], 'V1_open_old_pg'):
    V1_open_old_pg = _libs['grass_vector.7.8'].V1_open_old_pg
    V1_open_old_pg.argtypes = [POINTER(struct_Map_info), c_int]
    V1_open_old_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 516
if hasattr(_libs['grass_vector.7.8'], 'V2_open_old_ogr'):
    V2_open_old_ogr = _libs['grass_vector.7.8'].V2_open_old_ogr
    V2_open_old_ogr.argtypes = [POINTER(struct_Map_info)]
    V2_open_old_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 517
if hasattr(_libs['grass_vector.7.8'], 'V2_open_old_pg'):
    V2_open_old_pg = _libs['grass_vector.7.8'].V2_open_old_pg
    V2_open_old_pg.argtypes = [POINTER(struct_Map_info)]
    V2_open_old_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 518
if hasattr(_libs['grass_vector.7.8'], 'V1_open_new_nat'):
    V1_open_new_nat = _libs['grass_vector.7.8'].V1_open_new_nat
    V1_open_new_nat.argtypes = [POINTER(struct_Map_info), String, c_int]
    V1_open_new_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 519
if hasattr(_libs['grass_vector.7.8'], 'V1_open_new_ogr'):
    V1_open_new_ogr = _libs['grass_vector.7.8'].V1_open_new_ogr
    V1_open_new_ogr.argtypes = [POINTER(struct_Map_info), String, c_int]
    V1_open_new_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 520
if hasattr(_libs['grass_vector.7.8'], 'V1_open_new_pg'):
    V1_open_new_pg = _libs['grass_vector.7.8'].V1_open_new_pg
    V1_open_new_pg.argtypes = [POINTER(struct_Map_info), String, c_int]
    V1_open_new_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 521
if hasattr(_libs['grass_vector.7.8'], 'V1_rewind_nat'):
    V1_rewind_nat = _libs['grass_vector.7.8'].V1_rewind_nat
    V1_rewind_nat.argtypes = [POINTER(struct_Map_info)]
    V1_rewind_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 522
if hasattr(_libs['grass_vector.7.8'], 'V1_rewind_ogr'):
    V1_rewind_ogr = _libs['grass_vector.7.8'].V1_rewind_ogr
    V1_rewind_ogr.argtypes = [POINTER(struct_Map_info)]
    V1_rewind_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 523
if hasattr(_libs['grass_vector.7.8'], 'V1_rewind_pg'):
    V1_rewind_pg = _libs['grass_vector.7.8'].V1_rewind_pg
    V1_rewind_pg.argtypes = [POINTER(struct_Map_info)]
    V1_rewind_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 524
if hasattr(_libs['grass_vector.7.8'], 'V2_rewind_nat'):
    V2_rewind_nat = _libs['grass_vector.7.8'].V2_rewind_nat
    V2_rewind_nat.argtypes = [POINTER(struct_Map_info)]
    V2_rewind_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 525
if hasattr(_libs['grass_vector.7.8'], 'V2_rewind_ogr'):
    V2_rewind_ogr = _libs['grass_vector.7.8'].V2_rewind_ogr
    V2_rewind_ogr.argtypes = [POINTER(struct_Map_info)]
    V2_rewind_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 526
if hasattr(_libs['grass_vector.7.8'], 'V2_rewind_pg'):
    V2_rewind_pg = _libs['grass_vector.7.8'].V2_rewind_pg
    V2_rewind_pg.argtypes = [POINTER(struct_Map_info)]
    V2_rewind_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 527
if hasattr(_libs['grass_vector.7.8'], 'V1_close_nat'):
    V1_close_nat = _libs['grass_vector.7.8'].V1_close_nat
    V1_close_nat.argtypes = [POINTER(struct_Map_info)]
    V1_close_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 528
if hasattr(_libs['grass_vector.7.8'], 'V1_close_ogr'):
    V1_close_ogr = _libs['grass_vector.7.8'].V1_close_ogr
    V1_close_ogr.argtypes = [POINTER(struct_Map_info)]
    V1_close_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 529
if hasattr(_libs['grass_vector.7.8'], 'V1_close_pg'):
    V1_close_pg = _libs['grass_vector.7.8'].V1_close_pg
    V1_close_pg.argtypes = [POINTER(struct_Map_info)]
    V1_close_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 530
if hasattr(_libs['grass_vector.7.8'], 'V2_close_ogr'):
    V2_close_ogr = _libs['grass_vector.7.8'].V2_close_ogr
    V2_close_ogr.argtypes = [POINTER(struct_Map_info)]
    V2_close_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 531
if hasattr(_libs['grass_vector.7.8'], 'V2_close_pg'):
    V2_close_pg = _libs['grass_vector.7.8'].V2_close_pg
    V2_close_pg.argtypes = [POINTER(struct_Map_info)]
    V2_close_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 534
if hasattr(_libs['grass_vector.7.8'], 'V1_read_line_nat'):
    V1_read_line_nat = _libs['grass_vector.7.8'].V1_read_line_nat
    V1_read_line_nat.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), off_t]
    V1_read_line_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 536
if hasattr(_libs['grass_vector.7.8'], 'V1_read_line_ogr'):
    V1_read_line_ogr = _libs['grass_vector.7.8'].V1_read_line_ogr
    V1_read_line_ogr.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), off_t]
    V1_read_line_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 538
if hasattr(_libs['grass_vector.7.8'], 'V1_read_line_pg'):
    V1_read_line_pg = _libs['grass_vector.7.8'].V1_read_line_pg
    V1_read_line_pg.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), off_t]
    V1_read_line_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 540
if hasattr(_libs['grass_vector.7.8'], 'V2_read_line_nat'):
    V2_read_line_nat = _libs['grass_vector.7.8'].V2_read_line_nat
    V2_read_line_nat.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), c_int]
    V2_read_line_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 542
if hasattr(_libs['grass_vector.7.8'], 'V2_read_line_sfa'):
    V2_read_line_sfa = _libs['grass_vector.7.8'].V2_read_line_sfa
    V2_read_line_sfa.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), c_int]
    V2_read_line_sfa.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 544
if hasattr(_libs['grass_vector.7.8'], 'V2_read_line_pg'):
    V2_read_line_pg = _libs['grass_vector.7.8'].V2_read_line_pg
    V2_read_line_pg.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), c_int]
    V2_read_line_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 546
if hasattr(_libs['grass_vector.7.8'], 'V1_read_next_line_nat'):
    V1_read_next_line_nat = _libs['grass_vector.7.8'].V1_read_next_line_nat
    V1_read_next_line_nat.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V1_read_next_line_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 548
if hasattr(_libs['grass_vector.7.8'], 'V1_read_next_line_ogr'):
    V1_read_next_line_ogr = _libs['grass_vector.7.8'].V1_read_next_line_ogr
    V1_read_next_line_ogr.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V1_read_next_line_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 550
if hasattr(_libs['grass_vector.7.8'], 'V1_read_next_line_pg'):
    V1_read_next_line_pg = _libs['grass_vector.7.8'].V1_read_next_line_pg
    V1_read_next_line_pg.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V1_read_next_line_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 552
if hasattr(_libs['grass_vector.7.8'], 'V2_read_next_line_nat'):
    V2_read_next_line_nat = _libs['grass_vector.7.8'].V2_read_next_line_nat
    V2_read_next_line_nat.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V2_read_next_line_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 554
if hasattr(_libs['grass_vector.7.8'], 'V2_read_next_line_ogr'):
    V2_read_next_line_ogr = _libs['grass_vector.7.8'].V2_read_next_line_ogr
    V2_read_next_line_ogr.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V2_read_next_line_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 556
if hasattr(_libs['grass_vector.7.8'], 'V2_read_next_line_pg'):
    V2_read_next_line_pg = _libs['grass_vector.7.8'].V2_read_next_line_pg
    V2_read_next_line_pg.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V2_read_next_line_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 558
if hasattr(_libs['grass_vector.7.8'], 'V1_delete_line_nat'):
    V1_delete_line_nat = _libs['grass_vector.7.8'].V1_delete_line_nat
    V1_delete_line_nat.argtypes = [POINTER(struct_Map_info), off_t]
    V1_delete_line_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 559
if hasattr(_libs['grass_vector.7.8'], 'V1_delete_line_ogr'):
    V1_delete_line_ogr = _libs['grass_vector.7.8'].V1_delete_line_ogr
    V1_delete_line_ogr.argtypes = [POINTER(struct_Map_info), off_t]
    V1_delete_line_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 560
if hasattr(_libs['grass_vector.7.8'], 'V1_delete_line_pg'):
    V1_delete_line_pg = _libs['grass_vector.7.8'].V1_delete_line_pg
    V1_delete_line_pg.argtypes = [POINTER(struct_Map_info), off_t]
    V1_delete_line_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 561
if hasattr(_libs['grass_vector.7.8'], 'V2_delete_line_nat'):
    V2_delete_line_nat = _libs['grass_vector.7.8'].V2_delete_line_nat
    V2_delete_line_nat.argtypes = [POINTER(struct_Map_info), off_t]
    V2_delete_line_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 562
if hasattr(_libs['grass_vector.7.8'], 'V2_delete_line_sfa'):
    V2_delete_line_sfa = _libs['grass_vector.7.8'].V2_delete_line_sfa
    V2_delete_line_sfa.argtypes = [POINTER(struct_Map_info), off_t]
    V2_delete_line_sfa.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 563
if hasattr(_libs['grass_vector.7.8'], 'V2_delete_line_pg'):
    V2_delete_line_pg = _libs['grass_vector.7.8'].V2_delete_line_pg
    V2_delete_line_pg.argtypes = [POINTER(struct_Map_info), off_t]
    V2_delete_line_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 564
if hasattr(_libs['grass_vector.7.8'], 'V1_restore_line_nat'):
    V1_restore_line_nat = _libs['grass_vector.7.8'].V1_restore_line_nat
    V1_restore_line_nat.argtypes = [POINTER(struct_Map_info), off_t, off_t]
    V1_restore_line_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 565
if hasattr(_libs['grass_vector.7.8'], 'V2_restore_line_nat'):
    V2_restore_line_nat = _libs['grass_vector.7.8'].V2_restore_line_nat
    V2_restore_line_nat.argtypes = [POINTER(struct_Map_info), off_t, off_t]
    V2_restore_line_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 566
if hasattr(_libs['grass_vector.7.8'], 'V1_write_line_nat'):
    V1_write_line_nat = _libs['grass_vector.7.8'].V1_write_line_nat
    V1_write_line_nat.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V1_write_line_nat.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 568
if hasattr(_libs['grass_vector.7.8'], 'V1_write_line_ogr'):
    V1_write_line_ogr = _libs['grass_vector.7.8'].V1_write_line_ogr
    V1_write_line_ogr.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V1_write_line_ogr.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 570
if hasattr(_libs['grass_vector.7.8'], 'V1_write_line_pg'):
    V1_write_line_pg = _libs['grass_vector.7.8'].V1_write_line_pg
    V1_write_line_pg.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V1_write_line_pg.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 572
if hasattr(_libs['grass_vector.7.8'], 'V2_write_line_nat'):
    V2_write_line_nat = _libs['grass_vector.7.8'].V2_write_line_nat
    V2_write_line_nat.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V2_write_line_nat.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 574
if hasattr(_libs['grass_vector.7.8'], 'V2_write_line_sfa'):
    V2_write_line_sfa = _libs['grass_vector.7.8'].V2_write_line_sfa
    V2_write_line_sfa.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V2_write_line_sfa.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 576
if hasattr(_libs['grass_vector.7.8'], 'V2_write_line_pg'):
    V2_write_line_pg = _libs['grass_vector.7.8'].V2_write_line_pg
    V2_write_line_pg.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V2_write_line_pg.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 578
if hasattr(_libs['grass_vector.7.8'], 'V1_rewrite_line_nat'):
    V1_rewrite_line_nat = _libs['grass_vector.7.8'].V1_rewrite_line_nat
    V1_rewrite_line_nat.argtypes = [POINTER(struct_Map_info), off_t, c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V1_rewrite_line_nat.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 580
if hasattr(_libs['grass_vector.7.8'], 'V1_rewrite_line_ogr'):
    V1_rewrite_line_ogr = _libs['grass_vector.7.8'].V1_rewrite_line_ogr
    V1_rewrite_line_ogr.argtypes = [POINTER(struct_Map_info), off_t, c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V1_rewrite_line_ogr.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 582
if hasattr(_libs['grass_vector.7.8'], 'V1_rewrite_line_pg'):
    V1_rewrite_line_pg = _libs['grass_vector.7.8'].V1_rewrite_line_pg
    V1_rewrite_line_pg.argtypes = [POINTER(struct_Map_info), off_t, c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V1_rewrite_line_pg.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 584
if hasattr(_libs['grass_vector.7.8'], 'V2_rewrite_line_nat'):
    V2_rewrite_line_nat = _libs['grass_vector.7.8'].V2_rewrite_line_nat
    V2_rewrite_line_nat.argtypes = [POINTER(struct_Map_info), off_t, c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V2_rewrite_line_nat.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 586
if hasattr(_libs['grass_vector.7.8'], 'V2_rewrite_line_sfa'):
    V2_rewrite_line_sfa = _libs['grass_vector.7.8'].V2_rewrite_line_sfa
    V2_rewrite_line_sfa.argtypes = [POINTER(struct_Map_info), off_t, c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V2_rewrite_line_sfa.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 588
if hasattr(_libs['grass_vector.7.8'], 'V2_rewrite_line_pg'):
    V2_rewrite_line_pg = _libs['grass_vector.7.8'].V2_rewrite_line_pg
    V2_rewrite_line_pg.argtypes = [POINTER(struct_Map_info), off_t, c_int, POINTER(struct_line_pnts), POINTER(struct_line_cats)]
    V2_rewrite_line_pg.restype = off_t

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 592
if hasattr(_libs['grass_vector.7.8'], 'Vect_build_nat'):
    Vect_build_nat = _libs['grass_vector.7.8'].Vect_build_nat
    Vect_build_nat.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_build_nat.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 593
if hasattr(_libs['grass_vector.7.8'], 'Vect__build_downgrade'):
    Vect__build_downgrade = _libs['grass_vector.7.8'].Vect__build_downgrade
    Vect__build_downgrade.argtypes = [POINTER(struct_Map_info), c_int]
    Vect__build_downgrade.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 594
if hasattr(_libs['grass_vector.7.8'], 'Vect__build_sfa'):
    Vect__build_sfa = _libs['grass_vector.7.8'].Vect__build_sfa
    Vect__build_sfa.argtypes = [POINTER(struct_Map_info), c_int]
    Vect__build_sfa.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 595
if hasattr(_libs['grass_vector.7.8'], 'Vect_build_ogr'):
    Vect_build_ogr = _libs['grass_vector.7.8'].Vect_build_ogr
    Vect_build_ogr.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_build_ogr.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 596
if hasattr(_libs['grass_vector.7.8'], 'Vect_build_pg'):
    Vect_build_pg = _libs['grass_vector.7.8'].Vect_build_pg
    Vect_build_pg.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_build_pg.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 597
if hasattr(_libs['grass_vector.7.8'], 'Vect_build_line_area'):
    Vect_build_line_area = _libs['grass_vector.7.8'].Vect_build_line_area
    Vect_build_line_area.argtypes = [POINTER(struct_Map_info), c_int, c_int]
    Vect_build_line_area.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 598
if hasattr(_libs['grass_vector.7.8'], 'Vect_isle_find_area'):
    Vect_isle_find_area = _libs['grass_vector.7.8'].Vect_isle_find_area
    Vect_isle_find_area.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]
    Vect_isle_find_area.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 599
if hasattr(_libs['grass_vector.7.8'], 'Vect_attach_isle'):
    Vect_attach_isle = _libs['grass_vector.7.8'].Vect_attach_isle
    Vect_attach_isle.argtypes = [POINTER(struct_Map_info), c_int, POINTER(struct_bound_box)]
    Vect_attach_isle.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 600
if hasattr(_libs['grass_vector.7.8'], 'Vect_attach_isles'):
    Vect_attach_isles = _libs['grass_vector.7.8'].Vect_attach_isles
    Vect_attach_isles.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box)]
    Vect_attach_isles.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 601
if hasattr(_libs['grass_vector.7.8'], 'Vect_attach_centroids'):
    Vect_attach_centroids = _libs['grass_vector.7.8'].Vect_attach_centroids
    Vect_attach_centroids.argtypes = [POINTER(struct_Map_info), POINTER(struct_bound_box)]
    Vect_attach_centroids.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 605
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_line_geos'):
    Vect_read_line_geos = _libs['grass_vector.7.8'].Vect_read_line_geos
    Vect_read_line_geos.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_int)]
    Vect_read_line_geos.restype = POINTER(GEOSGeometry)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 606
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_to_geos'):
    Vect_line_to_geos = _libs['grass_vector.7.8'].Vect_line_to_geos
    Vect_line_to_geos.argtypes = [POINTER(struct_line_pnts), c_int, c_int]
    Vect_line_to_geos.restype = POINTER(GEOSGeometry)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 607
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_area_geos'):
    Vect_read_area_geos = _libs['grass_vector.7.8'].Vect_read_area_geos
    Vect_read_area_geos.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_read_area_geos.restype = POINTER(GEOSGeometry)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 608
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_area_points_geos'):
    Vect_get_area_points_geos = _libs['grass_vector.7.8'].Vect_get_area_points_geos
    Vect_get_area_points_geos.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_area_points_geos.restype = POINTER(GEOSCoordSequence)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 609
if hasattr(_libs['grass_vector.7.8'], 'Vect_get_isle_points_geos'):
    Vect_get_isle_points_geos = _libs['grass_vector.7.8'].Vect_get_isle_points_geos
    Vect_get_isle_points_geos.argtypes = [POINTER(struct_Map_info), c_int]
    Vect_get_isle_points_geos.restype = POINTER(GEOSCoordSequence)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 610
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_to_wkt'):
    Vect_line_to_wkt = _libs['grass_vector.7.8'].Vect_line_to_wkt
    Vect_line_to_wkt.argtypes = [POINTER(struct_line_pnts), c_int, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        Vect_line_to_wkt.restype = ReturnString
    else:
        Vect_line_to_wkt.restype = String
        Vect_line_to_wkt.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 611
if hasattr(_libs['grass_vector.7.8'], 'Vect_line_to_wkb'):
    Vect_line_to_wkb = _libs['grass_vector.7.8'].Vect_line_to_wkb
    Vect_line_to_wkb.argtypes = [POINTER(struct_line_pnts), c_int, c_int, POINTER(c_size_t)]
    Vect_line_to_wkb.restype = POINTER(c_ubyte)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 613
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_area_to_wkt'):
    Vect_read_area_to_wkt = _libs['grass_vector.7.8'].Vect_read_area_to_wkt
    Vect_read_area_to_wkt.argtypes = [POINTER(struct_Map_info), c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        Vect_read_area_to_wkt.restype = ReturnString
    else:
        Vect_read_area_to_wkt.restype = String
        Vect_read_area_to_wkt.errcheck = ReturnString

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 614
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_area_to_wkb'):
    Vect_read_area_to_wkb = _libs['grass_vector.7.8'].Vect_read_area_to_wkb
    Vect_read_area_to_wkb.argtypes = [POINTER(struct_Map_info), c_int, POINTER(c_size_t)]
    Vect_read_area_to_wkb.restype = POINTER(c_ubyte)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 615
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_line_to_wkb'):
    Vect_read_line_to_wkb = _libs['grass_vector.7.8'].Vect_read_line_to_wkb
    Vect_read_line_to_wkb.argtypes = [POINTER(struct_Map_info), POINTER(struct_line_pnts), POINTER(struct_line_cats), c_int, POINTER(c_size_t), POINTER(c_int)]
    Vect_read_line_to_wkb.restype = POINTER(c_ubyte)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 622
if hasattr(_libs['grass_vector.7.8'], 'Vect_read_colors'):
    Vect_read_colors = _libs['grass_vector.7.8'].Vect_read_colors
    Vect_read_colors.argtypes = [String, String, POINTER(struct_Colors)]
    Vect_read_colors.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 623
if hasattr(_libs['grass_vector.7.8'], 'Vect_remove_colors'):
    Vect_remove_colors = _libs['grass_vector.7.8'].Vect_remove_colors
    Vect_remove_colors.argtypes = [String, String]
    Vect_remove_colors.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 624
if hasattr(_libs['grass_vector.7.8'], 'Vect_write_colors'):
    Vect_write_colors = _libs['grass_vector.7.8'].Vect_write_colors
    Vect_write_colors.argtypes = [String, String, POINTER(struct_Colors)]
    Vect_write_colors.restype = None

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/defs/vector.h: 627
if hasattr(_libs['grass_vector.7.8'], 'RTreeSearch2'):
    RTreeSearch2 = _libs['grass_vector.7.8'].RTreeSearch2
    RTreeSearch2.argtypes = [POINTER(struct_RTree), POINTER(struct_RTree_Rect), POINTER(struct_ilist)]
    RTreeSearch2.restype = c_int

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 8
try:
    GV_DIRECTORY = 'vector'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 10
try:
    GV_FRMT_ELEMENT = 'frmt'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 12
try:
    GV_COOR_ELEMENT = 'coor'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 14
try:
    GV_HEAD_ELEMENT = 'head'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 16
try:
    GV_DBLN_ELEMENT = 'dbln'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 18
try:
    GV_HIST_ELEMENT = 'hist'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 20
try:
    GV_TOPO_ELEMENT = 'topo'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 22
try:
    GV_SIDX_ELEMENT = 'sidx'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 24
try:
    GV_CIDX_ELEMENT = 'cidx'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 26
try:
    GV_FIDX_ELEMENT = 'fidx'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 28
try:
    GV_COLR_ELEMENT = 'colr'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 30
try:
    GV_COLR2_DIRECTORY = 'vcolr2'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 32
try:
    GV_TIMESTAMP_ELEMENT = 'timestamp'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 45
try:
    PORT_DOUBLE = 8
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 46
try:
    PORT_FLOAT = 4
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 47
try:
    PORT_LONG = 4
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 48
try:
    PORT_INT = 4
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 49
try:
    PORT_SHORT = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 50
try:
    PORT_CHAR = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 51
try:
    PORT_OFF_T = 8
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 57
try:
    DBL_SIZ = 8
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 58
try:
    FLT_SIZ = 4
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 59
try:
    LNG_SIZ = 4
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 60
try:
    SHRT_SIZ = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 66
try:
    PORT_DOUBLE_MAX = 1.7976931348623157e+308
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 67
try:
    PORT_DOUBLE_MIN = 2.2250738585072014e-308
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 68
try:
    PORT_FLOAT_MAX = 3.40282347e+38
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 69
try:
    PORT_FLOAT_MIN = 1.17549435e-38
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 70
try:
    PORT_LONG_MAX = 2147483647
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 71
try:
    PORT_LONG_MIN = (-2147483647)
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 72
try:
    PORT_INT_MAX = 2147483647
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 73
try:
    PORT_INT_MIN = (-2147483647)
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 74
try:
    PORT_SHORT_MAX = 32767
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 75
try:
    PORT_SHORT_MIN = (-32768)
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 76
try:
    PORT_CHAR_MAX = 127
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 77
try:
    PORT_CHAR_MIN = (-128)
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 83
try:
    GV_FORMAT_NATIVE = 0
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 85
try:
    GV_FORMAT_OGR = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 87
try:
    GV_FORMAT_OGR_DIRECT = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 89
try:
    GV_FORMAT_POSTGIS = 3
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 92
try:
    GV_TOPO_NATIVE = 0
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 94
try:
    GV_TOPO_PSEUDO = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 96
try:
    GV_TOPO_POSTGIS = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 99
try:
    GV_1TABLE = 0
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 101
try:
    GV_MTABLE = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 104
try:
    GV_MODE_READ = 0
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 106
try:
    GV_MODE_WRITE = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 108
try:
    GV_MODE_RW = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 111
try:
    VECT_OPEN_CODE = 1428335138
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 113
try:
    VECT_CLOSED_CODE = 581575253
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 116
try:
    LEVEL_1 = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 118
try:
    LEVEL_2 = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 120
try:
    LEVEL_3 = 3
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 123
try:
    GV_BUILD_NONE = 0
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 125
try:
    GV_BUILD_BASE = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 127
try:
    GV_BUILD_AREAS = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 129
try:
    GV_BUILD_ATTACH_ISLES = 3
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 131
try:
    GV_BUILD_CENTROIDS = 4
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 133
try:
    GV_BUILD_ALL = GV_BUILD_CENTROIDS
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 136
def VECT_OPEN(Map):
    return (((Map.contents.open).value) == VECT_OPEN_CODE)

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 139
try:
    GV_MEMORY_ALWAYS = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 140
try:
    GV_MEMORY_NEVER = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 141
try:
    GV_MEMORY_AUTO = 3
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 144
try:
    GV_COOR_HEAD_SIZE = 14
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 146
try:
    GRASS_V_VERSION = '5.0'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 149
try:
    GV_COOR_VER_MAJOR = 5
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 150
try:
    GV_COOR_VER_MINOR = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 151
try:
    GV_TOPO_VER_MAJOR = 5
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 152
try:
    GV_TOPO_VER_MINOR = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 153
try:
    GV_SIDX_VER_MAJOR = 5
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 154
try:
    GV_SIDX_VER_MINOR = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 155
try:
    GV_CIDX_VER_MAJOR = 5
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 156
try:
    GV_CIDX_VER_MINOR = 0
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 160
try:
    GV_COOR_EARLIEST_MAJOR = 5
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 161
try:
    GV_COOR_EARLIEST_MINOR = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 162
try:
    GV_TOPO_EARLIEST_MAJOR = 5
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 163
try:
    GV_TOPO_EARLIEST_MINOR = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 164
try:
    GV_SIDX_EARLIEST_MAJOR = 5
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 165
try:
    GV_SIDX_EARLIEST_MINOR = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 166
try:
    GV_CIDX_EARLIEST_MAJOR = 5
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 167
try:
    GV_CIDX_EARLIEST_MINOR = 0
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 170
try:
    WITHOUT_Z = 0
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 171
try:
    WITH_Z = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 174
try:
    GV_LEFT = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 175
try:
    GV_RIGHT = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 178
try:
    GV_FORWARD = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 179
try:
    GV_BACKWARD = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 182
try:
    GV_POINT = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 183
try:
    GV_LINE = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 184
try:
    GV_BOUNDARY = 4
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 185
try:
    GV_CENTROID = 8
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 186
try:
    GV_FACE = 16
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 187
try:
    GV_KERNEL = 32
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 188
try:
    GV_AREA = 64
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 189
try:
    GV_VOLUME = 128
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 191
try:
    GV_POINTS = (GV_POINT | GV_CENTROID)
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 192
try:
    GV_LINES = (GV_LINE | GV_BOUNDARY)
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 195
try:
    GV_STORE_POINT = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 196
try:
    GV_STORE_LINE = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 197
try:
    GV_STORE_BOUNDARY = 3
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 198
try:
    GV_STORE_CENTROID = 4
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 199
try:
    GV_STORE_FACE = 5
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 200
try:
    GV_STORE_KERNEL = 6
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 201
try:
    GV_STORE_AREA = 7
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 202
try:
    GV_STORE_VOLUME = 8
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 205
try:
    GV_ON_AND = 'AND'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 206
try:
    GV_ON_OVERLAP = 'OVERLAP'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 217
try:
    GV_NCATS_MAX = PORT_INT_MAX
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 219
try:
    GV_FIELD_MAX = PORT_INT_MAX
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 221
try:
    GV_CAT_MAX = PORT_INT_MAX
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 224
try:
    GV_ASCII_FORMAT_POINT = 0
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 226
try:
    GV_ASCII_FORMAT_STD = 1
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 228
try:
    GV_ASCII_FORMAT_WKT = 2
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 259
try:
    HEADSTR = 50
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 262
try:
    GV_PG_FID_COLUMN = 'fid'
except:
    pass

# C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_defines.h: 264
try:
    GV_PG_GEOMETRY_COLUMN = 'geom'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 8
try:
    GV_DIRECTORY = 'vector'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 10
try:
    GV_FRMT_ELEMENT = 'frmt'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 12
try:
    GV_COOR_ELEMENT = 'coor'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 14
try:
    GV_HEAD_ELEMENT = 'head'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 16
try:
    GV_DBLN_ELEMENT = 'dbln'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 18
try:
    GV_HIST_ELEMENT = 'hist'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 20
try:
    GV_TOPO_ELEMENT = 'topo'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 22
try:
    GV_SIDX_ELEMENT = 'sidx'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 24
try:
    GV_CIDX_ELEMENT = 'cidx'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 26
try:
    GV_FIDX_ELEMENT = 'fidx'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 28
try:
    GV_COLR_ELEMENT = 'colr'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 30
try:
    GV_COLR2_DIRECTORY = 'vcolr2'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 32
try:
    GV_TIMESTAMP_ELEMENT = 'timestamp'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 45
try:
    PORT_DOUBLE = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 46
try:
    PORT_FLOAT = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 47
try:
    PORT_LONG = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 48
try:
    PORT_INT = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 49
try:
    PORT_SHORT = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 50
try:
    PORT_CHAR = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 51
try:
    PORT_OFF_T = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 57
try:
    DBL_SIZ = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 58
try:
    FLT_SIZ = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 59
try:
    LNG_SIZ = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 60
try:
    SHRT_SIZ = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 66
try:
    PORT_DOUBLE_MAX = 1.7976931348623157e+308
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 67
try:
    PORT_DOUBLE_MIN = 2.2250738585072014e-308
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 68
try:
    PORT_FLOAT_MAX = 3.40282347e+38
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 69
try:
    PORT_FLOAT_MIN = 1.17549435e-38
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 70
try:
    PORT_LONG_MAX = 2147483647
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 71
try:
    PORT_LONG_MIN = (-2147483647)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 72
try:
    PORT_INT_MAX = 2147483647
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 73
try:
    PORT_INT_MIN = (-2147483647)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 74
try:
    PORT_SHORT_MAX = 32767
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 75
try:
    PORT_SHORT_MIN = (-32768)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 76
try:
    PORT_CHAR_MAX = 127
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 77
try:
    PORT_CHAR_MIN = (-128)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 83
try:
    GV_FORMAT_NATIVE = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 85
try:
    GV_FORMAT_OGR = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 87
try:
    GV_FORMAT_OGR_DIRECT = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 89
try:
    GV_FORMAT_POSTGIS = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 92
try:
    GV_TOPO_NATIVE = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 94
try:
    GV_TOPO_PSEUDO = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 96
try:
    GV_TOPO_POSTGIS = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 99
try:
    GV_1TABLE = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 101
try:
    GV_MTABLE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 104
try:
    GV_MODE_READ = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 106
try:
    GV_MODE_WRITE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 108
try:
    GV_MODE_RW = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 111
try:
    VECT_OPEN_CODE = 1428335138
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 113
try:
    VECT_CLOSED_CODE = 581575253
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 116
try:
    LEVEL_1 = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 118
try:
    LEVEL_2 = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 120
try:
    LEVEL_3 = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 123
try:
    GV_BUILD_NONE = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 125
try:
    GV_BUILD_BASE = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 127
try:
    GV_BUILD_AREAS = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 129
try:
    GV_BUILD_ATTACH_ISLES = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 131
try:
    GV_BUILD_CENTROIDS = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 133
try:
    GV_BUILD_ALL = GV_BUILD_CENTROIDS
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 136
def VECT_OPEN(Map):
    return (((Map.contents.open).value) == VECT_OPEN_CODE)

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 139
try:
    GV_MEMORY_ALWAYS = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 140
try:
    GV_MEMORY_NEVER = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 141
try:
    GV_MEMORY_AUTO = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 144
try:
    GV_COOR_HEAD_SIZE = 14
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 146
try:
    GRASS_V_VERSION = '5.0'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 149
try:
    GV_COOR_VER_MAJOR = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 150
try:
    GV_COOR_VER_MINOR = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 151
try:
    GV_TOPO_VER_MAJOR = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 152
try:
    GV_TOPO_VER_MINOR = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 153
try:
    GV_SIDX_VER_MAJOR = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 154
try:
    GV_SIDX_VER_MINOR = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 155
try:
    GV_CIDX_VER_MAJOR = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 156
try:
    GV_CIDX_VER_MINOR = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 160
try:
    GV_COOR_EARLIEST_MAJOR = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 161
try:
    GV_COOR_EARLIEST_MINOR = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 162
try:
    GV_TOPO_EARLIEST_MAJOR = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 163
try:
    GV_TOPO_EARLIEST_MINOR = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 164
try:
    GV_SIDX_EARLIEST_MAJOR = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 165
try:
    GV_SIDX_EARLIEST_MINOR = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 166
try:
    GV_CIDX_EARLIEST_MAJOR = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 167
try:
    GV_CIDX_EARLIEST_MINOR = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 170
try:
    WITHOUT_Z = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 171
try:
    WITH_Z = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 174
try:
    GV_LEFT = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 175
try:
    GV_RIGHT = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 178
try:
    GV_FORWARD = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 179
try:
    GV_BACKWARD = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 182
try:
    GV_POINT = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 183
try:
    GV_LINE = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 184
try:
    GV_BOUNDARY = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 185
try:
    GV_CENTROID = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 186
try:
    GV_FACE = 16
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 187
try:
    GV_KERNEL = 32
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 188
try:
    GV_AREA = 64
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 189
try:
    GV_VOLUME = 128
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 191
try:
    GV_POINTS = (GV_POINT | GV_CENTROID)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 192
try:
    GV_LINES = (GV_LINE | GV_BOUNDARY)
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 195
try:
    GV_STORE_POINT = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 196
try:
    GV_STORE_LINE = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 197
try:
    GV_STORE_BOUNDARY = 3
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 198
try:
    GV_STORE_CENTROID = 4
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 199
try:
    GV_STORE_FACE = 5
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 200
try:
    GV_STORE_KERNEL = 6
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 201
try:
    GV_STORE_AREA = 7
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 202
try:
    GV_STORE_VOLUME = 8
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 205
try:
    GV_ON_AND = 'AND'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 206
try:
    GV_ON_OVERLAP = 'OVERLAP'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 217
try:
    GV_NCATS_MAX = PORT_INT_MAX
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 219
try:
    GV_FIELD_MAX = PORT_INT_MAX
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 221
try:
    GV_CAT_MAX = PORT_INT_MAX
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 224
try:
    GV_ASCII_FORMAT_POINT = 0
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 226
try:
    GV_ASCII_FORMAT_STD = 1
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 228
try:
    GV_ASCII_FORMAT_WKT = 2
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 259
try:
    HEADSTR = 50
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 262
try:
    GV_PG_FID_COLUMN = 'fid'
except:
    pass

# C:\\msys64\\usr\\src\\grass785\\dist.x86_64-w64-mingw32\\include\\grass\\vect\\dig_defines.h: 264
try:
    GV_PG_GEOMETRY_COLUMN = 'geom'
except:
    pass

site_att = struct_site_att # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 46

bound_box = struct_bound_box # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 65

gvfile = struct_gvfile # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 96

field_info = struct_field_info # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 134

dblinks = struct_dblinks # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 165

Port_info = struct_Port_info # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 186

recycle = struct_recycle # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 272

Version_info = struct_Version_info # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 278

dig_head = struct_dig_head # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 294

Coor_info = struct_Coor_info # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 379

Format_info_offset = struct_Format_info_offset # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 397

line_pnts = struct_line_pnts # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1675

Format_info_cache = struct_Format_info_cache # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 461

Format_info_ogr = struct_Format_info_ogr # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 516

Format_info_pg = struct_Format_info_pg # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 602

Format_info = struct_Format_info # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 713

Cat_index = struct_Cat_index # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 732

P_node = struct_P_node # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1448

P_line = struct_P_line # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1574

P_area = struct_P_area # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1605

P_isle = struct_P_isle # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1646

Plus_head = struct_Plus_head # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 784

Graph_info = struct_Graph_info # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1220

Map_info = struct_Map_info # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1259

P_topo_l = struct_P_topo_l # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1494

P_topo_b = struct_P_topo_b # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1509

P_topo_c = struct_P_topo_c # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1532

P_topo_f = struct_P_topo_f # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1543

P_topo_k = struct_P_topo_k # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1563

line_cats = struct_line_cats # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1702

cat_list = struct_cat_list # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1723

boxlist = struct_boxlist # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1750

varray = struct_varray # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1779

spatial_index = struct_spatial_index # C:/msys64/usr/src/grass785/dist.x86_64-w64-mingw32/include/grass/vect/dig_structs.h: 1799

# No inserted files

