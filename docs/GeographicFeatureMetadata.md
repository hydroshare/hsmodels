# TODO Jeff (title of class)

*TODO Jeff (description of class)*

## Properties

- **`url`** *(string)*: TODO Jeff.
- **`title`** *(string)*: TODO Jeff.
- **`subjects`** *(array)*: TODO Jeff. Default: `[]`.
    - **Items** *(string)*
- **`language`** *(string)*: TODO Jeff. Default: `eng`.
- **`additional_metadata`** *(object)*: TODO Jeff. Default: `{}`.
- **`spatial_coverage`**: TODO Jeff.
- **`period_coverage`**: TODO Jeff.
- **`rights`**: TODO Jeff.
- **`type`**: TODO Jeff.
- **`field_information`** *(array)*: TODO Jeff.
    - **Items**: Refer to *#/definitions/FieldInformation*.
- **`geometry_information`**: TODO Jeff.
- **`spatial_reference`**: TODO Jeff.
## Definitions

- **`PointCoverage`** *(object)*: TODO Jeff (description of class).
    - **`type`** *(string)*: TODO Jeff.
    - **`name`** *(string)*: TODO Jeff.
    - **`east`** *(number)*: TODO Jeff.
    - **`north`** *(number)*: TODO Jeff.
    - **`units`** *(string)*: TODO Jeff.
    - **`projection`** *(string)*: TODO Jeff.
- **`BoxCoverage`** *(object)*: TODO Jeff (description of class).
    - **`type`** *(string)*: TODO Jeff.
    - **`name`** *(string)*: TODO Jeff.
    - **`northlimit`** *(number)*: TODO Jeff.
    - **`eastlimit`** *(number)*: TODO Jeff.
    - **`southlimit`** *(number)*: TODO Jeff.
    - **`westlimit`** *(number)*: TODO Jeff.
    - **`units`** *(string)*: TODO Jeff.
    - **`projection`** *(string)*: TODO Jeff.
- **`PeriodCoverage`** *(object)*: TODO Jeff (description of class).
    - **`name`** *(string)*: TODO Jeff.
    - **`start`** *(string)*: TODO Jeff.
    - **`end`** *(string)*: TODO Jeff.
- **`Rights`** *(object)*: TODO Jeff (description of class).
    - **`statement`** *(string)*: TODO Jeff.
    - **`url`** *(string)*: TODO Jeff.
- **`AggregationType`** *(string)*: An enumeration. Must be one of: `['Generic', 'FileSet', 'GeoRaster', 'NetCDF', 'GeoFeature', 'RefTimeseries', 'TimeSeries']`.
- **`FieldInformation`** *(object)*: TODO Jeff (description of class).
    - **`field_name`** *(string)*: TODO Jeff.
    - **`field_type`** *(string)*: TODO Jeff.
    - **`field_type_code`** *(string)*: TODO Jeff.
    - **`field_width`** *(integer)*: TODO Jeff.
    - **`field_precision`** *(integer)*: TODO Jeff.
- **`GeometryInformation`** *(object)*: TODO Jeff (description of class).
    - **`feature_count`** *(integer)*: TODO Jeff. Default: `0`.
    - **`geometry_type`** *(string)*: TODO Jeff.
- **`BoxSpatialReference`** *(object)*: TODO Jeff (description of class).
    - **`type`** *(string)*: TODO Jeff.
    - **`name`** *(string)*: TODO Jeff.
    - **`northlimit`** *(number)*: TODO Jeff.
    - **`eastlimit`** *(number)*: TODO Jeff.
    - **`southlimit`** *(number)*: TODO Jeff.
    - **`westlimit`** *(number)*: TODO Jeff.
    - **`units`** *(string)*: TODO Jeff.
    - **`projection`** *(string)*: TODO Jeff.
    - **`projection_string`** *(string)*: TODO Jeff.
    - **`projection_string_type`** *(string)*: TODO Jeff.
    - **`datum`** *(string)*: TODO Jeff.
    - **`projection_name`** *(string)*: TODO Jeff.
- **`PointSpatialReference`** *(object)*: TODO Jeff (description of class).
    - **`type`** *(string)*: TODO Jeff.
    - **`name`** *(string)*: TODO Jeff.
    - **`east`** *(number)*: TODO Jeff.
    - **`north`** *(number)*: TODO Jeff.
    - **`units`** *(string)*: TODO Jeff.
    - **`projection`** *(string)*: TODO Jeff.
    - **`projection_string`** *(string)*: TODO Jeff.
    - **`projection_string_type`** *(string)*: TODO Jeff.
    - **`projection_name`** *(string)*: TODO Jeff.
