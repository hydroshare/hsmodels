from pydantic_core import Url


def __add__(self, other):
    return str(self) + other


def __radd__(self, other):
    return other + str(self)


# monkey patch string concatentation until pydantic implements Url as an extension of str again
# https://github.com/pydantic/pydantic-core/pull/1126

Url.__add__ = __add__
Url.__radd__ = __radd__
