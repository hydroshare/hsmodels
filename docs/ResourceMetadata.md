# TODO Jeff (title of class)

*TODO Jeff (description of class)*

## Properties

- **`type`** *(string)*: TODO Jeff.
- **`url`** *(string)*: TODO Jeff.
- **`identifier`** *(string)*: TODO Jeff.
- **`title`** *(string)*: TODO Jeff.
- **`abstract`** *(string)*: TODO Jeff.
- **`language`** *(string)*: TODO Jeff.
- **`subjects`** *(array)*: TODO Jeff. Default: `[]`.
    - **Items** *(string)*
- **`creators`** *(array)*: TODO Jeff. Default: `[]`.
    - **Items**: Refer to *#/definitions/Creator*.
- **`contributors`** *(array)*: TODO Jeff. Default: `[]`.
    - **Items**: Refer to *#/definitions/Contributor*.
- **`sources`** *(array)*: TODO Jeff. Default: `[]`.
    - **Items** *(string)*
- **`relations`** *(array)*: TODO Jeff. Default: `[]`.
    - **Items**: Refer to *#/definitions/Relation*.
- **`additional_metadata`** *(object)*: TODO Jeff. Can contain additional properties. Default: `{}`.
- **`rights`**: TODO Jeff.
- **`created`** *(string)*: TODO Jeff.
- **`modified`** *(string)*: TODO Jeff.
- **`published`** *(string)*: TODO Jeff.
- **`awards`** *(array)*: TODO Jeff. Default: `[]`.
    - **Items**: Refer to *#/definitions/AwardInfo*.
- **`spatial_coverage`**: TODO Jeff.
- **`period_coverage`**: TODO Jeff.
- **`publisher`**: TODO Jeff.
- **`citation`** *(string)*: TODO Jeff.
## Definitions

- **`Creator`** *(object)*: TODO Jeff (description of class).
    - **`name`** *(string)*: TODO Jeff.
    - **`phone`** *(string)*: TODO Jeff.
    - **`address`** *(string)*: TODO Jeff.
    - **`organization`** *(string)*: TODO Jeff.
    - **`email`** *(string)*: TODO Jeff.
    - **`homepage`** *(string)*: TODO Jeff.
    - **`hydroshare_user_id`** *(string)*: TODO Jeff.
    - **`identifiers`** *(object)*: TODO Jeff. Can contain additional properties. Default: `{}`.
- **`Contributor`** *(object)*: TODO Jeff (description of class).
    - **`name`** *(string)*: TODO Jeff.
    - **`phone`** *(string)*: TODO Jeff.
    - **`address`** *(string)*: TODO Jeff.
    - **`organization`** *(string)*: TODO Jeff.
    - **`email`** *(string)*: TODO Jeff.
    - **`homepage`** *(string)*: TODO Jeff.
    - **`hydroshare_user_id`** *(string)*: TODO Jeff.
    - **`identifiers`** *(object)*: TODO Jeff. Can contain additional properties. Default: `{}`.
- **`RelationType`** *(string)*: An enumeration. Must be one of: `['The content of this resource was copied from', 'The content of this resource is part of', 'Has Part', 'The content of this resource can be executed by', 'The content of this resource was created by', 'Version Of', 'Replaced By', 'The content of this resource serves as the data for', 'This resource cites', 'This resource is described by']`.
- **`Relation`** *(object)*: TODO Jeff (description of class).
    - **`type`**: TODO Jeff.
    - **`value`** *(string)*: TODO Jeff.
- **`Rights`** *(object)*: TODO Jeff (description of class).
    - **`statement`** *(string)*: TODO Jeff.
    - **`url`** *(string)*: TODO Jeff.
- **`AwardInfo`** *(object)*: TODO Jeff (description of class).
    - **`funding_agency_name`** *(string)*: TODO Jeff.
    - **`title`** *(string)*: TODO Jeff.
    - **`number`** *(string)*: TODO Jeff.
    - **`funding_agency_url`** *(string)*: TODO Jeff.
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
- **`Publisher`** *(object)*: TODO Jeff (description of class).
    - **`name`** *(string)*: TODO Jeff.
    - **`url`** *(string)*: TODO Jeff.
