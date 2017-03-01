"""
[status.py]

The Ergonomica `status` module.
"""

import platform
import multiprocessing

try:
    import psutil
except ImportError:
    raise Exception("[ergo: PackageError]: Please pip install `psutil` for the `stat` package.")

def _cpu(command):
    if command == "model":
        return platform.processor()
    elif commmand == "cores":
        return multiprocessing.cpu_count()

def cpu(env, args, kwargs):
    return list(map(_cpu, args))

 def _ram(command):
     if command == "free":
         return psutil.virtual_memory().free
    
def ram(env, args, kwargs):
     return list(map(_ram, args))

verbs = {"cpu":cpu,
         "ram":ram,
        }
