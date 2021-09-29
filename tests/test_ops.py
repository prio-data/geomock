
import unittest
import random
import numpy 
from shapely.geometry import Point
from geomock import random_geometry, ops

class TestOps(unittest.TestCase):
    def test_recenter(self):
        for i in range(100):
            new_centroid = Point((random.random(), random.random()))
            centered_polygon = ops.recenter(new_centroid, random_geometry.random_polygon(100,.5)).value
            for tgt,res in zip(new_centroid.xy, centered_polygon.centroid.xy):
                numpy.testing.assert_array_almost_equal(tgt,res)
