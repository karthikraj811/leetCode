import geopandas as gpd
import pandas as pd
import fiona
from fiona.drvsupport import supported_drivers
supported_drivers['KML'] = 'rw'

from geopandas.tools import sjoin

import shapely
from shapely.geometry import Point
from shapely import geometry
from shapely.geometry import Polygon

import numpy as np

import os


ap_path = r"C:\Users\Ganesh\Downloads\ID_Grab_POC.kml"
identifier = 'id_grab_poc'

## Don't need to change anything from here onwards
project_name = os.path.splitext(os.path.basename(ap_path))[0]
json_out = fr"C:\Users\Ganesh\Downloads\{project_name}.json"
csv_out = fr"C:\Users\Ganesh\Downloads\{project_name}.csv"