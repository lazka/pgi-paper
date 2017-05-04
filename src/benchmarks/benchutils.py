import math
import sys
import timeit
import platform


def average(r):
    return float(sum(r)) / len(r)


def variance(r):
    avg = average(r)
    return float(sum(map(lambda x: (x - avg) ** 2, r))) / (len(r) - 1)


def stdev(r):
    return math.sqrt(variance(r))


timer = timeit.default_timer

def has_jit_enabled():
    try:
        import pypyjit
    except ImportError:
        return False

    res = [False]
    def should_not_be_called(*args):
        res[0] = True
    pypyjit.set_compile_hook(should_not_be_called)
    for i in xrange(5000):
        pass
    pypyjit.set_compile_hook(None)
    return res[0]


def get_exec_info():
    return "VM: %s, Version: %s, JIT: %d" % (
        platform.python_implementation(),
        ", ".join(sys.version.splitlines()),
        has_jit_enabled())
