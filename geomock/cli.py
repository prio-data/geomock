
from typing import Tuple, List
from functools import wraps
import click
from shapely.geometry import Point
from shapely_geojson import Feature, dumps
from . import random_geometry, ops, util

@click.group()
def cli():
    pass

@cli.command(name = "polygon")
@click.argument("points", type=int)
@click.option("-n","--noise", type=float, default = .2)
@click.option("-x","--centroid-x", type=float, default = 0)
@click.option("-y","--centroid-y", type=float, default = 0)
@click.option("-p","--property", multiple=True, type=(str, str), default = [])
def polygon(
        points: int = 10,
        noise: float = .2,
        centroid_x: float = 0.0,
        centroid_y: float = 0.0,
        property: List[Tuple[str,str]] = []):
    geom = random_geometry.random_polygon(points, noise)
    geom = ops.recenter(geom, Point([(centroid_x, centroid_y)]))
    feature = Feature(geom,properties = {k:util.microparse(v) for k,v in property})
    click.echo(dumps(feature))
