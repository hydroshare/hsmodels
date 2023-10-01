from datetime import datetime
from typing import Dict, Literal, Optional

from pydantic import AnyUrl, ConfigDict, EmailStr, Field, HttpUrl, field_validator, model_validator

from hsmodels.namespaces import HSTERMS
from hsmodels.schemas import base_models
from hsmodels.schemas.base_models import BaseMetadata
from hsmodels.schemas.enums import ModelProgramFileType, RelationType, UserIdentifierType, VariableType
from hsmodels.schemas.root_validators import group_user_identifiers, parse_relation, parse_utc_offset_value
from hsmodels.schemas.validators import validate_user_id


class Relation(BaseMetadata):
    """
    A class used to represent the metadata associated with a resource related to the resource being described
    """

    model_config = ConfigDict(title='Related Resource Metadata')

    type: RelationType = Field(title="Relation type", description="The type of relationship with the related resource")
    value: str = Field(
        max_length=500,
        title="Value",
        description="String expressing the Full text citation, URL link for, or description of the related resource",
    )

    _parse_relation = model_validator(mode='before')(parse_relation)


class CellInformation(BaseMetadata):
    """
    A class used to represent the metadata associated with raster grid cells in geographic raster aggregations
    """

    model_config = ConfigDict(title='Raster Cell Metadata')

    # TODO: Is there such a thing as "name" for CellInformation?
    name: str = Field(default=None, max_length=500, title="Name", description="Name of the cell information",
                      rdf_predicate=HSTERMS.name)
    rows: int = Field(default=None, title="Rows",
                      description="The integer number of rows in the raster dataset",
                      rdf_predicate=HSTERMS.rows)
    columns: int = Field(
        default=None, title="Columns", description="The integer number of columns in the raster dataset",
        rdf_predicate=HSTERMS.columns
    )
    cell_size_x_value: float = Field(
        default=None,
        title="Cell size x value",
        description="The size of the raster grid cell in the x-direction expressed as a float",
        rdf_predicate=HSTERMS.cellSizeXValue
    )
    cell_data_type: str = Field(
        default=None, max_length=50, title="Cell data type", description="The data type of the raster grid cell values",
        rdf_predicate=HSTERMS.cellDataType
    )
    cell_size_y_value: float = Field(
        default=None,
        title="Cell size y value",
        description="The size of the raster grid cell in the y-direction expressed as a float",
        rdf_predicate=HSTERMS.cellSizeYValue
    )


class Rights(BaseMetadata):
    """
    A class used to represent the rights statement metadata associated with a resource
    """

    model_config = ConfigDict(title='Rights Metadata')

    statement: str = Field(
        title="Statement", description="A string containing the text of the license or rights statement",
        rdf_predicate=HSTERMS.rightsStatement
    )
    url: AnyUrl = Field(
        title="URL",
        description="An object containing the URL pointing to a description of the license or rights statement",
        rdf_predicate=HSTERMS.URL
    )

    @classmethod
    def Creative_Commons_Attribution_CC_BY(cls):
        return Rights(
            statement="This resource is shared under the Creative Commons Attribution CC BY.",
            url="http://creativecommons.org/licenses/by/4.0/",
        )

    @classmethod
    def Creative_Commons_Attribution_ShareAlike_CC_BY(cls):
        return Rights(
            statement="This resource is shared under the Creative Commons Attribution-ShareAlike CC BY-SA.",
            url="http://creativecommons.org/licenses/by-sa/4.0/",
        )

    @classmethod
    def Creative_Commons_Attribution_NoDerivs_CC_BY_ND(cls):
        return Rights(
            statement="This resource is shared under the Creative Commons Attribution-ShareAlike CC BY-SA.",
            url="http://creativecommons.org/licenses/by-nd/4.0/",
        )

    @classmethod
    def Creative_Commons_Attribution_NoCommercial_ShareAlike_CC_BY_NC_SA(cls):
        return Rights(
            statement="This resource is shared under the Creative Commons Attribution-NoCommercial-ShareAlike"
            " CC BY-NC-SA.",
            url="http://creativecommons.org/licenses/by-nc-sa/4.0/",
        )

    @classmethod
    def Creative_Commons_Attribution_NoCommercial_CC_BY_NC(cls):
        return Rights(
            statement="This resource is shared under the Creative Commons Attribution-NoCommercial CC BY-NC.",
            url="http://creativecommons.org/licenses/by-nc/4.0/",
        )

    @classmethod
    def Creative_Commons_Attribution_NoCommercial_NoDerivs_CC_BY_NC_ND(cls):
        return Rights(
            statement="This resource is shared under the Creative Commons Attribution-NoCommercial-NoDerivs "
            "CC BY-NC-ND.",
            url="http://creativecommons.org/licenses/by-nc-nd/4.0/",
        )

    @classmethod
    def Other(cls, statement: str, url: AnyUrl):
        return Rights(statement=statement, url=url)


class Creator(BaseMetadata):
    """
    A class used to represent the metadata associated with a creator of a resource
    """

    model_config = ConfigDict(title='Creator Metadata')

    name: str = Field(
        default=None, max_length=100, title="Name", description="A string containing the name of the creator"
    )
    phone: str = Field(
        default=None, max_length=25, title="Phone", description="A string containing a phone number for the creator"
    )
    address: str = Field(
        default=None, max_length=250, title="Address", description="A string containing an address for the creator"
    )
    organization: str = Field(
        default=None,
        max_length=200,
        title="Organization",
        description="A string containing the name of the organization with which the creator is affiliated",
    )
    email: EmailStr = Field(
        default=None, title="Email", description="A string containing an email address for the creator"
    )
    homepage: HttpUrl = Field(
        default=None,
        title="Homepage",
        description="An object containing the URL for website associated with the creator",
    )
    creator_order: Optional[int] = Field(
        default=None,
        title="Creator order",
        description="An integer to order creators",
        frozen=True,
    )
    hydroshare_user_id: int = Field(
        default=None,
        title="Hydroshare user id",
        description="An integer containing the Hydroshare user ID",
        frozen=True,
        json_schema_extra={"readOnly": True},
    )
    identifiers: Dict[UserIdentifierType, AnyUrl] = Field(
        default={},
        title="Creator identifiers",
        description="A dictionary containing identifier types and URL links to alternative identifiers for the creator",
    )
    _description_validator = field_validator("hydroshare_user_id", mode='before')(validate_user_id)

    _split_identifiers = model_validator(mode='before')(group_user_identifiers)

    @classmethod
    def from_user(cls, user):
        user_dict = user.dict()
        hydroshare_user_id = user.url.path.split("/")[-2]
        user_dict["hydroshare_user_id"] = hydroshare_user_id
        if user.website:
            user_dict["homepage"] = user.website

        return Creator(**user_dict)


class Contributor(BaseMetadata):
    """
    A class used to represent the metadata associated with a contributor to a resource
    """

    model_config = ConfigDict(title='Contributor Metadata')

    name: str = Field(default=None, title="Name", description="A string containing the name of the contributor")
    phone: str = Field(
        default=None, title="Phone", description="A string containing a phone number for the contributor"
    )
    address: str = Field(
        default=None, title="Address", description="A string containing an address for the contributor"
    )
    organization: str = Field(
        default=None,
        title="Organization",
        description="A string containing the name of the organization with which the contributor is affiliated",
    )
    email: EmailStr = Field(
        default=None, title="Email", description="A string containing an email address for the contributor"
    )
    homepage: HttpUrl = Field(
        default=None,
        title="Homepage",
        description="An object containing the URL for website associated with the contributor",
    )
    hydroshare_user_id: int = Field(
        default=None,
        title="Hyroshare user id",
        description="An integer containing the Hydroshare user ID",
        frozen=True,
        json_schema_extra={"readOnly": True},
    )
    identifiers: Dict[UserIdentifierType, AnyUrl] = Field(
        default={},
        title="Contributor identifiers",
        description="A dictionary containing identifier types and URL links to alternative identiers for the contributor",
    )

    _split_identifiers = model_validator(mode='before')(group_user_identifiers)

    @classmethod
    def from_user(cls, user):
        """
        Constructs a Contributor from a User object
        :param user: a User
        :return: a Contributor
        """
        user_dict = user.dict()
        hydroshare_user_id = user.url.path.split("/")[-2]
        user_dict["hydroshare_user_id"] = hydroshare_user_id
        if user.website:
            user_dict["homepage"] = user.website

        return Contributor(**user_dict)


class AwardInfo(BaseMetadata):
    """
    A class used to represent the metadata associated with funding agency credits for a resource
    """

    model_config = ConfigDict(title='Funding Agency Metadata')

    funding_agency_name: str = Field(
        title="Agency name", description="A string containing the name of the funding agency or organization",
        rdf_predicate=HSTERMS.fundingAgencyName
    )
    title: str = Field(
        default=None, title="Award title", description="A string containing the title of the project or award",
        rdf_predicate=HSTERMS.awardTitle
    )
    number: str = Field(
        default=None, title="Award number", description="A string containing the award number or other identifier",
        rdf_predicate=HSTERMS.awardNumber
    )
    funding_agency_url: AnyUrl = Field(
        default=None,
        title="Agency URL",
        description="An object containing a URL pointing to a website describing the funding award",
        rdf_predicate=HSTERMS.fundingAgencyURL
    )


class BandInformation(BaseMetadata):
    """
    A class used to represent the metadata associated with the raster bands of a geographic raster aggregation
    """

    model_config = ConfigDict(title='Raster Band Metadata')

    name: str = Field(max_length=500, title="Name", description="A string containing the name of the raster band",
                      rdf_predicate=HSTERMS.name
                      )
    variable_name: str = Field(
        default=None,
        max_length=100,
        title="Variable name",
        description="A string containing the name of the variable represented by the raster band",
        rdf_predicate=HSTERMS.variableName
    )
    variable_unit: str = Field(
        default=None,
        max_length=50,
        title="Variable unit",
        description="A string containing the units for the raster band variable",
        rdf_predicate=HSTERMS.variableUnit
    )
    no_data_value: str = Field(
        default=None,
        title="Nodata value",
        description="A string containing the numeric nodata value for the raster band",
        rdf_predicate=HSTERMS.noDataValue
    )
    maximum_value: str = Field(
        default=None,
        title="Maximum value",
        description="A string containing the maximum numeric value for the raster band",
        rdf_predicate=HSTERMS.maximumValue
    )
    comment: str = Field(
        default=None, title="Comment", description="A string containing a comment about the raster band",
        rdf_predicate=HSTERMS.comment
    )
    method: str = Field(
        default=None,
        title="Method",
        description="A string containing a description of the method used to create the raster band data",
        rdf_predicate=HSTERMS.method
    )
    minimum_value: str = Field(
        default=None,
        title="Minimum value",
        description="A string containing the minimum numerica value for the raster dataset",
        rdf_predicate=HSTERMS.minimumValue
    )


class FieldInformation(BaseMetadata):
    """
    A class used to represent the metadata associated with a field in the attribute table for a geographic
    feature aggregation
    """

    model_config = ConfigDict(title='Geographic Feature Field Metadata')

    field_name: str = Field(
        max_length=128, title="Field name", description="A string containing the name of the attribute table field",
        rdf_predicate=HSTERMS.fieldName
    )
    field_type: str = Field(
        max_length=128, title="Field type", description="A string containing the data type of the values in the field",
        rdf_predicate=HSTERMS.fieldType
    )
    # TODO: What is the "field_type_code"? It's not displayed on the resource landing page, but it's encoded in the
    #  aggregation metadata as an integer value.
    field_type_code: str = Field(
        default=None,
        max_length=50,
        title="Field type code",
        description="A string value containing a code that indicates the field type",
        rdf_predicate=HSTERMS.fieldTypeCode
    )
    field_width: int = Field(
        default=None, title="Field width", description="An integer value containing the width of the attribute field",
        rdf_predicate=HSTERMS.fieldWidth
    )
    field_precision: int = Field(
        default=None,
        title="Field precision",
        description="An integer value containing the precision of the attribute field",
        rdf_predicate=HSTERMS.fieldPrecision
    )


class GeometryInformation(BaseMetadata):
    """
    A class used to represent the metadata associated with the geometry of a geographic feature aggregation
    """

    model_config = ConfigDict(title='Geographic Feature Geometry Metadata')

    feature_count: int = Field(
        default=0,
        title="Feature count",
        description="An integer containing the number of features in the geographic feature aggregation",
        rdf_predicate=HSTERMS.featureCount
    )
    geometry_type: str = Field(
        max_length=128,
        title="Geometry type",
        description="A string containing the type of features in the geographic feature aggregation",
        rdf_predicate=HSTERMS.geometryType
    )


class Variable(BaseMetadata):
    """
    A class used to represent the metadata associated with a variable contained within a multidimensional aggregation
    """

    model_config = ConfigDict(title='Multidimensional Variable Metadata')

    name: str = Field(
        max_length=1000, title="Variable name", description="A string containing the name of the variable",
        rdf_predicate=HSTERMS.name
    )
    unit: str = Field(
        max_length=1000,
        title="Units",
        description="A string containing the units in which the values for the variable are expressed",
        rdf_predicate=HSTERMS.unit
    )
    type: VariableType = Field(title="Type", description="The data type of the values for the variable",
                               rdf_predicate=HSTERMS.type
                               )
    shape: str = Field(
        max_length=1000,
        title="Shape",
        description="A string containing the shape of the variable expressed as a list of dimensions",
        rdf_predicate=HSTERMS.shape
    )
    descriptive_name: str = Field(
        default=None,
        max_length=1000,
        title="Descriptive name",
        description="A string containing a descriptive name for the variable",
        rdf_predicate=HSTERMS.descriptive_name
    )
    method: str = Field(
        default=None,
        title="Method",
        description="A string containing a description of the method used to create the values for the variable",
        rdf_predicate=HSTERMS.method
    )
    missing_value: str = Field(
        default=None,
        max_length=1000,
        title="Missing value",
        description="A string containing the value used to indicate missing values for the variable",
        rdf_predicate=HSTERMS.missing_value
    )


class Publisher(BaseMetadata):
    """
    A class used to represent the metadata associated with the publisher of a resource
    """

    model_config = ConfigDict(title='Publisher Metadata')

    name: str = Field(
        max_length=200, title="Publisher name", description="A string containing the name of the publisher",
        rdf_predicate=HSTERMS.publisherName
    )
    url: AnyUrl = Field(
        title="Publisher URL", description="An object containing a URL that points to the publisher website",
        rdf_predicate=HSTERMS.publisherURL
    )


class TimeSeriesVariable(BaseMetadata):
    """
    A class used to represent the metadata associated with a variable contained within a time series aggregation
    """

    model_config = ConfigDict(title='Time Series Variable Metadata')

    variable_code: str = Field(
        max_length=50,
        title="Variable code",
        description="A string containing a short but meaningful code that identifies a variable",
        rdf_predicate=HSTERMS.VariableCode
    )
    variable_name: str = Field(
        max_length=100, title="Variable name", description="A string containing the name of the variable",
        rdf_predicate=HSTERMS.VariableName
    )
    variable_type: str = Field(
        max_length=100,
        title="Variable type",
        description="A string containing the type of variable from the ODM2 VariableType controlled vocabulary",
        rdf_predicate=HSTERMS.VariableType
    )
    # TODO: The NoData value for a variable in an ODM2 database is not always an integer.
    #  It could be a floating point value. We might want to change this to a string or a floating point value
    #  It is an integer in the HydroShare database, so will have to be updated there as well if changed
    no_data_value: int = Field(title="NoData value", description="The NoData value for the variable",
                               rdf_predicate=HSTERMS.NoDataValue
                               )
    variable_definition: str = Field(
        default=None,
        max_length=255,
        title="Variable definition",
        description="A string containing a detailed description of the variable",
        rdf_predicate=HSTERMS.VariableDefinition
    )
    speciation: str = Field(
        default=None,
        max_length=255,
        title="Speciation",
        description="A string containing the speciation for the variable from the ODM2 Speciation control vocabulary",
        rdf_predicate=HSTERMS.Speciation
    )


class TimeSeriesSite(BaseMetadata):
    """
    A class used to represent the metadata associated with a site contained within a time series aggregation
    """

    model_config = ConfigDict(title='Time Series Site Metadata')

    site_code: str = Field(
        max_length=200,
        title="Site code",
        description="A string containing a short but meaningful code identifying the site",
        rdf_predicate=HSTERMS.SiteCode
    )
    site_name: str = Field(
        default=None, max_length=255, title="Site name", description="A string containing the name of the site",
        rdf_predicate=HSTERMS.SiteName
    )
    elevation_m: float = Field(
        default=None,
        title="Elevation",
        description="A floating point number expressing the elevation of the site in meters",
        rdf_predicate=HSTERMS.Elevation_m
    )
    elevation_datum: str = Field(
        default=None,
        max_length=50,
        title="Elevation datum",
        description="A string expressing the elevation datum used from the ODM2 Elevation Datum controlled vocabulary",
        rdf_predicate=HSTERMS.ElevationDatum
    )
    site_type: str = Field(
        default=None,
        max_length=100,
        title="Site type",
        description="A string containing the type of site from the ODM2 Sampling Feature Type controlled vocabulary ",
        rdf_predicate=HSTERMS.SiteType
    )
    latitude: float = Field(
        default=None,
        title="Latitude",
        description="A floating point value expressing the latitude coordinate of the site",
        rdf_predicate=HSTERMS.Latitude
    )
    longitude: float = Field(
        default=None,
        title="Longitude",
        description="A floating point value expressing the longitude coordinate of the site",
        rdf_predicate=HSTERMS.Longitude
    )


class TimeSeriesMethod(BaseMetadata):
    """
    A class used to represent the metadata associated with a method contained within a time series aggregation
    """

    model_config = ConfigDict(title='Time Series Method Metadata')

    method_code: str = Field(
        max_length=50,
        title="Method code",
        description="A string containing a short but meaningful code identifying the method",
        rdf_predicate=HSTERMS.MethodCode
    )
    method_name: str = Field(
        max_length=200, title="Method name", description="A string containing the name of the method",
        rdf_predicate=HSTERMS.MethodName
    )
    method_type: str = Field(
        max_length=200,
        title="Method type",
        description="A string containing the method type from the ODM2 Method Type controlled vocabulary",
        rdf_predicate=HSTERMS.MethodType
    )
    method_description: str = Field(
        default=None, title="Method description",
        description="A string containing a detailed description of the method",
        rdf_predicate=HSTERMS.MethodDescription
    )
    method_link: AnyUrl = Field(
        default=None,
        title="Method link",
        description="An object containing a URL that points to a website having a detailed description of the method",
        rdf_predicate=HSTERMS.MethodLink
    )


class ProcessingLevel(BaseMetadata):
    """
    A class used to represent the metadata associated with a processing level contained within a time series
    aggregation
    """

    model_config = ConfigDict(title='Time Series Processing Level Metadata')

    processing_level_code: str = Field(
        max_length=50,
        title="Processing level code",
        description="A string containing a short but meaningful code identifying the processing level",
        rdf_predicate=HSTERMS.ProcessingLevelCode
    )
    definition: str = Field(
        default=None,
        max_length=200,
        title="Definition",
        description="A string containing a description of the processing level",
        rdf_predicate=HSTERMS.Definition
    )
    explanation: str = Field(
        default=None,
        title="Explanation",
        description="A string containing a more extensive explanation of the meaning of the processing level",
        rdf_predicate=HSTERMS.Explanation
    )


class Unit(BaseMetadata):
    """
    A class used to represent the metadata associated with a dimensional unit within a time series aggregation
    """

    model_config = ConfigDict(title='Time Series Units Metadata')

    type: str = Field(
        max_length=255,
        title="Unit type",
        description="A string containing the type of unit from the ODM2 Units Type controlled vocabulary",
        rdf_predicate=HSTERMS.UnitsType
    )
    name: str = Field(
        max_length=255,
        title="Unit name",
        description="A string containing the name of the unit from the ODM2 units list",
        rdf_predicate=HSTERMS.UnitsName
    )
    abbreviation: str = Field(
        max_length=20,
        title="Unit abbreviation",
        description="A string containing an abbreviation for the unit from the ODM2 units list",
        rdf_predicate=HSTERMS.UnitsAbbreviation
    )


class UTCOffSet(BaseMetadata):
    """
    A class used to represent the metadata associated with a UTC time offset within a time series aggregation)
    """

    model_config = ConfigDict(title='Time Series UTC Offset Metadata')

    value: float = Field(
        default=0,
        title="UTC offset value",
        description="A floating point number containing the UTC time offset associated with the data values expressed in hours",
        rdf_predicate=HSTERMS.value
    )


class TimeSeriesResult(BaseMetadata):
    """
    A class used to represent the metadata associated with a time series result within a time series aggregation
    """

    model_config = ConfigDict(title='Time Series Result Metadata')

    series_id: str = Field(
        max_length=36,
        title="Series ID",
        description="A string containing a unique identifier for the time series result",
        rdf_predicate=HSTERMS.timeSeriesResultUUID
    )
    unit: Unit = Field(
        default=None,
        title="Units",
        description="An object containing the units in which the values of the time series are expressed",

    )
    status: str = Field(
        default=None,
        max_length=255,
        title="Status",
        description="A string containing the status of the time series result chosen from the ODM2 Status controlled vocabulary",
        rdf_predicate=HSTERMS.Status
    )
    sample_medium: str = Field(
        max_length=255,
        title="Sample medium",
        description="A string containing the sample medium in which the time series result was measured chosen from the ODM2 Medium controlled vocabulary",
        rdf_predicate=HSTERMS.SampleMedium
    )
    value_count: int = Field(
        title="Value count",
        description="An integer value containing the number of data values contained within the time series result",
        rdf_predicate=HSTERMS.ValueCount
    )
    aggregation_statistic: str = Field(
        max_length=255,
        title="Aggregation statistic",
        description="A string containing the aggregation statistic associated with the values of the time series result chosen from the ODM2 Aggregation Statistic controlled vocabulary",
        rdf_predicate=HSTERMS.AggregationStatistic
    )
    # TODO: Not sure what "series_label" is. It's not an ODM2 thing
    # in HydroShare it is generated with this format
    # label = "{site_code}:{site_name}, {variable_code}:{variable_name}, {units_name}, {pro_level_code}, {method_name}"
    series_label: str = Field(
        default=None,
        max_length=255,
        title="Series label",
        description="A string containing a label for the time series result",
        rdf_predicate=HSTERMS.SeriesLabel
    )
    site: TimeSeriesSite = Field(
        title="Site",
        description="An object containing metadata about the site at which the time series result was created",
    )
    variable: TimeSeriesVariable = Field(
        title="Variablef",
        description="An object containing metadata about the observed variable associated with the time series result values",
    )
    method: TimeSeriesMethod = Field(
        title="Method",
        description="An object containing metadata about the method used to produce the time series result values",
    )
    processing_level: ProcessingLevel = Field(
        title="Processing level",
        description="An object containing metadata about the processing level or level of quality control to which the time series result values have been subjected",
    )
    utc_offset: float = Field(
        default=None,
        title="UTC Offset",
        description="A floating point value that represents the time offset from UTC time in hours associated with the time series result value timestamps",
    )
    _parse_utc_offset = model_validator(mode='before')(parse_utc_offset_value)


class BoxCoverage(base_models.BaseCoverage):
    """
    A class used to represent geographic coverage metadata for a resource or aggregation expressed as a
    latitude-longitude bounding box
    """

    model_config = ConfigDict(title='Box Coverage Metadata')

    type: Literal['box'] = Field(
        default="box",
        frozen=True,
        title="Geographic coverage type",
        description="A string containing the type of geographic coverage",
        json_schema_extra={"readOnly": True},
    )
    name: str = Field(
        default=None,
        title="Name",
        description="A string containing a name for the place associated with the geographic coverage",
    )
    northlimit: float = Field(
        gt=-90,
        lt=90,
        title="North limit",
        description="A floating point value containing the constant coordinate for the northernmost face or edge of the bounding box",
    )
    eastlimit: float = Field(
        gt=-180,
        lt=180,
        title="East limit",
        description="A floating point value containing the constant coordinate for the easternmost face or edge of the bounding box",
    )
    southlimit: float = Field(
        gt=-90,
        lt=90,
        title="South limit",
        description="A floating point value containing the constant coordinate for the southernmost face or edge of the bounding box",
    )
    westlimit: float = Field(
        gt=-180,
        lt=180,
        title="West limit",
        description="A floating point value containing the constant coordinate for the westernmost face or edge of the bounding box",
    )
    units: str = Field(
        title="Units",
        description="A string containing the units applying to the unlabelled numeric values of northlimit, eastlimit, southlimit, and westlimit",
    )
    projection: str = Field(
        default=None,
        title="Projection",
        description="A string containing the name of the projection used with any parameters required, such as ellipsoid parameters, datum, standard parallels and meridians, zone, etc.",
    )

    @model_validator(mode='after')
    def compare_north_south(self):
        if self.northlimit < self.southlimit:
            raise ValueError(f"North latitude [{self.northlimit}] must be greater than or equal to South latitude [{self.southlimit}]")
        return self


class BoxSpatialReference(base_models.BaseCoverage):
    """
    A class used to represent the metadata associated with the spatial reference of a geographic
    feature or raster aggregation expressed as a bounding box
    """

    model_config = ConfigDict(title='Box Spatial Reference Metadata')

    type: Literal['box'] = Field(
        default="box",
        frozen=True,
        title="Spatial reference type",
        description="A string containing the type of spatial reference",
        json_schema_extra={'readOnly': True},
    )
    name: str = Field(
        default=None,
        title="Name",
        description="A string containing a name for the place associated with the spatial reference",
    )
    northlimit: float = Field(
        title="North limit",
        description="A floating point value containing the constant coordinate for the northernmost face or edge of the bounding box",
    )
    eastlimit: float = Field(
        title="East limit",
        description="A floating point value containing the constant coordinate for the easternmost face or edge of the bounding box",
    )
    southlimit: float = Field(
        title="South limit",
        description="A floating point value containing the constant coordinate for the southernmost face or edge of the bounding box",
    )
    westlimit: float = Field(
        title="West limit",
        description="A floating point value containing the constant coordinate for the westernmost face or edge of the bounding box",
    )
    units: str = Field(
        title="Units",
        description="A string containing the units applying to the unlabelled numeric values of northlimit, eastlimit, southlimit, and westlimit",
    )
    # TODO: "projection" should probably be "projection_name"
    projection: str = Field(
        default=None,
        title="Projection",
        description="A string containing the name of the coordinate system used by the spatial reference",
    )
    projection_string: str = Field(
        title="Projection string", description="A string containing an encoding of the coordinate system parameters"
    )
    # TODO: I'm not sure what "projection_string_type" is - I don't see it in the RDF/XML encoding
    projection_string_type: str = Field(
        default=None,
        title="Projection string type",
        description="A string containing a description of the type of encoding for the projection string",
    )
    datum: str = Field(
        default=None,
        title="Datum",
        description="A string containing the name of the datum used by the coordinate system",
    )
    projection_name: str = Field(
        default=None, title="Projection name", description="A string containing the name of the coordinate system"
    )


class MultidimensionalBoxSpatialReference(BoxSpatialReference):
    """
    A class used to represent the metadata associated with the spatial reference of a multidimensional
    aggregation expressed as a bounding box
    """

    model_config = ConfigDict(title='Multidimensional Box Spatial Reference Metadata')


class PointCoverage(base_models.BaseCoverage):
    """
    A class used to represent geographic coverage metadata for a resource or aggregation expressed as a
    point location
    """

    model_config = ConfigDict(title='Point Coverage Metadata')

    type: Literal['point'] = Field(
        default="point",
        frozen=True,
        title="Geographic coverage type",
        description="A string containing the type of geographic coverage",
        json_schema_extra={"readOnly": True},
    )
    name: str = Field(
        default=None,
        title="Name",
        description="A string containing a name for the place associated with the geographic coverage",
    )
    east: float = Field(
        gt=-180, lt=180, title="East", description="The coordinate of the point location measured in the east direction"
    )
    north: float = Field(
        gt=-90, lt=90, title="North", description="The coordinate of the point location measured in the north direction"
    )
    units: str = Field(
        title="Units", description="The units applying to the unlabelled numeric values of north and east"
    )
    projection: str = Field(
        title="Projection",
        description="The name of the projection used with any parameters required, such as ellipsoid parameters, datum, standard parallels and meridians, zone, etc.",
    )


class PointSpatialReference(base_models.BaseCoverage):
    """
    A class used to represent the metadata associated with the spatial reference of a geographic
    feature or raster aggregation expressed as a point
    """

    model_config = ConfigDict(title='Point Spatial Reference Metadata')

    type: Literal['point'] = Field(
        default="point",
        frozen=True,
        title="Spatial reference type",
        description="A string containing the type of spatial reference",
        json_schema_extra={'readOnly': True},
    )
    name: str = Field(
        default=None,
        title="Name",
        description="A string containing a name for the place associated with the spatial reference",
    )
    east: float = Field(title="East", description="The coordinate of the point location measured in the east direction")
    north: float = Field(
        title="North", description="The coordinate of the point location measured in the north direction"
    )
    units: str = Field(
        title="Units", description="The units applying to the unlabelled numeric values of north and east"
    )
    projection: str = Field(
        title="Projection",
        description="A string containing the name of the coordinate system used by the spatial reference",
    )
    projection_string: str = Field(
        title="Projection string", description="A string containing an encoding of the coordinate system parameters"
    )
    # TODO: I'm not sure what "projection_string_type" is - I don't see it in the RDF/XML encoding
    projection_string_type: str = Field(
        default=None,
        title="Projection string type",
        description="A string containing a description of the type of encoding for the projection string",
    )
    projection_name: str = Field(
        default=None, title="Projection name", description="A string containing the name of the coordinate system"
    )


class MultidimensionalPointSpatialReference(PointSpatialReference):
    """
    A class used to represent the metadata associated with the spatial reference of a multidimensional
    aggregation expressed as a point
    """

    model_config = ConfigDict(title='Multidimensional Point Spatial Reference Metadata')


class PeriodCoverage(base_models.BaseCoverage):
    """
    A class used to represent temporal coverage metadata for a resource or aggregation
    """

    model_config = ConfigDict(title='Period Coverage Metadata')

    name: str = Field(default=None, title="Name", description="A string containing a name for the time interval")
    start: datetime = Field(
        title="Start",
        description="A datetime object containing the instant corresponding to the commencement of the time interval",
    )
    end: datetime = Field(
        title="End",
        description="A datetime object containing the instant corresponding to the termination of the time interval",
    )

    @model_validator(mode='after')
    def start_before_end(self):
        if self.start and self.end:
            if self.start > self.end:
                raise ValueError(f"start date [{self.start}] is after end date [{self.end}]")
        elif self.start and not self.end:
            raise ValueError(f"An end date was not included with start date [{self.start}]")
        elif self.end and not self.start:
            raise ValueError(f"A start date was not included with end date [{self.end}]")
        return self


class ModelProgramFile(BaseMetadata):
    """
    A class used to represent the metadata associated with a file used by a model program aggregation
    """

    model_config = ConfigDict(title='Model Program File Metadata')

    type: ModelProgramFileType = Field(
        title="Model program file type", description="The type of the file used by the model program"
    )
    url: AnyUrl = Field(
        title="Model program file url", description="The url of the file used by the model program"
    )
