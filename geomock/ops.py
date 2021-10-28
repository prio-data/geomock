import numpy as np
from pymonad.maybe import Just
from shapely.affinity import translate

def recenter(new_centroid, geom):
    trns = [0,0]
    origin = np.array(geom.centroid.xy)
    new = np.array(new_centroid.xy)
    diff = new - origin
    return translate(geom, *diff)
