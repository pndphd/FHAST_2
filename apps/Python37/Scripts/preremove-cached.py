import importlib.util
import gzip
import os
import sys

cachedirs = {}
with gzip.open("{}/etc/setup/{}.lst.gz".format(os.environ['OSGEO4W_ROOT'], sys.argv[1])) as f:
    for py in f:
        py = py.decode("utf-8").strip()
        if py.endswith(".py"):
            try:
                pyc = importlib.util.cache_from_source(py)
                os.remove(pyc)
                print("Removed {}".format(pyc))
                cachedirs[ os.path.dirname(pyc) ] = 1
            except:
                pass

for cachedir in sorted(cachedirs.keys(), reverse=True):
    try:
        os.rmdir(cachedir)
        print("Removed directory {}".format(cachedir))
    except:
        pass
