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
- **`abstract`** *(string)*: TODO Jeff.
- **`time_series_results`** *(array)*: TODO Jeff.
    - **Items**: Refer to *#/definitions/TimeSeriesResult*.
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
- **`Unit`** *(object)*: TODO Jeff (description of class).
    - **`type`** *(string)*: TODO Jeff.
    - **`name`** *(string)*: TODO Jeff.
    - **`abbreviation`** *(string)*: TODO Jeff.
- **`TimeSeriesSite`** *(object)*: TODO Jeff (description of class).
    - **`site_code`** *(string)*: TODO Jeff.
    - **`site_name`** *(string)*: TODO Jeff.
    - **`elevation_m`** *(number)*: TODO Jeff.
    - **`elevation_datum`** *(string)*: TODO Jeff.
    - **`site_type`** *(string)*: TODO Jeff.
    - **`latitude`** *(number)*: TODO Jeff.
    - **`longitude`** *(number)*: TODO Jeff.
- **`TimeSeriesVariable`** *(object)*: TODO Jeff (description of class).
    - **`variable_code`** *(string)*: TODO Jeff.
    - **`variable_name`** *(string)*: TODO Jeff.
    - **`variable_type`** *(string)*: TODO Jeff.
    - **`no_data_value`** *(integer)*: TODO Jeff.
    - **`variable_definition`** *(string)*: TODO Jeff.
    - **`speciation`** *(string)*: TODO Jeff.
- **`TimeSeriesMethod`** *(object)*: TODO Jeff (description of class).
    - **`method_code`** *(string)*: TODO Jeff.
    - **`method_name`** *(string)*: TODO Jeff.
    - **`method_type`** *(string)*: TODO Jeff.
    - **`method_description`** *(string)*: TODO Jeff.
    - **`method_link`** *(string)*: TODO Jeff.
- **`ProcessingLevel`** *(object)*: TODO Jeff (description of class).
    - **`processing_level_code`** *(string)*: TODO Jeff.
    - **`definition`** *(string)*: TODO Jeff.
    - **`explanation`** *(string)*: TODO Jeff.
- **`UTCOffSet`** *(object)*: TODO Jeff (description of class).
    - **`value`** *(number)*: TODO Jeff. Default: `0`.
- **`TimeSeriesResult`** *(object)*: TODO Jeff (description of class).
    - **`series_id`** *(string)*: TODO Jeff.
    - **`unit`**: TODO Jeff.
    - **`status`** *(string)*: TODO Jeff.
    - **`sample_medium`** *(string)*: TODO Jeff.
    - **`value_count`** *(integer)*: TODO Jeff.
    - **`aggregation_statistics`** *(string)*: TODO Jeff.
    - **`series_label`** *(string)*: TODO Jeff.
    - **`site`**: TODO Jeff.
    - **`variable`**: TODO Jeff.
    - **`method`**: TODO Jeff.
    - **`processing_level`**: TODO Jeff.
    - **`utc_offset`**: TODO Jeff.
