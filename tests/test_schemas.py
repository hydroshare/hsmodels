import pytest
from pydantic.schema import schema

from hsmodels.schemas import (
    FileSetMetadata,
    GeographicFeatureMetadata,
    GeographicRasterMetadata,
    ModelInstanceMetadata,
    ModelProgramMetadata,
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

read_only_fields = [
    (ResourceMetadata, ['type', 'identifier', 'created', 'modified', 'published', 'url']),
    (GeographicRasterMetadata, ['type', 'url']),
    (ModelProgramMetadata, ['type', 'url']),
    (ModelInstanceMetadata, ['type', 'url']),
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


additional_metadata_fields = [
    (ResourceMetadata, ['additional_metadata']),
    (GeographicRasterMetadata, ['additional_metadata']),
    (GeographicFeatureMetadata, ['additional_metadata']),
    (MultidimensionalMetadata, ['additional_metadata']),
    (ReferencedTimeSeriesMetadata, ['additional_metadata']),
    (FileSetMetadata, ['additional_metadata']),
    (SingleFileMetadata, ['additional_metadata']),
    (TimeSeriesMetadata, ['additional_metadata']),
    (ModelProgramMetadata, ['additional_metadata']),
    (ModelInstanceMetadata, ['additional_metadata']),
]


@pytest.mark.parametrize("additional_metadata_field", additional_metadata_fields)
def test_dictionary_field(additional_metadata_field):
    clazz, fields = additional_metadata_field
    s = schema([clazz])["definitions"][clazz.__name__]

    for field in fields:
        assert 'additionalProperties' not in s["properties"][field]
        assert 'default' not in s["properties"][field]
        assert s["properties"][field]['items'] == {'$ref': '#/definitions/AdditionalMetadata'}
