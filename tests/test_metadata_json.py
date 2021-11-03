import json

import pytest
from hsmodels.schemas.resource import ResourceMetadata, ResourceMetadataIn


@pytest.fixture()
def res_md():
    with open("data/json/resource.json", 'r') as f:
        return ResourceMetadata(**json.loads(f.read()))


def test_resource_additional_metadata_dictionary(res_md):
    assert res_md.additional_metadata == {"key1": "value1", "key2": "value2"}
    res_md_in = ResourceMetadataIn(**res_md.dict())
    assert res_md_in.additional_metadata == {"key1": "value1", "key2": "value2"}

    assert res_md_in.dict()["additional_metadata"] == {"key1": "value1", "key2": "value2"}
