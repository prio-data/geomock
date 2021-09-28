import functools
import numpy as np
from shapely import geometry

def array_shape(shape_type):
    def wrapper(fn):
        @functools.wraps(fn)
        def inner(*args,**kwargs):
            return shape_type(np.rollaxis(fn(*args,**kwargs),0))
        return inner
    return wrapper

def normalize_extent(array):
    for i in range(array.shape[1]):
        a = array[:,i]
        mn = np.min(a)

        if mn < 0:
            a += np.abs(mn)
        else:
            a -= mn

        array[:,i] = a/np.max(a)
    return array

def with_normal_extent(fn):
    @functools.wraps(fn)
    def inner(*args,**kwargs):
        return normalize_extent(fn(*args,**kwargs))
    return inner

@array_shape(geometry.Polygon)
@with_normal_extent
def random_polygon(points: int, noise: float = .1)-> geometry.Polygon:
    a = ((np.linspace(1, points, points) / points)*3.14)*2
    a = np.concatenate([a, [a[0]]])
    rnd = np.concatenate([[0], np.random.rand(points-1)*noise, [0]])
    rnd = np.ones(rnd.shape[0]) * (1-noise) + rnd
    return np.stack([np.sin(a) * rnd, np.cos(a) * rnd], axis = 1)
