#!/usr/bin/env python
import sys

#reload() to reload modules
if float(sys.version[:3]) >= 3.0:
    import importlib
    def reload(module):
        return importlib.reload(module)
