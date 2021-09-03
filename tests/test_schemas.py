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
    (ResourceMetadata, ['type', 'identifier', 'created', 'modified', 'published']),
    (GeographicRasterMetadata, ['type']),
    (GeographicFeatureMetadata, ['type']),
    (MultidimensionalMetadata, ['type']),
    (ReferencedTimeSeriesMetadata, ['type']),
    (FileSetMetadata, ['type']),
    (SingleFileMetadata, ['type']),
    (TimeSeriesMetadata, ['type']),
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
    for field in fields:
        assert s["properties"][field]["readOnly"] is True


exclude_fields = [
    (ResourceMetadata, ['url']),
    (GeographicRasterMetadata, ['url']),
    (GeographicFeatureMetadata, ['url']),
    (MultidimensionalMetadata, ['url']),
    (ReferencedTimeSeriesMetadata, ['url']),
    (FileSetMetadata, ['url']),
    (SingleFileMetadata, ['url']),
    (TimeSeriesMetadata, ['url']),
]


@pytest.mark.parametrize("exclude_field", exclude_fields)
def test_exclude(exclude_field):
    clazz, fields = exclude_field
    s = schema([clazz])["definitions"][clazz.__name__]
    for field in fields:
        assert field not in s["properties"]
