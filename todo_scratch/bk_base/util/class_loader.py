import sys
from importlib import import_module
from importlib.abc import MetaPathFinder
from importlib.util import spec_from_file_location


def import_module_from_file_location(name, location):
    class Finder(MetaPathFinder):
        @staticmethod
        def find_spec(fullname, *_):
            if fullname == name:
                return spec_from_file_location(name, location)

    finder = Finder()
    sys.meta_path.insert(0, finder)
    try:
        return import_module(name)
    finally:
        sys.meta_path.remove(finder)
