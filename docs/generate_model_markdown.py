import jsonschema2md
import json

from hsmodels.schemas.resource import ResourceMetadata
from hsmodels.schemas.aggregations import FileSetMetadata, GeographicRasterMetadata, GeographicFeatureMetadata, \
    MultidimensionalMetadata, ReferencedTimeSeriesMetadata, SingleFileMetadata, TimeSeriesMetadata


def write_md(model):
    sj_rm = model.schema_json()
    parser = jsonschema2md.Parser()
    parser.tab_size = 4
    md_lines = parser.parse_schema(json.loads(sj_rm))

    with open(f"{model.__name__}.md", "w") as f:
        f.writelines(md_lines)


write_md(ResourceMetadata)
write_md(FileSetMetadata)
write_md(GeographicRasterMetadata)
write_md(GeographicFeatureMetadata)
write_md(MultidimensionalMetadata)
write_md(ReferencedTimeSeriesMetadata)
write_md(SingleFileMetadata)
write_md(TimeSeriesMetadata)

