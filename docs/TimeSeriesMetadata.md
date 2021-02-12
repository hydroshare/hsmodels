# Time Series Aggregation Metadata

*A class used to represent the metadata associated with a time series aggregation

A time series aggregation consists of one or more time series datasets to which
aggregation-level metadata have been added. Time series datasets in HydroShare
consist of sequences of individual data values that are ordered in time to record
the changing trend of a certain phenomenon. They are stored in HydroShare using
ODM2 SQLite database files.*

## Properties

- **`url`** *(string)*: An object containing the URL of the resource.
- **`title`** *(string)*: A string containing a descriptive title for the resource.
- **`subjects`** *(array)*: A list of keyword strings expressing the topic of the resource. Default: `[]`.
    - **Items** *(string)*
- **`language`** *(string)*: The 3-character string for the language in which the metadata and content are expressed. Default: `eng`.
- **`additional_metadata`** *(object)*: A list of extended metadata elements expressed as key-value pairs. Default: `{}`.
- **`spatial_coverage`**: An object containing the geospatial coverage for the resource expressed as either a bounding box or point.
- **`period_coverage`**: An object containing the temporal coverage for a resource expressed as a date range.
- **`rights`**: An object containing information about the rights held in and over the resource and the license under which a resource is shared.
- **`type`**: A string expressing the aggregation type from the list of HydroShare aggregation types.
- **`time_series_results`** *(array)*: A list of time series results contained within the time series aggregation.
    - **Items**: Refer to *#/definitions/TimeSeriesResult*.
- **`abstract`** *(string)*: A string containing a summary of a resource.
## Definitions

- **`PointCoverage`** *(object)*: A class used to represent geographic coverage metadata for a resource or aggregation expressed as a
point location.
    - **`type`** *(string)*: A string containing the type of geographic coverage.
    - **`name`** *(string)*: A string containing a name for the place associated with the geographic coverage.
    - **`east`** *(number)*: The coordinate of the point location measured in the east direction.
    - **`north`** *(number)*: The coordinate of the point location measured in the north direction.
    - **`units`** *(string)*: The units applying to the unlabelled numeric values of north and east.
    - **`projection`** *(string)*: The name of the projection used with any parameters required, such as ellipsoid parameters, datum, standard parallels and meridians, zone, etc.
- **`BoxCoverage`** *(object)*: A class used to represent geographic coverage metadata for a resource or aggregation expressed as a
latitude-longitude bounding box.
    - **`type`** *(string)*: A string containing the type of geographic coverage.
    - **`name`** *(string)*: A string containing a name for the place associated with the geographic coverage.
    - **`northlimit`** *(number)*: A floating point value containing the constant coordinate for the northernmost face or edge of the bounding box.
    - **`eastlimit`** *(number)*: A floating point value containing the constant coordinate for the easternmost face or edge of the bounding box.
    - **`southlimit`** *(number)*: A floating point value containing the constant coordinate for the southernmost face or edge of the bounding box.
    - **`westlimit`** *(number)*: A floating point value containing the constant coordinate for the westernmost face or edge of the bounding box.
    - **`units`** *(string)*: A string containing the units applying to the unlabelled numeric values of northlimit, eastlimit, southlimit, and westlimit.
    - **`projection`** *(string)*: A string containing the name of the projection used with any parameters required, such as ellipsoid parameters, datum, standard parallels and meridians, zone, etc.
- **`PeriodCoverage`** *(object)*: A class used to represent temporal coverage metadata for a resource or aggregation.
    - **`name`** *(string)*: A string containing a name for the time interval.
    - **`start`** *(string)*: A datetime object containing the instant corresponding to the commencement of the time interval.
    - **`end`** *(string)*: A datetime object containing the instant corresponding to the termination of the time interval.
- **`Rights`** *(object)*: A class used to represent the rights statement metadata associated with a resource.
    - **`statement`** *(string)*: A string containing the text of the license or rights statement.
    - **`url`** *(string)*: An object containing the URL pointing to a description of the license or rights statement.
- **`AggregationType`** *(string)*: An enumeration. Must be one of: `['Generic', 'FileSet', 'GeoRaster', 'NetCDF', 'GeoFeature', 'RefTimeseries', 'TimeSeries']`.
- **`Unit`** *(object)*: A class used to represent the metadata associated with a dimensional unit within a time series aggregation.
    - **`type`** *(string)*: A string containing the type of unit from the ODM2 Units Type controlled vocabulary.
    - **`name`** *(string)*: A string containing the name of the unit from the ODM2 units list.
    - **`abbreviation`** *(string)*: A string containing an abbreviation for the unit from the ODM2 units list.
- **`TimeSeriesSite`** *(object)*: A class used to represent the metadata associated with a site contained within a time series aggregation.
    - **`site_code`** *(string)*: A string containing a short but meaningful code identifying the site.
    - **`site_name`** *(string)*: A string containing the name of the site.
    - **`elevation_m`** *(number)*: A floating point number expressing the elevation of the site in meters.
    - **`elevation_datum`** *(string)*: A string expressing the elevation datum used from the ODM2 Elevation Datum controlled vocabulary.
    - **`site_type`** *(string)*: A string containing the type of site from the ODM2 Sampling Feature Type controlled vocabulary .
    - **`latitude`** *(number)*: A floating point value expressing the latitude coordinate of the site.
    - **`longitude`** *(number)*: A floating point value expressing the longitude coordinate of the site.
- **`TimeSeriesVariable`** *(object)*: A class used to represent the metadata associated with a variable contained within a time series aggregation.
    - **`variable_code`** *(string)*: A string containing a short but meaningful code that identifies a variable.
    - **`variable_name`** *(string)*: A string containing the name of the variable.
    - **`variable_type`** *(string)*: A string containing the type of variable from the ODM2 VariableType controlled vocabulary.
    - **`no_data_value`** *(integer)*: The NoData value for the variable.
    - **`variable_definition`** *(string)*: A string containing a detailed description of the variable.
    - **`speciation`** *(string)*: A string containing the speciation for the variable from the ODM2 Speciation controllec vocabulary.
- **`TimeSeriesMethod`** *(object)*: A class used to represent the metadata associated with a method contained within a time series aggregation.
    - **`method_code`** *(string)*: A string containing a short but meaningful code identifying the method.
    - **`method_name`** *(string)*: A string containing the name of the method.
    - **`method_type`** *(string)*: A string containing the method type from the ODM2 Method Type controlled vocabulary.
    - **`method_description`** *(string)*: A string containing a detailed description of the method.
    - **`method_link`** *(string)*: An object containg a URL that points to a website having a detailed description of the method.
- **`ProcessingLevel`** *(object)*: A class used to represent the metadata associated with a processing level contained within a time series
aggregation.
    - **`processing_level_code`** *(string)*: A string containing a short but meaningful code identifying the processing level.
    - **`definition`** *(string)*: A string containing a description of the processing level.
    - **`explanation`** *(string)*: A string containing a more extensive explanation of the meaning of the processing level.
- **`UTCOffSet`** *(object)*: A class used to represent the metadata associated with a UTC time offset within a time series aggregation).
    - **`value`** *(number)*: A floating point number containing the UTC time offset associated with the data values expressed in hours. Default: `0`.
- **`TimeSeriesResult`** *(object)*: A class used to represent the metadata associated with a time series result within a time series aggregation.
    - **`series_id`** *(string)*: A string containing a unique identifier for the time series result.
    - **`unit`**: An object containing the units in which the values of the time series are expressed.
    - **`status`** *(string)*: A string containing the status of the time series result chosen from the ODM2 Status controlled vocabulary.
    - **`sample_medium`** *(string)*: A string containing the sample medium in which the time series result was measured chosen from the ODM2 Medium controlled vocabulary.
    - **`value_count`** *(integer)*: An integer value containing the number of data values contained within the time series result.
    - **`aggregation_statistics`** *(string)*: A string containing the aggregation statistic associated with the values of the time series result chosen from the ODM2 Aggregation Statistic controlled vocabulary.
    - **`series_label`** *(string)*: A string containing a label for the time series result.
    - **`site`**: An object containing metadata about the site at which the time series result was created.
    - **`variable`**: An object containing metadata about the observed variable associated with the time series result values.
    - **`method`**: An object containing metadata about the method used to produce the time series result values.
    - **`processing_level`**: An object containing metadata about the processing level or level of quality control to which the time series result values have been subjected.
    - **`utc_offset`**: An object containing a floating point value that represents the time offset from UTC time in hours associated with the time series result value timestamps.
