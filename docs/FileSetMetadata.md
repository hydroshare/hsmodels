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
