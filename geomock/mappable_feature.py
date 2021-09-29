from typing import Callable, TypeVar
from pymonad.maybe import Just, Nothing, Maybe
import shapely_geojson

T = TypeVar("T")

class Feature(shapely_geojson.Feature):
    def map(self, fn: Callable[[T],Maybe[T]]):
        new_geometry = fn(self.geometry)
        return new_geometry.maybe(
                Nothing, lambda geom: Just(Feature(geom, properties = self.properties))
                )
