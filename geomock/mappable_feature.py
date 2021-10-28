from typing import Callable, TypeVar
from pymonad.maybe import Just, Nothing, Maybe
import shapely_geojson

S = TypeVar("S")
T = TypeVar("T")

class Feature(shapely_geojson.Feature):
    def map(self: 'Feature', fn: Callable[[S],T]) -> 'Feature[T]':
        return Feature(fn(self.geometry), properties = self.properties)
