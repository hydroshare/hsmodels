from typing import Any, Callable, Optional

from pydantic.json_schema import JsonSchemaValue
from typing_extensions import Annotated

from datetime import datetime

from pydantic_core import core_schema
from pydantic import AnyUrl, BaseModel, EmailStr, Field, GetJsonSchemaHandler, HttpUrl, PositiveInt, \
    model_validator
from rdflib import BNode
from rdflib.term import Identifier as RDFIdentifier

from hsmodels.namespaces import DCTERMS, HSTERMS, RDF, RDFS
from hsmodels.schemas.enums import CoverageType, DateType, MultidimensionalSpatialReferenceType, SpatialReferenceType
from hsmodels.schemas.fields import (
    AwardInfo,
    BandInformation,
    CellInformation,
    FieldInformation,
    GeometryInformation,
    ProcessingLevel,
    Publisher,
    Rights,
    TimeSeriesMethod,
    TimeSeriesResult,
    TimeSeriesSite,
    TimeSeriesVariable,
    Unit,
    UTCOffSet,
    Variable,
)
from hsmodels.schemas.rdf.root_validators import parse_relation_rdf, rdf_parse_utc_offset, split_user_identifiers


class _RDFIdentifierTypePydanticAnnotation:
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        """
        Reference: https://docs.pydantic.dev/latest/usage/types/custom/#handling-third-party-types
        """

        def validate_identifier(value: str) -> RDFIdentifier:
            result = RDFIdentifier(value)
            return result

        from_int_schema = core_schema.chain_schema(
            [
                core_schema.str_schema(),
                core_schema.no_info_plain_validator_function(validate_identifier),
            ]
        )

        return core_schema.json_or_python_schema(
            json_schema=from_int_schema,
            python_schema=core_schema.union_schema(
                [
                    # check if it's an instance first before doing any further work
                    core_schema.is_instance_schema(RDFIdentifier),
                    from_int_schema,
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda instance: instance.toPython()
            ),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, _core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        # Use the same schema that would be used for RDFIdentifier
        return handler(_core_schema)


def get_RDF_IdentifierType(field: Field):
    return Annotated[RDFIdentifier, _RDFIdentifierTypePydanticAnnotation, field]


class RDFBaseModel(BaseModel):
    rdf_subject: get_RDF_IdentifierType(Field(default_factory=BNode))


class DCTypeInRDF(RDFBaseModel):
    is_defined_by: AnyUrl = Field(rdf_predicate=RDFS.isDefinedBy)
    label: str = Field(rdf_predicate=RDFS.label)


class RelationInRDF(RDFBaseModel):
    isExecutedBy: str = Field(rdf_predicate=HSTERMS.isExecutedBy, default=None)
    isCreatedBy: str = Field(rdf_predicate=HSTERMS.isCreatedBy, default=None)
    isDescribedBy: str = Field(rdf_predicate=HSTERMS.isDescribedBy, default=None)
    isSimilarTo: str = Field(rdf_predicate=HSTERMS.isSimilarTo, default=None)

    isPartOf: str = Field(rdf_predicate=DCTERMS.isPartOf, default=None)
    hasPart: str = Field(rdf_predicate=DCTERMS.hasPart, default=None)
    isVersionOf: str = Field(rdf_predicate=DCTERMS.isVersionOf, default=None)
    isReplacedBy: str = Field(rdf_predicate=DCTERMS.isReplacedBy, default=None)
    conformsTo: str = Field(rdf_predicate=DCTERMS.conformsTo, default=None)
    hasFormat: str = Field(rdf_predicate=DCTERMS.hasFormat, default=None)
    isFormatOf: str = Field(rdf_predicate=DCTERMS.isFormatOf, default=None)
    isRequiredBy: str = Field(rdf_predicate=DCTERMS.isRequiredBy, default=None)
    requires: str = Field(rdf_predicate=DCTERMS.requires, default=None)
    isReferencedBy: str = Field(rdf_predicate=DCTERMS.isReferencedBy, default=None)
    references: str = Field(rdf_predicate=DCTERMS.references, default=None)
    replaces: str = Field(rdf_predicate=DCTERMS.replaces, default=None)
    source: str = Field(rdf_predicate=DCTERMS.source, default=None)

    _parse_relation = model_validator(mode='before')(parse_relation_rdf)


class DescriptionInRDF(RDFBaseModel):
    abstract: str = Field(rdf_predicate=DCTERMS.abstract, default=None)


class IdentifierInRDF(RDFBaseModel):
    hydroshare_identifier: AnyUrl = Field(rdf_predicate=HSTERMS.hydroShareIdentifier)


class ExtendedMetadataInRDF(RDFBaseModel):
    value: str = Field(rdf_predicate=HSTERMS.value, default="")
    key: str = Field(rdf_predicate=HSTERMS.key)


class CellInformationInRDF(CellInformation, RDFBaseModel):
    pass


class DateInRDF(RDFBaseModel):
    type: DateType = Field(rdf_predicate=RDF.type)
    value: datetime = Field(rdf_predicate=RDF.value)


class RightsInRDF(Rights, RDFBaseModel):
    pass


class CreatorInRDF(RDFBaseModel):
    creator_order: Optional[PositiveInt] = Field(default=None, rdf_predicate=HSTERMS.creatorOrder)
    name: str = Field(default=None, rdf_predicate=HSTERMS.name)
    phone: str = Field(default=None, rdf_predicate=HSTERMS.phone)
    address: str = Field(default=None, rdf_predicate=HSTERMS.address)
    organization: str = Field(default=None, rdf_predicate=HSTERMS.organization)
    email: EmailStr = Field(default=None, rdf_predicate=HSTERMS.email)
    homepage: HttpUrl = Field(default=None, rdf_predicate=HSTERMS.homepage)
    hydroshare_user_id: int = Field(default=None, rdf_predicate=HSTERMS.hydroshare_user_id)
    ORCID: AnyUrl = Field(default=None, rdf_predicate=HSTERMS.ORCID)
    google_scholar_id: AnyUrl = Field(default=None, rdf_predicate=HSTERMS.GoogleScholarID)
    research_gate_id: AnyUrl = Field(default=None, rdf_predicate=HSTERMS.ResearchGateID)

    _group_identifiers = model_validator(mode='before')(split_user_identifiers)


class ContributorInRDF(RDFBaseModel):
    name: str = Field(default=None, rdf_predicate=HSTERMS.name)
    phone: str = Field(default=None, rdf_predicate=HSTERMS.phone)
    address: str = Field(default=None, rdf_predicate=HSTERMS.address)
    organization: str = Field(default=None, rdf_predicate=HSTERMS.organization)
    email: EmailStr = Field(default=None, rdf_predicate=HSTERMS.email)
    homepage: HttpUrl = Field(default=None, rdf_predicate=HSTERMS.homepage)
    hydroshare_user_id: int = Field(default=None, rdf_predicate=HSTERMS.hydroshare_user_id)
    ORCID: AnyUrl = Field(default=None, rdf_predicate=HSTERMS.ORCID)
    google_scholar_id: AnyUrl = Field(default=None, rdf_predicate=HSTERMS.GoogleScholarID)
    research_gate_id: AnyUrl = Field(default=None, rdf_predicate=HSTERMS.ResearchGateID)

    _group_identifiers = model_validator(mode='before')(split_user_identifiers)


class AwardInfoInRDF(AwardInfo, RDFBaseModel):
    pass


class BandInformationInRDF(BandInformation, RDFBaseModel):
    pass


class CoverageInRDF(RDFBaseModel):
    type: CoverageType = Field(rdf_predicate=RDF.type)
    value: str = Field(rdf_predicate=RDF.value)


class SpatialReferenceInRDF(RDFBaseModel):
    type: SpatialReferenceType = Field(rdf_predicate=RDF.type)
    value: str = Field(rdf_predicate=RDF.value)


class MultidimensionalSpatialReferenceInRDF(RDFBaseModel):
    type: MultidimensionalSpatialReferenceType = Field(rdf_predicate=RDF.type)
    value: str = Field(rdf_predicate=RDF.value)


class FieldInformationInRDF(FieldInformation, RDFBaseModel):
    pass


class GeometryInformationInRDF(GeometryInformation, RDFBaseModel):
    pass


class VariableInRDF(Variable, RDFBaseModel):
    pass


class PublisherInRDF(Publisher, RDFBaseModel):
    pass


class TimeSeriesVariableInRDF(TimeSeriesVariable, RDFBaseModel):
    pass


class TimeSeriesSiteInRDF(TimeSeriesSite, RDFBaseModel):
    pass


class TimeSeriesMethodInRDF(TimeSeriesMethod, RDFBaseModel):
    pass


class ProcessingLevelInRDF(ProcessingLevel, RDFBaseModel):
    pass


class UnitInRDF(Unit, RDFBaseModel):
    pass


class UTCOffSetInRDF(UTCOffSet, RDFBaseModel):
    pass


class TimeSeriesResultInRDF(TimeSeriesResult, RDFBaseModel):
    unit: UnitInRDF = Field(rdf_predicate=HSTERMS.unit, default=None)
    site: TimeSeriesSiteInRDF = Field(rdf_predicate=HSTERMS.site)
    variable: TimeSeriesVariableInRDF = Field(rdf_predicate=HSTERMS.variable)
    method: TimeSeriesMethodInRDF = Field(rdf_predicate=HSTERMS.method)
    processing_level: ProcessingLevelInRDF = Field(rdf_predicate=HSTERMS.processingLevel)
    utc_offset: UTCOffSetInRDF = Field(rdf_predicate=HSTERMS.UTCOffSet, default=None)

    _parse_utc_offset = model_validator(mode='before')(rdf_parse_utc_offset)
