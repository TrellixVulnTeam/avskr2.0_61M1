# Stubs for http.cookies (Python 3.5)

from typing import Generic, Mapping, MutableMapping, Optional, TypeVar, Union

_DataType = Union[str, Mapping[str, Union[str, 'Morsel']]]
_T = TypeVar('_T')

class CookieError(Exception): ...

class Morsel(Dict[str, str], Generic[_T]):
    value = ...  # type: str
    coded_value = ...  # type: _T
    key = ...  # type: str
    def set(self, key: str, val: str, coded_val: _T) -> None: ...
    def isReservedKey(self, K: str) -> bool: ...
    def output(self, attrs: Optional[List[str]] = ...,
               header: str = ...) -> str: ...
    def js_output(self, attrs: Optional[List[str]] = ...) -> str: ...
    def OutputString(self, attrs: Optional[List[str]] = ...) -> str: ...

class BaseCookie(MutableMapping[str, Morsel], Generic[_T]):
    def __init__(self, input: Optional[_DataType] = ...) -> None: ...
    def value_decode(self, val: str) -> _T: ...
    def value_encode(self, val: _T) -> str: ...
    def output(self, attrs: Optional[List[str]] = ..., header: str = ...,
               sep: str = ...) -> str: ...
    def js_output(self, attrs: Optional[List[str]] = ...) -> str: ...
    def load(self, rawdata: _DataType) -> None: ...
    def __setitem__(self, key: str, value: Union[str, Morsel]) -> None: ...

class SimpleCookie(BaseCookie): ...
