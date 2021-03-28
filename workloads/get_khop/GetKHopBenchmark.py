# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _GetKHopBenchmark
else:
    import _GetKHopBenchmark

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _GetKHopBenchmark.delete_SwigPyIterator

    def value(self):
        return _GetKHopBenchmark.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _GetKHopBenchmark.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _GetKHopBenchmark.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _GetKHopBenchmark.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _GetKHopBenchmark.SwigPyIterator_equal(self, x)

    def copy(self):
        return _GetKHopBenchmark.SwigPyIterator_copy(self)

    def next(self):
        return _GetKHopBenchmark.SwigPyIterator_next(self)

    def __next__(self):
        return _GetKHopBenchmark.SwigPyIterator___next__(self)

    def previous(self):
        return _GetKHopBenchmark.SwigPyIterator_previous(self)

    def advance(self, n):
        return _GetKHopBenchmark.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _GetKHopBenchmark.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _GetKHopBenchmark.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _GetKHopBenchmark.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _GetKHopBenchmark.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _GetKHopBenchmark.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _GetKHopBenchmark.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _GetKHopBenchmark:
_GetKHopBenchmark.SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _GetKHopBenchmark.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _GetKHopBenchmark.IntVector___nonzero__(self)

    def __bool__(self):
        return _GetKHopBenchmark.IntVector___bool__(self)

    def __len__(self):
        return _GetKHopBenchmark.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _GetKHopBenchmark.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _GetKHopBenchmark.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _GetKHopBenchmark.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _GetKHopBenchmark.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _GetKHopBenchmark.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _GetKHopBenchmark.IntVector___setitem__(self, *args)

    def pop(self):
        return _GetKHopBenchmark.IntVector_pop(self)

    def append(self, x):
        return _GetKHopBenchmark.IntVector_append(self, x)

    def empty(self):
        return _GetKHopBenchmark.IntVector_empty(self)

    def size(self):
        return _GetKHopBenchmark.IntVector_size(self)

    def swap(self, v):
        return _GetKHopBenchmark.IntVector_swap(self, v)

    def begin(self):
        return _GetKHopBenchmark.IntVector_begin(self)

    def end(self):
        return _GetKHopBenchmark.IntVector_end(self)

    def rbegin(self):
        return _GetKHopBenchmark.IntVector_rbegin(self)

    def rend(self):
        return _GetKHopBenchmark.IntVector_rend(self)

    def clear(self):
        return _GetKHopBenchmark.IntVector_clear(self)

    def get_allocator(self):
        return _GetKHopBenchmark.IntVector_get_allocator(self)

    def pop_back(self):
        return _GetKHopBenchmark.IntVector_pop_back(self)

    def erase(self, *args):
        return _GetKHopBenchmark.IntVector_erase(self, *args)

    def __init__(self, *args):
        _GetKHopBenchmark.IntVector_swiginit(self, _GetKHopBenchmark.new_IntVector(*args))

    def push_back(self, x):
        return _GetKHopBenchmark.IntVector_push_back(self, x)

    def front(self):
        return _GetKHopBenchmark.IntVector_front(self)

    def back(self):
        return _GetKHopBenchmark.IntVector_back(self)

    def assign(self, n, x):
        return _GetKHopBenchmark.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _GetKHopBenchmark.IntVector_resize(self, *args)

    def insert(self, *args):
        return _GetKHopBenchmark.IntVector_insert(self, *args)

    def reserve(self, n):
        return _GetKHopBenchmark.IntVector_reserve(self, n)

    def capacity(self):
        return _GetKHopBenchmark.IntVector_capacity(self)
    __swig_destroy__ = _GetKHopBenchmark.delete_IntVector

# Register IntVector in _GetKHopBenchmark:
_GetKHopBenchmark.IntVector_swigregister(IntVector)

class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _GetKHopBenchmark.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _GetKHopBenchmark.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _GetKHopBenchmark.DoubleVector___bool__(self)

    def __len__(self):
        return _GetKHopBenchmark.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _GetKHopBenchmark.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _GetKHopBenchmark.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _GetKHopBenchmark.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _GetKHopBenchmark.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _GetKHopBenchmark.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _GetKHopBenchmark.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _GetKHopBenchmark.DoubleVector_pop(self)

    def append(self, x):
        return _GetKHopBenchmark.DoubleVector_append(self, x)

    def empty(self):
        return _GetKHopBenchmark.DoubleVector_empty(self)

    def size(self):
        return _GetKHopBenchmark.DoubleVector_size(self)

    def swap(self, v):
        return _GetKHopBenchmark.DoubleVector_swap(self, v)

    def begin(self):
        return _GetKHopBenchmark.DoubleVector_begin(self)

    def end(self):
        return _GetKHopBenchmark.DoubleVector_end(self)

    def rbegin(self):
        return _GetKHopBenchmark.DoubleVector_rbegin(self)

    def rend(self):
        return _GetKHopBenchmark.DoubleVector_rend(self)

    def clear(self):
        return _GetKHopBenchmark.DoubleVector_clear(self)

    def get_allocator(self):
        return _GetKHopBenchmark.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _GetKHopBenchmark.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _GetKHopBenchmark.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _GetKHopBenchmark.DoubleVector_swiginit(self, _GetKHopBenchmark.new_DoubleVector(*args))

    def push_back(self, x):
        return _GetKHopBenchmark.DoubleVector_push_back(self, x)

    def front(self):
        return _GetKHopBenchmark.DoubleVector_front(self)

    def back(self):
        return _GetKHopBenchmark.DoubleVector_back(self)

    def assign(self, n, x):
        return _GetKHopBenchmark.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _GetKHopBenchmark.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _GetKHopBenchmark.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _GetKHopBenchmark.DoubleVector_reserve(self, n)

    def capacity(self):
        return _GetKHopBenchmark.DoubleVector_capacity(self)
    __swig_destroy__ = _GetKHopBenchmark.delete_DoubleVector

# Register DoubleVector in _GetKHopBenchmark:
_GetKHopBenchmark.DoubleVector_swigregister(DoubleVector)


def getDegrees(arg1):
    return _GetKHopBenchmark.getDegrees(arg1)

def degOrdDesc(arg1, arg2):
    return _GetKHopBenchmark.degOrdDesc(arg1, arg2)

def randomOrd(arg1, arg2):
    return _GetKHopBenchmark.randomOrd(arg1, arg2)

def degreeDistribution(arg1):
    return _GetKHopBenchmark.degreeDistribution(arg1)
class GetKHopBenchmark(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def getNeighboursVector(self, arg2, arg3):
        return _GetKHopBenchmark.GetKHopBenchmark_getNeighboursVector(self, arg2, arg3)

    def getAllSinkIds(self):
        return _GetKHopBenchmark.GetKHopBenchmark_getAllSinkIds(self)

    def getVectorWeights(self):
        return _GetKHopBenchmark.GetKHopBenchmark_getVectorWeights(self)

    def getExecTimes(self):
        return _GetKHopBenchmark.GetKHopBenchmark_getExecTimes(self)

    def getVsSeen(self):
        return _GetKHopBenchmark.GetKHopBenchmark_getVsSeen(self)

    def readGraph(self):
        return _GetKHopBenchmark.GetKHopBenchmark_readGraph(self)

    def printAllSinkIds(self):
        return _GetKHopBenchmark.GetKHopBenchmark_printAllSinkIds(self)

    def printVertexOrder(self):
        return _GetKHopBenchmark.GetKHopBenchmark_printVertexOrder(self)

    def displayStats(self):
        return _GetKHopBenchmark.GetKHopBenchmark_displayStats(self)

    def buildCumSum(self):
        return _GetKHopBenchmark.GetKHopBenchmark_buildCumSum(self)

    def calcOrder(self, arg2):
        return _GetKHopBenchmark.GetKHopBenchmark_calcOrder(self, arg2)

    def calcAllSinkIds(self):
        return _GetKHopBenchmark.GetKHopBenchmark_calcAllSinkIds(self)

    def calcStats(self):
        return _GetKHopBenchmark.GetKHopBenchmark_calcStats(self)

    def runBenchmark(self):
        return _GetKHopBenchmark.GetKHopBenchmark_runBenchmark(self)

    def runExperiment(self):
        return _GetKHopBenchmark.GetKHopBenchmark_runExperiment(self)

    def sample(self):
        return _GetKHopBenchmark.GetKHopBenchmark_sample(self)

    def __init__(self, arg2, arg3, arg4, arg5, arg6, arg7):
        _GetKHopBenchmark.GetKHopBenchmark_swiginit(self, _GetKHopBenchmark.new_GetKHopBenchmark(arg2, arg3, arg4, arg5, arg6, arg7))
    nNodes = property(_GetKHopBenchmark.GetKHopBenchmark_nNodes_get, _GetKHopBenchmark.GetKHopBenchmark_nNodes_set)
    nSinks = property(_GetKHopBenchmark.GetKHopBenchmark_nSinks_get, _GetKHopBenchmark.GetKHopBenchmark_nSinks_set)
    nIncomps = property(_GetKHopBenchmark.GetKHopBenchmark_nIncomps_get, _GetKHopBenchmark.GetKHopBenchmark_nIncomps_set)
    nSeenAll = property(_GetKHopBenchmark.GetKHopBenchmark_nSeenAll_get, _GetKHopBenchmark.GetKHopBenchmark_nSeenAll_set)
    path = property(_GetKHopBenchmark.GetKHopBenchmark_path_get, _GetKHopBenchmark.GetKHopBenchmark_path_set)
    order = property(_GetKHopBenchmark.GetKHopBenchmark_order_get, _GetKHopBenchmark.GetKHopBenchmark_order_set)
    nExpts = property(_GetKHopBenchmark.GetKHopBenchmark_nExpts_get, _GetKHopBenchmark.GetKHopBenchmark_nExpts_set)
    K = property(_GetKHopBenchmark.GetKHopBenchmark_K_get, _GetKHopBenchmark.GetKHopBenchmark_K_set)
    nSamples = property(_GetKHopBenchmark.GetKHopBenchmark_nSamples_get, _GetKHopBenchmark.GetKHopBenchmark_nSamples_set)
    mean = property(_GetKHopBenchmark.GetKHopBenchmark_mean_get, _GetKHopBenchmark.GetKHopBenchmark_mean_set)
    stdev = property(_GetKHopBenchmark.GetKHopBenchmark_stdev_get, _GetKHopBenchmark.GetKHopBenchmark_stdev_set)
    khopNeighbours = property(_GetKHopBenchmark.GetKHopBenchmark_khopNeighbours_get, _GetKHopBenchmark.GetKHopBenchmark_khopNeighbours_set)
    stats = property(_GetKHopBenchmark.GetKHopBenchmark_stats_get, _GetKHopBenchmark.GetKHopBenchmark_stats_set)
    edges = property(_GetKHopBenchmark.GetKHopBenchmark_edges_get, _GetKHopBenchmark.GetKHopBenchmark_edges_set)
    vertexOrder = property(_GetKHopBenchmark.GetKHopBenchmark_vertexOrder_get, _GetKHopBenchmark.GetKHopBenchmark_vertexOrder_set)
    sids = property(_GetKHopBenchmark.GetKHopBenchmark_sids_get, _GetKHopBenchmark.GetKHopBenchmark_sids_set)
    execTimes = property(_GetKHopBenchmark.GetKHopBenchmark_execTimes_get, _GetKHopBenchmark.GetKHopBenchmark_execTimes_set)
    vsSeen = property(_GetKHopBenchmark.GetKHopBenchmark_vsSeen_get, _GetKHopBenchmark.GetKHopBenchmark_vsSeen_set)
    graph = property(_GetKHopBenchmark.GetKHopBenchmark_graph_get, _GetKHopBenchmark.GetKHopBenchmark_graph_set)
    sortedWts = property(_GetKHopBenchmark.GetKHopBenchmark_sortedWts_get, _GetKHopBenchmark.GetKHopBenchmark_sortedWts_set)
    cumSumWts = property(_GetKHopBenchmark.GetKHopBenchmark_cumSumWts_get, _GetKHopBenchmark.GetKHopBenchmark_cumSumWts_set)
    __swig_destroy__ = _GetKHopBenchmark.delete_GetKHopBenchmark

# Register GetKHopBenchmark in _GetKHopBenchmark:
_GetKHopBenchmark.GetKHopBenchmark_swigregister(GetKHopBenchmark)



