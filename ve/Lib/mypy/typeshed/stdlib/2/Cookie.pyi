# Stubs for Cookie (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class CookieError(Exception): ...

class Morsel(dict):
    key = ... # type: Any
    def __init__(self): ...
    def __setitem__(self, K, V): ...
    def isReservedKey(self, K): ...
    value = ... # type: Any
    coded_value = ... # type: Any
    def set(self, key, val, coded_val, LegalChars=..., idmap=..., translate=...): ...
    def output(self, attrs=None, header=...): ...
    def js_output(self, attrs=None): ...
    def OutputString(self, attrs=None): ...

class BaseCookie(dict):
    def value_decode(self, val): ...
    def value_encode(self, val): ...
    def __init__(self, input=None): ...
    def __setitem__(self, key, value): ...
    def output(self, attrs=None, header=..., sep=...): ...
    def js_output(self, attrs=None): ...
    def load(self, rawdata): ...

class SimpleCookie(BaseCookie):
    def value_decode(self, val): ...
    def value_encode(self, val): ...

class SerialCookie(BaseCookie):
    def __init__(self, input=None): ...
    def value_decode(self, val): ...
    def value_encode(self, val): ...

class SmartCookie(BaseCookie):
    def __init__(self, input=None): ...
    def value_decode(self, val): ...
    def value_encode(self, val): ...

Cookie = ... # type: Any
