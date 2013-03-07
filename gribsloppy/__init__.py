"""Python bindings for ECMWF's grib_api."""

from gribsloppy import core


__all__ = [
    "GribFile",
    "__version__",
]


GribFile = core.GribFile

__version__ = "0.1.5"
