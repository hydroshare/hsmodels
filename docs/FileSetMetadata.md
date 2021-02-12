# File Set Aggregation Metadata

*A class used to represent the metadata associated with a file set aggregation

A file set aggregation consists of an arbitrary collection of files that are logically
grouped together as an aggregation and to which aggregation-level metadata have been
added. There may be any number of files in the aggregation, and files may be of any type.*

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
