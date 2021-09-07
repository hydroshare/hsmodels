import os

import pytest
from pydantic.schema import schema

from hsmodels.schemas import (
    FileSetMetadata,
    GeographicFeatureMetadata,
    GeographicRasterMetadata,
    MultidimensionalMetadata,
    ReferencedTimeSeriesMetadata,
    ResourceMetadata,
    SingleFileMetadata,
    TimeSeriesMetadata,
)
from hsmodels.schemas.fields import (
    BoxCoverage,
    BoxSpatialReference,
    Contributor,
    Creator,
    PointCoverage,
    PointSpatialReference,
)


@pytest.fixture(scope="function")
def change_test_dir(request):
    os.chdir(request.fspath.dirname)
    yield
    os.chdir(request.config.invocation_dir)


read_only_fields = [
    (ResourceMetadata, ['type', 'identifier', 'created', 'modified', 'published', 'url']),
    (GeographicRasterMetadata, ['type', 'url']),
    (GeographicFeatureMetadata, ['type', 'url']),
    (MultidimensionalMetadata, ['type', 'url']),
    (ReferencedTimeSeriesMetadata, ['type', 'url']),
    (FileSetMetadata, ['type', 'url']),
    (SingleFileMetadata, ['type', 'url']),
    (TimeSeriesMetadata, ['type', 'url']),
    (Creator, ['description']),
    (Contributor, ['description']),
    (BoxCoverage, ['type']),
    (BoxSpatialReference, ['type']),
    (PointSpatialReference, ['type']),
    (PointCoverage, ['type']),
]


@pytest.mark.parametrize("read_only_field", read_only_fields)
def test_readonly(read_only_field):
    clazz, fields = read_only_field
    s = schema([clazz])["definitions"][clazz.__name__]

    for prop in s["properties"]:
        if prop in fields:
            assert "readOnly" in s["properties"][prop] and s["properties"][prop]["readOnly"] is True
        else:
            assert "readOnly" not in s["properties"][prop]
