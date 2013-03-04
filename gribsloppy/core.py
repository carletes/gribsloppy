"""Implementation of gribsloppy."""

import ctypes
import os


__all__ = [
    "GribFile",
]


shlib = ctypes.CDLL("libgrib_api.so")


class grib_context(ctypes.Structure):
    pass


class grib_handle(ctypes.Structure):
    pass


# grib_handle* grib_handle_new_from_message_copy(grib_context *c,
#                                                void *data,
#                                                size_t *length)
grib_handle_new_from_message_copy = shlib.grib_handle_new_from_message_copy
grib_handle_new_from_message_copy.argtypes = [
    ctypes.POINTER(grib_context),
    ctypes.c_void_p,
    ctypes.c_long,
]
grib_handle_new_from_message_copy.restype = ctypes.POINTER(grib_handle)

# int grib_handle_delete(grib_handle *h)
grib_handle_delete = shlib.grib_handle_delete
grib_handle_delete.argtypes = [
    ctypes.POINTER(grib_handle),
]
grib_handle_delete.restype = ctypes.c_int

# int grib_get_double(grib_handle *h, const char *key, double *value)
grib_get_double = shlib.grib_get_double
grib_get_double.argtypes = [
    ctypes.POINTER(grib_handle),
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_double),
]
grib_get_double.restype = ctypes.c_int

# int grib_get_long(grib_handle *h, const char *key, long *value)
grib_get_long = shlib.grib_get_long
grib_get_long.argtypes = [
    ctypes.POINTER(grib_handle),
    ctypes.c_char_p,
    ctypes.POINTER(ctypes.c_long),
]
grib_get_long.restype = ctypes.c_int


class GribFile(object):

    """A context manager representing a GRIB file object.

    """

    def __init__(self, fname):
        self.fname = fname
        self._handle = None

    def __enter__(self):
        with open(self.fname, "rb") as f:
            msg = f.read()
        msg_len = os.stat(self.fname).st_size
        self._handle = grib_handle_new_from_message_copy(None, msg, msg_len)
        return self

    def __exit__(self, *exc_info):
        grib_handle_delete(self._handle)
        self._handle = None

    def get_double(self, key):
        """Get a double value from a key, if several keys of the same name are
        present, the last one is returned.

        """
        if self._handle is None:
            raise Exception("GRIB file %s not open" % (self.fname,))

        val = ctypes.c_double()
        rc = grib_get_double(self._handle, key, ctypes.byref(val))
        if rc:
            raise Exception("grib_get_long() failed: %d" % (rc,))
        return val.value

    def get_long(self, key):
        """Get a long value from a key, if several keys of the same name are
        present, the last one is returned.

        """
        if self._handle is None:
            raise Exception("GRIB file %s not open" % (self.fname,))

        val = ctypes.c_long()
        rc = grib_get_long(self._handle, key, ctypes.byref(val))
        if rc:
            raise Exception("grib_get_long() failed: %d" % (rc,))
        return val.value
