
from typing import Tuple, List, Optional
from functools import wraps
from toolz.functoolz import curry, compose
import click
from pymonad.maybe import Nothing
from shapely.geometry import Point
import shapely_geojson
from . import random_geometry, ops, util, mappable_feature

@click.group()
def cli():
    pass

@cli.command(name = "polygon")
@click.argument("points", type=int)
@click.option("-n","--noise", type=float, default = .2)
@click.option("-x","--centroid-x", type=float, default = None)
@click.option("-y","--centroid-y", type=float, default = None)
@click.option("-p","--property", multiple=True, type=(str, str), default = [])
def polygon(
        points: int = 10,
        noise: float = .2,
        centroid_x: float = 0.0,
        centroid_y: float = 0.0,
        property: List[Tuple[str,str]] = []):

    feature = mappable_feature.Feature(
            random_geometry.random_polygon(points, noise),
            properties = {k:util.microparse(v) for k,v in property}
            )

    if centroid_x is not None and centroid_y is not None:
        feature = feature.map(curry(ops.recenter, Point((centroid_x, centroid_y))))

    click.echo(shapely_geojson.dumps(feature))
