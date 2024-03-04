from typing import Optional, Union

from pydantic import AfterValidator, AnyUrl, HttpUrl
from pydantic.functional_serializers import PlainSerializer
from typing_extensions import Annotated


def url_to_string(url: Union[AnyUrl, HttpUrl]) -> str:
    return str(url)


def serializer_anyurl(url: Optional[str] = None) -> Union[AnyUrl, None]:
    if url is None:
        return None
    return AnyUrl(url)


def serializer_httpurl(url: Optional[str] = None) -> Union[HttpUrl, None]:
    if url is None:
        return None
    return HttpUrl(url)


AnyUrlStr = Annotated[
    AnyUrl,
    AfterValidator(url_to_string),
    PlainSerializer(lambda v: serializer_anyurl(v), return_type=AnyUrl),
]

HttpUrlStr = Annotated[
    HttpUrl,
    AfterValidator(url_to_string),
    PlainSerializer(lambda v: serializer_httpurl(v), return_type=HttpUrl),
]
