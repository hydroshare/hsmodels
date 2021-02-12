# Resource Metadata

*A class used to represent the metadata for a resource*

## Properties

- **`type`** *(string)*: An object containing a URL that points to the HydroShare resource type selected from the hsterms namespace.
- **`url`** *(string)*: An object containing the URL for a resource.
- **`identifier`** *(string)*: An object containing the URL-encoded unique identifier for a resource.
- **`title`** *(string)*: A string containing the name given to a resource.
- **`abstract`** *(string)*: A string containing a summary of a resource.
- **`language`** *(string)*: A 3-character string for the language in which the metadata and content of a resource are expressed.
- **`subjects`** *(array)*: A list of keyword strings expressing the topic of a resource. Default: `[]`.
    - **Items** *(string)*
- **`creators`** *(array)*: A list of Creator objects indicating the entities responsible for creating a resource. Default: `[]`.
    - **Items**: Refer to *#/definitions/Creator*.
- **`contributors`** *(array)*: A list of Contributor objects indicating the entities that contributed to a resource. Default: `[]`.
    - **Items**: Refer to *#/definitions/Contributor*.
- **`sources`** *(array)*: A list of strings containing references to related resources from which a described resource was derived. Default: `[]`.
    - **Items** *(string)*
- **`relations`** *(array)*: A list of Relation objects representing resources related to a described resource. Default: `[]`.
    - **Items**: Refer to *#/definitions/Relation*.
- **`additional_metadata`** *(object)*: A dictionary containing key-value pair metadata associated with a resource. Can contain additional properties. Default: `{}`.
- **`rights`**: An object congaining information about rights held in an over a resource.
- **`created`** *(string)*: A datetime object containing the instant associated with when a resource was created.
- **`modified`** *(string)*: A datetime object containing the instant associated with when a resource was last modified.
- **`published`** *(string)*: A datetime object containing the instant associated with when a resource was published.
- **`awards`** *(array)*: A list of objects containing information about the funding agencies and awards associated with a resource. Default: `[]`.
    - **Items**: Refer to *#/definitions/AwardInfo*.
- **`spatial_coverage`**: An object containing information about the spatial topic of a resource, the spatial applicability of a resource, or jurisdiction under with a resource is relevant.
- **`period_coverage`**: An object containing information about the temporal topic or applicability of a resource.
- **`publisher`**: An object containing information about the publisher of a resource.
- **`citation`** *(string)*: A string containing the biblilographic citation for a resource.
## Definitions

- **`Creator`** *(object)*: A class used to represent the metadata associated with a creator of a resource.
    - **`name`** *(string)*: A string containing the name of the creator.
    - **`phone`** *(string)*: A string containing a phone number for the creator.
    - **`address`** *(string)*: A string containing an address for the creator.
    - **`organization`** *(string)*: A string containing the name of the organization with which the creator is affiliated.
    - **`email`** *(string)*: A string containing an email address for the creator.
    - **`homepage`** *(string)*: An object containing the URL for website associated with the creator.
    - **`description`** *(string)*: A string containing a description of the creator.
    - **`identifiers`** *(object)*: A dictionary containing identifier types and URL links to alternative identiers for the creator. Can contain additional properties. Default: `{}`.
- **`Contributor`** *(object)*: A class used to represent the metadata associated with a contributor to a resource.
    - **`name`** *(string)*: A string containing the name of the contributor.
    - **`phone`** *(string)*: A string containing a phone number for the contributor.
    - **`address`** *(string)*: A string containing an address for the contributor.
    - **`organization`** *(string)*: A string containing the name of the organization with which the contributor is affiliated.
    - **`email`** *(string)*: A string containing an email address for the contributor.
    - **`homepage`** *(string)*: An object containing the URL for website associated with the contributor.
    - **`description`** *(string)*: A string containing a description of the contributor.
    - **`identifiers`** *(object)*: A dictionary containing identifier types and URL links to alternative identiers for the contributor. Can contain additional properties. Default: `{}`.
- **`RelationType`** *(string)*: An enumeration. Must be one of: `['The content of this resource was copied from', 'The content of this resource is part of', 'Has Part', 'The content of this resource can be executed by', 'The content of this resource was created by', 'Version Of', 'Replaced By', 'The content of this resource serves as the data for', 'This resource cites', 'This resource is described by']`.
- **`Relation`** *(object)*: A class used to represent the metadata associated with a resource related to the resource being described.
    - **`type`**: The type of relationship with the related resource.
    - **`value`** *(string)*: String expressing the Full text citation, URL link for, or description of the related resource.
- **`Rights`** *(object)*: A class used to represent the rights statement metadata associated with a resource.
    - **`statement`** *(string)*: A string containing the text of the license or rights statement.
    - **`url`** *(string)*: An object containing the URL pointing to a description of the license or rights statement.
- **`AwardInfo`** *(object)*: A class used to represent the metadata associated with funding agency credits for a resource.
    - **`funding_agency_name`** *(string)*: A string containing the name of the funding agency or organization.
    - **`title`** *(string)*: A string containing the title of the project or award.
    - **`number`** *(string)*: A string containing the award number or other identifier.
    - **`funding_agency_url`** *(string)*: An object containing a URL pointing to a website describing the funding award.
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
- **`Publisher`** *(object)*: A class used to represent the metadata associated with the publisher of a resource.
    - **`name`** *(string)*: A string containing the name of the publisher.
    - **`url`** *(string)*: An object containing a URL that points to the publisher website.
