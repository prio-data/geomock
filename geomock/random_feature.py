from typing import Dict, Any
from geomock import mappable_feature, random_geometry

def polygon(points: int, noise: int, properties = Dict[str,Any]):
    return mappable_feature.Feature(
            geometry = random_geometry.polygon(points, noise),
            properties = properties
            )
