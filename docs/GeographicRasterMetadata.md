# Geographic Raster Aggregation Metadata

*A class used to represent the metadata associated with a geographic raster aggregation

A geographic raster aggregation consists of the multiple content files that make up a
geographic raster dataset to which aggregation-level metadata have been added. Rasters
may have multiple files and multiple bands and are stored in HydroShare as GeoTIFF files.*

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
- **`band_information`**: An object containing information about the bands contained in the raster dataset.
- **`spatial_reference`**: An object containing spatial reference information for the dataset.
- **`cell_information`**: An object containing information about the raster grid cells.
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
- **`BandInformation`** *(object)*: A class used to represent the metadata associated with the raster bands of a geographic raster aggregation.
    - **`name`** *(string)*: A string containing the name of the raster band.
    - **`variable_name`** *(string)*: A string containing the name of the variable represented by the raster band.
    - **`variable_unit`** *(string)*: A string containing the units for the raster band variable.
    - **`no_data_value`** *(string)*: A string containing the numeric nodata value for the raster band.
    - **`maximum_value`** *(string)*: A string containing the maximum numeric value for the raster band.
    - **`comment`** *(string)*: A string containing a comment about the raster band.
    - **`method`** *(string)*: A string containing a description of the method used to create the raster band data.
    - **`minimum_value`** *(string)*: A string containing the minimum numerica value for the raster dataset.
- **`BoxSpatialReference`** *(object)*: A class used to represent the metadata associated with the spatial reference of a geographic
feature or raster aggregation expressed as a bounding box.
    - **`type`** *(string)*: A string containing the type of spatial reference.
    - **`name`** *(string)*: A string containing a name for the place associated with the spatial reference.
    - **`northlimit`** *(number)*: A floating point value containing the constant coordinate for the northernmost face or edge of the bounding box.
    - **`eastlimit`** *(number)*: A floating point value containing the constant coordinate for the easternmost face or edge of the bounding box.
    - **`southlimit`** *(number)*: A floating point value containing the constant coordinate for the southernmost face or edge of the bounding box.
    - **`westlimit`** *(number)*: A floating point value containing the constant coordinate for the westernmost face or edge of the bounding box.
    - **`units`** *(string)*: A string containing the units applying to the unlabelled numeric values of northlimit, eastlimit, southlimit, and westlimit.
    - **`projection`** *(string)*: A string containing the name of the coordinate system used by the spatial reference.
    - **`projection_string`** *(string)*: A string containing an encoding of the coordinate system parameters.
    - **`projection_string_type`** *(string)*: A string containing a description of the type of encoding for the projection string.
    - **`datum`** *(string)*: A string containing the name of the datum used by the coordinate system.
    - **`projection_name`** *(string)*: A string containing the name of the coordinate system.
- **`PointSpatialReference`** *(object)*: A class used to represent the metadata associated with the spatial reference of a geographic
feature or raster aggregation expressed as a point.
    - **`type`** *(string)*: A string containing the type of spatial reference.
    - **`name`** *(string)*: A string containing a name for the place associated with the spatial reference.
    - **`east`** *(number)*: The coordinate of the point location measured in the east direction.
    - **`north`** *(number)*: The coordinate of the point location measured in the north direction.
    - **`units`** *(string)*: The units applying to the unlabelled numeric values of north and east.
    - **`projection`** *(string)*: A string containing the name of the coordinate system used by the spatial reference.
    - **`projection_string`** *(string)*: A string containing an encoding of the coordinate system parameters.
    - **`projection_string_type`** *(string)*: A string containing a description of the type of encoding for the projection string.
    - **`projection_name`** *(string)*: A string containing the name of the coordinate system.
- **`CellInformation`** *(object)*: A class used to represent the metadata associated with raster grid cells in geographic raster aggregations.
    - **`name`** *(string)*: Name of the cell information.
    - **`rows`** *(integer)*: The integer number of rows in the raster dataset.
    - **`columns`** *(integer)*: The integer number of columns in the raster dataset.
    - **`cell_size_x_value`** *(number)*: The size of the raster grid cell in the x-direction expressed as a float.
    - **`cell_data_type`** *(string)*: The data type of the raster grid cell values.
    - **`cell_size_y_value`** *(number)*: The size of the raster grid cell in the y-direction expressed as a float.
