import os
from django.contrib.gis.utils import LayerMapping
from .models import district_boundaries,taluka_boundaries,state_maharashtra

district_boundaries_mapping = {
    'district_n' : 'district_n',
    'district_c' : 'district_c',
    'geom' : 'MULTIPOLYGON',
}

district_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'district_boundaries.shp'),
)

def run_district(verbose=True):
    lm = LayerMapping(
        district_boundaries, district_shp, district_boundaries_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=False, verbose=verbose)

taluka_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'taluka_boundaries.shp'),
)

taluka_boundaries_mapping = {
    'district_n' : 'district_n',
    'district_c' : 'district_c',
    'taluka_nam' : 'taluka_nam',
    'taluka_cod' : 'taluka_cod',
    'geom' : 'MULTIPOLYGON',
}

def run_taluka(verbose=True):
    lm = LayerMapping(
        taluka_boundaries, taluka_shp, taluka_boundaries_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=False, verbose=verbose)

maharashtra_mapping = {
    'st_nm' : 'ST_NM',
    'st_cen_cd' : 'ST_CEN_CD',
    'dt_cen_cd' : 'DT_CEN_CD',
    'district' : 'DISTRICT',
    'geom' : 'MULTIPOLYGON',
}

maha_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Maharashtra.shp'),
)

def run_maha(verbose=True):
    lm = LayerMapping(
        state_maharashtra, maha_shp, maharashtra_mapping ,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=False, verbose=verbose)