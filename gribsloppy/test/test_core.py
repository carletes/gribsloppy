import unittest

from gribsloppy import GribFile


__all__ = [
    "GribFileTest",
]


class GribFileTest(unittest.TestCase):

    def test_incorrect_usage(self):
        g = GribFile("regular_latlon_surface.grib1")

        with self.assertRaises(Exception) as exc:
            g.get_long("Ni")
        self.assertEqual("GRIB file regular_latlon_surface.grib1 not open",
                         exc.exception.message)

        with self.assertRaises(Exception) as exc:
            g.get_double("latitudeOfFirstGridPointInDegrees")
        self.assertEqual("GRIB file regular_latlon_surface.grib1 not open",
                         exc.exception.message)

    def test_read_file(self):
        # Calls are much simpler now!
        #
        # This is pretty much like
        #
        #   http://ecmwf.int/publications/manuals/grib_api/get_8c-example.html
        with GribFile("regular_latlon_surface.grib1") as g:
            self.assertEqual(16, g.get_long("Ni"))
            self.assertEqual(31, g.get_long("Nj"))
            self.assertEqual(60.0,
                             g.get_double("latitudeOfFirstGridPointInDegrees"))
            lon = g.get_double("longitudeOfFirstGridPointInDegrees")
            self.assertEqual(0.0, lon)
            self.assertEqual(0.0,
                             g.get_double("latitudeOfLastGridPointInDegrees"))
            self.assertEqual(30.0,
                             g.get_double("longitudeOfLastGridPointInDegrees"))
            self.assertEqual(2.0,
                             g.get_double("jDirectionIncrementInDegrees"))
            self.assertEqual(2.0,
                             g.get_double("iDirectionIncrementInDegrees"))


if __name__ == "__main__":
    unittest.main()
